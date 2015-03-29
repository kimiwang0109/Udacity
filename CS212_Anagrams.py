# -----------------
# User Instructions
# 
# This homework deals with anagrams. An anagram is a rearrangement 
# of the letters in a word to form one or more new words. 
#
# Your job is to write a function anagrams(), which takes as input 
# a phrase and an optional argument, shortest, which is an integer 
# that specifies the shortest acceptable word. Your function should
# return a set of all the possible combinations of anagrams. 
#
# Your function should not return every permutation of a multi word
# anagram: only the permutation where the words are in alphabetical
# order. For example, for the input string 'ANAGRAMS' the set that 
# your function returns should include 'AN ARM SAG', but should NOT 
# include 'ARM SAG AN', or 'SAG AN ARM', etc...
from copy import deepcopy

def anagrams(phrase, shortest=2):
    """Return a set of phrases with words from WORDS that form anagram
    of phrase. Spaces can be anywhere in phrase or anagram. All words 
    have length >= shortest. Phrases in answer must have words in 
    lexicographic order (not all permutations)."""
    # your code here
    phrase = phrase.replace(" ", '')
    words = sorted(list(find_words(phrase)))
    for elem in words:
        if len(elem) < shortest:
            words.remove(elem)
    #print words
    
    res = anagrams_helper(phrase, words, shortest, set(), [])
    results = set()
    for r in res:
        r = sorted(list(r))
        r = ' '.join(r)
        results.add(r)
    return results

def isSubstr(subphrase, phrase):
    for elem in subphrase:
        if subphrase.count(elem) > phrase.count(elem):
            return False
    return True  

def anagrams_helper(phrase, words, shortest, curSet, result):
    for i in range(len(words)-1):
        if isSubstr(words[i], phrase):
            temp = removed(phrase, words[i])
            #print phrase, temp, words[i]
            if temp == "":
                curSet_copy = deepcopy(curSet)
                curSet_copy.add(words[i])
                result.append(curSet_copy)
                #print result                
            elif len(temp) < shortest:
                continue
            else:
                curSet_copy = deepcopy(curSet)
                curSet_copy.add(words[i])
                #print 'o',curSet_copy               
                anagrams_helper(temp, words[i+1:], shortest, curSet_copy, result)
        else:
            continue
    return result     
                
# ------------
# Helpful functions
# 
# You may find the following functions useful. These functions
# are identical to those we defined in lecture. 

def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters

def find_words(letters):
    return extend_prefix('', letters, set())

def extend_prefix(pre, letters, results):
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre+L, letters.replace(L, '', 1), results)
    return results

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    "Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"
    wordset = set(open(filename).read().upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('words4k.txt')

# ------------
# Testing
# 
# Run the function test() to see if your function behaves as expected.

def test():
    assert 'DOCTOR WHO' in anagrams('TORCHWOOD')
    assert 'BOOK SEC TRY' in anagrams('OCTOBER SKY')
    assert 'SEE THEY' in anagrams('THE EYES')
    assert 'LIVES' in anagrams('ELVIS')
    assert anagrams('PYTHONIC') == set(['NTH PIC YO', 'NTH OY PIC', 'ON PIC THY', 'NO PIC THY', 'COY IN PHT','ICY NO PHT', 'ICY ON PHT', 'ICY NTH OP', 'COP IN THY', 'HYP ON TIC','CON PI THY', 'HYP NO TIC', 'COY NTH PI', 'CON HYP IT', 'COT HYP IN','CON HYP TI'])
    return 'tests pass'

#print anagrams('PYTHONIC') 
print test()
#print anagrams('ELVIS')