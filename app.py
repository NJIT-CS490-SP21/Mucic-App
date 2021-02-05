# # # # # # # # # # # # # # # # # # # # #
# Project 1: Milestone 1                #
# Class: CS490                          #
# Section: 002                          #                                    
# Due Date : 02/08/2021                 #
# Authon: @Ashutosh_Rana                #
# UCID: Ajr72                           #
# Github: Mindquaker                    #
# # # # # # # # # # # # # # # # # # # # #
import requests
import os
from dotenv import load_dotenv, find_dotenv
from random import randint

############################################# Authorization ####################################################
load_dotenv(find_dotenv()) 
AUTH_URL= "https://accounts.spotify.com/api/token" #url for authentication

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")


auth_response = requests.post(AUTH_URL,
{
    'grant_type': 'client_credentials',
    'client_id' :clientID,
    'client_secret' : clientSecret,
}
)
auth_response_data = auth_response.json()
auth_token = auth_response_data["access_token"]
header = {
 'Authorization': 'Bearer {token}'.format(token=auth_token)
 }
##################################################################################################################

###########################################     Song Info    #####################################################

"""TRACK_URL = "https://api.spotify.com/v1/tracks/"
song_id = "1ms5tNNdPouTtcD2oVF9Oz"
params = {
    "id" : song_id,
    
}
response =  requests.get(TRACK_URL + song_id, headers = header)

print(response.json()[])"""
artists = ["137W8MRPWKqSmrBGDBFSop","3TVXtAsR1Inumwj472S9r4","45PG2L6Fh2XvYL4ONzpdoW"]
selected_artist = artists[randint(0,3)]
BASE_URL = "https://api.spotify.com/v1/artists/"
params = { 
            "market" : "US"
            }
FINAL_URL = BASE_URL
response = requests.get(FINAL_URL+selected_artist+"/top-tracks", params = params,headers = header)

artist_name = response.json()["tracks"][0]["artists"][0]['name']
song_name = response.json()["tracks"][0]["name"]
song_preview_url =response.json()["tracks"][0]["external_urls"]["spotify"]
image_url =response.json()["tracks"][0]["album"]["images"][0]["url"]
album_info = {
    "song" : song_name,
    "artist" : artist_name,
    "song_url": song_preview_url,
    "image_url" : image_url
    }
print(album_info)
