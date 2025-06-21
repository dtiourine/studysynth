from fastapi import Depends, FastAPI, Security
from fastapi.security import HTTPBearer

from src.api.app.auth.service import VerifyToken
from src.api.app.quizzes.router import router as quizzes_router

token_auth_scheme = HTTPBearer()

app = FastAPI()
auth = VerifyToken()

app.include_router(quizzes_router)


@app.get('/api/public')
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! You don't need to be "
                "authenticated to see this.")
    }
    return result


@app.get("/api/private")
def private(auth_result: str = Security(auth.verify)):
    """A valid access token is required to access this route"""

    return auth_result

