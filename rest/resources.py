from flask import Flask, send_file
import os

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


@app.route('/get/<path:filename>')
def get_image(filename):
    """
    Returns the given image
    :param filename:
    :return:
    """

    folder = os.path.dirname(os.getcwd())
    filename = folder + '/' + filename

    print('/get_image ' + filename)

    return send_file(filename, mimetype='image/png')


def get_port():
    """
    Retrieves port
    :return:
    """
    return int(os.environ.get("PORT", 5000))


if __name__ == '__main__':
    app.run(debug=True, port=get_port(), host='0.0.0.0')