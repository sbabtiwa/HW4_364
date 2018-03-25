import requests
import json
from giphy_api_key import api_key

def get_gifs_from_giphy(search_string):
    """ Returns data from Giphy API with up to 5 gifs corresponding to the search input"""
    baseurl = "http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=5".format(search_string, api_key)
    gif_request = requests.get(baseurl)
    json_text = json.loads(gif_request.text)
    gif_list = []
    for each_gif in json_text["data"]:
    	gif_list.append(each_gif)
    print(gif_list)
    return gif_list


get_gifs_from_giphy(search_string = "happy")
    # TODO 364: This function should make a request to the Giphy API using the input search_string, and your api_key (imported at the top of this file)
    # Then the function should process the response in order to return a list of 5 gif dictionaries.
    # HINT: You'll want to use 3 parameters in the API request -- api_key, q, and limit. You may need to do a bit of nested data investigation and look for API documentation.
    # HINT 2: test out this function outside your Flask application, in a regular simple Python program, with a bunch of print statements and sample invocations, to make sure it works!
