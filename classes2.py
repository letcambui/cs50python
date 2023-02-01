class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] #1- criamos uma lista vazia, apra adicionar passageiros ao voo

    def add_passenger(self, name):
        if not self.open_seats(): # 5- se NÃO HÁ lugares disponiveis:
            return False
        self.passengers.append(name)
        return True #3- objeto individual, usamos a palavra chave self e utilizamos append para adicionar nome de passageiros a lista vazia

    def open_seats(self):
        return self.capacity - len(self.passengers) #4- def sao functions, essa serve para dizer quantos lugares vazio temos


flight = Flight(3) #2- definimos que a capacidade desse voo é de 3 pessoas

people = ["harry", "Ron", "Hermione", "Ginny"]
for i in people:
  #6 - vamos tentar adicionar uma pessoa da lista people no voo e deixar o resultado salvo na variavel success. 7 - inicialmente era uma variavel, mas notamos que seria melhor virar condição. antes era success = flight.add_passenger(i). agora é como está abaixo
    if flight.add_passenger(i):
        print(f"Add {i} to flighy successfully.")
    else: 
        print(f"No available seats for {i}")    
    
      
