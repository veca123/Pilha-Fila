#Pilha
class Empty(Exception):
    def __init__(self, valor):
      self.valor = valor

    def __str__(self):
      return repr(self.valor)

class VetorPilha:

  def __init__(self):
    self._dado = []                       

  def __len__(self):
    return len(self._dado)

  def esta_vazia(self):
    return len(self._dado) == 0

  def push(self, elemento):
    self._dado.append(elemento)                 

  def top(self):
    if self.esta_vazia():
      print('pilha vazia')
      return None
    else:
      return self._dado[-1]                 # o ultimo elemento da pilha

  def pop(self):
    if self.esta_vazia():
      print('pilha vazia')
      return None
    else:
      return self._dado.pop()               # retira o ultimo elemento

if __name__ == '__main__':

    def ExibePilha(p):
        pilha_auxiliar = VetorPilha() # cria pilha auxiliar
        print('[', end="")
        while(not p.esta_vazia()): # se a pilha nao ficar vazia
            print(p.top(), end=" ") # retorna o elemento do topo da pilha
            pilha_auxiliar.push(p.pop()) # coloca o elemento na pilha auxiliar
        while(not pilha_auxiliar.esta_vazia()):
            p.push(pilha_auxiliar.pop())
        pilha_auxiliar = None
        print(']\n')

        
    pilha = VetorPilha()                 
    pilha.push(5)                        
    pilha.push(3)
    pilha.push(7)                        
    pilha.push(9)                                          
    pilha.push(4)                                        
    pilha.push(6)                        
    pilha.push(8)
    print("Retorna se a pilha esta cheia ou vazia:")                       
    print(pilha.esta_vazia())             #se a pilha estiver cheia retorna falso e se a pilha estiver vazia retorna verdadeiro 
    print()
    pilha.pop()
    print("Retorna o elemento que está no topo da pilha")
    print(pilha.top())                    #retorna o elemento do topo da pilha
    print()
    print("Exibição da pilha:")     
    ExibePilha(pilha)                     #exibe a pilha
    print()
    print("Mostra a quantidade dos elementos da pilha:") 
    print(len(pilha))                     #quantidade de elementos na pilha
