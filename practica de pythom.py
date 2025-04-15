#creo la clase Persona con "class" y cierro con ":" 
class Persona:
    #uso el metodo "__init__" que me ayuda en asignar valores manualmente asi no los hago yo 
    #Le asigno dos valores el "nombre" de la persona y su "edad"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #Creo un metodo que lo unica que hara sera mostrarme la info de la persona y lo muestra en la pantalla
    def mostrar_info(self):
        print(f"You name is {self.nombre}, Your old is  {self.edad} ")

    #Hgo otro metodo para que puedan cambiar su nombre porque es bueno
    #Lo que hace es que "modificar_info" puede cambiar lo que guardo en las variables
    #ejemplo simple creo a "persona1" cuyo nombre es pato pero si coloco "persona1.modificar_info("juan")" su nombre se cambia y listo  
    def modificar_info(self, nuevo_nombre, nueva_edad):
        self.nombre = nuevo_nombre
        self.edad = nueva_edad

    #esta funcion es para bueno crear perosonas coloque "@classmethod" porque tenia 2 opciones la primera
    #era colocar "@classmethod" y hacer que sea un metodo de la clase o la segunda era hacer un metodo normal pero
    #tenia que colocar un objeto para llamar la funcion y seria algo como "objeto = Persona("juan", 30)" y luego
    #llamarlo con crear_persona y no queria, ademas porque me daba error 
    @classmethod
    def crear_persona(cls, nombre, edad):
        return cls(nombre, edad)

#Se usa el método crear_persona para crear un objeto persona1 con nombre "Juan" y edad 25.
#Se muestra la información con mostrar_info(), lo que imprimirá:
#cree un objeto "persona1" usando el metodo "crear_persona" con el nombre "juan" de "25"
#Luego "use mostrar_info()" que lo imprime en la pantalla
#pero luego "juan" se quiso cambiar el nombre a "juansito" usando 
persona1 = Persona.crear_persona("Juan", 25)
persona1.mostrar_info()
persona1.modificar_info("Carlos", 30)
persona1.mostrar_info()