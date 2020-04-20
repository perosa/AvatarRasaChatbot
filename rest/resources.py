from flask import Flask, send_file
import os
import logging
from util.file_util import get_random_file

try:
    app = Flask(__name__)
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
except Exception as e:
    logging.exception("Error at startup")


@app.route('/ping')
def ping():
    """
    Ping the endpoint
    :return:
    """
    logging.info('/ping')
    return "ping Ok"


@app.route('/get/<style>/<gender>')
def get_image(style, gender):
    """
    Returns the given image
    :param gender:
    :param style:
    :return:
    """

    folder = '/rest/resources/avatars/' + style + '/' + gender

    filename = get_random_file(folder)

    return send_file(filename, mimetype='image/png')


def get_port():
    """
    Retrieves port
    :return:
    """
    return int(os.environ.get("PORT", 5000))


if __name__ == '__main__':
    app.run(debug=False, port=get_port(), host='0.0.0.0')


