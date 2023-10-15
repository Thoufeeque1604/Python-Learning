'''def sort_without_function(a, dictt):
    length = len(a)
    for i in range(0, length):
        if a[i] == 0:
            dictt['count_z']+=1
        elif a[i] == 1:
            dictt['count_o']+=1
        else:
            dictt['count_t']+=1
    print(dictt)
    sorted_list = []
    for i in range(0, dictt['count_z']):
        sorted_list.append(0)
    for i in range(0, dictt['count_o']):
        sorted_list.append(1)
    for i in range(0, dictt['count_t']):
        sorted_list.append(2)
    print(sorted_list)
'''

if __name__ == "__main__":
    a = [0, 2, 1, 0, 1, 0, 1, 0, 0, 0, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 0]
    '''dictt ={
        'count_o': 0,
        'count_t': 0,
        'count_z': 0
        }'''
    #zero_list=[]
    zero_list = list(filter(lambda a: a==0, a))
    one_list = list(filter(lambda a: a==1,a))
    two_list = list(filter(lambda a: a==2,a))
    sorted = zero_list+one_list+two_list
    print(sorted)
    #sort_without_function(a, dictt)