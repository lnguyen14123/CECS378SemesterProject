# script that takes advantage of google search api to reverse image search pictures of target
# Usage: python image_search.py <image path> "<API_KEY>" "<Search Engine ID>"
import sys
from imgurpython import ImgurClient as imgur
import requests
import base64

# from google_images_search import GoogleImagesSearch

#Imgur Client: f0af1953936b647
#Imgur Secret: 15cf26798f8c0cdadf9953f82255a5c08e17f379
#Endpoint: https://api.imgur.com/3/image

client_id = 'f0af1953936b647'
client_secret = '15cf26798f8c0cdadf9953f82255a5c08e17f379'
file_path = 'C:\\Users\\BryanPC\\Downloads\\wombatpic.jpg'

def main(): 
    encoded_string = None

    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    headers = {
        'Authorization': 'Client-ID {}'.format(client_id)
    }

    print(headers)
    print(encoded_string)
    print("uploading")
    res = requests.post(url="https://api.imgur.com/3/image", headers=headers, data={
        "image": encoded_string
    })
    print(res.json())

    
if __name__ == "__main__":
    main()


