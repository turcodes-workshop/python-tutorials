
# args = tuple, keywordargs->kwargs = dict

def userInfo(*args):
    # print(type(args))
    print(args)
    

# print(userInfo("hasan",1231231))


def userInfo(**kwargs):
    # print(type(kwargs))
    print(kwargs)
    for key,val in kwargs.items():
        print(f"{key} {val}")


# print(userInfo(hasan=123,test=12341234))


def ordering(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

ordering(1,2,3,45,56,546,19,156,19,hasan="123",test="0410,")
