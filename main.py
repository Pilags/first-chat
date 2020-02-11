from flask import Flask, json, jsonify, render_template, request


app = Flask('app')


@app.route('/')
def index_lapa():
  return render_template('chat.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5000, debug=True)