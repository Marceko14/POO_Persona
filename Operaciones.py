# CLASS OPERACIONES 
# NULL CONSTRUCTION
class Operaciones2:
    def __init__(self):
        self.num1 = 0 
        self.num2 = 0
        self.result = 0
    def sumar(self):
        self.result = self.num1 + self.num2
        sumando = "La suma es {} ".format(self.result)
        print(sumando)
    def restar(self):
        self.result = self.num1 - self.num2
        restando = "La resta es {}".format(self.result)
        print(restando)
    def division(self):
        self.result = self.num1 / self.num2 
        resultado = "La división es {}".format(self.result)
        print(resultado)
    def multiplicacion(self):
        self.result = self.num1 * self.num2 
        multiplicando = "la multiplicación es {}".format(self.result)
        print(multiplicando)
# CONSTRAIN PARAMERS
class Operaciones:
    pass 


operacion = Operaciones2()
texto = "BIENVENIDO AL SISTEMA"      
ancho = 10 
centrado = texto.center(ancho,'*')
print(centrado)
print("Elija una opcion")
print("a) sumar")
print("b) restar")
print("c) división")
print("d) multiplicación")

opcion = str(input("Ingrese su opcion: "))

if (opcion == 'a'):
    print("Opcion suma")
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un segundo numero: "))
    operacion.num1 = a
    operacion.num2 = b
    operacion.sumar()
    
elif (opcion == 'b'):
    print("opcion resta")
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un segundo numero: "))
    operacion.num1 = a
    operacion.num2 = b
    operacion.restar()
    
elif (opcion == 'c'):
    print("opcion division")
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un segundo numero: "))
    operacion.num1 = a
    operacion.num2 = b
    operacion.division()
    
elif (opcion == 'd'):
    print("opcion multiplicacion")
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un segundo numero: "))
    operacion.num1 = a
    operacion.num2 = b
    operacion.multiplicacion()
else:
    print("no existe esa opcion")
    
    
    

    
    
    
    
    




  



