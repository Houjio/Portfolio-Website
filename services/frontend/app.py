from flask import Flask, render_template, make_response, request, redirect
import requests
from json import loads

app = Flask(__name__)


def verify_key(key: int, input: bool = False):
    if key is None or key == "":
        error = "No key was submited" if input else ""
        return render_template('no_key.html', error=error)

    url = f"http://192.168.111.10:8080/acess/{key}"
    r = requests.get(url)

    if r.status_code == 404:
        error = "Your acess key is invalid" if input else ""
        return render_template('no_key.html', error=error)

    return loads(r.content)


@app.route('/', methods=['GET'])
def index():
    key = request.cookies.get('key')
    resp = verify_key(key=key)
    if not isinstance(resp, dict):  # it is invalid valid
        return resp

    return render_template("index.html")


@app.route('/', methods=['POST'])
def setKey():
    key = request.form.get("key")
    resp = verify_key(key=key, input=True)
    if not isinstance(resp, dict):  # it is invalid valid
        return resp

    sucess = make_response(redirect("/"))
    sucess.set_cookie('key', key)

    return sucess


@app.route('/cv')
def cv():
    key = request.cookies.get('key')
    resp = verify_key(key=key)
    if not isinstance(resp, dict):  # it is invalid valid
        return resp

    return render_template("cv.html")


@app.route('/coverletter')
def coverletter():
    key = request.cookies.get('key')
    resp = verify_key(key=key)
    if not isinstance(resp, dict):  # it is invalid valid
        return resp

    return render_template("coverletter.html", **resp)


@app.route('/tester')
def tester():
    return render_template("tester.html")


if __name__ == '__main__':
    app.run()
