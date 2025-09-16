from typing import List, Dict, Any
from interfaces import Animal, Voavel, Nadavel, Corredor, TipoAnimal

class AnimalService:
    """Serviço para gerenciar e interagir com animais"""
    
    def __init__(self):
        self.animais: List[Animal] = []
    
    def adicionar_animal(self, animal: Animal) -> str:
        """Adiciona um animal à lista e retorna mensagem de confirmação"""
        self.animais.append(animal)
        nome_animal = getattr(animal, 'nome', 'Sem nome')
        return f"✅ {animal.__class__.__name__} '{nome_animal}' adicionado!"
    
    def listar_animais(self) -> str:
        """Lista todos os animais e retorna como string"""
        if not self.animais:
            return "Nenhum animal cadastrado."
        
        resultado = "\n🐾 Lista de Animais:"
        for i, animal in enumerate(self.animais, 1):
            info = animal.get_info()
            resultado += f"\n{i}. {info['nome']} ({info['tipo']}) - Som: {info['som']}"
        
        return resultado
    
    def fazer_animais_emitirem_som(self) -> str:
        """Faz todos os animais emitirem som e retorna como string"""
        if not self.animais:
            return "Nenhum animal para emitir som."
        
        resultado = "\n🎵 Sons dos Animais:"
        for animal in self.animais:
            info = animal.get_info()
            resultado += f"\n{info['nome']}: {animal.emitir_som()}"
        
        return resultado
    
    def executar_habilidades_especiais(self) -> str:
        """Executa habilidades especiais e retorna como string"""
        if not self.animais:
            return "Nenhum animal para demonstrar habilidades."
        
        resultado = "\n🌟 Habilidades Especiais:"
        
        for animal in self.animais:
            info = animal.get_info()
            
            # Verifica se o animal tem o método voar (duck typing)
            if hasattr(animal, 'voar') and callable(getattr(animal, 'voar')):
                resultado += f"\n✈️  {info['nome']}: {animal.voar()}"
            
            # Verifica se o animal tem o método nadar
            if hasattr(animal, 'nadar') and callable(getattr(animal, 'nadar')):
                resultado += f"\n🏊 {info['nome']}: {animal.nadar()}"
            
            # Verifica se o animal tem o método correr
            if hasattr(animal, 'correr') and callable(getattr(animal, 'correr')):
                resultado += f"\n🏃 {info['nome']}: {animal.correr()}"
        
        return resultado
    
    def filtrar_por_tipo(self, tipo: TipoAnimal) -> List[Animal]:
        """Filtra animais por tipo"""
        return [animal for animal in self.animais if animal.get_info()['tipo'] == tipo.value]
    
    def estatisticas(self) -> Dict[str, Any]:
        """Retorna estatísticas sobre os animais"""
        tipos = {}
        for animal in self.animais:
            tipo = animal.get_info()['tipo']
            tipos[tipo] = tipos.get(tipo, 0) + 1
        
        return {
            "total_animais": len(self.animais),
            "por_tipo": tipos,
            "com_voavel": sum(1 for a in self.animais if hasattr(a, 'voar')),
            "com_nadavel": sum(1 for a in self.animais if hasattr(a, 'nadar')),
            "com_corredor": sum(1 for a in self.animais if hasattr(a, 'correr'))
        }
    
    def get_animal_por_nome(self, nome: str) -> Animal | None:
        """Retorna animal pelo nome ou None se não encontrado"""
        for animal in self.animais:
            info = animal.get_info()
            if info['nome'].lower() == nome.lower():
                return animal
        return None