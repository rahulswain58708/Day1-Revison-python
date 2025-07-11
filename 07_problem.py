a = 5
b = 0
print(bool(a), bool(b))
# Why does this happen?
'''bool(5) returns True because any non-zero number is considered True 
in a Boolean context.bool(0) returns False because zero is considered False.'''