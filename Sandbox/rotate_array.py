# Python3 implementation of right rotation
# of an array K number of times

# Function to rightRotate array
def RightRotate(a, n, k):

    # If rotation is greater
    # than size of array
    k = k % n;
    b = []
    for i in range(0, n):

        if(i < k):

            # Printing rightmost
            # kth elements
            #print(a[n + i - k], end = " ");
            b.append(a[n + i - k - 2])

        else:
            b.append(a[i - k])
            #Prints array after
            # 'k' elements
            #print(a[i - k], end = " ");


    print(b);

# Driver code
Array = [ 1, 2, 3, 4, 5, 6, 7];
N = len(Array);
K = 2;

RightRotate(Array, N, K);


