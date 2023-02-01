class Point():
    def __init__ (self, input1, input2):
        self.x = input1
        self.y = input2 

p = Point(2, 8)
print(p.x)
print(p.y)















# __init metodo ou funcao que vai ser chamada automaticamente sempre que eu tentar criar um novo ponto. argumento self representa o objeto em questão, referencia o objeto que estamos lidando atualmente e isso pode mudar. (no caaso, x e y)
