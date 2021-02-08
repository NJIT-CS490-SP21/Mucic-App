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
import music




############################################          Creating the Flask App  ###############################################################################
                                                                                                                                                            #
app = Flask(__name__) # creating the app                                                                                                                    #
@app.route("/") #route for the web app                                                                                                                      #
def posting_song_info_on_the_webpage():                                                                                                                     #
                                                                                                                                                            #           
    return render_template("index.html", # sending data to index.html                                                                                       #
    song_name = music.song_name,                                                                                                                            #
    artist_name = music.artist_name,                                                                                                                        #
    song_preview_url = music.song_preview_url,                                                                                                              #
    image_url = music.image_url,                                                                                                                            #
                                                                                                                                                            #
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
