# Classes
class Dispositivo():
    def __init__(self, nome):
        self.nome = nome
    def retornaID(self):
        return self.nome

class Atuador(Dispositivo):
    def __init__(self, nome, estado = "desligado"):
        super().__init__(nome)
        self.estado = estado
    def exibeEstado(self, estadoLed = 0, nomeLed = None):
        if (estadoLed == 0):
            estado = "desligado"
        else:
            estado = "ligado"
        return print(f'O {self.nome} está com o {nomeLed} {estado}')

class LED(Atuador):
    def __init__(self, nome, estado = 0):
        super().__init__(nome, estado)
    def liga(self):
        self.estado = 1
    def desliga(self):
        self.estado = 0

class Motor(Atuador):
    def __init__(self, nome, estado=0):
        super().__init__(nome, estado)
        self.direcao = None
        self.velocidade = 0
        
    def atribuiDirecao(self, direcao):
        if ((direcao == 0) or (direcao == 1)):
            self.direcao = direcao
        else:
            return print("Direção inválida")
    
    def atribuiVelocidade(self, velocidade):
        if(velocidade > 255 or velocidade < 0):
            return print("Velocidade fora do limite")
        else:
            self.velocidade = velocidade
    
    def exibeEstado(self):
        if (self.estado == 0):
            estado = "desligado"
            return print(f'{self.nome} está {estado}')
        else:
            estado = "ligado"
            return print(f'{self.nome} está {estado}, direção {self.direcao} e velocidade {self.velocidade}')

# Objetos
atuador1 = Atuador("Atuador1")
led1 = LED("LED1")
led2 = LED("LED2")
motor1 = Motor("Motor1", 1)
motor2 = Motor("Motor2")


# Código para testar a classe LED
led1.liga()
led2.desliga()

# # Código para testar a classe Atuador
atuador1.exibeEstado(led1.estado, led1.nome)
atuador1.exibeEstado(led2.estado, led2.nome)

# Código para testar a classe Motor
motor1.atribuiDirecao(1)
motor1.atribuiVelocidade(100)
motor1.exibeEstado()
motor1.atribuiDirecao(2)
motor1.atribuiVelocidade(100)
motor1.exibeEstado()
motor1.atribuiDirecao(1)
motor1.atribuiVelocidade(256)
motor1.exibeEstado()
