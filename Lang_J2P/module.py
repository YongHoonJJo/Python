### Module ###

import mod1

print(mod1.sum(3, 4)) # 7

print(mod1.safe_sum(3, 5)) # 8
print(mod1.safe_sum(3, 'a')) 
# You can't add a to b
# None

from mod1 import sum, safe_sum
# from mod1 import *

print(sum(5, 10)) # 15

import mod2

a = mod2.Math()
print(a.solv(2)) # 12.566368


### another way to import module ###

# import sys
# sys.path # You can show the directory built in Python Library
# sys.path.append("~/Python/J2P/MyModules")

### setting PythonPATH

# set PYTHONPATH=C:\Python\Mymodules : win
