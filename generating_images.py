"""
This script takes in the spotify track to generate colours for
The script then prints to output.txt an array of colours (1 for each segment)
-> output.txt will then have a n*3 array (3 values for each segment, for n segments)

As a note: the trained model (song_to_colour_embeddings.keras and song_to_colour_model.keras) is required

Requirements:
* Keras, Tensorflow, Numpy, Requests (builtin)
* my environment is python==3.8

Output.txt:
* r g b {space separated values}
* length n {1 set of [r g b] value for each segment }

"""
import sys
import keras
import tensorflow

# loading the track in
track = sys.argv[1]

# loading the Neural Networks in
decoder = keras.models.load_model("./song_to_colour_model.pt/")
embeddings = keras.models.load_model("./song_to_colour_embeddings.pt/")

# Now I need to request the song: I am just going to use my AUTH
import requests

songs_post = requests.post("https://accounts.spotify.com/api/token", {
    "grant_type": "client_credentials",
    "client_id": "9091428112f642238a9e07928c27c936",
    "client_secret": "3f02f5968512445c88452e7397b9d2e0"
},  headers={"Content-Type": "application/x-www-form-urlencoded"})
songs_post.json()['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=songs_post.json()['access_token'])
}

BASE_URL = 'https://api.spotify.com/v1/'
r = requests.get(BASE_URL + 'tracks/{}'.format(track), headers=headers)
r = r.json()
# given the values of the track what do I find
audio_analysis = f"https://api.spotify.com/v1/audio-analysis/{track}"
r = requests.get(audio_analysis, headers=headers)
r = r.json()
# sections = r["sections"]
segments = r["segments"] # it is assumed that there are 11 values in segments


# preprocessing the segments (making sure the network can take them)

import numpy as np
test_x = list()
for item in segments:
    current_list = list()
    for i in item:
        if(type(item[i]) != list):
            current_list.append(item[i])
        else:
            current_list.extend(item[i])
    test_x.append(np.array(current_list))
    
test_x = np.array(test_x)

# getting the embeddings for these segment values
predicted_embeddings = embeddings(test_x)

# throwing these embeddings into the model (should give us what we want)
output = decoder(predicted_embeddings)

# Now writing this array into the output.txt file
with open('output.txt', 'w') as the_file:
    for i in range(output.shape[0]):
        line = ""+str(output[i].numpy()[0])+" "+str(output[i].numpy()[1]) + " " + str(output[i].numpy()[2]) + "\n"
        the_file.write(line)