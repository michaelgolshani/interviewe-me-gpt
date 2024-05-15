from flask import Blueprint
import requests


hello_world_routes = Blueprint('hello', __name__)


@hello_world_routes.route('/', methods=["GET"])
def hello_world():
    print('we are in hello world')

    return {'Message': "Hello World"}


