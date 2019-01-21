
#Merge sort implementation
# Complexity: nlog(n)
# Space complexity: O(n)
# YOu are using the same variable 'sortTheList'. So when smaller list is sorted, the next call made to bigger list 
# that has the smaller list, it's left and right sides are already sorted

def MergeSort(sortTheList):
    if len(sortTheList)>1:
        mid = len(sortTheList)//2
        leftList = sortTheList[:mid]
        rightList = sortTheList[mid:]
        
        print("Left: {0}".format(leftList))
        print("Right: {0}".format(rightList))

        MergeSort(leftList)
        MergeSort(rightList)

        i, j, k=0,0,0

        while i < len(leftList) and j < len(rightList):
            print("In while left: {0}".format(leftList))
            print("In while right: {0}".format(rightList))
            print("0:{0}".format(sortTheList))
            if leftList[i] < rightList[j]:
                #IMPORTANT: you have to update the same list. You cannot create a new list
                sortTheList[k] = leftList[i]
                i += 1
                print("1:{0}".format(sortTheList))
            else:
                sortTheList[k] = rightList[j]
                j += 1
                print("2:{0}".format(sortTheList))

            k = k+1 

        while j < len(rightList):
            sortTheList[k] = rightList[j]
            k = k+1
            j = j+1
            print("3:{0}".format(sortTheList))

        while i < len(leftList):
            sortTheList[k] = leftList[i]
            i = i+1
            k = k+1
            print("4:{0}".format(sortTheList))

        print("List to be sorted1:{0}".format(sortTheList))

        return sortTheList    

listToBeSorted = [54,26,93,17,77,31,44,55,20]
print("List to be sorted: {0}".format(listToBeSorted))
sortedList = MergeSort(listToBeSorted)
print("We have the sorted list!: {0}".format(sortedList))