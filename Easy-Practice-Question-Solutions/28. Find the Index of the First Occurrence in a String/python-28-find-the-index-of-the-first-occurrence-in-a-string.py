def strStr(haystack: str, needle: str):
    if needle not in haystack:
        return -1
    
    return haystack.find(needle)

print(strStr("sadbutsad", "sad"))