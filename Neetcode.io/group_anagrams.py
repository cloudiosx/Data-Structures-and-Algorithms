# Sorting algorithm | Time: (m * nlogn) | Space: O(1) | m is the length of the input array and n is the length of the input strings
# Hashmap | Time: O(m*n*26) | Space: O(n) | m = total # of input strings we are given and n is the average length of each string

from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list) # https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work

    for str in strs:
        count = [0] * 26 # a ... z

        for char in str:
            count[ord(char) - ord("a")] += 1

        res[tuple(count)].append(str) # https://stackoverflow.com/questions/7257588/why-cant-i-use-a-list-as-a-dict-key-in-python

    return res.values()