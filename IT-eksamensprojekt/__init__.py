from flask import Flask, render_template, request
import json
import database

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/responselist/')
def testing():
    trigger = request.args.get('trigger')
    response = request.args.get('response')
    if (trigger or response) == None:
        database.post_response(trigger,response)

    return render_template('content/Test.html',
                            trigger=trigger,
                            response=response)

if __name__ == "__main__":
    app.run()
