def generate_power_set(arr):
    power_set = []
    l = len(arr)
    for i in range(2 ** l):
        temp_set = []
        binary_representation = to_binary(i, l)
        for j in range(len(binary_representation)):
            if binary_representation[j] == 1:
                temp_set.append(arr[j])
        power_set.append(temp_set)
    return power_set


def to_binary(n, bit_size):
    result = [0] * bit_size

    while n != 0:
        result[bit_size - 1] = n % 2
        n /= 2
        n = int(n)
        bit_size -= 1
    return result


print(generate_power_set([1, 2, 3]))
