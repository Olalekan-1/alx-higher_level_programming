#!/usr/bin/python3
output = ""
for i in range(ord('Z'), ord('@'), -1):
    if i % 2 == 0:
        output += chr(i).lower()
    else:
        output += chr(i).upper()

print("{}".format(output), end="")
