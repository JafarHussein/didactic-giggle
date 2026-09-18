# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]


class Solution:
    def groupAnagrams(self, strs):
        all_character_count=[]
        
        for word in strs:
            character_counter={}
            for character in word:
                if character in character_counter:
                    character_counter[character]+=1
                else:
                    character_counter[character]=1
                    
            all_character_count.append(character_counter)
            
        groups={}
        
        
        for original_word, count in zip(strs,all_character_count):
            key=tuple(sorted(count.items()))
            if key in groups:
                groups[key].append(original_word)
            else:
                groups[key]=[original_word]
                
                
        return list(groups.values())
    
strs = ["act","pots","tops","cat","stop","hat"]    
sol_instance=Solution()
print(sol_instance.groupAnagrams(strs))
            