class Usuarios:
    def __init__(self,nombre,direccion,telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
#-----------------------------------------
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
#------------------------------------------
    def getDireccion(self):
        return self.direccion
    def setDireccion(self,direccion):
        self.direccion=direccion
#-----------------------------------------
    def getTelefono(self):
        return self.telefono
    def setTelefono(self,telefono):
        self.telefono=telefono
#-----------------------------------------
    def info_usuario(self):
        print(f"El usuario es {self.getNombre()}, su direccion es: {self.getDireccion()}, su telefono es: {self.getTelefono()}")
#--------------CLIENTE--------------------
class Cliente(Usuarios):
    def __init__(self, nombre, direccion, telefono,num_clietne):
        super().__init__(nombre, direccion, telefono)
        self.__num_cliente=num_clietne

    def getNumClie(self):
        return self.__num_cliente
    def setNumClie(self,num_cliente):
        self.__num_cliente=num_cliente
#-----------------------------------------
def info_usuario(self):
        print(f"El usuario es {self.getNombre()}, su direccion es: {self.getDireccion()}, su telefono es: {self.getTelefono()}, su numero de cliente es: {self.getNumClie()}")
#-------------EMPLEADOS-------------------
class Empleados(Usuarios):
    def __init__(self, nombre, direccion, telefono,salario,num_empleado,tipo):
        super().__init__(nombre, direccion, telefono)
        self._salario=salario
        self._num_empleadio=num_empleado
        self._tipo=tipo
#-------------------------------------------
    def getSalario(self):
        return self._salario
    def setSalario(self,salario):
        self._salario=salario
#-------------------------------------------
    def getNumEmple(self):
        return self._num_empleadio
    def setNumEmple(self,num__num_empleadio):
        self._num_empleadio=num__num_empleadio
#-------------------------------------------
    def getTipo(self):
        return self._tipo
    def setTipo(self,tipo_tipo):
        self._tipo=tipo_tipo
#------------------------------------------
    def info_usuario(self):
        print(f"El usuario es {self.getNombre()}, su direccion es: {self.getDireccion()}, su telefono es: {self.getTelefono()}, su numero de empleado es: {self.getNumEmple()}, su salario es: {self.getSalario()}, su tipo es: {self.getTipo()}")


