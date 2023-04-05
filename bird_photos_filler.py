import os
import json

species_x_remaining_photos = dict()

def json_to_dict(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

#restore the dict from the json dump
species_x_urls=json_to_dict('species_x_urls.json')
for species in species_x_urls:
    #print("Species: " + species + " urls: " + str(len(species_x_urls[species])))
    if len(species_x_urls[species]) < 200:
        remaining_photos = 200 - len(species_x_urls[species])
        species = species.replace("_", " ") # better to search without the underscore _ inside keyword
        species_x_remaining_photos[species] = remaining_photos

#print(species_x_remaining_photos)
for species in species_x_remaining_photos:
    remaining_photos = species_x_remaining_photos[species]
    species = species.replace(" ","_") #restore the underscore _ for inserting the scraped photos into the right folder
    os.system("python image_downloader.py \""+species+"\" -e Bing --driver api -n "+str(remaining_photos)+" -j 30 -t 10 -o ./download_images/"+species)