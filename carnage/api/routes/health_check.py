"""Module that implements the Health Check Route."""

from fastapi import APIRouter


class HealthCheckRoute:
    """Class that implements the health check routes for an API request."""

    def __init__(self) -> None:
        """Constructor for HTTP API route."""
        self.router = APIRouter(
            prefix="/health_check",
            tags=["health-check"],
        )

        self.router.add_api_route(
            "/",
            self.health_check,
            methods=["GET"],
            status_code=200,
        )

    async def health_check(self) -> dict[str, bool]:
        """Async method that check for application health."""
        return {"alive": True}


route = HealthCheckRoute()
