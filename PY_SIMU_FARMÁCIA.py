import pandas as pd

#CRIANDO TABELA DE CLIENTES
dados_cliente = {
    'Nome': [],
    'CPF': [],
    'Idade': [],
    'Genero': [],
    'Cidade': []
}

tb_cliente = pd.DataFrame(dados_cliente)


# CRIANDO TABELA DE REMÉDIOS
dados_medicamentos = {
    'Abreviação': ['PAR', 'ASP', 'DIP', 'IBP', 'LTD', 'ANT', 'CET', 'OMZ', 'NIT', 'RAN'],
    'Medicamento': ['Paracetamol', 'Aspirina', 'Dipirona', 'Ibuprofeno', 'Loratadina',
                    'Amoxicilina', 'Cetirizina', 'Omeprazol', 'Nitazoxanida', 'Ranitidina'],
    'Preço (R$)': [27.22, 19.07, 16.88, 19.58, 7.09, 15.39, 37.25, 20.14, 12.64, 14.58],
    'Estoque': [10, 5, 12, 7, 4, 8, 6, 3, 9, 11]
}

tb_medicamentos = pd.DataFrame(dados_medicamentos)


#CRIANDO TABELA DE VENDAS
dados_vendas = ({
    'CPF': [],
    'Código do Produto': [],
    'Preço (R$)': [],
    'Quantidade': [],
    'Valor (R$)': [],
    'Nota Fiscal': [],
    'Data': []
})
tb_vendas = pd.DataFrame(dados_vendas)


#----------- COMEÇANDO O PROGRAMA -----------
END = "S" #USADO PARA REPETIR O PROGRAMA COM CLIENTES DIFERENTES

print("Atualmente temos os seguintes medicamentos e seus valores: ")
print(tb_medicamentos)

print("Deseja adicionar algum medicamento?") #ADICIONANDO NOVOS MEDICAMENTOS
EDIT=str(input("Pressione S para sim e qualquer outra tecla para iniciar as compras: ")).upper()
print()

while EDIT== "S": #REPETIÇÃO PARA SEMPRE QUE QUISER ADICIONAR NOVOS MEDICAMENTOS
    while True:
        cod = str(input("Insira o código do seu produto: ")).upper()
        novo_cod = ''.join(char for char in cod if char.isalpha())  # Filtra letras
        print()

        # Verificando se o código tem 3 letras
        if len(novo_cod) != 3:
            print("Código inválido! O código deve ter exatamente 3 letras.")
            print()
            continue

        # Verificando se o código já está na lista
        if novo_cod in tb_medicamentos['Abreviação'].values:
            print("Código já cadastrado! Insira um novo código.")
            print()
            continue

        # Se passar pelas verificações, o loop é interrompido
        print(f"Código {novo_cod} válido!.")
        print()
        break


    novo_med = str(input("Insira o nome do medicamento: "))
    print()

    novo_preco = float(input("Insira o preço deste medicamento: "))
    print()

    novo_estoque = int(input("Insira a quantidade deste medicamento em estoque: "))
    print()

    tb_medicamentos.loc[len(tb_medicamentos)] = [novo_cod, novo_med, novo_preco, novo_estoque]
    print()
    print(tb_medicamentos)
    print()
    print("Deseja adicionar algum medicamento?")
    EDIT=str(input("Pressione S para sim e qualquer outra tecla para iniciar as compras: "))

valorFIN = 0.0
while END == "S":

    #CADASTRANDO CPF
    user_cpf=str(input("Insira seu CPF: "))
    print()
    num_cpf = ''.join(char for char in user_cpf if char.isdigit())


    #VALIDANDO CPF
    while len(num_cpf) != 11:
        print("CPF inserido inválido!")
        print()
        user_cpf=str(input("Insira seu CPF: "))
        num_cpf = ''.join(char for char in user_cpf if char.isdigit()) #MANTER SOMENTE NÚMEROS DO CPF

    fin_cpf = num_cpf[:3] + "." + num_cpf[3:6] + "." + num_cpf[6:9] + "-" + num_cpf[9:11] #FORMATANDO CPF
    print("Seu CPF é:", fin_cpf)


    #VERIFICANDO CPF NA TABELA
    if tb_cliente['CPF'].isin([fin_cpf]).any():
        print("Seu CPF já está cadastrado!")

    else:
        print("Seu CPF NÃO está cadastrado!")
        print()
        print("Vamos efetuar o cadastro:")
        print()


    #INICIANDO CADASTRO
        nome = str(input("Insira seu nome: "))
        nome_cliente=nome.lower()
        print()

        idade_cliente = int(input("Insira sua idade em anos: "))
        print()

        cidade = str(input("Insira sua cidade: "))
        cidade_cliente = cidade.lower()
        print()

        gen = str(input("Insira seu gênero / F para feminino e M para masculino: "))
        gen_cliente = gen.lower()
        print()

        #INSERINDO DADOS NA TABELA
        tb_cliente.loc[len(tb_cliente)] = [nome_cliente, fin_cpf, idade_cliente, gen_cliente, cidade_cliente]
        print(tb_cliente)
        print()


    #COMEÇANDO AS COMPRAS
    print("----- VAMOS AS COMPRAS -----")
    print()


    # Imprimindo a lista de medicamentos com preços
    for index, row in tb_medicamentos.iterrows():
        print(f"{row['Abreviação']} = {row['Medicamento']} - R$ {row['Preço (R$)']:.2f} - Estoque: {row['Estoque']} unidades")

    FIM_COMPRA="" #AO FINAL DO CÓDIGO, FIM="S" PARA ENCERRAR A COMPRA!

    valorTT=0 #ESTIPULANDO VALOR INICIAL DA COMPRA COMO 0,00


    #GERAR NOTA FISCAL ALEATÓRIA
    import random

    nf_random=random.randint(0, 999999) #GERANDO NÚMERO ALEATÓRIO ENTRE 0 E 999999
    NF = "NF"+str(nf_random).zfill(6)


    #GERANDO DATAS ALEATÓRIAS
    from datetime import datetime, timedelta

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

        cod=str(input("Insira o código do produto desejado: "))
        print()
        cod_prod= cod.upper() #SELECIONANDO CÓDIGO DO PRODUTO DESEJADO

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
                cod=str(input("Insira o código do produto desejado: "))
                print()
                cod_prod= cod.upper()

        quant=int(input("Insira a quantidade desejada: ")) #QUANTIDADE DE REMÉDIOS
        print()

        while quant > estoque: #QUANTIDADE MAIOR QUE ESTOQUE:
            print(f"Estoque insuficiente. Disponível apenas {estoque} unidades.")
            print()
            quant = int(input("Insira a quantidade desejada: "))

        print(f"Quantidade em estoque: {estoque}. Pedido de {quant} unidades aceito.")
        print()

        tb_medicamentos.loc[tb_medicamentos['Abreviação'] == cod_prod, 'Estoque'] -= quant # Subtraímos do estoque após o pedido ser aceito

        preco = tb_medicamentos.loc[tb_medicamentos['Abreviação'] == cod_prod, 'Preço (R$)'].values[0] #PREÇO DO REMÉDIO SELECIONADO

        valor = quant * preco

        valorTT = valorTT + valor #VALOR TOTAL DA COMPRA

        print("O valor para", quant, "unidades do medicamento", cod_prod, "é R$", valor)
        print()
        print("O valor total da compra é", valorTT)

        #ADICIONANDO AS INFORMAÇÕES NA TABELA DE VENDAS
        tb_vendas.loc[len(tb_vendas)] = [fin_cpf, cod_prod, preco, quant, valor, NF, data]

        fim=str(input("Deseja finalizar a compra? 'S' para sim ou qualquer outro digito para não: "))
        print()
        FIM_COMPRA=fim.upper()

    print("O valor final da compra é R$", valorTT)
    print()
    print()
    print("Mais alguém para ser atendido?")
    end=str(input("S para sim e qualquer digito para não: "))
    print()
    END=end.upper()
    valorFIN= valorFIN + valorTT

#FILTRANDO RELATÓRIOS
print("Deseja gerar algum relatório?")

filt = str(input("Insira S para sim ou pressione qualquer outra tecla para não: ")).upper()
while filt == "S":

    print()
    print("1 - Filtrar dia")
    print("2 - Filtrar medicamento")
    print("3 - Filtrar NF")
    print("4 - Filtrar CPF")
    print()

    while True:
        FILTRO = input("Insira o número referente ao filtro que deseja aplicar: ")

        # Verifica se a entrada é um número e se está entre 1 e 4
        if FILTRO.isdigit() and 1 <= int(FILTRO) <= 4:
            FILTRO = int(FILTRO)
            break  # Saímos do loop se a entrada for válida
        else:
            print("Por favor, insira um número válido (1 a 4).")

    # Aplica o filtro escolhido
    if FILTRO == 1:
        filtro_data = input("Insira a data desejada (formato AAAA-MM-DD): ")
        try:
            # Verifica se a data foi inserida corretamente no formato desejado
            filtro_data = datetime.strptime(filtro_data, "%Y-%m-%d").date()
            print(f"Filtrando por data: {filtro_data}")

            # Verificando se a data existe na coluna "Data" da tabela tb_vendas
            # Primeiro convertemos a coluna "Data" para o mesmo formato de datetime
            tb_vendas['Data'] = pd.to_datetime(tb_vendas['Data']).dt.date

            # Filtrando as vendas com a data especificada
            tb_filtrada = tb_vendas[tb_vendas['Data'] == filtro_data]

            # Verificando se há dados filtrados e mostrando o resultado
            if not tb_filtrada.empty:
                print(f"Exibindo as vendas da data: {filtro_data}")
                print(tb_filtrada)
            else:
                print(f"Não há vendas registradas para a data: {filtro_data}")

        except ValueError:
            print("Data inválida! Use o formato AAAA-MM-DD.")

    elif FILTRO == 2:
        filtro_medicamento = str(input("Insira o código do medicamento desejado: ")).upper()
        print(f"Filtrando por medicamento: {filtro_medicamento}")

        while filtro_medicamento not in tb_medicamentos['Abreviação'].values:
            print("Este código é inválido")
            print()
            filtro_medicamento = input("Insira o código do medicamento desejado: ")

        while filtro_medicamento not in tb_vendas['Código do Produto'].values:
            print("Não houve compra deste medicamento!")
            print()
            filtro_medicamento = input("Insira o código do medicamento desejado: ")

        tb_filtrada = tb_vendas[tb_vendas['Código do Produto'] == filtro_medicamento]
        print(f"Exibindo as vendas com o medicamento: {filtro_medicamento}")
        print(tb_filtrada)

    elif FILTRO == 3:
        NF = (input("Insira a nota fiscal desejada no formato 000000 (somente os números): "))
        print()

        while len(NF) != 6:
            print("NF inválida!")
            NF = (input("Insira a nota fiscal desejada no formato 000000 (somente os números): "))
    
        filtro_nf= "NF"+NF

        print(f"Filtrando por nota fiscal: {filtro_nf}")

        while filtro_nf not in tb_vendas['NF'].values:
            print("Nota fiscal não localizada!")
            filtro_nf = input("Insira a nota fiscal desejada: ")

        tb_filtrada = tb_vendas[tb_vendas['Nota Fiscal'] == filtro_nf]
        print(f"Exibindo a nota fiscal: NF{filtro_nf}")
        print(tb_filtrada)

    elif FILTRO == 4:
        cpf = str(input("Insira o CPF desejado (somente os números): "))
        print()

        while len(cpf) != 11:
            print("CPF incorreto!")
            cpf = str(input("Insira o CPF desejado (somente os números): "))

        filtro_cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11] #FORMATANDO CPF
        print(f"Filtrando por CPF: {filtro_cpf}")

        while filtro_cpf not in tb_vendas['CPF'].values:
            print("CPF não localizado!")
            filtro_cpf = input("Insira a nota fiscal desejada: ")

        tb_filtrada = tb_vendas[tb_vendas['CPF'] == filtro_cpf]
        print(f"Exibindo compras do cpf: {filtro_cpf}")
        print(tb_filtrada)

    # Pergunta se deseja gerar mais algum filtro
    print("Deseja visualizar mais algum filtro?")
    filt = input("Insira S para sim ou pressione qualquer outra tecla para não: ").upper()

print()
print()
print("TABELA DE CLIENTES:")
print(tb_cliente)

print()
print()
print("TABELA DE MEDICAMENTOS:")
print(tb_medicamentos)

print()
print()
print("TABELA DE VENDAS:")
tb_vendas = tb_vendas.sort_values(by='Data')
print(tb_vendas)
print('TOTAL VENDIDO: ',valorFIN)