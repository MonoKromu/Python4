def from_string_to_list(string, container):
    container += [int(i) for i in string.split()]


nums = [1, 5, 10]
from_string_to_list(input(), nums)
print(nums)
