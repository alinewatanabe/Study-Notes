#Importando bibliotecas:
from os import system
from time import sleep

# Definindo Classes:
class Cliente():
    def __init__(self, nome, CPF):
        self.nome = nome
        self.__CPF = CPF
        self.__saldo = 0
        self.__limite = 0
    
    def exibeCPF(self):
        print(f"CPF: {self.__CPF}")
    
    def exibeSaldo(self):
        print(f"Saldo: {self.__saldo}")
    
    def deposito(self, valor):
        self.__saldo += valor
    
    def pagamento(self, valor):
        if (self.__saldo + self.__limite) >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")
            
    def alterar_limite(self, valor):
        self.__limite = valor
       
 
 # ---------------------------------------- Testing Client Class ---------------------------------------- #
         
# my_client = Cliente("João", "123.456.789-00")
# print(my_client.nome)
# my_client.exibeCPF()
# my_client.deposito(100)
# my_client.exibeSaldo()
# my_client.pagamento(50)
# my_client.exibeSaldo()
# my_client.alterar_limite(100)
# my_client.exibeSaldo()
# my_client.pagamento(200)
# my_client.exibeSaldo()

class_list = []
CPF_list = []
repeat = "y"

while(repeat == "y"):
    print("\n 1 - Register a new client \n 2 - Make a deposit \n 3 - Make a payment \n 4 - Change the limit \n 5 - See the account balance ")
    option = int(input("What do you want to do? "))
    if (option == 1):
        client_names = input("Write the name of the client: ")
        client_CPF = int(input("Write the CPF of the client: "))

        if(client_CPF in CPF_list):
            print("This client is already registered")

        else:
            CPF_list.append(client_CPF)
            class_list.append(Cliente(client_names, client_CPF))
    else:
        client_CPF = int(input("Write the CPF of the client: "))
        if(client_CPF not in CPF_list):
            print("This client is not registered")
        else:
            if (option == 2):
                for i in range(len(class_list)):
                    if(client_CPF == class_list[i]._Cliente__CPF):
                        print(f"Welcome, {class_list[i].nome}!")
                        class_list[i].exibeSaldo()
                        deposit_value = int(input("Write the deposit value: "))
                        class_list[i].deposito(deposit_value)
                        class_list[i].exibeSaldo()
            elif (option == 3):
                for i in range(len(class_list)):
                    if(client_CPF == class_list[i]._Cliente__CPF):
                        print(f"Welcome, {class_list[i].nome}!")
                        class_list[i].exibeSaldo()
                        payment_value = int(input("Write the payment value: "))
                        class_list[i].pagamento(payment_value)
                        class_list[i].exibeSaldo()
            elif (option == 4):
                for i in range(len(class_list)):
                    if(client_CPF == class_list[i]._Cliente__CPF):
                        print(f"Welcome, {class_list[i].nome}!")
                        print(f"Current limit: {class_list[i]._Cliente__limite}")
                        new_limit = int(input("Write the new limit: "))
                        class_list[i].alterar_limite(new_limit)
                        print(f"New limit: {class_list[i]._Cliente__limite}")
            elif (option == 5):
                for i in range(len(class_list)):
                    if(client_CPF == class_list[i]._Cliente__CPF):
                        print(f"Welcome, {class_list[i].nome}!")
                        class_list[i].exibeSaldo()
            else:
                print("Invalid option")
        
    repeat = input("Do you want to do something else? (y/n): ").lower()
    sleep(3)
    system("cls")