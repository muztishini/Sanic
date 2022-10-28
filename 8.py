# this is our 'main.py' file
from sanic import Sanic
from sanic import response
from sanic.log import logger
from controller import my_bp

app = Sanic(__name__)

# app.blueprint(my_bp)  # registering route defined by blueprint
#
# app.static('/floral_image.jpg',
#            '/sanic_demo / ws_Beautiful_flowers_1920x1080.jpg',
#            '/sanic_demo/index.html')


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


@app.route("/display")
def display(request):
    return response.file('C:\\Python\\Sanic\\test.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)