from src.api.app.auth.service import VerifyToken

auth_service = VerifyToken()


async def get_current_user():
    return auth_service.verify

