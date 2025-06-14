from decimal import Decimal,getcontext
# establemcemos un contexto de presicion alta 
getcontext ().prec=50
#hacemos una operacion matematica precisa 
numero1=Decimal("1.123456789123456789")
numero2=Decimal("2.987654321987654321")
resultado=numero1*numero2
print(f"resultado preciso:{resultado}")
