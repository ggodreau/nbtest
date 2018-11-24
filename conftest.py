# this is the 'setup' file for all the other test in this
# and subdirectories!
import pytest
from out import wrap

print('hello world?')

gvar = 2

f= open("test.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close()


f=open("test.txt", "r")
print(i)
