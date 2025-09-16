from animals.terrestrial import Cachorro, Gato
from animals.aerial import Passaro, Morcego
from animals.aquatic import Peixe, Tartaruga
from services.animal_service import AnimalService
from interfaces import TipoAnimal

def main():
    """Função principal do sistema"""
    
    # Inicializar serviço
    service = AnimalService()
    
    # Criar alguns animais
    rex = Cachorro("Rex", "Pastor Alemão", 3)
    felix = Gato("Felix", "Preto")
    piupiu = Passaro("PiuPiu", "Canário", 15)
    batman = Morcego("Batman", 60)
    nemo = Peixe("Nemo", "Palhaço", 30)
    donatello = Tartaruga("Donatello", 15)
    
    # Adicionar animais ao serviço
    print(service.adicionar_animal(rex))
    print(service.adicionar_animal(felix))
    print(service.adicionar_animal(piupiu))
    print(service.adicionar_animal(batman))
    print(service.adicionar_animal(nemo))
    print(service.adicionar_animal(donatello))
    
    # Demonstrar funcionalidades
    print("\n" + "="*50)
    print(service.listar_animais())
    
    print("\n" + "="*50)
    print(service.fazer_animais_emitirem_som())
    
    print("\n" + "="*50)
    print(service.executar_habilidades_especiais())
    
    # Mostrar estatísticas
    print("\n" + "="*50)
    stats = service.estatisticas()
    print("📊 Estatísticas:")
    print(f"Total de animais: {stats['total_animais']}")
    print("Por tipo:")
    for tipo, quantidade in stats['por_tipo'].items():
        print(f"  {tipo}: {quantidade}")
    
    print(f"Animais que voam: {stats['com_voavel']}")
    print(f"Animais que nadam: {stats['com_nadavel']}")
    print(f"Animais que correm: {stats['com_corredor']}")
    
    # Filtrar animais aquáticos
    print("\n" + "="*50)
    aquaticos = service.filtrar_por_tipo(TipoAnimal.AQUATICO)
    print("🌊 Animais Aquáticos:")
    for animal in aquaticos:
        info = animal.get_info()
        print(f"  {info['nome']} - {animal.nadar()}")

if __name__ == "__main__":
    main()