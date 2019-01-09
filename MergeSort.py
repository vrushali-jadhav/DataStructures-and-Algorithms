
#Merge sort implementation
# Complexity: nlog(n)

def MergeSort(listToBeSorted):
    if len(listToBeSorted)>1:
        mid = len(listToBeSorted)//2
        leftList = listToBeSorted[:mid]
        rightList = listToBeSorted[mid:]
        
        print("Left: {0}".format(leftList))
        print("Right: {0}".format(rightList))

        MergeSort(leftList)
        MergeSort(rightList)

        i, j, k=0,0,0

        while i < len(leftList) and j < len(rightList):
            print("In while left: {0}".format(leftList))
            print("In while right: {0}".format(rightList))
            print("0:{0}".format(listToBeSorted))
            if leftList[i] < rightList[j]:
                #IMPORTANT: you have to update the same list. You cannot create a new list
                listToBeSorted[k] = leftList[i]
                i += 1
                print("1:{0}".format(listToBeSorted))
            else:
                listToBeSorted[k] = rightList[j]
                j += 1
                print("2:{0}".format(listToBeSorted))

            k = k+1 

        while j < len(rightList):
            listToBeSorted[k] = rightList[j]
            k = k+1
            j = j+1
            print("3:{0}".format(listToBeSorted))

        while i < len(leftList):
            listToBeSorted[k] = leftList[i]
            i = i+1
            k = k+1
            print("4:{0}".format(listToBeSorted))

        return listToBeSorted    

listToBeSorted = [54,26,93,17,77,31,44,55,20]
print("List to be sorted: {0}".format(listToBeSorted))
sortedList = MergeSort(listToBeSorted)
print("We have the sorted list!: {0}".format(sortedList))
