# some code which is supposed to generate a lot of calls

BIG_NUM = 1000

def fun3():
    pass

def fun2():
    for i in xrange(BIG_NUM):
        fun3()

def fun1():
    for i in xrange(BIG_NUM):
        fun2()


if __name__ == '__main__':
    fun1()
