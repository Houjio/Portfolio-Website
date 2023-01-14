from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
   key = request.cookies.get('key')
   if key is None:
      return "What is your key"
   return render_template("index.html")

@app.route('/setKey/<key>')
def setKey(key):
   resp = make_response("We set your key")
   resp.set_cookie('key', key)
   return resp

@app.route('/cv')
def cv():
   return render_template("cv.html")

@app.route('/coverletter')
def coverletter():
   return render_template("coverletter.html")

@app.route('/tester')
def tester():
   return render_template("tester.html")

if __name__ == '__main__':
   app.run()
