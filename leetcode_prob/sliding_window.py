
def sliding_window(given_arr, k_const):

    # n must be greater than k
    if k_const > len(given_arr):
        print("Invalid Input")
        exit(-1)

    # Compute sum of first window of size k
    window_sum = sum(arr[:k_const])
    print("current window sum : ", window_sum)

    # Compute sum of first window of size k
    max_sum = window_sum

    # Compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.
    for i in range(len(given_arr)-k_const):
        window_sum = window_sum - given_arr[i] + given_arr[i+k_const]
        max_sum = max(window_sum, max_sum)
    print(max_sum)


arr = [7, 2, 5, 1, 6, 9, 4]
k = 3
sliding_window(arr, k)
