from cryptography.fernet import Fernet, MultiFernet
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect

from carnage.api.auth.authentication import WebSocketJWTBearer
from carnage.constants import CARNAGE_CHAT_SECRET_KEY
from carnage.database.repository.account import AccountRepository
from carnage.database.repository.chat import GlobalChatRepository


class GlobalChatRoute:
    def __init__(self) -> None:
        self.account_repository = AccountRepository()
        self.repository = GlobalChatRepository()

        self.router = APIRouter(prefix="/chat", tags=["chat"])
        # This prevents adding the same users to the active connections
        self._active_connections: dict[str, WebSocket] = {}

        self.router.add_api_websocket_route(
            "/global/{from_account_id}",
            self.websocket,
        )

    async def connect(
        self,
        from_account_id: str,
        websocket: WebSocket,
    ) -> None:
        await websocket.accept()
        self._active_connections[from_account_id] = websocket

    async def disconnect(
        self,
        from_account_id: str,
        websocket: WebSocket,
    ) -> None:
        self._active_connections.pop(from_account_id)
        await self.broadcast(f"Client {from_account_id} disconnected.")

    async def broadcast(self, text: str) -> None:
        for _, websocket in self._active_connections.items():
            await websocket.send_text(text)

    async def save_message_to_database(
        self,
        from_account_id: str,
        message: str,
        channel: str,
    ) -> None:
        account = self.account_repository.select_by_id(
            identifier=from_account_id,
        )[0]
        encrypted_message = MultiFernet(
            [
                Fernet(CARNAGE_CHAT_SECRET_KEY),
                Fernet(account.secret_key),
            ],
        ).encrypt(message.encode("utf-8"))
        self.repository.insert(
            {
                "message": encrypted_message.decode(),
                "channel_chat_id": channel,
                "from_account_id": from_account_id,
            },
        )

    async def websocket(
        self,
        websocket: WebSocket,
        from_account_id: str,
        _: str = Depends(WebSocketJWTBearer()),
    ) -> None:
        await self.connect(from_account_id, websocket)
        try:
            while True:
                data = await websocket.receive_json()
                await self.broadcast(f"{from_account_id}: {data}")
                await self.save_message_to_database(
                    from_account_id,
                    data["message"],
                    data["channel"],
                )
        except WebSocketDisconnect:
            await self.disconnect(from_account_id, websocket)


route = GlobalChatRoute()
