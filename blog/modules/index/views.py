from . import index_blu


@index_blu.route('/')
def index():
    return 'Hello World'
