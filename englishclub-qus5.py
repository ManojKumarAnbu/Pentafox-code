def compare(word1,word2):
    result=""
    for i in range(len(word1)):
        if word1[i] in word2:
            continue
        else:
            result=result+word1[i]
    return result
word1=input()
word2=input()
res1=compare(word1,word2)
res2=compare(word2,word1)
print(res1+res2)
