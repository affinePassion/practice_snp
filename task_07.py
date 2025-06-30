def combine_anagrams(words_array):
    anagram_groups = {}
    
    for word in words_array:
        sorted_letters = ''.join(sorted(word.lower()))
        
        if sorted_letters in anagram_groups:
            anagram_groups[sorted_letters].append(word)
        else:
            anagram_groups[sorted_letters] = [word]
    
    return list(anagram_groups.values())

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))