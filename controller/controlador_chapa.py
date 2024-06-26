from abstracts.abstract_controlador import AbstractControlador
from view.tela_chapa import TelaChapa
from model.chapa import Chapa
from exceptions.chapa_ja_cadastrada import ChapaJaCadastradaException


class ControladorChapa(AbstractControlador):
    def __init__(self, controlador_urna) -> None:
        self.__controlador_urna = controlador_urna
        self.__tela_chapa = TelaChapa()
        self.__chapas = []

    @property
    def controlador_urna(self):
        return self.__controlador_urna

    @property
    def tela_chapa(self) -> TelaChapa:
        return self.__tela_chapa

    @property
    def chapas(self) -> list:
        return self.__chapas

    def seleciona_chapa(self):
        indice_chapa = self.tela_chapa.get_chapa(self.chapas)
        chapa = self.chapas[indice_chapa]
        return chapa

    def adiciona_chapa(self):
        try:
            dados_chapa = self.tela_chapa.get_dados_chapa()
            for chapa in self.chapas:
                if dados_chapa["num_chapa"] == chapa.num_chapa:
                    raise ChapaJaCadastradaException

            self.chapas.append(Chapa(dados_chapa["num_chapa"],
                                     dados_chapa["nome_chapa"]))

        except Exception as e:
            self.tela_chapa.alert(e)

    def deleta_chapa(self) -> None:
        if not self.chapas:
            self.tela_chapa.alert("Não há chapas cadastradas")
            return
        chapa = self.seleciona_chapa()
        if not chapa:
            return
        self.chapas.remove(chapa)

    def altera_chapa(self):
        if not self.chapas:
            self.tela_chapa.alert('Não há chapas cadastradas')
            return
        chapa = self.seleciona_chapa()
        if not chapa:
            return

        dados_atualizados = self.tela_chapa.get_dados_chapa()
        chapa.num_chapa = dados_atualizados["num_chapa"]
        chapa.nome_chapa = dados_atualizados["nome_chapa"]

    def lista_chapas(self):
        if not self.chapas:
            self.tela_chapa.alert('Não há chapas cadastradas')
            return
        for chapa in self.chapas:
            self.tela_chapa.exibe_chapa(
                {'num_chapa': chapa.num_chapa, 'nome_chapa': chapa.nome_chapa, 'candidatos': chapa.candidatos})

    def add_candidato_chapa(self, candidato: 'Candidato'):
        for chapa in self.chapas:
            if candidato in chapa.candidatos:
                return
            if chapa == candidato.chapa:
                chapa.candidatos.append(candidato)

    def remove_candidato_chapa(self, candidato: 'Candidato'):
        for chapa in self.chapas:
            if chapa == candidato.chapa:
                chapa.candidatos.remove(candidato)

    def inicia_tela(self) -> None:
        acoes = {1: self.altera_chapa, 2: self.adiciona_chapa,
                 3: self.lista_chapas, 4: self.deleta_chapa, 5: self.retorna}

        while True:
            acoes[self.tela_chapa.exibe_opcoes()]()
