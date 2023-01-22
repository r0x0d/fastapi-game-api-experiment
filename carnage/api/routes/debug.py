# MIT License
#
# Copyright (c) 2022, Rodolfo Olivieri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Module that implements the Debug Route."""

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
"""Template for the websocket page. Used only for debug purposes."""


class DebugRoute:
    """Class that implements some debug routes for an API request."""

    def __init__(self) -> None:
        """Route that is used only for debug purposes."""
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
        """Async method that defines the social logins authentication."""
        template = '<li><a href="/api/v1/authentication/{}/login">{}</a></li>'
        html = [
            template.format(social, social.title())
            for social in ["google", "github", "gitlab"]
        ]
        return HTMLResponse("<ul>{}</ul>".format("".join(html)))

    async def global_chat(self) -> HTMLResponse:
        """Async method that defines the chat."""
        html = WEBSOCKET_PAGE_TEMPLATE % (
            "Global Chat",
            "Global Chat",
            "api/v1/chat/global",
        )
        return HTMLResponse(html)


route = DebugRoute()
