# file a.py
print("a", end='')

# file b.py
import a
print("b", end='')

# file c.py
print("c", end='')
import a
import b

