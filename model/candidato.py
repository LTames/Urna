from model.eleitor import Eleitor


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
    def cargo(self) -> CargoCandidato:
        return self.__cargo

    @property
    def chapa(self) -> Chapa:
        return self.__chapa

    @numero.setter
    def numero(self, numero: int) -> None:
        self.numero = numero

    @cargo.setter
    def cargo(self, cargo: CargoCandidato) -> None:
        self.cargo = cargo

    @chapa.setter
    def chapa(self, chapa: Chapa) -> None:
        self.chapa = chapa
