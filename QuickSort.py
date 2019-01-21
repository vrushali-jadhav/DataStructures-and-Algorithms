class QuickSort:
    def SortList(self, sortThisList, min, max):

        if min < max:
            seperator = self.FindSeperator(sortThisList,min,max)

            self.SortList(sortThisList,min,seperator-1)
            self.SortList(sortThisList,seperator+1,max)

        return sortThisList
    
    def FindSeperator(self, sortThisList, min, max):
        #make 1st element pivot
        pivot = sortThisList[min]

        i = min+1
        j=max

        done = False
        iflag = False
        jflag = False
        
        print("first:{0}".format(min))
        print("last:{0}".format(max))
        print("alist:{0}".format(sortThisList))
        
        while not done:
            
            if sortThisList[i]<= pivot and not iflag:
                i += 1
            else:
                iflag = True

            if sortThisList[j]>=pivot and not jflag:
                j -= 1
            else:
                jflag = True

            if i>j:
                done = True
            
            if iflag and jflag:
                tmp = sortThisList[i]
                sortThisList[i] = sortThisList[j]
                sortThisList[j] = tmp
                iflag = False
                jflag = False
        
        tmp = sortThisList[min]
        sortThisList[min] = sortThisList[j]
        sortThisList[j] = tmp 
        return j

if __name__=="__main__":
    listToBeSorted = [54,26,93,17,77,31,44,55,20]
    m = QuickSort()
    m.SortList(listToBeSorted,0,len(listToBeSorted)-1)
    print("Sorted list is:{0}".format(listToBeSorted))