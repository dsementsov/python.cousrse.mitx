
s = "itkedulgrouawlnejkmxml"

longest_substring = ""
for start in range(len(s)):
    end = 0
    current_substring = ""
    while True:
        if not current_substring or s[start+end] >= current_substring[-1]:
            current_substring += s[start+end]
        else:
            break
        end += 1
        if (start + end) >= len(s):
            break
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring
print ("Longest substring in alphabetical order is:", longest_substring)



longest_substring = ""
#'abcdefghijklmnopqrstuvwxyz'
for i in range(len(s)):
    current_substring = ""
    for char in s[i:]:
        if not current_substring or current_substring[-1] <= char:
            current_substring += char
        if len(current_substring) >= len(longest_substring):
            longest_substring = current_substring
print ("Longest substring in alphabetical order is:", longest_substring)