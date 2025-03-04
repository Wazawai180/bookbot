def get_word_count(file_contents):
    word_count = len(file_contents.split())
    return word_count

def character_count(file_contents):
    file_contents = file_contents.lower()
    char_count = {}
    for char in file_contents: #Iterate over text
        if char in char_count: #If the char is already in dict increment
            char_count[char] += 1
        else: #If not, add char with count 1
            char_count[char] = 1
    return char_count

def sort_on(d): #Sort key needed for sort_count (not sure why yet)
    return d["frequency"]

def sort_count(char_count): #Sorted list of dicts w/ chars & frequency
    frequency_list = []
    for char in char_count:
        frequency_list.append({"char": char, "frequency": char_count[char]})
    frequency_list.sort(reverse=True, key=sort_on)
    return frequency_list