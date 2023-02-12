import time

start = time.time()

### Array 
# Q242. Valid Anagram
# 26ms (96%)
def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    map = {}
    for letter in s:
        appears = map.get(letter, 0)
        map[letter] = appears + 1
    for letter in t:
        appears = map.get(letter, 0)
        map[letter] = appears - 1
    print(len(map))
    for value in map.values():
        if value != 0:
            return False
    return True

end = time.time()
print(f"Run time: {(end-start) * 10000} miliseconds")