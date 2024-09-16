[QUESTION 3 READ ME]

---------------------------------------------------------------------------

Installations:
1. Python 3.x
2. Flask
3. Flask-SocketIO
4. Flask-CORS

---------------------------------------------------------------------------

Setting up project:
1.Download the project folder.
2.Install necessary dependencies using CLI if not already installed
  ( pip install Flask Flask-SocketIO Flask-CORS )
3.In your CLI, navigate to the project folder and run ( python sender.py ) 
   OR
  Alternatively, use the debugging function in your compiler.
4. Use the broadcast function by open your browser and navigate to ( http://127.0.0.1:5000/alert )

---------------------------------------------------------------------------

Scripts:
1. sender.py
This Python script sets up a Flask server with WebSocket capabilities  using Flask-SocketIO. It handles broadcasting weather alerts to all connected clients.
2. send_alert.html
This HTML file provides a user interface for entering weather alert details and sending them via WebSocket to the server.

---------------------------------------------------------------------------


Usage:
1. Sending Alerts
   1.1 After running sender.py, open the web page in your browser by navigate to ( http://127.0.0.1:5000/alert ).
   1.2 Fill out the form with the following details:
       Date and Time of Occurrence
       Type of Alert
       Location
       Description
   1.3 Click the "Send Alert" button to broadcast the alert to all connected clients.

2. Receiving Alerts
   2.1 All connected clients will see the broadcasted alerts in real-time in the "Received Alerts" text area.

---------------------------------------------------------------------------
