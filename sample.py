
L = [10,40,20,30,10,20,10,20,30,20,30,30,20,40,40]

#from collections import Counter
print ("Normal sort :", sorted(L) )
a=sorted(L,key=L.count,reverse=True)
print ("Sort with len :", sorted(L,key=L.count,reverse=True))
print(a)



def fun1(fun2):
    print("i got decorator")
    fun2()


@fun1
def ordinary():
    print("I am ordinary")


