##def f():
##    s = 'this is local variable'
##    print(s)
##
##f()
##print(s)


##a = 10 # global variable, throu
##
##def fun():
##    a = 15 # local variable, local to fun()
##    print("In function", a)
##    print("Address of a in function", id(a))
##
##fun()
##print("Outsid the function", a)
##print("Address of a outside the function", id(a))

##def fun():
##    print("Accessing from another function", z)
##
##z = 10 # global variable
##fun()
##print("Accessing globally", z)

##def fun():
##    a = 'this is inside function'
##    print(a)
##
##fun()
##print("outside the function", a)

##a = 10
##
##def fun1():
##    print("Accessing from fun1()", a)
##    
##def fun2():
##    b = 20
##    print("Adding local variable b and global variable a", a + b)
##    
##def fun3():
##    a += 1 # Not possible *
##    print("Changed value of global variable a is", a)
##
##fun1()
##fun2()
##fun3()
##a = 10
##
##def fun1():
##    global a
##    a += 1 # Not possible *
##    print("Changed value of global variable a is", a)
##
##fun1()
##print("Variable value outside of the function", a)


##a = [10, 20, 30, 40]
##
##def fun():
##    a = [10, 20, 30, 40]
##    print("List a inside function", a)
##    print("ID of a inside function", id(a))
##
##fun()
##print("List a outside function", a)
##print("ID of a outside function", id(a))








##a = [10, 20, 30, 40]
##
##def fun():
##    a[1] = 200
##    print("Inside the function", a)
##
##fun()
##print("Outside the function", a)


##a = [10, 20, 30]
##
##def fun():
##    global a
##    a = [10, 20]
##    print("Inside the function", a)
##
##fun()
##print("Outside the function", a)



##a = [10, 20, 30]
##
##def fun():
##    a.append(40)
##
##fun()
##print(a)












##def fun():
##    global a
##    a = 15
##    print("Inside function", a)
##fun()
##print("Outside the function", a)


##a = [10, 20, 30]
##def fun():
##    global a
##    a = [10, 20]
##
##fun()
##print(a)









































