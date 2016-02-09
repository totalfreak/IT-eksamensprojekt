from flask import Flask, render_template, request, url_for
import json
import database
import commands
import points

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/hvadsiger/', methods = ["GET"])
def hvadsiger():
    img_url = request.args.get('img_url') # Link to the image
    img_type = request.args.get('option') # Boolean value whether or not it's a thumbs up or down
    if (img_url or img_type) != None:
        database.post("hvadsiger", {"img_url": img_url, "img_type": img_type})
    data = database.get_unique_id('hvadsiger', 'img_url', 'img_type')
    return render_template('content/hvadsiger.html', data=data)

@app.route('/points')
def pointspage():
    points_dict = points.get_points()
    print type(points_dict)
    return render_template('content/points.html', data=points_dict.items())

if __name__ == "__main__":
    app.run(debug = True)
