from abstracts.abstract_tela import AbstractTela


class TelaUrna(AbstractTela):
    def exibe_opcoes(self):
        print(f'--- Eleições 2022 ---')
        print('Escolha uma das opções abaixo')
        print('1 - Configurar Urna')
        print('2 - Cadastrar Candidato')
        print('3 - Cadastrar Chapa')
        print('4 - Cadastrar Eleitor')
        print('5 - Votar')
        print('6 - Gerar Relatório dos Votos')
        print('7 - Encerrar Sessão')

        opcao = self.get_int_input("Digite a opção: ", 7)
        return opcao

    def exibe_relatorio(self, dados_relatorio):
        pass

    def exibe_resultado(self, dados_resultado):
        pass

    def get_dados_configuracao(self):
        print(f'--- Configuração da Urna ---')
        max_eleitores = self.get_int_input(
            "Digite o número máximo de eleitores: ")
        max_candidatos = self.get_int_input(
            "Digite o número máximo de candidatos: ")
        turno = self.get_int_input("Digite o turno da eleição: ", 2)

        return {"max_eleitores": max_eleitores,
                "max_candidatos": max_candidatos, "turno": turno}

    def get_voto(self, cargo: str):
        print(f'Vote para o candidato a {cargo}')
        num_candidato = self.get_int_input(f'Número do candidato: ', 98, True)
        
        print('1 - Sim')
        print('2 - Corrige')
        confirma = self.get_int_input('Confirma ?: ', 2)

        return {'num_candidato': num_candidato, 'confirma': confirma}
