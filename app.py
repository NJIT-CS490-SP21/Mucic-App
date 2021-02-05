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
from flask import Flask, render_template

############################################# Authorization ####################################################
load_dotenv(find_dotenv())                                                                                     #
AUTH_URL= "https://accounts.spotify.com/api/token" #url for authentication                                     #
                                                                                                               #
clientID = os.getenv("CLIENT_ID") #client id from the spotify api                                              #
clientSecret = os.getenv("CLIENT_SECRET") #client secret from sptify api                                       #
                                                                                                               #
                                                                                                               #
auth_response = requests.post(AUTH_URL, #authentication request                                                #
{                                                                                                              #
    'grant_type': 'client_credentials',                                                                        #
    'client_id' :clientID,                                                                                     #
    'client_secret' : clientSecret,                                                                            #
}                                                                                                              #
)                                                                                                              #
auth_response_data = auth_response.json() #Respononse from the api                                             #
auth_token = auth_response_data["access_token"] #authentication token                                          #
header = { #authentication header for the get request                                                          #
 'Authorization': 'Bearer {token}'.format(token=auth_token)                                                    #
 }                                                                                                             #
################################################################################################################


############################################          Creating the Flask App  ###############################################################################
                                                                                                                                                            #
app = Flask(__name__) # creating the app                                                                                                                    #
@app.route("/") #route for the web app                                                                                                                      #
def posting_song_info_on_the_webpage():                                                                                                                     #
                                                                                                                                                            #
#################################################             Song Info        ###############################################################              #
    artists = ["137W8MRPWKqSmrBGDBFSop","3TVXtAsR1Inumwj472S9r4","45PG2L6Fh2XvYL4ONzpdoW"] #list of artist ids from spotify                  #              #
                                                                                                                                             #              #
    selected_artist = artists[randint(0,2)] #selecting random artist                                                                         #              #
                                                                                                                                             #              #
    BASE_URL = "https://api.spotify.com/v1/artists/" #first part of the url that will be used inextracting the data                          #              #
    params = {                                                                                                                               #              #
                "market" : "US" #parameter in the get request                                                                                #              #
            }                                                                                                                                #              #
                                                                                                                                             #              #
    response = requests.get(BASE_URL+selected_artist+"/top-tracks", params = params,headers = header) #requesting data from the ai           #              #
    song_index = randint(0,len(response.json()["tracks"])-1) #index of the song list to select random song                                   #              #
    image_index = randint(0,len(response.json()["tracks"][song_index]["album"]["images"])-1) #index for selectinf random images from list    #              #                                      
    artist_name =response.json()["tracks"][0]["artists"][0]['name'] #name of the artist                                                      #              #
    song_name = response.json()["tracks"][song_index]["name"] #name of the song                                                              #              #
    song_preview_url =response.json()["tracks"][song_index]["external_urls"]["spotify"] #link for the song                                   #              #
    image_url =response.json()["tracks"][song_index]["album"]["images"][image_index]["url"] #link for the images                             #              #
##############################################################################################################################################              #
    return render_template("index.html", # sending data to index.html                                                                                       #
    song_name = song_name,                                                                                                                                  #
    artist_name = artist_name,                                                                                                                              #
    song_preview_url = song_preview_url,                                                                                                                    #
    image_url = image_url                                                                                                                                   #
    )                                                                                                                                                       #
                                                                                                                                                            #
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0 #code for updating style.css                                                                                      #
app.run(        #running the application                                                                                                                    #
    port = int(os.getenv("PORT",8080)),                                                                                                                     #
    host = os.getenv("IP","0.0.0.0"),                                                                                                                       #
    debug = True                                                                                                                                            #
    )                                                                                                                                                       #
                                                                                                                                                            #
#############################################################################################################################################################