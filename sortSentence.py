#Question -> https://leetcode.com/problems/sorting-the-sentence/
class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        orginal_sentence = ''
        words = s.split()
        ordered_words = [0 for _ in range(len(words))]

        for word in words:
            
            ordered_words[int(word[-1]) - 1] = word
            
        orginal_sentence=' '.join([word[0 : len(word)-1] for word in ordered_words])
        return orginal_sentence
        
            
        
