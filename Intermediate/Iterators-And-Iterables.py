# ###### Iterators And Iterables ######

# =================================
# Using a class

class MyRange:
    
    def __init__(self,start,end):
        self.value = start
        self.end = end
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1,10)

for num in nums:
    print(num,end=" ")
# =================================        
# Using a function

def myrange(start,end):
    current = start
    while current < end:
        yield current
        current += 1
        
nums = myrange(1,10)

for num in nums:
    print(num,end=" ")
# =================================            
# Example
# ---------------------------------        
# Using a class

class test:
    
    def __init__(self,Sentence):
        self.Sentence = Sentence
        self.index = 0
        self.words = self.Sentence.split()
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]
    
my_sentence = test("This is a test")

for word in my_sentence:
    print(word)    
# ---------------------------------        
# Using a function

def sentence(sentence):
    for word in sentence.split():
        yield word

my_sentence = sentence("This is a test")

print(my_sentence)
print(next(my_sentence))
print(next(my_sentence))
