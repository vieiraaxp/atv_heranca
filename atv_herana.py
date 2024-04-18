class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print('o animal faz algum som.')

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def __str__(self) -> str:
        return f'{self.nome}'

    def fazer_som(self):
        print('au au')

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):
        print('miau')

class Papagaio(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):
        print('piu piu')

class Pato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):    
        print('quack quack')

if __name__ == '__main__':
    cachorro = Cachorro('Totó','Pastor Alemão')
    gato = Gato('juju', 'siamês')
    papagaio = Papagaio('neymar', 'papagaio verdadeiro')
    pato = Pato('patolino', 'azuleiga')
    
    cachorro.fazer_som()
    gato.fazer_som()
    papagaio.fazer_som()
    pato.fazer_som()
