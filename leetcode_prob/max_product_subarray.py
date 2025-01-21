input_array = [2, 3, -2, -4]


def max_prod_subarray(input_array):
    max_product = input_array[0]
    min_product = input_array[0]
    result = input_array[0]

    for i in range(1, len(input_array)):
        num = input_array[i]
        if num < 0:
            max_product, min_product = min_product, max_product

        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        result = max(result, max_product)

        return result


final_result = max_prod_subarray(input_array)
print(final_result)
