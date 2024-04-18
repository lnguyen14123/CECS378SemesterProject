# script to lookup full name
# installation: pip install beautifulsoup4
#               pip install google
# Usage: python3 fullname_lookup.py "fullname" 
import sys
from googlesearch import search

if __name__ == "__main__":
    # Setting command line arguments to variables
    fullname = sys.argv[1]
    
    for j in search(fullname, tld="co.in", num=30, stop=15, pause=2):
        print(j)

