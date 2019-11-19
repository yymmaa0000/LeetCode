# 642. Design Search Autocomplete System
# Hard
# 55246FavoriteShare
# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:
# 1.  The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
# 2.  The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
# 3.  If less than 3 hot sentences exist, then just return as many as you can.
# 4.  When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
# Your job is to implement the following functions:
# The constructor function:
# AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.
# Now, the user wants to input a new sentence. The following function will provide the next character the user types:
# List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.
 
# Example:
# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
# The system have already tracked down the following sentences and their corresponding times:
# "i love you" : 5 times
# "island" : 3 times
# "ironman" : 2 times
# "i love leetcode" : 2 times
# Now, the user begins another search:

# Operation: input('i')
# Output: ["i love you", "island","i love leetcode"]
# Explanation:
# There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

# Operation: input(' ')
# Output: ["i love you","i love leetcode"]
# Explanation:
# There are only two sentences that have prefix "i ".

# Operation: input('a')
# Output: []
# Explanation:
# There are no sentences that have prefix "i a".

# Operation: input('#')
# Output: []
# Explanation:
# The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
 
# Note:
# 1.  The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
# 2.  The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
# 3.  Please use double-quote instead of single-quote when you write test cases even for a character input.
# 4.  Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
class Node:
    def __init__(self,val):
        self.val = val
        self.baby = [None]*27
        
class AutocompleteSystem:
    def to_int(self,char):
        if char == " ": return 0
        else: 
            char = char.lower()
            return ord(char) - ord("a")+1
        
    def to_char(self,num):
        if num == 0: return " "
        else: return chr(ord('a') + num - 1)
        
    def get_all_sentence(self,root):
        val = []
        result = []
        if root.val != 0: 
            result.append("")
            val.append(root.val)
        
        for i in range(len(root.baby)):
            x = root.baby[i]
            if x != None:
                temp,hot = self.get_all_sentence(x)
                if len(temp) == 0: 
                    result.append(self.to_char(i))
                else:
                    for y in temp:
                        result.append(self.to_char(i)+y)
                val.extend(hot)
        return result,val
    
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Node(0)
        self.cur = self.trie
        self.history = ""
        for i in range(len(sentences)):
            curr_node = self.trie
            for j in range(len(sentences[i])):
                branch = self.to_int(sentences[i][j])
                if curr_node.baby[branch] == None:
                    curr_node.baby[branch] = Node(0)
                curr_node = curr_node.baby[branch]
                if j == len(sentences[i]) - 1:
                    curr_node.val = times[i]
                    break
            
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.cur.val += 1
            self.cur = self.trie
            self.history = ""
            return []
        branch = self.to_int(c)
        self.history += c
        if self.cur.baby[branch] == None:
            self.cur.baby[branch] = Node(0)
            self.cur = self.cur.baby[branch]
            return []
        
        self.cur = self.cur.baby[branch]
        result = []
        word,val = self.get_all_sentence(self.cur)
        if len(word) < 2: result = word
        else:
            poop = []
            for x,y in zip(word,val):
                poop.append([x,y])
            poop.sort(key = lambda x:(-x[1],x[0]))
            poop 
            for i in range(min(len(poop),3)):
                result.append(poop[i][0])
        final_fuck = []
        if len(result) == 0:final_fuck = [self.history]
        else:
            for x in result:final_fuck.append(self.history+x)
        
        return final_fuck
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
