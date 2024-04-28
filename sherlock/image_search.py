# script that takes advantage of google search api to reverse image search pictures of target
# Usage: python image_search.py <image path> "<API_KEY>" "<Search Engine ID>"
import sys
from imgurpython import ImgurClient as imgur
import requests
from serpapi import GoogleSearch
import base64

# from google_images_search import GoogleImagesSearch

#Imgur Client: f0af1953936b647
#Imgur Secret: 15cf26798f8c0cdadf9953f82255a5c08e17f379
#Endpoint: https://api.imgur.com/3/image

#Serp API Key: abdc4ceec32ee7065547ea930bc8b064f1fa7f6ff51fc46ad0246e682e82a160
#Endpoint: https://serpapi.com/search?engine=google_reverse_image

client_id = 'f0af1953936b647'
client_secret = '15cf26798f8c0cdadf9953f82255a5c08e17f379'
file_path = 'C:\\Users\\BryanPC\\Downloads\\lebron.jpg'

def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def main(output_path='website_list.txt'): 
    encoded_string = None
    websiteList = []

    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    headers = {
        'Authorization': 'Client-ID {}'.format(client_id)
    }

    print("uploading")
    res = requests.post(url="https://api.imgur.com/3/image", headers=headers, data={
        "image": encoded_string
    })
    resUpload = res.json()
    searchLink = resUpload['data']['link']
    print(searchLink)

    params = {
        "engine": "google_reverse_image",
        "image_url": searchLink,
        "api_key": "abdc4ceec32ee7065547ea930bc8b064f1fa7f6ff51fc46ad0246e682e82a160"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    image_results = results["image_results"]

    print(type(image_results))

    for dictionary in image_results:
        if "link" in dictionary:
            print(dictionary["link"])
            websiteList.append(dictionary["link"])
        if "sitelinks" in dictionary:
            for linkdict in dictionary["sitelinks"]["list"]:
                websiteList.append(linkdict["link"])
                print(linkdict["link"])

    with open(output_path, 'w') as file:
        for site in websiteList:
            file.write(f"{site}\n") #write base word
        file.close()
if __name__ == "__main__":
    main()


