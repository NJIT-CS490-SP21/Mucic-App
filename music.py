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
    artists = ["137W8MRPWKqSmrBGDBFSop","3TVXtAsR1Inumwj472S9r4","6eUKZXaKkcviH0Ku9w2n3V","04gDigrS5kc9YWfZHwBETP"]                          #                          
    #list of artist ids from spotify                                                                                                         #              
                                                                                                                                             #              
    selected_artist = artists[randint(0,3)] #selecting random artist                                                                         #              
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
                                                                                                                             #
    return info_dict                                                                                                                         #
############################################################################################################################################## 



def get_artist_info(artist_name):
    artists = ["137W8MRPWKqSmrBGDBFSop","3TVXtAsR1Inumwj472S9r4","6eUKZXaKkcviH0Ku9w2n3V","04gDigrS5kc9YWfZHwBETP"]                          #                          
    if artist_name.lower() =="wiz khalifa":
        artist_id = artists[0]
    elif artist_name.lower() == "drake":
        artist_id = artists[1]
    elif artist_name.lower() == "ed sheeran":
        artist_id = artists[2]
    else:
        artist_id = artists[3]
    
    BASE_URL="https://api.spotify.com/v1/artists"
    params ={
        "ids":artist_id,
    }
    
    artist_response = requests.get(BASE_URL,params = params, headers = header)
    artist_data =artist_response.json()
    total_followers = artist_data["artists"][0]["followers"]["total"]
    image_url = artist_data["artists"][0]["images"][0]["url"]
    
    song_url = "https://api.spotify.com/v1/artists/"+artist_id+"/top-tracks"
    song_params= {
        "market": "US"
    }
    song_response = requests.get(song_url, params = song_params,headers = header)
    song_response_data = song_response.json()
    
    top_songs = {}
    for i in range(3):
        top_songs["song"+str(i+1)]={
                "song_name" :song_response_data["tracks"][i]["name"],
                "song_preview_url": song_response_data["tracks"][i]["preview_url"],
                "song_poster":song_response_data["tracks"][i]["album"]["images"][0]["url"],
                "lyrics_url" : get_lyrics(song_response_data["tracks"][i]["name"],artist_name)
                
            }
    artist_info = {
        "artist_name" :song_response_data["tracks"][0]["artists"][0]['name'],
        "total_followers":total_followers,
        "image_url" : image_url,
        "song1" : top_songs["song1"],
        "song2" : top_songs["song2"],
        "song3" : top_songs["song3"]
    } 
    
    return(artist_info)
