
from .hash_table import Hash_table

def repeated_word(txt:str):
    string = txt.split(" ")
    hashy = Hash_table()
     
    for word in string:
        if "," in word:
            word = word.replace(',', "")
        if hashy.contain(word.lower()):
            return word
        hashy.add(word.lower(),1) 
    return "not found"

x= "Once upon a time, there was a brave princess who..."        
y = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
z = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
print(repeated_word(z))