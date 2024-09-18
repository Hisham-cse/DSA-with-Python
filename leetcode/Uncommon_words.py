class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        word1=s1.split()
        word2=s2.split()
        uncommon=[]
        for word in word1:
            if word1.count(word) ==1 and word not in word2 :
                uncommon.append(word)
        for word in word2:
            if word2.count(word)==1 and word not in word1:
                uncommon.append(word)
        return uncommon


s1="this apple is sweet"
s2="this apple is sour"
s=Solution()
print(s.uncommonFromSentences(s1,s2))