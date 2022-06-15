# Part1_B: insertionSort


# Time complexity: O(n^2)    0/5


def insertion_sort(array):
    # return sorted array
    
    for i in range(len(array)):
        j = i

        while (j > 0) and array[j - 1] > array[j]:

            temp = array[j - 1]
            array[j - 1] = array[j]
            array[j] = temp

            j -= 1
    


    return array

    




if __name__ == '__main__':
    pass

