#Fibonacci
print("¿cuántos términos desea?")
n=int(input())
def Fibonacci(n):
    a=0
    b=1
    for i in range(n):
        c= a+b
        a= b
        b= c
    return b
for x in range(n):
    print(Fibonacci(x))
