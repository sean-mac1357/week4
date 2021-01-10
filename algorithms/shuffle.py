import random
# Given a string s and an integer list indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.


s = "odce"
indices = [1, 2, 0, 3]
ans = ""

for i in range(len(indices)):
    ans += s[indices.index(i)]
print(ans)
