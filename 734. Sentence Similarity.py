# 734. Sentence Similarity
# Easy
# 138225FavoriteShare
# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.
# For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].
# Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.
# However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.
# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].
# Note:
# •   The length of words1 and words2 will not exceed 1000.
# •   The length of pairs will not exceed 2000.
# •   The length of each pairs[i] will be 2.
# •   The length of each words[i] and pairs[i][j] will be in the range [1, 20].
class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        dic = {}
        for x,y in pairs:
            if x not in dic: dic[x] = [y]
            else: dic[x].append(y)
        for i in range(len(words1)):
            if words1[i] == words2[i]: continue
            if words1[i] not in dic: 
                if words2[i] not in dic: return False
                if words1[i] not in dic[words2[i]]: return False
                continue
            if words2[i] not in dic:
                if words2[i] not in dic[words1[i]]: return False
                continue
            if (words2[i] not in dic[words1[i]]) and (words1[i] not in dic[words2[i]]):
                return False
        return True
