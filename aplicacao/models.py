# Classe que representa um cliente no sistema.
class Cliente:
    def __init__(
        self,
        nome,
        email,
        telefone=None,
        endereco=None,
        estado_civil=None,
        documento=None,
        cpf_cnpj = None,
        cadastro_ativo=True,
        situacao_profissional=None
    ):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.estado_civil = estado_civil
        self.documento = documento
        self.cpf_cnpj = cpf_cnpj
        self.cadastro_ativo = cadastro_ativo
        self.situacao_profissional = situacao_profissional

#Representação textual do cliente. Útil para logs e visualizações no terminal.
    def __repr__(self):
        return (
            f"Cliente(nome={self.nome}, email={self.email}, telefone={self.telefone}, "
            f"endereco={self.endereco}, estado_civil={self.estado_civil}, documento={self.documento}, "
            f"cpf_cnpj={self.cpf_cnpj} cadastro_ativo={self.cadastro_ativo}, situacao_profissional={self.situacao_profissional})"
        )
