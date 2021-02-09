# Project1-ajr72 Spotify Music Web App
This reository have python, css and html files which will dynamically retrive information about a trop track of a perticular randomly chosen artist from a list of 3 artists using Spotify Track API.
# Technologies used in this Project:
  * **HTML**: To create a structure of the webpage.
  * **CSS**: To give style and design to the webpage.
  * **Python**: It is programing language which will host the Flask Framewrk.
  * **Flask Framework**: to create a server and connect backend and frontend.
  * **Spotify Track API**: To fetch the information about the tack.
## HTML
    Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser.
## CSS
    Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.
## Python
    Python is an interpreted, high-level and general-purpose programming language. We will use it to create the backend of or Web App.
## Flask
    Flask is a lightweight WSGI web application framework which will help use to connect our backend with frontend created with html and css.
## Spotify Track API
    It is a API Provided by Spotify INC, A music providing company to retrive  infromation about a track in ```JSON``` format.
# Lirbaries to install:
  1.  ```Requests```: to request data from the api.
     
      ->command to install : ```pip install requests```
  2. os: to interact with the operating system to get so data like data from .env file and also to provide port number and ip address of the pc to the app.
    
      ->``` os``` is a prebuilt library.
  3. ```load_dot env and find_env from dotenv```: to load and find the .env file which stores keys of the api provided by spotify api.
      
        ->command to install: ```pip install python-dotenv```
  4. ```random```: to generate random number
    
      -> it is prebuilt library
  5. ```Flask and render_template from flask```: to create,run and render the app.
      
        -> command to install : ```pip install flask ```
  
 
 Deploying the app (app.py and music.py):
  1. First of all we need to create a developer account in [Soptify](https://developer.spotify.com/dashboard/login) to get ```CLIENT ID``` and ```CLIENT SECRET``` to the API.
  2. create .env file to store client id and client secret.
  3. authenticate ourself using the client id and client secrete as shown in the documentation.
      For that we need to send post request in proper format and get the access token from the response.
  4. Create an app using Flask.
  5. Set route to ("/") which the root of the route.
  6. Create a list of your Favourite artists's spotify 'artist's id'.
  7. Select a random artist from the list.
  8. Use Spotify's Artist Api to fetch data about the artist.
  9. Send a get request with proper endpoints and parameters and headers.
  10. Us the response to extract the information about artist's top track like song's name, preview url,images,etc.
  11. Render these data snd dend it to index.html.
 
 
 
 Problem I faced:
  1. I had an issue with the loging in tot the github via terminal.
      Solution: I disable the two way authentication feature and it solved the issue.
  2. I had an isuue when ushing the commit, it was not pushing the commits.
      Solution: I used git pull' command first and the used 'git push' command and it solved the issue.
  3. Whenever I recieved the response in the json format, the response was so messy.
      Solution: I used a chrome extention called "Awesome JSON Viewer" so it was very easy to get the parent node for any child node>
      Here is the link of the extention : https://awesomeopensource.com/project/rbrahul/Awesome-JSON-Viewer

