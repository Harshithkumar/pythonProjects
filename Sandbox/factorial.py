
from loguru import logger
from itertools import combinations
import snoop

@snoop
#@logger.catch()
def fact(x: int):
    if x==1:
        return 1
    else:
        return (x * fact(x-1))
num = 1
print(f"The factorial of {num} is {fact(num)}")



# 5* fact(4) = 20
# 4* fact(3) = 24
# 3* fact(2) = 6
# 2* fact(1) = 2
# 1* fact(0) = 1

