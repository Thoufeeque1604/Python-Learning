import string
'''def count_substring(string, sub_string):
    a[] = string
    b[] = sub_string

    return

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    #count =
    count_substring(string, sub_string)
    print(count_substring(string, sub_string))'''

'''str = input("enter string")
substr = input("enter substring")'''
'''a=list(str)
b=list(substr)
c = []
i=j=k=0
count =0
istrue = str.__contains__(substr)
print(istrue)
if istrue:
    for i in range(0, len(a)):
        if a[i] == b[j]:
            v = i
            for k in range(0, len(b)):
                c[k] = a[v]
                v = v+1
            x = ""
            x.join(c)
            if x==c:
                count +=1
else:
    print("the string doesnt contain substring")

'''
'''count = 0
for i in range(len(str)):
    if str[i:].startswith(substr):
        #count += 1
        print(i)

#print(count)'''

s = input()
a = s.split(" ")
v = ""
c= ""
'''new_str = s.capitalize()
i = new_str.index(" ")
new_str_2 = new_str.replace(new_str[i+1],new_str[i+1].upper())
print(new_str_2)'''
for i in range(0, len(a)):
    v = "".join(a[i]+"").capitalize()
    c +=v

print(c)

'''j = ""
a="hello"
b="baby"
c= "".join((a,b))
print (c)'''




