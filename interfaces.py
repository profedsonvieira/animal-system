from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
from enum import Enum

class TipoAnimal(Enum):
    TERRESTRE = "terrestre"
    AEREO = "aéreo"
    AQUATICO = "aquático"

class Animal(ABC):
    """Interface base para todos os animais"""
    
    @abstractmethod
    def emitir_som(self) -> str:
        """Retorna o som característico do animal"""
        raise NotImplementedError("Método emitir_som deve ser implementado")
    
    @abstractmethod
    def mover(self) -> str:
        """Retorna a descrição do movimento"""
        raise NotImplementedError("Método mover deve ser implementado")
    
    @abstractmethod
    def get_info(self) -> dict:
        """Retorna informações do animal"""
        raise NotImplementedError("Método get_info deve ser implementado")

@runtime_checkable
class Voavel(Protocol):
    """Interface para animais que voam"""
    def voar(self) -> str:
        """Método que deve ser implemented"""
        ...

@runtime_checkable
class Nadavel(Protocol):
    """Interface para animais que nadam"""
    def nadar(self) -> str:
        """Método que deve ser implementado"""
        ...

@runtime_checkable
class Corredor(Protocol):
    """Interface para animais que correm"""
    def correr(self) -> str:
        """Método que deve ser implementado"""
        ...