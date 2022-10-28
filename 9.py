from sanic import Sanic
from sanic.response import text

app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")

# starting app
# sanic 9.app
