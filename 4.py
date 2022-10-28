# this is our 'main.py' file
from sanic import Sanic
from sanic import response
from sanic.log import logger
from controller import my_bp

app = Sanic(__name__)

# registering route defined by blueprint
app.blueprint(my_bp)


# webapp path defined used 'route' decorator
@app.route("/")
def run(request):
    return response.text("Hello World !")


@app.route("/post", methods=['POST'])
def on_post(request):
    try:
        return response.json({"content": request.json})
    except Exception as ex:
        import traceback
        logger.error(f"{traceback.format_exc()}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
