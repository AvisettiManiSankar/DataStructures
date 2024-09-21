from collections import deque

def reverseString(word):
    stack = deque()
    for char in word:
        stack.append(char)

    word = ""
    
    while stack:
        word+=stack.pop()
    
    return word


word = "We will conquere COVI-19"

output = reverseString(word)
print(output)