# script to lookup fullname of target on google
# Usage: python fullname_lookup.py "fullname" "<API_KEY>" "<Search Engine ID>"
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4: # arg variables must be correct
        print("Usage: python fullname_lookup.py \"fullname\" \"<API_KEY>\" \"<Search Engine ID>\"")
        sys.exit(1)

    fullname = sys.argv[1]
    Project_API_KEY = sys.argv[2] # user must use their own API credentials
    Project_CX = sys.argv[3] # search engine ID

