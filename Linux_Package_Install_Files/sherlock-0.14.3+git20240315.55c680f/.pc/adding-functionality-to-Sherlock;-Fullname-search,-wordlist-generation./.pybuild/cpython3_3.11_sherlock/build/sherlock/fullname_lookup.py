# script to lookup full name
# installation: pip install beautifulsoup4
#               pip install google
# Usage: python3 fullname_lookup.py "fullname" 
import sys
import os
from googlesearch import search

def fullname_lookup(fullname):
    print(type(fullname))
    if type(fullname) == type("string"): #replace spaces with "_"
        file_name = f"{fullname.replace(' ', '_')}_name_search.txt"
    elif type(fullname) == type(["list"]):
        file_name = '_'.join(sys.argv[1:])  # Combines list of strings into one string

    # Opens .txt in append mode, creates if doesn't exist
    with open(file_name, 'a') as file:
        # Simulates a google search, writing each individual link into a file
        for j in search(fullname, tld="co.in", num=30, stop=15, pause=2):
            file.write(j + "\n")

    if os.path.exists(".google-cookie"):
        os.remove(".google-cookie")

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python3 fullname_lookup.py [fullname] ")
        sys.exit(1)
    fullname = " ".join((sys.argv[1:]))
    fullname_lookup(fullname)
    