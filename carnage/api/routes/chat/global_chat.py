"""Module that implements the Global Chat Route."""

from cryptography.fernet import Fernet, MultiFernet
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect

from carnage.api.auth.authentication import WebSocketJWTBearer
from carnage.constants import CARNAGE_CHAT_SECRET_KEY
from carnage.database.repository.account import AccountRepository
from carnage.database.repository.chat import GlobalChatRepository


class GlobalChatRoute:
    """Class that implements the global chat routes for an websocket."""

    def __init__(self) -> None:
        """Default constructor for the API route."""
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
        """Async method that handles a new client connection.

        :param from_account_id: The account id connected to the websocket.
        :param websocket: The webscoket instance to connect.
        """
        await websocket.accept()
        self._active_connections[from_account_id] = websocket

    async def disconnect(
        self,
        from_account_id: str,
    ) -> None:
        """Async method that handles the disconnection of a client.

        :param from_account_id: The account id connected to the websocket.
        """
        self._active_connections.pop(from_account_id)
        await self.broadcast(f"Client {from_account_id} disconnected.")

    async def broadcast(self, text: str) -> None:
        """Async method to broadcast a message to other connections.

        :param text: The text to be sent.
        """
        for _, websocket in self._active_connections.items():
            await websocket.send_text(text)

    async def save_message_to_database(
        self,
        from_account_id: str,
        message: str,
        channel: str,
    ) -> None:
        """Async method to save messages in the database.

        :param from_account_id: The account id connected to the websocket.
        :param message: The actual message to be processed.
        :param channel: The chanel that the message was sent.
        """
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
        """Async method that handles the webscoket for the global chat route.

        :param websocket: The webscoket instance to connect.
        :param from_account_id: The account id connected to the websocket.
        """
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
            await self.disconnect(from_account_id)


route = GlobalChatRoute()
