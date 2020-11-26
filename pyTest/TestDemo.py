def hello(name):
    strHello = "Hello, " +name
    return strHello

print(hello("Python!"))

import sys
from loguru import logger

#logger.debug("That's it ,beautiful and simple logging!")

#logger.add("file_{time}.log")
#logger.add("file_1.log",rotation="100kb")

@logger.catch
def my_function(x,y,z):
    a = 1/(x+y+z)
    logger.info(a)
    return a

a = my_function(1,1,-2)
#logger.info(a)

import  pytest

