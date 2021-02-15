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
    image_url = info["image_url"],
    link_to_lyrics=info["lyrics_url"]#
                                                                                                                                                            #
    )                                                                                                                                                       #
                                                                                                                                                            #
                                                                                                                                                      #
#############################################################################################################################################################

                                                                                                                  #
@app.route("/wiz-khalifa")
def getting_wiz_info():
    artist_info = music.get_artist_info("wiz khalifa")
    return render_template("artist.html",
    artist_name = artist_info["artist_name"],
    total_followers = artist_info["total_followers"],
    image_url = artist_info["image_url"],
    song1_name = artist_info["song1"]["song_name"],
    song1_preview_url = artist_info["song1"]["song_preview_url"],
    song1_poster = artist_info["song1"]["song_poster"],
    song1_lyric_link  = artist_info["song2"]["lyrics_url"],
    song2_name = artist_info["song2"]["song_name"],
    song2_preview_url = artist_info["song2"]["song_preview_url"],
    song2_poster = artist_info["song2"]["song_poster"],
    song2_lyric_link  = artist_info["song2"]["lyrics_url"],
    song3_name = artist_info["song3"]["song_name"],
    song3_preview_url = artist_info["song3"]["song_preview_url"],
    song3_poster = artist_info["song3"]["song_poster"],
    song3_lyric_link  = artist_info["song3"]["lyrics_url"]
    )
@app.route("/drake")
def getting_drake_info():
    artist_info = music.get_artist_info("drake")
    return render_template("artist.html",
    artist_name = artist_info["artist_name"],
    total_followers = artist_info["total_followers"],
    image_url = artist_info["image_url"],
    song1_name = artist_info["song1"]["song_name"],
    song1_preview_url = artist_info["song1"]["song_preview_url"],
    song1_poster = artist_info["song1"]["song_poster"],
    song1_lyric_link  = artist_info["song2"]["lyrics_url"],
    song2_name = artist_info["song2"]["song_name"],
    song2_preview_url = artist_info["song2"]["song_preview_url"],
    song2_poster = artist_info["song2"]["song_poster"],
    song2_lyric_link  = artist_info["song2"]["lyrics_url"],
    song3_name = artist_info["song3"]["song_name"],
    song3_preview_url = artist_info["song3"]["song_preview_url"],
    song3_poster = artist_info["song3"]["song_poster"],
    song3_lyric_link  = artist_info["song3"]["lyrics_url"]
    )
@app.route("/ed-sheeran")
def getting_ed_info():
    artist_info = music.get_artist_info("ed sheeran")
    return render_template("artist.html",
    artist_name = artist_info["artist_name"],
    total_followers = artist_info["total_followers"],
    image_url = artist_info["image_url"],
    song1_name = artist_info["song1"]["song_name"],
    song1_preview_url = artist_info["song1"]["song_preview_url"],
    song1_poster = artist_info["song1"]["song_poster"],
    song1_lyric_link  = artist_info["song2"]["lyrics_url"],
    song2_name = artist_info["song2"]["song_name"],
    song2_preview_url = artist_info["song2"]["song_preview_url"],
    song2_poster = artist_info["song2"]["song_poster"],
    song2_lyric_link  = artist_info["song2"]["lyrics_url"],
    song3_name = artist_info["song3"]["song_name"],
    song3_preview_url = artist_info["song3"]["song_preview_url"],
    song3_poster = artist_info["song3"]["song_poster"],
    song3_lyric_link  = artist_info["song3"]["lyrics_url"]
    )
@app.route("/maroon-5")
def getting_maroon_info():
    artist_info = music.get_artist_info("maroon 5")
    return render_template("artist.html",
    artist_name = artist_info["artist_name"],
    total_followers = artist_info["total_followers"],
    image_url = artist_info["image_url"],
    song1_name = artist_info["song1"]["song_name"],
    song1_preview_url = artist_info["song1"]["song_preview_url"],
    song1_poster = artist_info["song1"]["song_poster"],
    song1_lyric_link  = artist_info["song2"]["lyrics_url"],
    song2_name = artist_info["song2"]["song_name"],
    song2_preview_url = artist_info["song2"]["song_preview_url"],
    song2_poster = artist_info["song2"]["song_poster"],
    song2_lyric_link  = artist_info["song2"]["lyrics_url"],
    song3_name = artist_info["song3"]["song_name"],
    song3_preview_url = artist_info["song3"]["song_preview_url"],
    song3_poster = artist_info["song3"]["song_poster"],
    song3_lyric_link  = artist_info["song3"]["lyrics_url"]
    )
    
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0 #code for updating style.css                                                                                      #
app.run(        #running the application                                                                                                                    #
    port = int(os.getenv("PORT",8080)), # port number for the application                                                                                   #
    host = os.getenv("IP","0.0.0.0"),  #Ip address of the host                                                                                              #
    debug = True # to keep running the server                                                                                                               #
    ) 