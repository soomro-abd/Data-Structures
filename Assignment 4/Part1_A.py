# Part1_A: Merge Sort

# Time complexity: O(nlogn)    0/5
def merge_sort(array):
# return sorted array
    length = len(array)

    if length == 1:
        return array

    midPoint = length // 2

    firstHalf = array[0: midPoint]
    secondHalf = array[midPoint :]

    firstHalf = merge_sort(firstHalf)
    secondHalf = merge_sort(secondHalf)

    return merge(firstHalf, secondHalf)


def merge(array1, array2):
    #merges the two arrays in a sorted order

    result = []

    while(array1 and array2):
        
        if array1[0] > array2[0]:
            result.append(array2[0])
            array2.pop(0)
        else:
            result.append(array1[0])
            array1.pop(0)

    if array1:
        result += array1
    
    result += array2
    
    return result

if __name__ == '__main__':
    # print(merge_sort([1,2,5,6,8,1,3,6,8,3,5,67]))
    pass
