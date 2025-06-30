def count_words(string):
    word_count = {}
    
    words = string.lower().split()
    
    for word in words:
        clean_word = ''.join([char for char in word if char.isalpha()])
        if not clean_word:
            continue
        
        if clean_word in word_count:
            word_count[clean_word] += 1
        else:
            word_count[clean_word] = 1
    
    return word_count

print(count_words("A man, a plan, a canal -- Panama")) 
print(count_words("Doo bee doo bee doo")) 