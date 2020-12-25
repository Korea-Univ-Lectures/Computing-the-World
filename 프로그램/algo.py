def reverse1(A):
    i = 0
    B = [None]*len(A)
    i=0
    while i < (len(A)):
        B[len(A)-1-i] = A[i]
        i += 1
    return B

"""def reverse2(A):
    i = 0
    while i < (len(A)/2):
        A[i], A[len(A)-1-i] = A[len(A)-1-i], A[i]
        i += 1
    return A"""

def selection_sort(arr):
    print(arr)
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
    
    # n(n-1)/2

def bubble_sort(arr):
    print(arr)
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
        print(arr)
    # n(n-1)/2

def insertion_sort(arr):
    print(arr)
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        print(arr)
    # n(n-1)/2

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
    # n (log(n))

# 검색 알고리즘들
def BasicSearch(A, key):
    for i in range(0, len(A)):
        if key == A[i] : return key
    # n

def binary_search(A, first, last, key):
    if last < first : print('false')
    else :
        f_mid = (first+last)/2
        mid = int(f_mid)
        if key == A[mid] : print("found")
        elif key > A[mid]:
            binary_search(A, mid+1, last, key)
        else:
            binary_search(A, first, mid-1, key)

def TowerOfHanoi(n , source, destination, auxiliary): 
    if n==1: 
        print ("Move disk 1 from source",source,"to destination",destination )
        return

    TowerOfHanoi(n-1, source, auxiliary, destination) 
    print ("Move disk",n,"from source",source,"to destination",destination )
    TowerOfHanoi(n-1, auxiliary, destination, source) 
          
# Driver code 

# A, C, B are the name of rods 
  
# Contributed By Dilip Jain 

# 하노이 탑은 재귀적으로 해겱가능, n disks can be calculated as: 2^n - 1

def BubbleSort(li):
    list_length = len(li)

    #length가 4라면
    #바깥 루프는 3번 돌아야 하므로
    #range()는 0, 1, 2까지 즉 range(3)이 되야 하므로
    #range(list_length-1)이 되어야 한다.
    for i in range(list_length-1):
        print(li)
        #안쪽 루프는 1번당 3-> 2-> 1
        #즉 range(4 - 0 - 1) ->
        #range(4 - 1 - 1) ->
        #range(4 - 2 - 1)
        #range(list_leng - i - 1)
        for j in range(list_length-i-1):
            #만약 앞에 있는 값이 크다면 두 개를 교환
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


if __name__ == "__main__":
    li = [7, 20, 94, 1, 18, 25, 4]
    BubbleSort(li)
    print(li)

