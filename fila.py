class VetorFila:
    CAPACIDADE = 10         # Controla a capacidade de todos as novas filas

    def __init__(self):
        #Cria a fila vazia
        self._dado = [None] * VetorFila.CAPACIDADE 
        self._tamanho = 0
        self._frente = 0

    def __len__(self):
        #Mostra o tamanho da fila
        return self._tamanho

    def estavazia(self):          #Verifica se a fila esta vazia
        return self._tamanho == 0

    def primeiro(self):
        if self.is_empty():
            print('pilha vazia')
            return None
        else:
            return self._data[self._frente]
    def dequeue(self):              #Remove um elemento da fila  
        if self.estavazia():
            print('fila vazia')
            return None  
        else:
            resposta = self._dado[self._frente]
            self._dado[self._frente] = None         # Garante que não colete lixo
            self._frente = (self._frente + 1) % len(self._dado)
            self._tamanho -= 1
            return resposta

    def enqueue(self, elem):          #Coloca um elemento na fila
        if self._tamanho == len(self._dado):
            self._resize(2 * len(self.dado))     # dobra o tamanho do vetor
        avail = (self._frente + self._tamanho) % len(self._dado)
        self._dado[avail] = elem
        self._tamanho += 1

fila = VetorFila()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(5)
fila.enqueue(6)
fila.enqueue(7)
fila.enqueue(8)
fila.enqueue(9)
fila.enqueue(10)

print('tamanho da fila:',fila.__len__()) #Exibe o tamanho da fila
while not fila.estavazia():
  print(fila.dequeue())
print("Fila vazia")
