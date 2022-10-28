# Romans_blueprint.py snippet
from sanic import Blueprint, html, Sanic
from jinja2 import Environment, PackageLoader, select_autoescape

app = Sanic(__name__)

# Инициализировать схему и определить путь к статической папке
bp = Blueprint('novels_blueprint')
bp.static('/static', './static/novels')

# jinjia2 config
env = Environment(
    loader=PackageLoader('views.novels_blueprint', '../templates/novels'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']))


def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))


@bp.route("/")
async def index(request):
    return template('index.html', title='index')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)