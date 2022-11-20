from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from carnage.api.routes.authentication.base import BaseAuthentication


class DebugRoute(BaseAuthentication):
    def __init__(
        self,
    ) -> None:

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

    async def socials_auth(self) -> HTMLResponse:
        template = '<li><a href="/api/v1/authentication/{}/login">{}</a></li>'
        html = [
            template.format(social, social.title())
            for social in ["google", "github", "gitlab"]
        ]
        return HTMLResponse("<ul>{}</ul>".format("".join(html)))


route = DebugRoute()
