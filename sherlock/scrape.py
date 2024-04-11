import requests
from bs4 import BeautifulSoup
import re

# Function to extract visible text from a webpage
def extract_visible_text(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=1)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.content, 'html.parser')
            visible_text = soup.get_text()
            visible_text_list = visible_text.split()

            # Define a regular expression pattern to match only alphanumeric characters
            alphanumeric_pattern = re.compile(r'[^A-Za-z0-9]')

            # Remove non-alphanumeric characters from each element in the array
            visible_text_list = [re.sub(alphanumeric_pattern, '', s) for s in visible_text_list]

            # remove words that are only 1 character or longer than 20
            visible_text_list = [elem for elem in visible_text_list if (len(elem) > 1  and len(elem) <= 20)]

            # shorten the list to 100 words max
            if(len(visible_text_list) > 100):
                visible_text_list = visible_text_list[:100]


            print(f"Successfully fetched URL: {url}.")

            return visible_text_list

        else:
            print(f"Failed to fetch URL: {url}. Status code: {response.status_code}")
            return None
    
    except requests.exceptions.Timeout:
        # Handle timeout
        print(f"Request timed out for: {url}")

    
    except Exception as e:
        print(f"Error fetching URL: {url}. Exception: {e}")
        return None


def main(username,file_path):
    urls = ""
    output_path = username + '_words.txt'

    # Open the text file in read mode
    with open((file_path), 'r') as file:
        # Read the entire contents of the file
        urls = file.read()

    # List of Sherlock URLs
    sherlock_urls_list = urls.strip().split('\n')
    sherlock_urls_list = sherlock_urls_list[:-1]
    # sherlock_urls_list = sherlock_urls_list[16:20] 

    # Extract visible text from each URL
    counter = 0
    total_len = len(sherlock_urls_list)

    with open(output_path, "w") as file:
        # remove contents if file already exists
        file.truncate(0)
    
    for url in sherlock_urls_list:
        # print(f"Fetching content from URL: {url}")
        counter = counter + 1
        print(f"{counter}/{total_len}", end=" ")
        visible_text = extract_visible_text(url)

        if visible_text:            
            with open(output_path, 'a') as file:
                for word in visible_text:
                    file.write(word)
                    file.write("\n")

    return output_path # return filepath for words



if __name__ == "__main__":
    main()