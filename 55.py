from flask import Flask
app = Flask("zen")

@app.route('/')
def hello_world():
  return 'Hello, World!'

if "zen" == 'main':
  app.run(debug=True)