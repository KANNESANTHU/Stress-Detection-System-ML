from flask import Flask, Response, render_template
from test import hello,fun,analyse,showpointsgraph,sorns,sugg,retstrval
import cv2
import matplotlib.pyplot as plt
app = Flask(__name__, template_folder='C:/Users/divya reddy/Desktop/Project/Stress/templates')
video=cv2.VideoCapture(0)
global points
@app.route('/login')
def home():
    return render_template('index.html')

@app.route('/link')
def link():
    return render_template('link.html')




@app.route('/predict', methods=['POST', 'GET'])
def predict(): 
    hello()
    return render_template('link.html')
    return Response(gen(video), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sgraph')
def sgraph():
    #print(points)
    #return points
    p=fun()
    l=[]
    for i in range(len(p)):
        l.append(i+1)
    plt.xlabel("Frames")
    plt.ylabel("Stres Value")
    plt.plot(l,p,'b')
    plt.show()
    return render_template('analyse.html')

@app.route('/analysesvalue')
def analysevalue():
    analyse()
    return render_template('analyse.html')

global svalue
@app.route('/sorns')
def sornss():
    sorns()
    return render_template('analyse.html')

@app.route('/sugg')
def suggestion():
    svalue=retstrval()
    if svalue>=70:
        return render_template('highstr.html')
    elif svalue<40:
        return render_template('lowstr.html')
    else:
        return render_template('avgstr.html')

@app.route('/showpointsgraph')
def showpoints():
    showpointsgraph()
    return render_template('analyse.html')

@app.route('/graph')
def graph():
    return render_template('analyse.html')



@app.route('/stop')
def stop():
    return str(ord('q'))
    return "Hello stop is working"
    #return render_template('stop.html')

"""def gen(video):
    while True:
        success, image = video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')"""

def gen(test):
    while(True):
        frame=test.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



if __name__ == '__main__':
    app.run(debug=False,threaded=False)