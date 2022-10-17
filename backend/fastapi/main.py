import os
import secrets

import redis
import sentry_sdk
# from sentry_sdk.integrations.asyncio import AsyncioIntegration
# from sentry_sdk.integrations.fastapi import FastApiIntegration
# from sentry_sdk.integrations.starlette import StarletteIntegration

from fastapi import Depends, FastAPI, Form, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi_pagination import add_pagination

import api


sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN", None),
    environment=os.getenv("ENV", "local"),
    traces_sample_rate=1.0,
    send_default_pii=True,
    debug=True,
    integrations=[
        # AsyncioIntegration(),
        # StarletteIntegration(transaction_style="endpoint"),
        # FastApiIntegration(transaction_style="endpoint"),
    ]
)

app = FastAPI(debug=True)
app.include_router(api.router)

add_pagination(app)


@app.get("/")
async def home():
    """
    curl --cookie "REQ_TYPE=home" http://localhost:8000/
    """
    return {"Hello": "Home World"}


@app.get("/debug-sentry")
async def debug_sentry():
    """
    curl --cookie "REQ_TYPE=debug-sentry" http://localhost:8000/debug-sentry
    """
    bla = 1 / 0
    return {"debug_sentry": "true"}


@app.post("/post")
async def post(username: str = Form(), password: str = Form()):
    """
    curl -X POST http://localhost:8000/post --cookie "REQ_TYPE=form" -H "Content-Type: application/x-www-form-urlencoded" -d "username=grace_hopper_form&password=welcome123"
    curl -X POST http://localhost:8000/post --cookie "REQ_TYPE=json" -H "Content-Type: application/json" -d '{"username":"grace_hopper_json","password":"welcome123"}'
    curl -X POST http://localhost:8000/post --cookie "REQ_TYPE=post" -F username=grace_hopper_post -F password=hello123
    """
    bla = 1 / 0
    return {"message": f"Your name is {username}"}


security = HTTPBasic()

def _get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(
        credentials.username, "grace_hopper_basic"
    )
    correct_password = secrets.compare_digest(credentials.password, "welcome123")
    if not (correct_username and correct_password):
        bla = 1 / 0
    return credentials.username


@app.get("/members-only/{member_id}")
async def members_only(member_id: int, username: str = Depends(_get_current_username)):
    """
    curl --cookie "REQ_TYPE=anonymous" http://localhost:8000/members-only/123
    curl --cookie "REQ_TYPE=logged-in" -u 'grace_hopper_basic:welcome123' http://localhost:8000/members-only/123
    """
    if username:
        bla = 1 / 0
        return {"message": f"Hello, {username} (id: {member_id})"}
    return {"message": "Hello, you are not invited!"}


class MyCustomCounterMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        # only handle http requests
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        path = scope.get("path")

        async def count_hits_to_url(message):
            if message["type"] == "http.response.start":
                # increase counter of url path
                redis_client = redis.Redis(host='localhost', port=6379)
                redis_client.incr(path)

            await send(message)

        await self.app(scope, receive, count_hits_to_url)

app.add_middleware(MyCustomCounterMiddleware)