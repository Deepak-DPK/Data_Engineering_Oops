a = [1, 2, 3]  # A list object is created. 'a' points to it.
b = a          # 'b' now points to the SAME list object.

b.append(4)    # We modify the object via 'b'.

print(a)       # Output: [1, 2, 3, 4] -> 'a' sees the change too!