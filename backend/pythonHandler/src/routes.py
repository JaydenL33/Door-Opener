from flask import Blueprint, jsonify, request, Response, current_app
from datetime import datetime
import json
import math
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import serial

# The API Route when api:// is localhost:5000/ or 134.122.104.123:5000/

api = Blueprint("api", __name__)

# Defining Serial Communication Port




@api.route("/", methods=["GET"])
def testFunction():

	ser = serial.Serial('/dev/ttyACMO0')
	ser.write(b'a')
	ser.close()

	req = request.json
	print(req)

	
	return 'successful'



@api.route("/data", methods=["GET"])
def dataCall():
	# req = request.json
 
	res = {
	"successful": True,
	"data": [],
	}
 
	res["data"] = puller()
 
	# for i in range(len(constructedData)):
	#   res["data"].append(constructedData[i])
 
	res = json.dumps(res) # json serializer
	return Response(res, status=200, mimetype="application/json")
 
 


