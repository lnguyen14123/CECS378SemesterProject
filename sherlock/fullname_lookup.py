# script to lookup full name
# installation: pip install beautifulsoup4
#               pip install google
# Usage: python3 fullname_lookup.py "fullname" 
import sys
import os
from googlesearch import search

if __name__ == "__main__":
    fullname = '-'.join(sys.argv[1:])  # Combines command line arguments into one string

    # Checks incase .txt file exits, is so remove it
    if os.path.exists(fullname):
        os.remove(fullname)
    file = open(fullname, "w")

    # Simulates a google search, writing each individual link into a file
    for j in search(fullname, tld="co.in", num=30, stop=15, pause=2):
        file.write(j + "\n")  

    file.close()