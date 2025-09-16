from interfaces import Animal, Voavel, TipoAnimal

class Passaro(Animal, Voavel):
    def __init__(self, nome: str, especie: str, envergadura: float):
        self.nome = nome
        self.especie = especie
        self.envergadura = envergadura
    
    def emitir_som(self) -> str:
        return "Piu piu!"
    
    def mover(self) -> str:
        return "Voando pelo céu"
    
    def voar(self) -> str:
        return f"{self.nome} está voando a {self.envergadura}cm de envergadura!"
    
    def get_info(self) -> dict:
        return {
            "nome": self.nome,
            "especie": self.especie,
            "envergadura": self.envergadura,
            "tipo": TipoAnimal.AEREO.value,
            "som": self.emitir_som()
        }

class Morcego(Animal, Voavel):
    def __init__(self, nome: str, velocidade_voo: int):
        self.nome = nome
        self.velocidade_voo = velocidade_voo
    
    def emitir_som(self) -> str:
        return "Ecolocalização (inaudível para humanos)"
    
    def mover(self) -> str:
        return "Voando à noite"
    
    def voar(self) -> str:
        return f"{self.nome} voa a {self.velocidade_voo} km/h!"
    
    def get_info(self) -> dict:
        return {
            "nome": self.nome,
            "velocidade_voo": self.velocidade_voo,
            "tipo": TipoAnimal.AEREO.value,
            "som": self.emitir_som()
        }