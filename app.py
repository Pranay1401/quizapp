from os import environ

from __init__ import create_app
from waitress import serve

app = create_app()

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=environ.get("BIND_PORT") or 8000)
