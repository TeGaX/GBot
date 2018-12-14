import os

api_key = os.environ.get('api_key', None)
api_hash = os.environ.get('api_hash', None)
screen_shot_layer_access_key = os.environ.get('screen_shot_layer_access_key', None)
open_weather_map_appid = os.environ.get('open_weather_map_appid', None)
logger_group = os.environ.get('logger_group', None)

API_KEY="api_key"    #get from my.telegram.org
API_HASH="api_hash"  #get from my.telegram.org
SCREEN_SHOT_LAYER_ACCESS_KEY="screen_shot_layer_access_key"           #For using .screencapture commad...please refer readme for getting the key
OPEN_WEATHER_MAP_APPID="open_weather_map_appid"        #FOR USING .weather Command
LOGGER_GROUP="logger_group"
LOGGER=     #Incase you want to turn off logging, put this to false
CONSOLE_LOGGER_VERBOSE=True
PM_AUTO_BAN=False
DB_URI='postgres://userbot:userbot@localhost/userbot'	#dis is 4 db
