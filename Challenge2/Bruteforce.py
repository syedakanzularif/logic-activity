def window_bruteforce(log,pattern):
    if len(pattern)>len(log):
        return ""
    smallest=""
    for i in range(len(log)):
        for j in range(i,len(log)):
            sub=log[i:j+1]
            valid=True
            for ch in pattern:
                if sub.count(ch)<pattern.count(ch):
                    valid=False
                    break
            if valid:
                if smallest=="" or len(sub)<len(smallest):
                        smallest=sub
    return smallest
print(window_bruteforce("ADOBECODEBANC","ABC"))
