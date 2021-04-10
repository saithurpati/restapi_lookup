from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import requests,os
import json


app = Flask(__name__, static_url_path='')
API_URL = 'https://www.travel-advisory.info/api'



@app.route('/diag', methods=['GET'])
def diag():
    try:
        r = requests.get(API_URL)
        data = json.loads(r.text)
        return data["api_status"]
    except:
        return {'http_status':500, 'cache-control':  'no-cache' ,'status': 'unavailable'}

@app.route('/health', methods=['GET'])
def health():
    try:
        return {'http_status':200, 'cache-control':  'no-cache' ,'status': 'available'}
    except:
        return {'http_status':500, 'cache-control':  'no-cache' ,'status': 'unavailable'}

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST' and 'countryname' in request.form:
        countryname = request.form['countryname']
        r = requests.get(API_URL)
        #create temp dictionary
        countylist = {}


        with open('data.json', 'w') as outputfile:
            json.dump(json.loads(r.text), outputfile)

        with open('data.json') as json_file:
            data = json.load(json_file)

        for key in data["data"]:
            countylist.update({data["data"][key]["name"].upper(): key})

        Rstatus = []
        for cc in countryname.split(","):
            try:
                Rstatus.append(countylist[cc.upper()])
            except:
                Rstatus.append("Country name:" + cc + " not Found")
        return {'http_status':200,'body': Rstatus}

    elif request.method == 'POST':
        return {'http_status':206, 'cache-control':  'no-cache' ,'status': 'available', 'body': 'Please provide country name'}



if __name__ == '__main__':
    app.run(host='0.0.0.0')
