# script to lookup full name
# installation: pip install beautifulsoup4
#               pip install google
# Usage: python3 fullname_lookup.py "fullname" 
# 
# Reference of Google Search:
# https://www.geeksforgeeks.org/performing-google-search-using-python-code/
import sys
import os
from googlesearch import search

def main():
    file_name = '_'.join(sys.argv[1:])  # Combines command line arguments into one string
    fullname =' '.join(sys.argv[1:])

    # Checks incase .txt file exits, is so remove it
    if os.path.exists(file_name):
        os.remove(file_name)
    file = open(file_name, "w")

    # Simulates a google search, writing each individual link into a file
    # "tld='com'" - the top level domain, set to Google USA
    # "num=30" - the number of search results per page
    # "stop=15" - the total number of search results to retrieve
    # "pause=2" - time to wait between HTTP request to Google, prevents two many request from occuring
    for j in search(fullname, tld="com", num=30, stop=15, pause=2):
        file.write(j + "\n")  

    file.close()

if __name__ == "__main__":
    main()
    
