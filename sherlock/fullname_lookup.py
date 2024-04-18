# script to lookup full name
# installation: pip install beautifulsoup4
#               pip install google
# Usage: python3 fullname_lookup.py "fullname" 
import sys
import os
from googlesearch import search

if __name__ == "__main__":
    if os.path.exists("fullname-search.txt"):
        os.remove("fullname-search.txt")

    # Setting command line arguments to variables
    fullname = sys.argv[1]
    file = open("fullname-search.txt", "w")

    
    for j in search(fullname, tld="co.in", num=30, stop=15, pause=2):
        file.write(j + "\n")

    file.close()
