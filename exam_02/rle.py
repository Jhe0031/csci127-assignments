def encode(s):
    list = []
    count = 0
    i = 0
    while i <= len(s)-1:
        if i == len(s)-1:
            count += 1
            list.append('[' + s[i] + ', ' + str(count) + ']')
        elif s[i] == s[i+1]:
            count += 1
        elif s[i] != s[i+1]:
            count += 1
            list.append('[' + s[i] + ', ' + str(count) + ']')
            count = 0
        i += 1
    return list
print(encode("abbaaacddaaa"))
print(encode("abcd"))
print(encode("cbbbbbdee"))

##Not complete
##new_s = []
##def decode():