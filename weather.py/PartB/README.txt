[QUESTION 2 README]

---------------------------------------------------------------------------

Installations:
1. Python 3.x
2. requests dependencies

---------------------------------------------------------------------------

Setting up project:
1.Download the project folder.
2.Install necessary dependencies using CLI if not installed.
  ( pip install requests )

---------------------------------------------------------------------------

Scripts:

First, run app.py from Part A folder to start the web api.

1. upload_weather_data.py
   to upload weather data from weather_data.csv to the web api.
Usage:
In your CLI, navigate to the project folder and run 
( python upload_weather_data.py ) 
OR
Alternatively, use the debugging function in your compiler.

2. download_weather_data.py
   to downloads all the weather data from the web api and saves it to get_weather_data.csv
Usage:
In your CLI, navigate to the project folder and run 
( python download_weather_data.py ) 
OR
Alternatively, use the debugging function in your compiler.

3. update_station_ids.py
   to updates station ID on the server based on changes specified in station_id_updates.csv
Usage:
In your CLI, navigate to the project folder and run 
( python update_station_id.py ) 
OR
Alternatively, use the debugging function in your compiler.

---------------------------------------------------------------------------

To view changes in table after running the script:
1. Open the weather_data.sqlite using DB browser for SQLite
   OR
   build in SQLite viewer in your compiler.
   OR
   open your browser and navigate to ( http://127.0.0.1:5000/api/weather )
