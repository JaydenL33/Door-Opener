from flask import Blueprint, jsonify, request, Response, current_app
from datetime import datetime
import json
import math
import environConfig
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import serial

# The API Route when api:// is localhost:5000/ or 134.122.104.123:5000/

api = Blueprint("api", __name__)

# Defining Serial Communication Port



"""
Route: ("IPADDR:3000/test")
Function: The function first takes the request from request.json to process the GETREQUEST, which should be null.


## Test Function

```
POST api://test


body        application/json
-----------------------
{
    NULL
}


returns     application/json
-----------------------
{
    successful: bool,
    totalhits: int,
    date: str,
    text: [
        {
            name: str,
            count: int,

        }
    ]
    
}


"""

@api.route("/", methods=["GET"])
def testFunction():
    ser = serial.serial('/dev/ttyACMO0')
    ser.write(b'a')

    while(ser.read() != 'w'):
        pass

    ser.write(b'b')
    ser.close()




	req = request.json
	
	return Response(res, status=200, mimetype="application/json")

 


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
 
 


def puller():
    """Write records stored in a DataFrame to a SQL database.

    Databases supported by SQLAlchemy are supported.
    Tables can be newly created, appended to, or overwritten.

    see: pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
    """
    def dbConnect():
        # pull sensitive settings from local.env for database login
        env = environConfig.safe_environ()
        URI_str = env("DB_URI")
        engine = db.create_engine(URI_str)
        return engine
    
    # create a session with our engine
    engine = dbConnect()
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    # connect the engine
    connection = engine.connect()
    # create a query with the current session
    # Create a definition of the existing table for sqlalchemy
    COVID19 = db.Table("COVID19", db.MetaData(), autoload=True, autoload_with=engine)
    queryset = session.query(COVID19).limit(100).all()
    # queryset = db.select([BP_06]).limit(100)
    # ResultProxy = connection.execute(queryset)

    return queryset

# @api.route("/")
# def serverCheck():
#     """Return a friendly HTTP greeting."""
#     return "Server Running"