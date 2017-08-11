
# Questions:
# Is the list ordered?
# Are the both positive and negative numbers?

# Naive aproach O(n^2)
# For each element on list, for each element on the list that is not itself, does it add up to it?

def indices_that_add_to_target_cuadratic(nums, target):
    n = len(nums)
    for i in range(0, n):
        current = nums[i]
        for j in range(0, n):
            if i == j:
                continue
            pair = nums[j]
            if current + pair == target:
                return [i, j]
    raise Exception("Didn't find a solution")

def indices_that_add_to_target_linear(nums, target):
    n = len(nums)
    complements = {}
    for i in range(0, n):
        current = nums[i]
        looking_for = target - current
        complement_index = complements.get(looking_for)
        if complement_index is None:
            complements[current] = i
        else:
            return [complement_index, i]
    raise Exception("Didn't find a solution")
