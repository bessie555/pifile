#!/usr/bin/env python
from flask import Flask, request, abort, jsonify
import requests
import json
import datetime
import Adafruit_DHT as dht
from flask import Response


app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def handle_get():

    returnData = ""

    now = int(datetime.datetime.now().strftime("%s")) * 1000

    h, t = dht.read_retry(dht.DHT22, 4)
    
    returnData = "measurement_temperature " + str("{0:.2f}".format(t) + " " + str(now) + "\n"
    returnData += "measurement_humidity " + str("{0:.2f}".format(h) + " " + str(now) + "\n"

    # url = "http://api.openweathermap.org/data/2.5/weather?id=3363094&APPID=501a5c69fb18a133ef4e4f1a1224f524"

    # It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
    #myResponse = requests.get(url)
    #print (myResponse.status_code)

    # For successful API call, response code will be 200 (OK)
    # if(myResponse.ok):
    #     jData = json.loads(myResponse.content)

    #     # returnData = {
    #     #     'timestamp': str(datetime.datetime.now()),
    #     #     'temperature': str("{0:.2f}".format(round(jData['main']['temp']-273.15),2)),
    #     #     'humidity': str("{0:.2f}".format(round(jData['main']['humidity']),2)),
    #     #     'pressure': str("{0:.2f}".format(round(jData['main']['pressure']),2))
    #     # }

    #     now = int(datetime.datetime.now().strftime("%s")) * 1000

    #     returnData = "measurement_temperature " + str("{0:.2f}".format(round(jData['main']['temp']-273.15),2)) + " " + str(now) + "\n"
    #     returnData += "measurement_humidity " + str("{0:.2f}".format(round(jData['main']['humidity']),2)) + " " + str(now) + "\n"
        

    r = Response(response=returnData, status=200, mimetype="text/plain")
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r

if __name__ == '__main__':
    print("Listening...")
    app.run(debug=True, host='0.0.0.0', port=8080)