from interfaces import Animal, Nadavel, TipoAnimal

class Peixe(Animal, Nadavel):
    def __init__(self, nome: str, especie: str, profundidade_maxima: int):
        self.nome = nome
        self.especie = especie
        self.profundidade_maxima = profundidade_maxima
    
    def emitir_som(self) -> str:
        return "Glub glub!"
    
    def mover(self) -> str:
        return "Nadando na água"
    
    def nadar(self) -> str:
        return f"{self.nome} nada até {self.profundidade_maxima}m de profundidade!"
    
    def get_info(self) -> dict:
        return {
            "nome": self.nome,
            "especie": self.especie,
            "profundidade_maxima": self.profundidade_maxima,
            "tipo": TipoAnimal.AQUATICO.value,
            "som": self.emitir_som()
        }

class Tartaruga(Animal, Nadavel):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def emitir_som(self) -> str:
        return "Som de tartaruga (quase inaudível)"
    
    def mover(self) -> str:
        return "Nadando lentamente"
    
    def nadar(self) -> str:
        return f"{self.nome} nada calmamente com {self.idade} anos!"
    
    def get_info(self) -> dict:
        return {
            "nome": self.nome,
            "idade": self.idade,
            "tipo": TipoAnimal.AQUATICO.value,
            "som": self.emitir_som()
        }