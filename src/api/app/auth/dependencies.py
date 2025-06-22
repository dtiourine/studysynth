# from fastapi.security import HTTPBearer, SecurityScopes, HTTPAuthorizationCredentials
#
# from src.api.app.auth.service import VerifyToken
# from fastapi import Depends, Security
#
# auth_service = VerifyToken()
# security = HTTPBearer()
#
#
# async def get_current_user(
#         token: HTTPAuthorizationCredentials = Depends(security)
# ) -> dict:
#     """Get current user from JWT token"""
#     security_scopes = SecurityScopes()
#     return await auth_service.verify(security_scopes, token)
#
