'''def insert_item(a,b):
    list.insert(a,b)

def remove_item(a):
    list.remove(a)

def append_item(a):
    list.append(a)

def sort_item():
    list.sort()

def pop_item():
    list.pop()

def reverse_item():
    list.reverse()

n = int(input())
list = []
cmd = []
for i in range(0,n):
    cmd =input().split()
    if cmd[0]=="insert":
        a = int(cmd[1])
        b = int(cmd[2])
        insert_item(a,b)
    elif cmd[0]=="remove":
        a = int(cmd[1])
        remove_item(a)
    elif cmd[0]=="append":
        a = int(cmd[1])
        append_item(a)
    elif cmd[0]=="sort":
        sort_item()
    elif cmd[0]=="pop":
        pop_item()
    elif cmd[0]=="reverse":
        reverse_item()
    else:
        print(list)'''

'''n = int(input())
list = []
cmd = []
#for _ in range(n):
s = input().split()
cmd = s[0]
args = s[1:]
if cmd !="print":
    #cmd += "("+ ",".join(args) +")"
    cmd = cmd+"("+ ",".join(args) +")"
        #eval("l."+cmd)
    print(cmd)
    else:
        print l'''













#print (cmd)