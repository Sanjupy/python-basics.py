from itertools import count


def word_count(str):
    counts=dict()
    words=str.split()  #words is taken because str is converted into list during this

    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts
print(word_count("this is sanjeev kumar"))


    







print(word_count("this is sanjeev kumar"))