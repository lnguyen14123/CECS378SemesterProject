Description: <short summary of the patch>
 TODO: Put a short summary on the line above and replace this paragraph
 with a longer explanation of this change. Complete the meta-information
 with other relevant fields (see below for details). To make it easier, the
 information below has been extracted from the changelog. Adjust it or drop
 it.
 .
 sherlock (0.14.3+git20240315.55c680f-1) unstable; urgency=medium
 .
   * New upstream version 0.14.3+git20240315.55c680f
Author: Josenilson Ferreira da Silva <nilsonfsilva@hotmail.com>

---
The information above should follow the Patch Tagging Guidelines, please
checkout https://dep.debian.net/deps/dep3/ to learn about the format. Here
are templates for supplementary fields that you might want to add:

Origin: (upstream|backport|vendor|other), (<patch-url>|commit:<commit-id>)
Bug: <upstream-bugtracker-url>
Bug-Debian: https://bugs.debian.org/<bugnumber>
Bug-Ubuntu: https://launchpad.net/bugs/<bugnumber>
Forwarded: (no|not-needed|<patch-forwarded-url>)
Applied-Upstream: <version>, (<commit-url>|commit:<commid-id>)
Reviewed-By: <name and email of someone who approved/reviewed the patch>
Last-Update: 2024-04-20

--- sherlock-0.14.3+git20240315.55c680f.orig/.pybuild/cpython3_3.11_sherlock/build/sherlock/fullname_lookup.py
+++ sherlock-0.14.3+git20240315.55c680f/.pybuild/cpython3_3.11_sherlock/build/sherlock/fullname_lookup.py
@@ -1,13 +1,31 @@
-# script to lookup fullname of target on google
-# Usage: python fullname_lookup.py "fullname" "<API_KEY>" "<Search Engine ID>"
+# script to lookup full name
+# installation: pip install beautifulsoup4
+#               pip install google
+# Usage: python3 fullname_lookup.py "fullname" 
 import sys
+import os
+from googlesearch import search
 
-if __name__ == "__main__":
-    if len(sys.argv) != 4: # arg variables must be correct
-        print("Usage: python fullname_lookup.py \"fullname\" \"<API_KEY>\" \"<Search Engine ID>\"")
-        sys.exit(1)
+def fullname_lookup(fullname):
+    print(type(fullname))
+    if type(fullname) == type("string"): #replace spaces with "_"
+        file_name = f"{fullname.replace(' ', '_')}_name_search.txt"
+    elif type(fullname) == type(["list"]):
+        file_name = '_'.join(sys.argv[1:])  # Combines list of strings into one string
+
+    # Opens .txt in append mode, creates if doesn't exist
+    with open(file_name, 'a') as file:
+        # Simulates a google search, writing each individual link into a file
+        for j in search(fullname, tld="co.in", num=30, stop=15, pause=2):
+            file.write(j + "\n")
 
-    fullname = sys.argv[1]
-    Project_API_KEY = sys.argv[2] # user must use their own API credentials
-    Project_CX = sys.argv[3] # search engine ID
+    if os.path.exists(".google-cookie"):
+        os.remove(".google-cookie")
 
+if __name__ == "__main__":
+    if len(sys.argv) < 1:
+        print("Usage: python3 fullname_lookup.py [fullname] ")
+        sys.exit(1)
+    fullname = " ".join((sys.argv[1:]))
+    fullname_lookup(fullname)
+    
\ No newline at end of file
--- sherlock-0.14.3+git20240315.55c680f.orig/.pybuild/cpython3_3.11_sherlock/build/sherlock/sherlock.py
+++ sherlock-0.14.3+git20240315.55c680f/.pybuild/cpython3_3.11_sherlock/build/sherlock/sherlock.py
@@ -28,8 +28,9 @@ from .sites import SitesInformation
 from colorama import init
 from argparse import ArgumentTypeError
 
-### importing modules our team needs
+### importing additional modules our team needs
 from bs4 import BeautifulSoup
+from googlesearch import search
 ###
 module_name = "Sherlock: Find Usernames Across Social Networks"
 __version__ = "0.14.3"
@@ -121,6 +122,7 @@ def generate_passwords(wmap, filepath):
     with open(filepath, 'a') as file:
         for wrd in wmap.keys():
             file.write(f"{wrd}\n") #write base word
+            file.write(f"{wrd[0].upper()+wrd[1:]}") #capital only
 
             for i in range(10): # write all words starting with uppercase and ending with each digit
                 upper = wrd[0].upper() + wrd[1:]
@@ -135,7 +137,6 @@ def gen_wordlist(words_file_path, output
 ###
 
 ### from scrape.py
-
 # Function to extract visible text from a webpage
 def extract_visible_text(url):
     try:
@@ -217,6 +218,23 @@ def scrape(username,file_path):
     return output_path # return filepath for words
 ###
 
+### from fullname_lookup.py
+# pass in a string
+def fullname_lookup(fullname):
+    file_name = f"{fullname.replace(' ', '_')}_name_search.txt"
+
+    count = 0
+    # Opens .txt in append mode, creates if doesn't exist
+    with open(file_name, 'a') as file:
+        # Simulates a google search, writing each individual link into a file
+        for j in search(fullname, tld="co.in", num=30, stop=15, pause=2):
+            file.write(j + "\n")
+            count += 1
+
+    if os.path.exists(".google-cookie"):
+        os.remove(".google-cookie")
+    return count
+###
 def get_response(request_future, error_type, social_network):
     # Default for Response object if some failure occurs.
     response = None
@@ -734,7 +752,7 @@ def main():
     )
     parser.add_argument(
         "username",
-        nargs="+",
+        nargs="*",
         metavar="USERNAMES",
         action="store",
         help="One or more usernames to check with social networks. Check similar usernames using {?} (replace to '_', '-', '.').",
@@ -762,17 +780,25 @@ def main():
         default=False,
         help="Include checking of NSFW sites from default list.",
     )
-
+    ### added by our team
     parser.add_argument(
-        "--wordlist",
+        "--wordlist", 
         "-w",
         action="store_true",
-        default=True,
+        default=False,
         help="Scrape words from found websites and create a wordlist from them.",
     )
+    parser.add_argument(
+        "--name-search",
+        "-ns",
+        dest="name_search",
+        default=None,
+        help="Lookup a target by their fullname on google. Receive a file of links.",
+    )
+    ###
 
     args = parser.parse_args()
-    # print(args)
+    # print(type(args.name_search))
 
     # If the user presses CTRL-C, exit gracefully without throwing errors
     signal.signal(signal.SIGINT, handler)
@@ -795,6 +821,13 @@ def main():
     except Exception as error:
         print(f"A problem occurred while checking for an update: {error}")
 
+    if args.name_search is not None:
+        print(f"Conducting name search of \"{args.name_search}\" on google...")
+        count = fullname_lookup(args.name_search)
+        print(f"Name search completed with {count} results.")
+        if len(args.username) == 0:
+            sys.exit(1)
+
     # Argument check
     # TODO regex check on args.proxy
     if args.tor and (args.proxy is not None):
--- sherlock-0.14.3+git20240315.55c680f.orig/.pybuild/cpython3_3.12_sherlock/build/sherlock/fullname_lookup.py
+++ sherlock-0.14.3+git20240315.55c680f/.pybuild/cpython3_3.12_sherlock/build/sherlock/fullname_lookup.py
@@ -1,13 +1,31 @@
-# script to lookup fullname of target on google
-# Usage: python fullname_lookup.py "fullname" "<API_KEY>" "<Search Engine ID>"
+# script to lookup full name
+# installation: pip install beautifulsoup4
+#               pip install google
+# Usage: python3 fullname_lookup.py "fullname" 
 import sys
+import os
+from googlesearch import search
 
-if __name__ == "__main__":
-    if len(sys.argv) != 4: # arg variables must be correct
-        print("Usage: python fullname_lookup.py \"fullname\" \"<API_KEY>\" \"<Search Engine ID>\"")
-        sys.exit(1)
+def fullname_lookup(fullname):
+    print(type(fullname))
+    if type(fullname) == type("string"): #replace spaces with "_"
+        file_name = f"{fullname.replace(' ', '_')}_name_search.txt"
+    elif type(fullname) == type(["list"]):
+        file_name = '_'.join(sys.argv[1:])  # Combines list of strings into one string
+
+    # Opens .txt in append mode, creates if doesn't exist
+    with open(file_name, 'a') as file:
+        # Simulates a google search, writing each individual link into a file
+        for j in search(fullname, tld="co.in", num=30, stop=15, pause=2):
+            file.write(j + "\n")
 
-    fullname = sys.argv[1]
-    Project_API_KEY = sys.argv[2] # user must use their own API credentials
-    Project_CX = sys.argv[3] # search engine ID
+    if os.path.exists(".google-cookie"):
+        os.remove(".google-cookie")
 
+if __name__ == "__main__":
+    if len(sys.argv) < 1:
+        print("Usage: python3 fullname_lookup.py [fullname] ")
+        sys.exit(1)
+    fullname = " ".join((sys.argv[1:]))
+    fullname_lookup(fullname)
+    
\ No newline at end of file
--- sherlock-0.14.3+git20240315.55c680f.orig/.pybuild/cpython3_3.12_sherlock/build/sherlock/sherlock.py
+++ sherlock-0.14.3+git20240315.55c680f/.pybuild/cpython3_3.12_sherlock/build/sherlock/sherlock.py
@@ -28,8 +28,9 @@ from .sites import SitesInformation
 from colorama import init
 from argparse import ArgumentTypeError
 
-### importing modules our team needs
+### importing additional modules our team needs
 from bs4 import BeautifulSoup
+from googlesearch import search
 ###
 module_name = "Sherlock: Find Usernames Across Social Networks"
 __version__ = "0.14.3"
@@ -121,6 +122,7 @@ def generate_passwords(wmap, filepath):
     with open(filepath, 'a') as file:
         for wrd in wmap.keys():
             file.write(f"{wrd}\n") #write base word
+            file.write(f"{wrd[0].upper()+wrd[1:]}") #capital only
 
             for i in range(10): # write all words starting with uppercase and ending with each digit
                 upper = wrd[0].upper() + wrd[1:]
@@ -135,7 +137,6 @@ def gen_wordlist(words_file_path, output
 ###
 
 ### from scrape.py
-
 # Function to extract visible text from a webpage
 def extract_visible_text(url):
     try:
@@ -217,6 +218,23 @@ def scrape(username,file_path):
     return output_path # return filepath for words
 ###
 
+### from fullname_lookup.py
+# pass in a string
+def fullname_lookup(fullname):
+    file_name = f"{fullname.replace(' ', '_')}_name_search.txt"
+
+    count = 0
+    # Opens .txt in append mode, creates if doesn't exist
+    with open(file_name, 'a') as file:
+        # Simulates a google search, writing each individual link into a file
+        for j in search(fullname, tld="co.in", num=30, stop=15, pause=2):
+            file.write(j + "\n")
+            count += 1
+
+    if os.path.exists(".google-cookie"):
+        os.remove(".google-cookie")
+    return count
+###
 def get_response(request_future, error_type, social_network):
     # Default for Response object if some failure occurs.
     response = None
@@ -734,7 +752,7 @@ def main():
     )
     parser.add_argument(
         "username",
-        nargs="+",
+        nargs="*",
         metavar="USERNAMES",
         action="store",
         help="One or more usernames to check with social networks. Check similar usernames using {?} (replace to '_', '-', '.').",
@@ -762,17 +780,25 @@ def main():
         default=False,
         help="Include checking of NSFW sites from default list.",
     )
-
+    ### added by our team
     parser.add_argument(
-        "--wordlist",
+        "--wordlist", 
         "-w",
         action="store_true",
-        default=True,
+        default=False,
         help="Scrape words from found websites and create a wordlist from them.",
     )
+    parser.add_argument(
+        "--name-search",
+        "-ns",
+        dest="name_search",
+        default=None,
+        help="Lookup a target by their fullname on google. Receive a file of links.",
+    )
+    ###
 
     args = parser.parse_args()
-    # print(args)
+    # print(type(args.name_search))
 
     # If the user presses CTRL-C, exit gracefully without throwing errors
     signal.signal(signal.SIGINT, handler)
@@ -795,6 +821,13 @@ def main():
     except Exception as error:
         print(f"A problem occurred while checking for an update: {error}")
 
+    if args.name_search is not None:
+        print(f"Conducting name search of \"{args.name_search}\" on google...")
+        count = fullname_lookup(args.name_search)
+        print(f"Name search completed with {count} results.")
+        if len(args.username) == 0:
+            sys.exit(1)
+
     # Argument check
     # TODO regex check on args.proxy
     if args.tor and (args.proxy is not None):
--- sherlock-0.14.3+git20240315.55c680f.orig/sherlock.egg-info/requires.txt
+++ sherlock-0.14.3+git20240315.55c680f/sherlock.egg-info/requires.txt
@@ -1,7 +1,9 @@
 PySocks>=1.7.0
+beautifulsoup4>=4.12.2
 certifi>=2019.6.16
 colorama>=0.4.1
 exrex>=0.11.0
+google>=3.0.0
 openpyxl<=3.0.10
 pandas>=1.0.0
 requests-futures>=1.0.0
--- sherlock-0.14.3+git20240315.55c680f.orig/sherlock/sherlock.py
+++ sherlock-0.14.3+git20240315.55c680f/sherlock/sherlock.py
@@ -821,6 +821,7 @@ def main():
     except Exception as error:
         print(f"A problem occurred while checking for an update: {error}")
 
+    ### added by our team
     if args.name_search is not None:
         print(f"Conducting name search of \"{args.name_search}\" on google...")
         count = fullname_lookup(args.name_search)
@@ -828,6 +829,12 @@ def main():
         if len(args.username) == 0:
             sys.exit(1)
 
+    if len(args.username) == 0:
+        parser.print_usage()
+        print("You must have a username and/or name search argument.")
+        sys.exit(1)
+    ###
+
     # Argument check
     # TODO regex check on args.proxy
     if args.tor and (args.proxy is not None):
--- sherlock-0.14.3+git20240315.55c680f.orig/sherlock/wordlist_generator.py
+++ sherlock-0.14.3+git20240315.55c680f/sherlock/wordlist_generator.py
@@ -1,20 +1,11 @@
 # python script that should take in a raw txt file of words 
 # that have been accumulated from social media webpages 
 # preferably created by the target
-import sys
 import os
-import scrape
 
 def sorted_by_values(d): # return a sorted dictionary by values descending
     return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
 
-# give an iterable (containing elements you want to write to file) and a filepath 
-# to write values to file in append mode
-def write_to_file(txt,filepath):
-    with open(filepath, 'a') as file:
-        for line in txt:
-            file.write(f"{line}\n")
-
 # can edit this function to filter out unnecessary words
 def create_wrd_map(filepath):
     word_freq = dict()
@@ -35,12 +26,13 @@ def generate_passwords(wmap, filepath):
     with open(filepath, 'a') as file:
         for wrd in wmap.keys():
             file.write(f"{wrd}\n") #write base word
-
+            file.write(f"{wrd[0].upper()+wrd[1:]}") #capital only
+            
             for i in range(10): # write all words starting with uppercase and ending with each digit
                 upper = wrd[0].upper() + wrd[1:]
                 file.write(f"{upper}{i}\n")
 
-def main(words_file_path, output_path='target_wordlist.txt'):
+def gen_wordlist(words_file_path, output_path='target_wordlist.txt'):
     words = create_wrd_map(words_file_path) # create word frequency map from txt file of words that were scraped
     words = sorted_by_values(words)
     
@@ -48,5 +40,4 @@ def main(words_file_path, output_path='t
     os.remove(words_file_path) # done with words txt file
     
 if __name__ == "__main__":
-    main()
-
+    gen_wordlist()
\ No newline at end of file
