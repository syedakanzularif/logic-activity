OPTIMIZED SOLUTION FOR PROBLEM 2
def minWindow(log, pattern):
    need = {}
    for ch in pattern:
        need[ch] = need.get(ch, 0) + 1
    have = {}
    left = 0
    count = 0
    min_len = float('inf')
    answer = ""
    for right in range(len(log)):
        ch = log[right]
        have[ch] = have.get(ch, 0) + 1
        if ch in need and have[ch] == need[ch]:
            count += 1
        while count == len(need):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                answer = log[left:right+1]
            have[log[left]] -= 1
            if log[left] in need and have[log[left]] < need[log[left]]:
                count -= 1
            left += 1
    return answer
print(minWindow("ADOBECODEBANC","ABC"))
print(minWindow("a","a"))
print(minWindow("a","aa"))


        
