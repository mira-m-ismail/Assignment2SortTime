def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2


        # splitting the array into odd and even indexed boxes
        odd_indexes = arr[1::2]
        even_indexes = arr[::2]


        #recursive calls for sorting odd and even indexed parts
        merge_sort(odd_indexes)
        merge_sort(even_indexes)


        # merging sorted odd and even indexed parts
        i = j = k = 0
        while i < len(odd_indexes) and j < len(even_indexes):
            if odd_indexes[i] < even_indexes[j]:
                arr[k]= odd_indexes[i]
                i += 1
            else:
                arr[k] = even_indexes[j]
                j += 1
            k += 1


        # checking if any element was left
        while i < len(odd_indexes):
            arr[k] = odd_indexes[i]
            i += 1


        while j < len(even_indexes):
            arr[k] = even_indexes[j]
            j += 1
            k += 1



def insertion_sort(arr):

    # transverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # move elements of arr[0..i-1] that are > than key.
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr



def quick_sort(arr):
    if(len(arr)) <= 1:
       return arr
    else:
        pivot = arr[0] #choose first element as pivot
                                                            # pivot = arr[random.randrange(0,len(arr)-1)] #random index
                                                            # pivot = arr[len(arr)-1]                     #last index
                                                            # pivot = arr[len(arr)//2]                    #middle index
        smaller = [] # to store elements smaller than pivot
        equal = [] # to store elements equal than pivot
        larger = [] # to store elements larger than pivot


        for x in arr:
            if x < pivot:
                smaller.append(x)
            elif x == pivot:	
                equal.append(x)
            else:
                larger.append(x)


        return quick_sort(smaller) + equal + quick_sort(larger)


def quick_insertion_sort(arr):
    def isSorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]: 
                    return False # if value of element is greater than the value of the next element, the list is not sorted
            return True
    
    if (len(arr)) <= 1:
       return arr   # base case 1
    elif len(arr) < 2:
        return arr  # base case 2
    elif len(arr) <= 10:
        return insertion_sort(arr)  # base case 3: switches to insertion sort when array is short in length due to its efficiency
    elif isSorted(arr) == True:
        return arr  # base case 4: if array is already sorted
    else:
        pivot = arr[0] #choose first element as pivot
                                                            # pivot = arr[random.randrange(0,len(arr)-1)] #random index
                                                            # pivot = arr[len(arr)-1]                     #last index
                                                            # pivot = arr[len(arr)//2]                    # middle index
        smaller = [] # to store elements smaller than pivot
        equal = [] # to store elements equal than pivot
        larger = [] # to store elements larger than pivot


        for x in arr:
            if x < pivot:
                smaller.append(x)
            elif x == pivot:	
                equal.append(x)
            else:
                larger.append(x)


        return quick_sort(smaller) + equal + quick_sort(larger)