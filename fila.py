class VetorFila:
    CAPACIDADE = 10         # Controla a capacidade de todos as novas filas

    def __init__(self):
        #Cria a fila vazia
        self._dado = [None] * VetorFila.CAPACIDADE 
        self._tamanho = 0
        self._atras = 0

    def __len__(self):
        #Mostra o tamanho da fila
        return self._tamanho

    def esta_vazia(self):          #Verifica se a fila esta vazia
        return self._tamanho == 0

    def primeiro(self):
        if self.esta_vazia():
            print('fila vazia')
            return None
        else:
            return self._dado[self._atras]
    def dequeue(self):              #Remove um elemento da fila  
        if self.esta_vazia():
            print('fila vazia')
            return None  
        else:
            resposta = self._dado[self._atras]
            self._dado[self._atras] = None         # Garante que não colete lixo
            self._atras = (self._atras + 1) % len(self._dado)
            self._tamanho -= 1
            return resposta

    def enqueue(self, elem):          #Coloca um elemento na fila
        if self._tamanho == len(self._dado):
            self._resize(2 * len(self.dado))     # dobra o tamanho do vetor
        avail = (self._atras + self._tamanho) % len(self._dado)
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
fila.dequeue()

print('tamanho da fila:',fila.__len__()) #Exibe o tamanho da fila
while not fila.esta_vazia():
  print(fila.dequeue())
print("Fila vazia")
