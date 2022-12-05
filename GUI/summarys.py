import math
class Summary():
    def __init__(self, corpus):
        self.corpus = corpus
        self.paragraph = corpus.split("\n")
        self.D = len(self.paragraph)
        print(self.paragraph)
        print(self.D)
    
    def TermFrequency(self):
        unique_word = set(self.corpus.split(" "))
        tf = {}
        for uw in unique_word:
            tf[uw] = self.corpus.count(uw)
        return tf

        

s = Summary('''Hello world This is me Hello Hello World
123
456''')
print(s.TermFrequency())