myOutput = [1, True, "dog"]
myOutput =myOutput [1:]
myOutput={"good":True, "bad":False}
myOutput = myOutput ["good"]

myNum=int(input("enter a number"))
def isPrime(myNum):
    for i in range (2,myNum):
        if myNum%i==0:
            return("not prime")
        
    return("prime")
print(isPrime(myNum))