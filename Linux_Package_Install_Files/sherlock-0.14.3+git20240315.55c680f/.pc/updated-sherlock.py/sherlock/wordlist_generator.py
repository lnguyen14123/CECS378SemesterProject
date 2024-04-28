# python script that should take in a raw txt file of words 
# that have been accumulated from social media webpages 
# preferably created by the target
import sys
import os
import scrape

def sorted_by_values(d): # return a sorted dictionary by values descending
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

# give an iterable (containing elements you want to write to file) and a filepath 
# to write values to file in append mode
def write_to_file(txt,filepath):
    with open(filepath, 'a') as file:
        for line in txt:
            file.write(f"{line}\n")

# can edit this function to filter out unnecessary words
def create_wrd_map(filepath):
    word_freq = dict()
    with open(filepath, "r") as file:
        for line in file:
            word = line.strip().lower()
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq

# pass in wordmap and a filepath to create permutations and write to file
#  writes in append mode
def generate_passwords(wmap, filepath):
    # special_char = set("!","@") # can implement later
    with open(filepath, 'a') as file:
        for wrd in wmap.keys():
            file.write(f"{wrd}\n") #write base word

            for i in range(10): # write all words starting with uppercase and ending with each digit
                upper = wrd[0].upper() + wrd[1:]
                file.write(f"{upper}{i}\n")

def main(words_file_path, output_path='target_wordlist.txt'):
    words = create_wrd_map(words_file_path) # create word frequency map from txt file of words that were scraped
    words = sorted_by_values(words)
    
    generate_passwords(words, output_path)
    os.remove(words_file_path) # done with words txt file
    
if __name__ == "__main__":
    main()

