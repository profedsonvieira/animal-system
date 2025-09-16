from interfaces import Animal, Corredor, TipoAnimal

class Cachorro(Animal, Corredor):
    def __init__(self, nome: str, raca: str, idade: int):
        self.nome = nome
        self.raca = raca
        self.idade = idade
    
    def emitir_som(self) -> str:
        return "Au Au!"
    
    def mover(self) -> str:
        return "Correndo com quatro patas"
    
    def correr(self) -> str:
        return f"{self.nome} está correndo rapidamente!"
    
    def get_info(self) -> dict:
        return {
            "nome": self.nome,
            "raca": self.raca,
            "idade": self.idade,
            "tipo": TipoAnimal.TERRESTRE.value,
            "som": self.emitir_som()
        }

class Gato(Animal, Corredor):
    def __init__(self, nome: str, cor: str):
        self.nome = nome
        self.cor = cor
    
    def emitir_som(self) -> str:
        return "Miau!"
    
    def mover(self) -> str:
        return "Andando silenciosamente"
    
    def correr(self) -> str:
        return f"{self.nome} está correndo ágilmente!"
    
    def get_info(self) -> dict:
        return {
            "nome": self.nome,
            "cor": self.cor,
            "tipo": TipoAnimal.TERRESTRE.value,
            "som": self.emitir_som()
        }