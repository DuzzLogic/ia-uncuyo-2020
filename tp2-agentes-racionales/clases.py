import random
import numpy as np

class env:
    steps = 0
    puntos = 0
    # 0 = limpio
    # 1 = sucio
    # 2 = aspiradora
    def __init__ (self,sizeX,sizeY,init_posX,init_posY,dirt_rate):
        tamaño = sizeX*sizeY

        self.sizeX = sizeX
        self.sizeY = sizeY
        self.m = np.zeros((sizeX,sizeY))
        self.init_posX = init_posX
        self.init_posY = init_posY
        self.dirtSlotsAmount = int((dirt_rate * tamaño)/100)
        self.m[init_posX][init_posY] = 2
        
        i = 0

        #Se ensucia de forma random el ambiente
        while (i < self.dirtSlotsAmount):
            slotX = random.randint(0,self.sizeX-1)
            slotY = random.randint(0,self.sizeY-1)
            if (self.m[slotX][slotY] == 0):
                self.m[slotX][slotY] = 1
                i = i + 1

        print("Ambiente generado")

    def accept_action(self,action,x,y):
        # arriba abajo izquierda derecha limpiar nohacernada
        if (action == "izquierda"):
            if (x-1 >= 0):
                self.steps = self.steps + 1
                return True
            return False
        elif (action == "derecha"):
            if (x+1 < self.sizeX):
                self.steps = self.steps + 1
                return True
            return False
        elif (action == "abajo"):
            if (y-1 >= 0):
                self.steps = self.steps + 1
                return True
            return False
        elif (action == "arriba"):
            if (y+1 < self.sizeY):
                self.steps = self.steps + 1
                return True
            return False
        elif (action == "limpiar"):
            if (self.is_dirty(x,y) == True):
                self.puntos = self.puntos + 1
                self.steps = self.steps + 1
                self.m[x][y] = 2
                self.dirtSlotsAmount -= 1
        else:
            self.steps = self.steps + 1

    def is_dirty(self,x,y):
        if (self.m[x][y] == 3):
            return True
        return False

    def get_performance(self):
        return self.puntos/self.steps

    def print_environment(self):
        print('\n'*5)
        for a in range(0,self.sizeX):
            for b in range(0,self.sizeY):
                print("|",int(self.m[a][b]),end=' ')
            print("|")


class agentRandom:
    def __init__(self,env):
        self.env = env
        self.x = env.init_posX
        self.y = env.init_posY
        self.comenzar()

    def up(self):
        x = self.env.accept_action("izquierda",self.x,self.y)
        if (x == True):
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] - 2
            self.x = self.x-1
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] + 2
            return True
        return False

    def down(self):
        x = self.env.accept_action("derecha", self.x,self.y)
        if (x == True):
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] - 2
            self.x = self.x+1
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] + 2
            return True
        return False

    def left(self):
        x = self.env.accept_action("abajo", self.x,self.y)
        if (x == True):
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] - 2
            self.y = self.y-1
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] + 2
            return True
        return False

    def right(self):
        x = self.env.accept_action("arriba", self.x,self.y)
        if (x == True):
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] - 2
            self.y = self.y+1
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] + 2
            return True
        return False

    def suck(self):  # Limpia
        self.env.accept_action("limpiar", self.x,self.y)

    def idle(self):  # no hace nada
        self.env.accept_action("nada", self.x,self.y)

    def comenzar(self):
        while (True):
            rand = random.randint(0,3)
            
            if(int(self.env.dirtSlotsAmount) == 0):
                self.env.print_environment()

                print("Limpieza finalizada")
                print("Performance obtenido: ", self.env.get_performance())
                print("Etapas: ", self.env.steps)
                print("Puntos: ", self.env.puntos)

                break


            if self.env.is_dirty(self.x,self.y):
                self.suck()
            else:
                if (rand == 0): # arriba
                    self.up()
                elif (rand == 1): # abajo
                    self.down()
                elif (rand == 2):  # izquierda
                    self.left()
                else: # derecha
                    self.right()

            #self.env.print_environment()


class agent:
    def __init__(self,env):
        self.env = env
        self.x = env.init_posX
        self.y = env.init_posY
        self.comenzar()

    def up(self):
        x = self.env.accept_action("izquierda",self.x,self.y)
        if (x == True):
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] - 2
            self.x = self.x-1
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] + 2
            return True
        return False

    def down(self):
        x = self.env.accept_action("derecha", self.x,self.y)
        if (x == True):
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] - 2
            self.x = self.x+1
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] + 2
            return True
        return False

    def left(self):
        x = self.env.accept_action("abajo", self.x,self.y)
        if (x == True):
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] - 2
            self.y = self.y-1
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] + 2
            return True
        return False

    def right(self):
        x = self.env.accept_action("arriba", self.x,self.y)
        if (x == True):
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] - 2
            self.y = self.y+1
            self.env.m[self.x][self.y] = self.env.m[self.x][self.y] + 2
            return True
        return False

    def suck(self):  # Limpia
        self.env.accept_action("limpiar", self.x,self.y)

    def idle(self):  # no hace nada
        self.env.accept_action("nada", self.x,self.y)

    def comenzar(self):
        lm = [5]

        while (True):
            
            if(int(self.env.dirtSlotsAmount) == 0):
                self.env.print_environment()

                print("Limpieza finalizada")
                print("Performance obtenido: ", self.env.get_performance())
                print("Etapas: ", self.env.steps)
                print("Puntos: ", self.env.puntos)
                
                break

            if self.env.is_dirty(self.x,self.y):
                self.suck()
            else:
                if lm[0] == 5:
                    rand = random.randint(0,3) 
                else:
                    while(True):
                        rand = random.randint(0,3)
                        if rand != lm[0]:
                            break

                if (rand == 0): # arriba
                    lm[0] = 1
                    self.up()
                elif (rand == 1): # abajo
                    lm[0] = 0
                    self.down()
                elif (rand == 2):  # izquierda
                    lm[0] = 3
                    self.left()
                else: # derecha
                    lm[0] = 2
                    self.right()



            #self.env.print_environment()		