from flask import Flask, render_template, make_response, request, redirect
from werkzeug.middleware.proxy_fix import ProxyFix

import requests
from json import loads

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

with open("language.json", 'r') as language_file:
    LANGUAGE = loads(language_file.read(), strict=False)

def verify_key(cookies: dict, input: bool = False):
    key = cookies.get('key')

    if key is None or key == "":
        error = "No key was submited" if input else ""
        return render_template('no_key.html', error=error), None

    url = f"http://192.168.111.10:8080/access/{key}"
    r = requests.get(url)

    if r.status_code == 404:
        error = "Your access key is invalid" if input else ""
        return render_template('no_key.html', error=error), None

    resp = loads(r.content)

    if cookies.get("lang") == "french":
        wording = LANGUAGE['fr']
    else:
        wording = LANGUAGE['en']

    return resp, wording


@app.route('/', methods=['GET'])
def index():
    cookies = request.cookies
    resp, wording = verify_key(cookies=cookies)
    if not isinstance(resp, dict):  # it is invalid valid
        return resp

    return render_template("index.html", wording=wording)


@app.route('/', methods=['POST'])
def setKey():
    cookie = request.form
    resp, wording = verify_key(cookies=cookie, input=True)
    if not isinstance(resp, dict):  # it is invalid valid
        return resp

    success = make_response(redirect("/"))
    success.set_cookie('key', cookie['key'])

    language = "french" if resp.get("french") else "english"
    success.set_cookie('lang', language)

    return success

@app.route('/lang', methods=['GET'])
def setLanguage():
    current_language = request.cookies.get('lang')
    success = make_response(redirect("/"))
    language = "french" if current_language == "english" else "english"
    success.set_cookie('lang', language)

    return success


@app.route('/cv')
def cv():
    cookies = request.cookies
    resp, wording = verify_key(cookies=cookies)
    if not isinstance(resp, dict):  # it is invalid valid
        return resp

    return render_template("cv.html", wording=wording, jobType=resp.get("jobType"))


@app.route('/coverletter')
def coverletter():
    cookies = request.cookies
    resp, wording = verify_key(cookies=cookies)
    if not isinstance(resp, dict):  # it is invalid valid
        return resp

    return render_template("coverletter.html", wording=wording, coverLetter=resp['coverLetter'])

if __name__ == '__main__':
    app.run()
