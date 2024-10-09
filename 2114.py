class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max=0
        for sentence in sentences:
            count=len(sentence.split())
            if count>max:
                max=count
        return max
