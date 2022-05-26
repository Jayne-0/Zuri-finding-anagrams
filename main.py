# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagrams(word1, word2):
# [assignment] Add your code here
    if(sorted(word1)==sorted(word2)):
      return True
    else:
      return False

# find_anagrams("hello", "ello")
# find_anagrams("crook", "rocko")
# find_anagrams("cool", "cool")

print(find_anagrams("hello", "ello")) 
print(find_anagrams("crook", "rocko")) 
print(find_anagrams("cool", "cool"))

def find_anagram(word, anagram):
    # [assignment] Add your code here

    return True

