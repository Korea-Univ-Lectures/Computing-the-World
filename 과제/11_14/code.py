def selection_sort(arr):
    print(arr)
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)

def bubble_sort(arr):
    print(arr)
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
        print(arr)

def insertion_sort(arr):
    print(arr)
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        print(arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2-1]
    print(pivot)
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
            
    print(quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr))
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

if __name__ == "__main__":
    array = list([9, 12, 7, 4, 55, 2])
    #election_sort(array)
    #bubble_sort(array)
    #insertion_sort(array)
    arr = quick_sort(array)
    print(arr)
