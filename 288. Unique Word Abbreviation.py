# 288. Unique Word Abbreviation
# Medium
# 75978FavoriteShare
# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:
# a) it                      --> it    (no abbreviation)

#      1
#      ↓
# b) d|o|g                   --> d1g

#               1    1  1
#      1---5----0----5--8
#      ↓   ↓    ↓    ↓  ↓    
# c) i|nternationalizatio|n  --> i18n

#               1
#      1---5----0
#      ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
# Example:
# Given dictionary = [ "deer", "door", "cake", "card" ]

# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true
class ValidWordAbbr:
    def abv(self,word):
        if len(word) < 3: return word
        return word[0]+str(len(word)-2)+word[-1]
        

    def __init__(self, dictionary: List[str]):
        self.dictionary = dictionary
        self.dic = {}
        for x in set(dictionary):
            y = self.abv(x)
            if y not in self.dic: self.dic[y] = 1
            else: self.dic[y] += 1
        print(self.dic)
        print(self.dictionary)
        

    def isUnique(self, word: str) -> bool:
        x = self.abv(word)
        if x not in self.dic: return True
        if word not in self.dictionary: return False
        if self.dic[x] == 1: return True
        return False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
 
