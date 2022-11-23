from fastapi import APIRouter
from fastapi.responses import HTMLResponse

WEBSOCKET_PAGE_TEMPLATE: str = """
<!DOCTYPE html>
<html>
    <head>
        <title>%s</title>
    </head>
    <body>
        <h1>%s</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = "11f5e35d-8047-4769-b865-70b1554b71a1"
            document.querySelector("#ws-id").textContent = client_id;
            let url = `ws://localhost:5050/%s/${client_id}?token=token`
            var ws = new WebSocket(url);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(JSON.stringify(
                        {
                            "message": input.value,
                            "channel": "a4aaa911-a102-4c1a-b72b-967d8319c139"
                        }
                    )
                )
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


class DebugRoute:
    def __init__(self) -> None:

        self.router = APIRouter(
            prefix="/debug",
            tags=["debug"],
        )

        self.router.add_api_route(
            "/auth",
            self.socials_auth,
            methods=["GET"],
            status_code=200,
        )
        self.router.add_api_route(
            "/chat/global",
            self.global_chat,
            methods=["GET"],
            status_code=200,
        )

    async def socials_auth(self) -> HTMLResponse:
        template = '<li><a href="/api/v1/authentication/{}/login">{}</a></li>'
        html = [
            template.format(social, social.title())
            for social in ["google", "github", "gitlab"]
        ]
        return HTMLResponse("<ul>{}</ul>".format("".join(html)))

    async def global_chat(self) -> HTMLResponse:
        html = WEBSOCKET_PAGE_TEMPLATE % (
            "Global Chat",
            "Global Chat",
            "api/v1/chat/global",
        )
        return HTMLResponse(html)


route = DebugRoute()
