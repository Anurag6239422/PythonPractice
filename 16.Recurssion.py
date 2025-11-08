#Recurssion Program

def myfun1() :

    myfun2()
    print("Function 1")

def myfun2() :

    print("Function 2")

myfun1()
myfun2()

#Now, calling same function again and again

def fun1(x) :

    if x != 0 :
        print(f"Recurssion Function {x}")
        fun1(x-1)

fun1(3)