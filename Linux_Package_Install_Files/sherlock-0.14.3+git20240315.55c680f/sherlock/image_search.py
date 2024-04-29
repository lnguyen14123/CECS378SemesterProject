# script that takes advantage of google search api to reverse image search pictures of target
# Usage: python image_search.py <image path> "<API_KEY>" "<Search Engine ID>"
import sys
# from google_images_search import GoogleImagesSearch

if __name__ == "__main__":
    if len(sys.argv) != 4: # arg variables must be correct
        print("Usage: python image_search.py <image_path> \"<API_KEY>\" \"<Search Engine ID>\"")
        sys.exit(1)

    image_path = sys.argv[1]
    Project_API_KEY = sys.argv[2] # user must use their own API credentials
    Project_CX = sys.argv[3] # search engine ID
