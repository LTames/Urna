from model.eleitor import Eleitor
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from model.cargo_candidato import CargoCandidato
    from model.chapa import Chapa
    from model.tipo_eleitor import TipoEleitor 


class Candidato(Eleitor):
    def __init__(self, cpf: str, nome: str, email: str, endereco: str, tipo_eleitor: TipoEleitor,
                 numero: int, chapa: Chapa, cargo: CargoCandidato) -> None:
        super().__init__(cpf, nome, email, endereco, tipo_eleitor)
        self.__numero = numero
        self.__cargo = cargo
        self.__chapa = chapa

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cargo(self):
        return self.__cargo

    @property
    def chapa(self):
        return self.__chapa

    @numero.setter
    def numero(self, numero: int) -> None:
        self.__numero = numero

    @cargo.setter
    def cargo(self, cargo) -> None:
        self.__cargo = cargo

    @chapa.setter
    def chapa(self, chapa) -> None:
        self.__chapa = chapa
