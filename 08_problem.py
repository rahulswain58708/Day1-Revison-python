x = [1, 2, 3]
y = x
y.append(4)
print(x)
# Why did x also change?
'''Because y = x does not create a new list, it only creates a new reference (or alias) to the same list in memory.

So both x and y point to the same object.

When you do y.append(4), you're modifying the list itself — and since x also points to that list, x reflects the change.'''