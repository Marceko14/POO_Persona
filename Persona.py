




#CLASE PERSONA 
class Personas:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = 0
        
    def mostrar(self):
        mensaje = "Hola mi nombre es {} {} y tengo {} años".format(self.nombre,self.apellido,self.edad)
        print(mensaje)




class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre 
        self.apellido = apellido 
        self.edad = edad 
        
        
    def saludar(self):
        resultado = "Hola mi nombre completo es {} {} y mi edad es {} años.".format(self.nombre,self.apellido,self.edad)
        print(resultado)
    @property
    def nombre(self):
        print("Leyendo nombre")
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
        
    
    
    @property 
    def apellido(self):
        print("Leyendo apellido")
        return self._apellido
    
    @apellido.setter
    def apellido(self,nuevo_apellido):
        self._apellido = nuevo_apellido
        
    @property
    def edad(self):
        print("Leyendo edad")
        return self._edad
    
    @edad.setter
    def edad(self,nueva_edad):
        self._edad = nueva_edad
        
        
persona1 = Personas()

name = str(input("Ingrese su primer nombre: "))
apel = str(input("Ingrese su primer apellido: "))
old = int(input("Ingrese su edad actual: "))
persona1.nombre = name
persona1.apellido = apel
persona1.edad = old

persona1.mostrar()







        