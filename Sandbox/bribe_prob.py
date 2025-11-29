def minimum_bribes(q):
    bribes = 0
    for i in range(len(q)-1, -1, -1):
        # Check if any person has moved more than two positions forward
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        bribe_max = max(0, q[i] - 2)
        # Count the number of bribes by checking how many people each person has passed
        for j in range(bribe_max, i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)

# Example usage:
q1 = [1, 2, 3, 5, 4, 6, 7, 8]
q2 = [4, 1, 2, 3]
minimum_bribes(q1)  # Output: 1
minimum_bribes(q2)  # Output: Too chaotic
