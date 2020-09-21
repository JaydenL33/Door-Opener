# Version 3.1
# Created by Aaron Su 16 Dec 2019
# Modified by Jayden Lee 15/04/2020

from src import create_app

server = create_app()

Local = False
if Local == False:
    server.run(debug=False, host='134.122.104.123')
else:
    server.run(debug=False, host='localhost')
