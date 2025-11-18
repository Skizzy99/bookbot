def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def get_count_by_character(text):
    dictionary = {} 
    for char in text:
        c = char.lower()
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1 
    return dictionary

def sort_on(items):
    return items["num"]

def get_sorted_dicts(dictionary):
    dict_list = []
    
    for key in dictionary:
        char_dict = {}
        char_dict["char"] = key
        char_dict["num"] = dictionary[key]
        dict_list.append(char_dict)
        
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    

