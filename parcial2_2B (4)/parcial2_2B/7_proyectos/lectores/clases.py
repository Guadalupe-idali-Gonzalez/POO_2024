class Lectores:

    def __init__(self, nombre,direccion,telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono

    def reserva(self):
        self.reserva

    def entrega(self):
        self.entrega

    #Getter y setter

    def setNombre(self,nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre
    def setDireccion(self,direccion):
        self.nombre=direccion
    def getDireccion(self):
        return self.direccion
    def setTelefono(self,telefono):
        self.nombre=telefono
    def getTelefono(self):
        return self.telefono
    def getInfo(self):
        print(f"El lector se llama: {self.getNombre()}, con direccion: {self.getDireccion()} y telefono: {self.getTelefono()}")

    

    
class Estudiante(Lectores):
    def __init__(self,nombre,direccion,telefono,carrera,matricula):
        super().__init__(nombre,direccion,telefono)
        self._carrera=carrera
        self._matricula=matricula

    def ProCarrera(self):
        return self._carrera
    def ProMatricula(self):
        return self._matricula
    
    def getInfo(self):
        print(f"El estudiante {self.getNombre()}, con direccion: {self.getDireccion()}, telefono: {self.getTelefono()}, cursa la carrera: {self.ProCarrera()} y su matricula es: {self.ProMatricula()}")

class Docente(Lectores):
    def __init__(self,nombre,direccion,telefono,modalidad,num_empleado):
        super().__init__(nombre,direccion,telefono)
        self.__modalidad=modalidad
        self.__num_empleado=num_empleado

    def privModalidad(self):
        return self.__modalidad
    def privEmpleado(self):
        return self.__num_empleado
    
    def getInfo(self):
        print(f"El docente: {self.getNombre()}, con direccion: {self.getDireccion()}, telefono: {self.getTelefono()}, su modalidad es:: {self.privModalidad()} y su numero de empleado: {self.privEmpleado()}")
 