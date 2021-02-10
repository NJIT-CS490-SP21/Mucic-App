# # # # # # # # # # # # # # # # # # # # #
# Project 1: Milestone 1                #
# Class: CS490                          #
# Section: 002                          #                                    
# Due Date : 02/08/2021                 #
# Author: @Ashutosh_Rana                #
# UCID: Ajr72                           #
# Github: Mindquaker                    #
# # # # # # # # # # # # # # # # # # # # #
import music
import os
from flask import Flask, render_template



############################################          Creating the Flask App  ###############################################################################
                                                                                                                                                            #
app = Flask(__name__) # creating the app                                                                                                                    #
@app.route("/") #route for the web app                                                                                                                      #
def posting_song_info_on_the_webpage():                                                                                                                     #
    info = music.extract_info()                                                                                                                             #           
    return render_template("index.html", # sending data to index.html                                                                                       #
    song_name = info["song_name"],                                                                                                                          #
    artist_name = info["artist_name"],                                                                                                                      #
    song_preview_url = info["song_preview_url"],                                                                                                            #
    image_url = info["image_url"],                                                                                                                          #
                                                                                                                                                            #
    )                                                                                                                                                       #
                                                                                                                                                            #
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0 #code for updating style.css                                                                                      #
app.run(        #running the application                                                                                                                    #
    port = int(os.getenv("PORT",8080)), # port number for the application                                                                                   #
    host = os.getenv("IP","0.0.0.0"),  #Ip address of the host                                                                                              #
    debug = True # to keep running the server                                                                                                               #
    )                                                                                                                                                       #
                                                                                                                                                            #
#############################################################################################################################################################
