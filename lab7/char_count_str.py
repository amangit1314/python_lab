myStr = input("enter string : ")

freq = {}

for i in myStr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)
