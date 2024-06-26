# script that takes advantage of google search api to reverse image search pictures of target
import sys
from imgurpython import ImgurClient
from serpapi import GoogleSearch
import base64
import requests

def image_search(file_path, client_id, api_key, output_path='website_list.txt'): 
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
        "api_key": api_key
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
    if len(sys.argv) < 4:
        print("Usage: python3 image_search.py [image path] [Imgur Client ID] [SerpAPI Key]")
        sys.exit(1)
    image_search(sys.argv[1], sys.argv[2], sys.argv[3])


