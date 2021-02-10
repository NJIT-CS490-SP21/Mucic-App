# Project1-ajr72 Spotify Music Web App
This reository have python, css and html files which will dynamically retrive information about a trop track of a perticular randomly chosen artist from a list of 3 artists using Spotify Artist API.
# Technologies used in this Project:
  * **HTML**: To create a structure of the webpage.
  * **CSS**: To give style and design to the webpage.
  * **Python**: It is programing language which will host the Flask Framewrk.
  * **Flask Framework**: to create a server and connect backend and frontend.
  * **Spotify Artist API**: To fetch the information about the tack  f a perticuar artist.
## HTML
    Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser.
## CSS
    Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.
## Python
    Python is an interpreted, high-level and general-purpose programming language. We will use it to create the backend of or Web App.
## Flask
    Flask is a lightweight WSGI web application framework which will help use to connect our backend with frontend created with html and css.
## Spotify Artist API
    It is a API Provided by Spotify INC, A music providing company to retrive  infromation about a track in JSON format.
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
  2. create ```.env``` file to store client id and client secret.
      * We need to export client id and client secret.
      * export CLIENT_ID = your client id.
      * export CLIENT_SECRET = your client secret.
  ### In music.py 
  3. We need to authenticate ourself, for that we need to send ```POST``` request in proper format and get the ```access token``` from the response using, the ```client id ``` and ```client secrete``` as shown [here](https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow) or [here](https://stmorse.github.io/journal/spotify-api.html).
  4.Now we need to import libraries we have installed.
  5. Now we have to create a list of our Favourite artists's spotify's ```artist's id```. 
  6. Select a random artist from the list.
  7. Use ```Spotify's Artist Api``` to fetch data about the artist and song.
  8. Send a ```GET``` request with proper endpoints, parameters and headers.
  9. After geetting the response back in ```JSON``` format we can retrieve information like the song's name, artist, link for the son's preview and link for the poster of the song.
  ### In app.py
  10. Import music.py and Flask library.
  11. Create an app using Flask using ```app = Flask(__name__)``` command.
  12. Set route to ("/") which the root of the route.
  13. Render these data send dend it to index.html.
  **Don't forget to add .env file to .gitignore to protect your keys. **
 
 
 
 # Technical Errors and Issues I faced:
  1. I had an issue with the loging in ot the github via terminal. It was not granting me the permission to loging even if I entered the correct username and password.
      **Solution**: After few hours of research on internet and with the help of fellow students on slacks I found out the solution. I disable the two way authentication feature and it solved the issue and then I generated a ssh key in my terminal and added it to my github account.
  2. I had an isuue when pushing the commit. After adding my files and commining the changes whenev I tried to push changes github wad not letting me to push the changes.
      **Solution** : The issue was,  that while generating ssh key and adding to the github I put the wrong repository name. To solve this issue first I remove the original remote orign and than I again added remote origin with the correct repository name. And then I followed the step which I used to initialize the git that i used on first hand.
  3. Whenever I recieved the response in the json format, the response was so messy.
      Solution: I used a chrome extention called ```Awesome JSON Viewer```. So I needed to copy the response which I recieved from the GET request in the text box. And then it will process the resonse and butified it. It was very easy to get a parent node just by clicking the child node.
      [Here](https://awesomeopensource.com/project/rbrahul/Awesome-JSON-Viewer) is the link of the extention 
      
  # Current problems with the Web App.
  1. My app does not have good design yet.
  2. The webpage is static it does not have other functionality other than playing previews of songs.
  3. CSS of the webpages needs to improve and html structure should also be improved.
  # What I would do to improve my future projects.
   I would learn different technologies. I will practice a lot to use the technologies I have learned. I will ge help from professor, TAs and my peers. I will also do my own research and try to find solution by myself.

