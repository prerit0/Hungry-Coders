# Create two versions of the number 100: one as an integer and one as a string. Show the difference by displaying their types and what happens when you try to add them

version_1_int = 100
version_2_string = '100'

print(version_1_int, type(version_1_int))
print(version_2_string, type(version_2_string))

print(version_1_int+version_1_int)
print(version_2_string+version_2_string)

# Expected Output (example)
# 100 <class 'int'>
# "100" <class 'str'>
# 200 (number addition)
# "100100" (string concatenation)