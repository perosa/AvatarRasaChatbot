from flask import Flask, send_file
import os

import sys

print(sys.path)

from rest.util.file_util import get_random_file

try:
    app = Flask(__name__)
except Exception as e:
    print("Error at startup")


@app.route('/ping')
def ping():
    """
    Ping the endpoint
    :return:
    """
    print('/ping')
    return "ping Ok"


@app.route('/get/<style>/<gender>')
def get_image(style, gender):
    """
    Returns the given image
    :param gender:
    :param style:
    :return:
    """

    folder = os.getcwd() + '/resources/avatars/' + style + '/' + gender

    filename = get_random_file(folder)

    return send_file(filename, mimetype='image/png')


def get_port():
    """
    Retrieves port
    :return:
    """
    return int(os.environ.get("PORT", 5000))


if __name__ == '__main__':
    app.run(debug=True, port=get_port(), host='0.0.0.0')
