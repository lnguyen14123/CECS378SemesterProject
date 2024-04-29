# python script that should take in a raw txt file of words 
# that have been accumulated from social media webpages 
# preferably created by the target
import os

def sorted_by_values(d): # return a sorted dictionary by values descending
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

# can edit this function to filter out unnecessary words
def create_wrd_map(filepath):
    word_freq = dict()
    possible_dates = set()
    with open(filepath, "r") as file:
        for line in file:
            word = line.strip().lower()
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
            if word.isnumeric():
                possible_dates.add(word)
    return word_freq, possible_dates

# pass in wordmap and a filepath to create permutations and write to file
#  writes in append mode
def generate_passwords(wmap, dates, filepath):
    special_char = set(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', ',', '.', '<', '>', '/', '?'])
    with open(filepath, 'a') as file:
        for wrd in wmap.keys():
            file.write(f"{wrd}\n") #write base word
            file.write(f"{wrd[0].upper()+wrd[1:]}\n") #capital only

            for date in dates:
                file.write(f"{wrd}{date}\n")
                file.write(f"{wrd[0].upper()}{wrd[1:]}{date}\n")
            for char in special_char:
                file.write(f"{wrd}{char}\n")
                file.write(f"{wrd[0].upper()}{wrd[1:]}{char}\n")
            for i in range(10): # write all words starting with uppercase and ending with each digit
                file.write(f"{wrd}{i}\n")
                file.write(f"{wrd[0].upper()}{wrd[1:]}{i}\n")

def gen_wordlist(words_file_path, output_path='target_wordlist.txt'):
    words,dates = create_wrd_map(words_file_path) # create word frequency map from txt file of words that were scraped
    # words = sorted_by_values(words)
    
    generate_passwords(words,dates,output_path)
    os.remove(words_file_path) # done with words txt file
    
if __name__ == "__main__":
    gen_wordlist("apex_fanatic2020_words.txt","apex_fanatic2020_wordlist.txt")

