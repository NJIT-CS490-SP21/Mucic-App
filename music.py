# # # # # # # # # # # # # # # # # # # # #
# Project 1: Milestone 2                #
# Class: CS490                          #
# Section: 002                          #                                    
# Due Date : 02/08/2021                 #
# Author: @Ashutosh_Rana                #
# UCID: Ajr72                           #
# Github: Mindquaker                    #
# # # # # # # # # # # # # # # # # # # # #
import requests
import os
from dotenv import load_dotenv, find_dotenv
from random import randint


############################################# Spotify Authorization ############################################
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


############################################# Getting Genius Lyrics ############################################
def get_lyrics(song_name,artist_name)  :                                                                       #
    BASE_URL_GENIUS= "https://api.genius.com/" #url for authentication                                         #
    search_url = BASE_URL_GENIUS+"search"                                                                      #
    genius_clientID = os.getenv("GENIUS_CLIENT_ID") #client id from the spotify api                            #
    genius_clientSecret = os.getenv("GENIUS_CLIENT_SECRET") #client secret from sptify api                     # 
    auth_token= os.getenv("GENIUS_ACCESS_TOKEN")                                                               #
    genius_params = {                                                                                               
    "User-Agent": "CompuServe Classic/1.22",
    "Accept": "application/json",
    "Host": "api.genius.com",
    "q": song_name 
    }
    headers = {                                                                                                #
    "Authorization": "Bearer " + auth_token                                                                    #
    }                                                                                                          #
    genius_response = requests.get(search_url, #authentication request                                         #
    params=genius_params,                                                                                      #    
    headers = headers                                                                                          #
    #                                                                                                          #
    )                                                                                                          # 
                                                                                                               #
    genius_response_data = genius_response.json() #Respononse from the api                                     #
    hits = genius_response_data["response"]["hits"]                                                            #
    for i in  range(len(hits)):                                                                                #
        if  artist_name.lower() in hits[i]["result"]["full_title"].lower()  :                                  #
            link = genius_response_data["response"]["hits"][i]["result"]["url"]                                #
            break                                                                                              #
        else:                                                                                                  #
            link = genius_response_data["response"]["hits"][0]["result"]["url"]                                #
    return link                                                                                                #
################################################################################################################





#################################################             Song Info        ###############################################################              
                                                                                                                                             #
def extract_info():                                                                                                                          #
    artists = ["137W8MRPWKqSmrBGDBFSop","3TVXtAsR1Inumwj472S9r4","64KEffDW9EtZ1y2vBYgq8T"] #list of artist ids from spotify                  #              
                                                                                                                                             #              
    selected_artist = artists[randint(0,2)] #selecting random artist                                                                         #              
                                                                                                                                             #              
    BASE_URL = "https://api.spotify.com/v1/artists/" #first part of the url that will be used inextracting the data                          #              
    params = {                                                                                                                               #              
                "market" : "US" #parameter in the get request                                                                                #              
        }                                                                                                                                    #              
                                                                                                                                             #              
    response = requests.get(BASE_URL+selected_artist+"/top-tracks", params = params,headers = header) #requesting data from the api          #       
    data = response.json()                                                                                                                   #       
    song_index = randint(0,len(response.json()["tracks"])-1) #index of the song list to select random song                                   #              
    artist_name =data["tracks"][0]["artists"][0]['name'] #name of the artist                                                                 #              
    song_name = data["tracks"][song_index]["name"] #name of the song                                                                         #              
    song_preview_url =data["tracks"][song_index]["preview_url"] #link for the song                                                           #                                                                                         #              #
    image_url =data["tracks"][song_index]["album"]["images"][0]["url"] #link for the images                                                  #
    link_to_lyrics = get_lyrics(song_name,artist_name)                                                                                       #
    info_dict ={"song_name": song_name,"artist_name": artist_name,"song_preview_url": song_preview_url, "image_url":image_url,               #
                "lyrics_url":link_to_lyrics                                                                                                  #
    }                                                                                                                                        #
    print(info_dict)                                                                                                                         #
    return info_dict                                                                                                                         #
##############################################################################################################################################   
extract_info()
