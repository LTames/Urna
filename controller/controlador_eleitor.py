from abstracts.abstract_controlador import AbstractControlador
from view.tela_eleitor import TelaEleitor
from model.eleitor import Eleitor, TipoEleitor
from exceptions.max_eleitores import MaxEleitoresException
from exceptions.eleitor_inexistente import EleitorInexistenteException
from exceptions.eleitor_ja_cadastrado import EleitorJaCadastradoException


class ControladorEleitor(AbstractControlador):
    def __init__(self, controlador_urna) -> None:
        self.__controlador_urna = controlador_urna
        self.__tela_eleitor = TelaEleitor()
        self.__eleitores = []

    @property
    def controlador_urna(self):
        return self.__controlador_urna

    @property
    def tela_eleitor(self) -> TelaEleitor:
        return self.__tela_eleitor

    @property
    def eleitores(self) -> list:
        return self.__eleitores

    def seleciona_eleitor(self, cpf: str = None):
        try:
            if not cpf:
                cpf = self.tela_eleitor.get_cpf_eleitor()
            for eleitor in self.eleitores:
                if eleitor.cpf == cpf:
                    return eleitor
            raise EleitorInexistenteException
        except Exception as e:
            self.tela_eleitor.alert(e)

    def adiciona_eleitor(self):
        if len(self.eleitores) == self.controlador_urna.urna.max_eleitores:
            raise MaxEleitoresException

        try:
            dados_eleitor = self.tela_eleitor.get_dados_eleitor()
            for eleitor in self.eleitores:
                if dados_eleitor["cpf"] == eleitor.cpf:
                    raise EleitorJaCadastradoException

            self.eleitores.append(Eleitor(dados_eleitor["cpf"],
                                          dados_eleitor["nome"],
                                          dados_eleitor["email"],
                                          dados_eleitor["endereco"],
                                          TipoEleitor(dados_eleitor["tipo_eleitor"])))

        except Exception as e:
            self.tela_eleitor.alert(e)

    def deleta_eleitor(self):
        if not self.eleitores:
            self.tela_eleitor.alert("Não há eleitores cadastrados")
            return
        eleitor = self.seleciona_eleitor(self.tela_eleitor.get_cpf_eleitor())
        if not eleitor:
            return
        self.eleitores.remove(eleitor)

    def altera_eleitor(self) -> None:
        if not self.eleitores:
            self.tela_eleitor.alert('Não há eleitores cadastrados')
            return
        eleitor = self.seleciona_eleitor()
        if not eleitor:
            return

        dados_atualizados = self.tela_eleitor.get_dados_eleitor()
        eleitor.cpf = dados_atualizados["cpf"]
        eleitor.nome = dados_atualizados["nome"]
        eleitor.email = dados_atualizados["email"]
        eleitor.endereco = dados_atualizados["endereco"]
        eleitor.tipo_eleitor = TipoEleitor(dados_atualizados["tipo_eleitor"])

    def lista_eleitores(self):
        if not self.eleitores:
            self.tela_eleitor.alert('Não há eleitores cadastrados')
            return
        for eleitor in self.eleitores:
            self.tela_eleitor.exibe_eleitor({'cpf': eleitor.cpf, 'nome': eleitor.nome,
                                             'email': eleitor.email, 'endereco': eleitor.endereco,
                                             'tipo_eleitor': eleitor.tipo_eleitor.value[1]})

    def add_candidato_eleitores(self, candidato: 'Candidato'):
        try:
            if candidato in self.eleitores:
                return

            for eleitor in self.eleitores:
                if eleitor.cpf == candidato.cpf:
                    raise EleitorJaCadastradoException
            self.eleitores.append(candidato)
        except Exception as e:
            self.tela_eleitor.alert(e)

    def remove_candidato_eleitores(self, candidato: 'Candidato'):
        self.eleitores.remove(candidato)

    def inicia_tela(self) -> None:
        acoes = {1: self.altera_eleitor, 2: self.adiciona_eleitor,
                 3: self.lista_eleitores, 4: self.deleta_eleitor, 5: self.retorna}

        while True:
            acoes[self.tela_eleitor.exibe_opcoes()]()
