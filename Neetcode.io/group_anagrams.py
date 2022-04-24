# Sorting algorithm | Time: (m * nlogn) | Space: O(1) | m is the length of the input array and n is the length of the input strings
# Hashmap | Time: O(m*n*26) | Space: O(n) | m = total # of input strings we are given and n is the average length of each string

from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list)

    for str in strs:
        count = [0] * 26 # a ... z

        for char in str:
            count[ord(char) - ord("a")] += 1

        res[tuple(count)].append(str)

    return res.values()