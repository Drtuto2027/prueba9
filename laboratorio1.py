#usamos recursion para memorizacion para calcular numeros de fibonacci
def fibonacci(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo)
    return memo[n]
#calcular el numero de fobonacci de 50 
resultado =fibonacci(50)
print("fibonacci de 50 es :",resultado)