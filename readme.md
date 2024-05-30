# Main file is generating_images.py 

# What this is
This software takes in a track link from spotify, and generates a colour sequence from the song
I trained a Diffusion model for this, but cannot provide the model code due to
ongoing non-release clauses.

## Requirements
- python 3.8
- keras
- tensorflow
- numpy

## To Use:
python generating_images.py {track}
- Here track is like: 3OW71NQ1TzF5ssYbdanIGN?si=610a6566c5454b7e&nd=1&dlsi=994f057055c44909 - {this is for Echo Sax End (Looped)}
- Track is some spotify track link

## What happens
- Script gets that track analysis from spotify
- Script passes the track segments into model
- Model outputs one colour for each segment into output.txt
    - each line in output.txt is a given segments colour in [r g b]
        - space delimited and floats between 0 and 1 (multiply by 255 to get usual [0...255] range of RGB)
        - I have attached an example
     
    



https://github.com/GeraldFreis/ColourGeneratorFromSongs/assets/91832029/50cbbd3d-9d0f-4abe-9e7e-edf9b1a5b874


