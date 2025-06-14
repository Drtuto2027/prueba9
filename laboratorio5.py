def sumar_o_defaul(a,b):
    return(a or 0)+(b or 0)
print(sumar_o_defaul(5,None))
print(sumar_o_defaul(None,None))
print(sumar_o_defaul(10,20))
