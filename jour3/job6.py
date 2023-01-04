def alpha():
    alphabet=''
    for i in range(97,123):
        alphabet+=chr(i)
    return alphabet
i = 1
j = 0
alphabet = (alpha()*10)
while i < len(alphabet):
    print(alphabet[j:i])
    between = i-j
    j = i
    i += between + 1