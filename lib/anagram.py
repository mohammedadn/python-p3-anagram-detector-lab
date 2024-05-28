# your code goes here!
# your code goes here!
class Anagram():
    
    def __init__(self, word):
        self.words = sorted([letter for letter in word]) 
    
    def match(self,  arr):        
        matched = []
        for i in arr:
            if sorted([letter for letter in i]) == self.words:
                matched.append(i)

        return matched
   
    