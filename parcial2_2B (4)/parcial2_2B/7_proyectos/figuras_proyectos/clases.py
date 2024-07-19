
class Figura:
    def init(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible

    def getx(self):
        return self.x
    def setx(self,x):
        self.x=x
    def gety(self):
        return self.y
    def sety(self,y):
        self.y=y

    def visibile(self, visible):
        self.visible = visible

    def getvisible(self):
        return self.visibile
    def setvisible(self, visible):
        self.visibile=visible

    def mostrar(self):
        self.visible = True
    def getmostrar(self):
        return self.visible
    def setmostrar(self,visible):
        self.mostrar=visible

    def ocultar(self):
        self.visible = False

    def set_mostrar(self, mostrar):
        self.mover = False

    def move(self, mostrar):
        self.mover = mostrar
        if self.mover == True:
            print("La figura se está moviendo o se está moviendo")
        else:
            print("La figura no se está moviendo o no se movió")
    
    def getInfo(self):
        print(f"X = {self.x()}\nY = {self.y()}\visible: {self.visible()}")


class rectangulo(Figura):

    def __init__(self,x,y,visible,alto,ancho):
        super().__init__(x,y,visible)
        self.alto=alto
        self.ancho=ancho

    def area(self):
        return self.alto * self.ancho

    
    
    def getInfo(self):
        print(f"Tiene un area de {self.area}")

class circulo(Figura):
    def __init__(self,x,y,visible,radio):
        super().__init__(radio)
        self.radio=radio

    def area(self):
        return 3.14 * (self.radio ** 2)

    def get_radio(self):
        self.radio=3.1416
    
    def getInfo(self):
        print(f"Radio = {self.x()}\nvisible: {self.visible()} y area {self.area()}")