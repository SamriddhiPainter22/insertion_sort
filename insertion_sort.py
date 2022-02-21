#cresting function for insertion sort

def insertion_sort(list1):


    #outer loop to traverse 1to len(list1)

    for i in range(1,len(list1)):
        value=list1[i]

        j=i-1

        while j>=0 and value<list1[j]:
            list1[j+1]=list1[j]


            j-=1
            list1[j+1]=value

    return list1

    list1=[10,3,5,6,7]

    print("This is the unsorted list :",list1)

    print("This is the sorted list :",insertion_sort(list1))