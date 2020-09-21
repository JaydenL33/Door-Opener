# Version 3.1
# Created by Aaron Su 16 Dec 2019
# Modified by Jayden Lee 21/09/2020

from src import create_app

server = create_app()

Local = True
if Local == False:
    server.run(debug=False, host='', port=3030)
else:
    server.run(debug=False, host='localhost', port=3030)
