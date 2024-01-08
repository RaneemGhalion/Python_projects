import random
import time

def naive_search(l,target):
    for i in range(len(l)):
        if l[i]==target:
            return i
    return -1



lst=[1,2,3,4,5,6,7,8,9,10]
# result=naive_search(lst,5)

# print(result)


# # binary search 
def binary_search(l,target,low=None,high=None):

    if low is None:
        low=0
    if high is None:
        high=len(l)-1
    midpoint=(low+high)//2
    # print(midpoint)
    if l[midpoint]==target:
        # print("lst",l[midpoint])
        return midpoint
    if l[midpoint]<target:
        low=midpoint+1
        # high=len(l)-1
        return binary_search(l,target,low,high)
    elif l[midpoint]>target:
        low=0
        high=midpoint-1
        return binary_search(l,target,low,high)
    else:
        print("not exist")




print(binary_search(lst,10,0,len(lst)-1))


if __name__=="__main__":

    length=1000
    sorted_list=set()
    while len(sorted_list)<length:
        sorted_list.add(random.randint(-3*length,3*length))

    sorted_list=sorted(list(sorted_list))
    start=time.time()
    for target in sorted_list:
        naive_search(sorted_list,target)
    end=time.time()

    print("naive search time ",(end-start)/length,"seconds")
    
    
    start=time.time()

    for target in sorted_list:
        naive_search(sorted_list,target)
    end=time.time()

    print("binary search time ",(end-start)/length,"seconds")
    


