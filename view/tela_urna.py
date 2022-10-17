from abstracts.abstract_tela import AbstractTela


class TelaUrna(AbstractTela):
    def exibe_opcoes(self):
        print(f'{"=" * 8} Eleições 2022 {"=" * 8}')
        print('Escolha uma das opções abaixo')
        print('1 - Configurar Urna')
        print('2 - Cadastrar Candidato')
        print('3 - Cadastrar Chapa')
        print('4 - Cadastrar Eleitor')
        print('5 - Votar')
        print('6 - Gerar Relatório dos Votos')

        opcao = self.get_opcao_escolhida("Digite a opção: ", [1, 2, 3, 4, 5, 6])
        return opcao

    def exibe_relatorio(self, dados_relatorio):
        pass

    def exibe_resultado(self, dados_resultado):
        pass

    def get_dados_configuracao(self):
        print(f'{"=" * 8} CONFIGURAÇÃO DA URNA {"=" * 8}')

        while True:
            try:
                max_eleitores = int(input("Digite o número máximo de eleitores: "))
                if max_eleitores <= 0:
                    raise ValueError
                max_candidatos = int(input("Digite o número máximo de candidatos: "))
                if max_candidatos <= 0:
                    raise ValueError
                turno = int(input("Digite o turno da eleição: "))
                
                while not 1 <= turno <= 2:
                    print("Turno inválido, digite um turno entre 1 e 2")
                    turno = int(input("Digite o turno da eleição: "))

                return {"max_eleitores": max_eleitores, "max_candidatos": max_candidatos, "turno": turno}
            except ValueError:
                print("Utilize apenas dígitos maiores que 0!")

    def get_dados_votos(self):
        pass

