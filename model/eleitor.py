class Eleitor():
    def __init__(self, cpf: str, nome: str, email: str, endereco: str, tipo_eleitor: TipoEleitor) -> None:
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__endereco = endereco
        self.__tipo_eleitor = tipo_eleitor

        @property
        def cpf(self) -> str:
            return self.__cpf

        @property
        def nome(self) -> str:
            return self.__nome

        @property
        def email(self) -> str:
            return self.__email

        @property
        def endereco(self) -> str:
            return self.__endereco

        @property
        def tipo_eleitor(self) -> TipoEleitor:
            return self.__tipo_eleitor

        @cpf.setter
        def cpf(self, cpf) -> None:
            self.cpf = cpf

        @nome.setter
        def nome(self, nome) -> None:
            self.nome = nome

        @email.setter
        def email(self, email) -> None:
            self.email = email

        @endereco.setter
        def endereco(self, endereco) -> None:
            self.endereco = endereco

        @tipo_eleitor.setter
        def tipo_eleitor(self, tipo_eleitor) -> None:
            self.tipo_eleitor = tipo_eleitor
