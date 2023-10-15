#import re

S = 'ABCCDCCDC'

sub = "CCD"

#str =" "

count = 0

'''for match in re.finditer("CD", s):
    count = count+1

print(count)'''

'''while sub in s:
    index = s.find(sub)
    str = s[:index]+s[index+1:]
    count = count+1


print(count)'''

while sub in S:
    i = S.find(sub)
    print("BEFORE", S)
    #print(S[:i])
    S = S[:i] + S[i + 2:]
    print("AFTER", S)
    count += 1

print(count)

'''k = sub in S
print(k)'''

