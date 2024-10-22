import pandas as pd
import random
from datetime import datetime, timedelta
import subprocess
import sys

# ABRIR JANELA EXECUTÁVEL ---------------------------
if len(sys.argv) == 1:
    # Executa o script em uma nova janela do terminal
    subprocess.Popen(['start', 'cmd', '/k', 'python', 'PY_SIMU_PHARMACY.py', 'sub'], shell=True)
else:
    # Este código será executado na nova janela aberta
    print()


#CARREGAR PLANILHAS ---------------------------
# Carregar a planilha de medicamentos
file_path_medicamentos = r'C:\Users\Pichau\Desktop\PHARMACY PROJECT\TB_CADASTRO_MEDICAMENTOS.xlsx'
tb_medicamentos = pd.read_excel(file_path_medicamentos, engine='openpyxl')

# Carregar a tabela de vendedores
file_path_vendedores = r'C:\Users\Pichau\Desktop\PHARMACY PROJECT\TB_CADASTRO_VENDEDOR.xlsx'
tb_vendedores = pd.read_excel(file_path_vendedores, engine='openpyxl')

# Carregar a planilha de clientes
file_path_clientes = r'C:\Users\Pichau\Desktop\PHARMACY PROJECT\TB_CADASTRO_CLIENTE.xlsx'
tb_cliente = pd.read_excel(file_path_clientes, engine='openpyxl')

# Carregar a planilha de vendas
file_path_vendas = r'C:\Users\Pichau\Desktop\PHARMACY PROJECT\TB_CADASTRO_VENDAS.xlsx'
tb_vendas = pd.read_excel(file_path_vendas, engine='openpyxl')


#FUNÇÕES ---------------------------
def menu_vendedor():
    while True:  # Mantém o menu ativo até que uma opção válida seja escolhida
        print("\nO que deseja?")
        print("1 - CADASTRAR NOVO MEDICAMENTO")
        print("2 - CADASTRAR NOVO VENDEDOR")
        print("3 - ALTERAR ESTOQUE")
        print("4 - MENU DE USUÁRIO")
        print("0 - TROCAR DE VENDEDOR")
        print("9 - FECHAR PROGRAMA")  # Opção para fechar o programa

        # Recebe a opção do vendedor
        try:
            OPC = int(input("Insira a opção desejada: "))
            if OPC in [1, 2, 3, 4, 0]:  # Se a opção for válida
                return OPC  # Retorna a opção escolhida
            elif OPC == 9:  # Se o usuário quiser encerrar
                print("Encerrando o programa...")
                exit()  # Encerra o programa
            else:  # Opção inválida
                print("Opção inválida! Por favor, insira um número válido.")
        except ValueError:  # Se o usuário não digitar um número
            print("Opção inválida! Por favor, insira um número.")

def menu_usuario():
    while True:  # Mantém o menu ativo até que uma opção válida seja escolhida
        print("\n--- MENU DE USUÁRIOS ---")
        print("1 - VENDEDOR")
        print("2 - CLIENTE")
        print("9 - FECHAR PROGRAMA")  # Opção para fechar o programa

        # Recebe a opção do usuário
        try:
            USU = int(input("Que tipo de usuário você é: "))
            if USU in [1, 2]:  # Se a opção for válida
                return USU  # Retorna a opção escolhida
            elif USU == 9:  # Se o usuário quiser encerrar
                print("\nEncerrando o programa...\n")
                exit()  # Encerra o programa
            else:  # Opção inválida
                print("\nOpção inválida! Por favor, insira um número.\n")
        except ValueError:  # Se o usuário não digitar um número
                print("\nOpção inválida! Por favor, insira um número.\n")


#INÍCIO DO CÓDIGO ---------------------------
print("\n--- TABELA DE MEDICAMENTOS ---\n")
print(tb_medicamentos)

USU = 0

while USU == 0:
    USU = menu_usuario()
    if USU == 0:
        print("\nOPÇÃO INVÁLIDA")
        USU = menu_usuario()

while USU<1 or USU>2:
    print("\nOPÇÃO INVÁLIDA")
    USU = menu_usuario()



# CÓDIGO PARA VENDEDOR ---------------------------
OPC = 0
while USU == 1:
    # VERIFICANDO CPF DO VENDEDOR
    while OPC == 0:
        cpf = str(input("\nInsira o CPF do vendedor cadastrado: "))
        cpf_vendedor = ''.join(char for char in cpf if char.isdigit())

        # VALIDANDO CPF DE VENDEDOR
        while len(cpf_vendedor) != 11:
            print("CPF inserido inválido!")
            print()
            cpf = str(input("Insira corretamento o CPF de vendedor cadastrado: "))
            cpf_vendedor = ''.join(char for char in cpf if char.isdigit())

        cpf_vendedor_fin = cpf_vendedor[:3] + "." + cpf_vendedor[3:6] + "." + cpf_vendedor[6:9] + "-" + cpf_vendedor[9:11]
        print("Seu CPF é:", cpf_vendedor_fin)

        # CPF encontrado na tabela de vendedores!
        if cpf_vendedor_fin in tb_vendedores['CPF'].values:
            # Obter o nome do vendedor
            nome_vendedor = tb_vendedores.loc[tb_vendedores['CPF'] == cpf_vendedor_fin, 'Nome'].values[0]
            print("CPF ENCONTRADO no cadastro de vendedores!")
            print("Nome do vendedor:", nome_vendedor)  # Mostra o nome do vendedor

            # Menu de opções!
            print()
            OPC = menu_vendedor()

    while OPC not in [0, 1, 2, 3, 4, 9]:
        print()
        print("OPÇÃO INVÁLIDA")
        print()
        OPC = menu_vendedor()

    # CADASTRAR NOVO MEDICAMENTO:
    while OPC == 1:
        # Solicitar o código do produto
        cod_prod = str(input("Insira o código do produto que deseja adicionar: ")).upper()

        # Verificar se o código do produto está na planilha
        if cod_prod in tb_medicamentos['Abreviação'].values:  
            print("PRODUTO JÁ INSERIDO!.")
            produto_info = tb_medicamentos.loc[tb_medicamentos['Abreviação'] == cod_prod]
            print(produto_info)

            print()
            OPC = menu_vendedor()
        else:
            # Adicionar um novo produto
            nome_prod = str(input("Insira o nome do medicamento: ")).lower()
            preco_prod = round(float(input("Insira o preço do medicamento: ")), 2)
            estoque_prod = int(input("Insira a quantidade em estoque do produto: "))

            novo_produto = pd.DataFrame({
                'Abreviação': [cod_prod],
                'Medicamento': [nome_prod],
                'Preço (R$)': [preco_prod],
                'Estoque': [estoque_prod]
            })

            tb_medicamentos = pd.concat([tb_medicamentos, novo_produto], ignore_index=True)
            tb_medicamentos.to_excel(file_path_medicamentos, index=False, engine='openpyxl')

            print("Novo medicamento adicionado com sucesso!")
            print("--- TABELA DE MEDICAMENTOS ATUALIZADA ---")
            print(tb_medicamentos)
            print()

            # Menu de opções!
            print()
            OPC = menu_vendedor()

    # CADASTRAR NOVO VENDEDOR:
    while OPC == 2:
        print()
        cpf = str(input("Insira o CPF para cadastro: "))

        cpf_cadastro = ''.join(char for char in cpf if char.isdigit())

        # VALIDANDO CPF DE VENDEDOR
        while len(cpf_cadastro) != 11:
            print("CPF inserido inválido!")
            cpf = str(input("Insira corretamente o CPF de vendedor cadastrado: "))
            cpf_cadastro = ''.join(char for char in cpf if char.isdigit())

        cpf_cadastro_fin = cpf_cadastro[:3] + "." + cpf_cadastro[3:6] + "." + cpf_cadastro[6:9] + "-" + cpf_cadastro[9:11]
        print("O CPF inserido é:", cpf_cadastro_fin)

        # Carregar a tabela de vendedores
        tb_vendedores = pd.read_excel(file_path_vendedores, engine='openpyxl')

        # CPF encontrado na tabela de vendedores!
        if cpf_cadastro_fin in tb_vendedores['CPF'].values:
            # Obter o nome do vendedor correto
            nome_vendedor = tb_vendedores.loc[tb_vendedores['CPF'] == cpf_cadastro_fin, 'Nome'].values[0]
            print(f"CPF ENCONTRADO no cadastro de vendedores! Nome do vendedor: {nome_vendedor}.")
            
                # Menu de opções!
            print()
            OPC = menu_vendedor()

        else:
            # CPF não registrado, então cadastrar um novo vendedor
            print()

            nome_vendedor = str(input("Insira o nome deste novo vendedor(a): "))
            print()

            cod_vendedor = str(input("Insira o código deste novo vendedor(a): "))
            print()

            gen_vendedor = str(input("Insira o gênero deste novo vendedor(a): ")).upper()
            while gen_vendedor !="M" or gen_vendedor !="F":
                print()
                print("Gênero inserido inválido")
                gen_vendedor = str(input("Insira o gênero deste novo vendedor(a): ")).upper()

            print()
            idade_vendedor = int(input("Insira a idade, em anos, deste novo vendedor(a): "))

            # Adicionar informações na planilha de vendedor
            novo_vendedor = pd.DataFrame({
                'CPF': [cpf_cadastro_fin],
                'Código do Vendedor': [cod_vendedor],
                'Nome': [nome_vendedor],
                'Sexo': [gen_vendedor],
                'Idade': [idade_vendedor]
            })

            tb_vendedores = pd.concat([tb_vendedores, novo_vendedor], ignore_index=True)
            tb_vendedores.to_excel(file_path_vendedores, index=False, engine='openpyxl')
            print("Novo vendedor adicionado com sucesso!")
            print("--- TABELA DE VENDEDORES ATUALIZADA ---")
            print(tb_vendedores)
            print()
            OPC = menu_vendedor()

    while OPC == 4:
            USU = menu_usuario()
            if USU == 1 or USU == 2:
                OPC = 0

            elif USU != 1 and USU != 2:
                print()
                print("OPÇÃO INVÁLIDA")
                OPC = menu_vendedor()
            
    while OPC == 3:
        print(tb_medicamentos)
        cod_stq = str(input("Insira o código do medicamento que deseja alterar o estoque: "))
        medicamento = tb_medicamentos[tb_medicamentos['Abreviação'] == cod_stq]

        if not medicamento.empty:
            # Exibe o estoque atual
            estoque_atual = medicamento['Estoque'].values[0]
            print(f"Estoque atual de {cod_stq}: {estoque_atual} unidades")
            
            # Solicita o novo valor de estoque
            novo_estoque = -1
            while novo_estoque < 0:  # Verifica se o valor é positivo
                try:
                    novo_estoque = int(input("Insira o novo valor de estoque (positivo e inteiro): "))
                    if novo_estoque >= 0:
                        # Atualiza o valor do estoque no DataFrame
                        tb_medicamentos.loc[tb_medicamentos['Abreviação'] == cod_stq, 'Estoque'] = novo_estoque
                        
                        # Salva o DataFrame atualizado no Excel
                        tb_medicamentos.to_excel(file_path_medicamentos, index=False, engine='openpyxl')
                        print("Estoque atualizado com sucesso!")

                        # Exibe a linha do medicamento com o novo valor de estoque
                        medicamento_atualizado = tb_medicamentos[tb_medicamentos['Abreviação'] == cod_stq]
                        print("Linha atualizada do medicamento:")
                        print(medicamento_atualizado)

                    else:
                        print("Por favor, insira um valor positivo.")
                except ValueError:
                    print("Por favor, insira um número inteiro válido.")
            
            # Volta ao menu após alterar o estoque
            print()
            OPC = menu_vendedor()
        else:
            # Se o código não for encontrado, volta ao menu
            print()
            print("OPÇÃO INVÁLIDA")
            print()
            OPC = menu_vendedor()
            
    else:
        if USU == 1:
            print("CPF NÃO ENCONTRADO no cadastro de vendedores!")
            print()
            USU = menu_usuario()


# CÓDIGO PARA CLIENTE ---------------------------
while USU == 2:

    # CADASTRANDO CPF
    user_cpf = str(input("Insira seu CPF: "))
    print()
    num_cpf = ''.join(char for char in user_cpf if char.isdigit())

    # VALIDANDO CPF
    while len(num_cpf) != 11:
        print("CPF inserido inválido!")
        print()
        user_cpf = str(input("Insira seu CPF: "))
        num_cpf = ''.join(char for char in user_cpf if char.isdigit())  # MANTER SOMENTE NÚMEROS DO CPF

    cli_cpf = num_cpf[:3] + "." + num_cpf[3:6] + "." + num_cpf[6:9] + "-" + num_cpf[9:11]  # FORMATANDO CPF
    print("Seu CPF é:", cli_cpf)

    # VERIFICANDO CPF NA TABELA
    if tb_cliente['CPF'].isin([cli_cpf]).any():
        print("Seu CPF já está cadastrado!")
        nome_cliente = tb_cliente.loc[tb_cliente['CPF'] == cli_cpf, 'Nome'].values[0]
        print(f"Bem-vindo, {nome_cliente}!")

    else:
        print("Seu CPF NÃO está cadastrado!")
        print()
        print("Vamos efetuar o cadastro:")
        print()

        # INICIANDO CADASTRO
        nome = str(input("Insira seu nome: "))
        nome_cliente = nome.lower()
        print()

        idade_cliente = int(input("Insira sua idade em anos: "))
        print()

        cidade = str(input("Insira sua cidade: "))
        cidade_cliente = cidade.lower()
        print()

        gen = str(input("Insira seu gênero / F para feminino e M para masculino: "))
        gen_cliente = gen.upper()
        print()

        # INSERINDO DADOS NA TABELA
        tb_cliente.loc[len(tb_cliente)] = [nome_cliente, cli_cpf, idade_cliente, gen_cliente, cidade_cliente]

        # Salvar as alterações na planilha de clientes
        tb_cliente.to_excel(file_path_clientes, index=False, engine='openpyxl')
        
        print(tb_cliente)
        print()

    # COMEÇANDO AS COMPRAS
    print("----- VAMOS AS COMPRAS -----")
    print()

    # Imprimindo a lista de medicamentos com preços
    for index, row in tb_medicamentos.iterrows():
        print(f"{row['Abreviação']} = {row['Medicamento']} - R$ {row['Preço (R$)']:.2f} - Estoque: {row['Estoque']} unidades")

    FIM_COMPRA = ""  # AO FINAL DO CÓDIGO, FIM="S" PARA ENCERRAR A COMPRA!

    valorTT = 0  # ESTIPULANDO VALOR INICIAL DA COMPRA COMO 0,00

    # GERAR NOTA FISCAL ALEATÓRIA
    nf_random = random.randint(0, 999999)  # GERANDO NÚMERO ALEATÓRIO ENTRE 0 E 999999
    NF = "NF" + str(nf_random).zfill(6)

    # GERANDO DATAS ALEATÓRIAS
    # Definir o intervalo de datas
    data_inicio = datetime(2024, 7, 1)
    data_fim = datetime(2024, 7, 31)

    # Calcular o número de dias no intervalo
    dias_intervalo = (data_fim - data_inicio).days

    # Gerar um número aleatório de dias
    dias_aleatorios = random.randint(0, dias_intervalo)

    # Adicionar os dias aleatórios à data de início
    data_aleatoria = data_inicio + timedelta(days=dias_aleatorios)
    data = data_aleatoria

    while FIM_COMPRA != "S":
        cod = str(input("Insira o código do produto desejado: "))
        print()
        cod_prod = cod.upper()  # SELECIONANDO CÓDIGO DO PRODUTO DESEJADO

        while True:
            if cod_prod in tb_medicamentos['Abreviação'].values:
                preco = tb_medicamentos.loc[tb_medicamentos['Abreviação'] == cod_prod, 'Preço (R$)'].values[0]
                estoque = tb_medicamentos.loc[tb_medicamentos['Abreviação'] == cod_prod, 'Estoque'].values[0]

                print(f"O preço do medicamento {cod_prod} é R$ {preco:.2f}")
                print()

                break  # Sai do loop se a abreviação for válida
            else:
                print("Código do medicamento não encontrado. Tente novamente.")
                print()
                cod = str(input("Insira o código do produto desejado: "))
                print()
                cod_prod = cod.upper()

        quant = int(input("Insira a quantidade desejada: "))  # QUANTIDADE DE REMÉDIOS
        print()

        while quant > estoque:  # QUANTIDADE MAIOR QUE ESTOQUE:
            print(f"Estoque insuficiente. Disponível apenas {estoque} unidades.")
            print()
            quant = int(input("Insira a quantidade desejada: "))

        print(f"Quantidade em estoque: {estoque}. Pedido de {quant} unidades aceito.")
        print()

        tb_medicamentos.loc[tb_medicamentos['Abreviação'] == cod_prod, 'Estoque'] -= quant  # Subtraímos do estoque após o pedido ser aceito

        #CÓDIGO DO VENDEDOR DA COMPRA
        while True:
            cod_vendedor = input("Insira o código do vendedor (somente 3 letras): ").upper()

            # Verifica se o código tem 3 letras e se são apenas letras
            if len(cod_vendedor) == 3 and cod_vendedor.isalpha():
                # Verifica se o código existe na planilha de vendedores
                if cod_vendedor in tb_vendedores['Código do Vendedor'].values:
                    print(f"Código {cod_vendedor} encontrado!")
                    break  # Código válido, sair do loop
                else:
                    print(f"Código {cod_vendedor} não encontrado no cadastro de vendedores.")
            else:
                print("Código inválido! Certifique-se de usar apenas 3 letras.")


        #PUXA O PREÇO REGISTRADO DIRETO TA TABELA DE MEDICAMENTOS
        preco = tb_medicamentos.loc[tb_medicamentos['Abreviação'] == cod_prod, 'Preço (R$)'].values[0]  # PREÇO DO REMÉDIO SELECIONADO
        

        #VALOR FINAL POR QUANTIDADE DE PRODUTO
        valor = quant * preco


        #VALOR FINAL DA COMPRA
        valorTT += valor  # VALOR TOTAL DA COMPRA

        print("O valor para", quant, "unidades do medicamento", cod_prod, "é R$", valor)
        print()
        print("O valor total da compra é", valorTT)

        # ADICIONANDO AS INFORMAÇÕES NA TABELA DE VENDAS
        tb_vendas.loc[len(tb_vendas)] = [cli_cpf, cod_vendedor, cod_prod, preco, quant, valor, NF, data]

        # Salvar as alterações na planilha de vendas
        tb_vendas.to_excel(file_path_vendas, index=False, engine='openpyxl')

        fim = str(input("Deseja finalizar a compra? 'S' para sim ou qualquer outro dígito para não: "))
        print()
        FIM_COMPRA = fim.upper()

    ultima_venda = tb_vendas[tb_vendas['Nota Fiscal'] == NF]

    # Verificar se há vendas correspondentes

    print(f"--- {NF} ---")
    print(ultima_venda)
    print("O valor final da compra é R$", valorTT)
    print()
    print()
    print("Mais alguém para ser atendido?")
    end = str(input("S para sim e qualquer dígito para não: ")).upper()
    if end !='S':
        OPC = 3
    else:
        USU = 0
