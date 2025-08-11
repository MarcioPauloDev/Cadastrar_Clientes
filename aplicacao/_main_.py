from aplicacao.models import *
from aplicacao.services import *

# Função principal do menu

def menu():


    cliente = Cliente
    email = ""
    telefone = 0
    endereco = ""
    nome = ""
    cpf_cnpj = 0
    estado_civil = ""
    situacao = ""
    documento = ""
    ativo = False
    while True:
        print("\n======= MENU DE CLIENTES =======")
        print("1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("5. Sair")

        opcao = int(input("Escolha uma opção: "))

        # Opção 1: Adiciona novo cliente
        if opcao == 1:
            print("\n--- Cadastro de Novo Cliente ---")
            escolhaDocumento = int(input("Tipo do documento:\n1. CPF\n2. CNPJ \n: "))
            if escolhaDocumento == 1:
                documento = "CPF"
                cpf_cnpj = int(input("CPF: "))
                nome = input("Nome: ")
                telefone = int(input("Telefone: "))
                endereco = input("Endereço: ")
                email = input("Email: ")
                escolhaEstado = input("Estado Civil:\n1. Solteiro.\n2. Casado. \n3. Viuvo.\n: ")
                if escolhaEstado == "1":
                    estado_civil = "solteiro"
                elif escolhaEstado == "2":
                    estado_civil = "casado"
                elif escolhaEstado == "3":
                    estado_civil = "viuvo"
                escolhaSituacao = input("Situação profissional:\n1. Empregado.\n2. Autonomo.\n3. Desempregado.\n: ")
                if escolhaSituacao == "1":
                    situacao = 'empregado'
                elif escolhaSituacao == "2":
                    situacao = 'autonomo'
                elif escolhaSituacao == "3":
                    situacao = 'desempregado'
            elif escolhaDocumento == 2:
                documento = "CNPJ"
                cpf_cnpj = int(input("CNPJ: "))
                nome = input("Nome da empresa: ")
                telefone = int(input("Telefone: "))
                endereco = input("Endereço: ")
                email = input("Email: ")
                estado_civil = "nada consta"
                situacao = "empresa"
            escolhaAtivo = input("Estatus do Cliente? 1-[Ativo]\n2-[Inativo]: ")
            if escolhaAtivo == "1":
                ativo = True
            elif escolhaAtivo == "2":
                ativo = False

            cliente = Cliente(
                nome=nome,
                email=email,
                telefone=telefone,
                endereco=endereco,
                estado_civil=estado_civil,
                documento=documento,
                cpf_cnpj=cpf_cnpj,
                cadastro_ativo=ativo,
                situacao_profissional=situacao
            )

            adicionar_cliente(cliente)
            print("✅ Cliente adicionado com sucesso!")

        # Opção 2: Lista todos os clientes
        elif opcao == 2:
            print("\n--- Lista de Clientes ---")
            clientes = listar_clientes()
            for c in clientes:
                print(f"ID: {c[0]}\n",f"Nome: {c[1]}" if c[6] == "CPF" else f"Nome da empresa: {c[1]}",f"\nEmail: {c[2]}\nTelefone: {c[3]}\nAtivo: {'Sim' if c[7] else 'Não'}")

        # Opção 3: Atualiza dados de um cliente existente
        elif opcao == 3:
            print("\n--- Atualizar Cliente ---")
            cliente_id = int(input("ID do cliente: "))
            cliente_select = selecionar_cliente(cliente_id)
            if cliente_select[6] == "CPF":
                nome = input("Novo Nome: ")
                email = input("Novo email: ")
                telefone = input("Novo telefone: ")
                endereco = input("Novo endereço: ")
                escolhaEstado = input("Novo estado civil:\n1. Solteiro.\n2. Casado. \n3. Viuvo.\n: ")
                if escolhaEstado == "1":
                    estado_civil = "solteiro"
                elif escolhaEstado == "2":
                    estado_civil = "casado"
                elif escolhaEstado == "3":
                    estado_civil = "viuvo"
                escolhaSituacao = input("Nova situação profissional:\n1. Empregado.\n2. Autonomo.\n3. Desempregado.\n: ")
                if escolhaSituacao == "1":
                    situacao = 'empregado'
                elif escolhaSituacao == "2":
                    situacao = 'autonomo'
                elif escolhaSituacao == "3":
                    situacao = 'desempregado'
            elif cliente_select[6] == "CNPJ":
                nome = input("Novo nome da empresa: ")
                email = input("Novo email: ")
                telefone = input("Novo telefone: ")
                endereco = input("Novo endereço: ")
            escolhaAtivo = input("Cadastro ativo? 1-[Sim]\n2-[Não] ")
            if escolhaAtivo == "1":
                ativo = True
            elif escolhaAtivo == "2":
                ativo = False

            cliente = Cliente(
                nome=nome,
                email=email,
                telefone=telefone,
                endereco=endereco,
                estado_civil=cliente_select[5],
                documento=cliente_select[6],
                cpf_cnpj=cliente_select[7],
                cadastro_ativo=ativo,
                situacao_profissional=cliente_select[9]
            )

            atualizar_cliente(cliente_id, cliente)
            print("✅ Cliente atualizado com sucesso!")

        # Opção 4: Remove um cliente
        elif opcao == 4:
            print("\n--- Deletar Cliente ---")
            cliente_id = int(input("ID do cliente a ser deletado: "))
            deletar_cliente(cliente_id)
            print("🗑️ Cliente removido com sucesso!")

        # Opção 5: Sair do sistema
        elif opcao == 5:
            print("Encerrando o sistema. Até mais!")
            break

        else:
            print("⚠️ Opção inválida. Tente novamente.")


# Executa o menu se o script for chamado diretamente
if __name__ == "__main__":
    menu()
