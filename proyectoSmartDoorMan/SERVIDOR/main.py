#FUNCIONAMIENTO  EN CONJUNTO

from flask import Flask, render_template, Response, request
from camera_pi import Camera


import time
import threading
import os

#pi_camera = Camera(flip=False) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

#background process happening without any refreshing
@app.route('/lock')
def lock():
    print ("Lock")
    os.system("python servo.py 1 2 0.1 1")       
    return ("nothing")

@app.route('/unlock')
def unlock():
    print ("Unlock")
    os.system("python servo.py 89 90 0.1 1")       
    return ("nothing")


@app.route('/', methods=['GET', 'POST'])
def move():
    result = ""
    if request.method == 'POST':
        
        return render_template('index.html', res_str=result)
                        
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
    


