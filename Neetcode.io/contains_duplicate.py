# Brute force nested loops | Time: O(n^2) | Space: O(1) | n = length of the array, size of the input array
# Sorting algorithm | Time: O(nlogn) | Space: O(1) | n = length of the array, size of the input array
# Hashset | Time: O(n) | Space: O(n) | n = length of the array, size of the input array
def containsDuplicate(nums) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False
