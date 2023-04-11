# # Python3 implementation to print left
# # rotation of any array K times
# from collections import deque
#
# # Function For The k Times Left Rotation
# def leftRotate(arr, k, n):
#
#     # The collections module has deque class
#     # which provides the rotate(), which is
#     # inbuilt function to allow rotation
#     arr = deque(arr)
#
#     # using rotate() to left rotate by k
#     arr.rotate(-k)
#     arr = list(arr)
#
#     # Print the rotated array from
#     # start position
#     for i in range(n):
#         print(arr[i], end = " ")
#
# # Driver Code
# if __name__ == '__main__':
#
#     arr = [ 1, 3, 5, 7, 9, 11, 13, 15]
#     n = len(arr)
#     k = 3
#
#     # Function Call
#     leftRotate(arr, k, n)

# This code is contributed by math_lover

#===========================================================================
#another wonderful solution
# Python implementation of left rotation of
# an array K number of times

# Function to leftRotate array multiple times


def leftRotate(arr, n, k):

    # To get the starting point of rotated array
    mod = k % n
    #output = [] Taking a new list to get the output

    # Prints the rotated array from start position
    for i in range(n):
        print(arr[(mod + i) % n], end=' ')
    #print(output)

# Driver code
arr = [1, 3, 5, 7, 9,11,13,15]
n = len(arr)
k = 3

# Function Call
leftRotate(arr, n, k)
#
# k = 3
#
# # Function Call
# leftRotate(arr, n, k)
#
# k = 4
#
# # Function Call
# leftRotate(arr, n, k)

# This code is contributed by Sachin Bisht
