from sanic import Sanic
from sanic.response import Request
from sanic_ext import render

app = Sanic(__name__)

# Отображает HTML файл из папки templates

app.static('/static', './static')  # подключает папку static


@app.get("/")
@app.ext.template("index.html")
async def handler(request: Request):
    return {"seq": ["one", "two"]}


@app.get("/alt")
async def handler(request: Request):
    return await render("index.html", context={"seq": ["three", "four"]}, status=400)


@app.get("/ctrl")
@app.ext.template("index.html")
async def handler(request: Request):
    return await render(context={"seq": ["five", "six"]}, status=400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, auto_reload=True)
