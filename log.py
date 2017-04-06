# _*_ coding:utf-8 _*_
import functools

def log(func):

    @functools.wraps(func)
    def wrapper(*args, **kw):
        print ('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def logger(text='DEBUG'):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kw):
            print ('%s %s:' % (text, func.__name__))
            returnvalue = func(*args, **kw)
            print ('hello, world!')
            return returnvalue
        return wapper
    return decorator

@log
def now():
    print ('2017-03-05')

@logger('execute')
def today():
    print ('2017-03-06')




today()

now()
