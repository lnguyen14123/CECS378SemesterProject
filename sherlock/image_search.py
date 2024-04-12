# script that takes advantage of google search api to reverse image search pictures of target
# Usage: python image_search.py <image path> "<API_KEY>" "<Search Engine ID>"
import sys
from imgurpython import ImgurClient as imgur
import requests

# from google_images_search import GoogleImagesSearch

#Imgur Client: f0af1953936b647
#Imgur Secret: 15cf26798f8c0cdadf9953f82255a5c08e17f379
#Endpoint: https://api.imgur.com/3/image

client_id = 'f0af1953936b647'
client_secret = '15cf26798f8c0cdadf9953f82255a5c08e17f379'

def main(): 
    headers = {
        'Authorization': f"Client-ID {{{{{client_id}}}}}"
    }
    print("uploading")
    res = requests.post("https://api.imgur.com/3/image", headers=headers, data={"type": "image", "title": "Wombat testing upload", "image": "C:\\Users\\BryanPC\\Downloads\\wombatpic.png"})
    print(res.json())

    
if __name__ == "__main__":
    main()


