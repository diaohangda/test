import flask
from flask import Flask
from flask_web.Get_Data import get_Data

app = Flask(__name__)

@app.route('/')
def hello():
    Data = get_Data()
    tmp = Data.get_all_data()
    return flask.render_template('index.html',fang=tmp)

@app.route('/Charts_of_one')
def Vis_one():
    return flask.render_template('Charts_of_one.html')

@app.route('/Charts_of_two')
def Vis_two():
    return flask.render_template('Charts_of_two.html')

@app.route('/Charts_of_thr')
def Vis_thr():
    return flask.render_template('Charts_of_thr.html')

@app.route('/Charts_of_page')
def Vis_page():
    return flask.render_template('Charts_of_page.html')



if __name__=="__main__":
    app.debug = True
    app.run()