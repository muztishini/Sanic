from sanic import Sanic, response
from sanic.exceptions import ServerError, NotFound

app = Sanic(__name__)

# app.static('/floral_image.jpg',
#            '/sanic_demo / ws_Beautiful_flowers_1920x1080.jpg',
#            '/templates')

# # raise Exception
# @app.route('/timeout')
# async def terminate(request):
#     raise ServerError("Gateway Timeout error", status_code=504)
#
#
# @app.exception(NotFound)
# async def ignore_5xx(request, exception):
#     return response.text(f"Gateway is always up: {request.url}")


@app.route('/')
async def test(request):
    # return response.file('/templates/index.html')
    return response.html('<h1>Hello!</h1>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
