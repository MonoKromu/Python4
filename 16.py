def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        # sequence = sequence + [next_element]
        sequence += [next_element]


nums = [1, 1, 2]
print(nums)
continue_fibonacci_sequence(nums, 10)
print(nums)
