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