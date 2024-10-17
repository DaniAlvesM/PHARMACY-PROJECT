**ENGLESH**

In this data analysis project, I decided to recreate the sales and customer/vendor registration system for a pharmacy. The system would start with a Python project using the Pandas library to create a table where the registrations of medications, their codes, and stock quantities would be inserted. Then, we would use a second table for customer registration and verification, recording their CPF (Brazilian ID number), names, ages, genders, and cities.

The program starts by displaying the available medications and asking for the customer's CPF. If the customer is not registered, their registration is completed by entering their personal information. After that, the sales process begins by asking for the codes of the desired products and their quantities. After each code and quantity are entered, the corresponding price of the medication is displayed. Once all medications and quantities are selected, the final purchase price is shown.

Then, the program generates an invoice with a random 6-digit number and records the sale in a "tb_sales" table, registering the customer's CPF, the purchased medications and quantities, and generating a random date.

Additionally, starting the data analysis process, at the end of the program, it is possible to request the visualization of tables with specific filters, such as requesting a particular CPF, medication, date, or desired invoice number.

Next steps:

- Integrate the program with Excel
- Add a sellers' table
- Create a user menu
- Verify sellers' and customers' CPFs in Excel
- Register new sellers, medications, and customers in Python and upload to the Excel folder

**PORTUGUÊS**

Neste projeto de análise de dados decidi recriar o sistema de vendas e cadastro de clientes e vendedores de uma farmácia. O sistema começaria com um projeto em python utilizando a biblioteca pandas para crianção de tabela onde seriam inseridos os cadastros de medicamentos, seus códigos e quantidade em estoque. Em seguida usariamos uma segunda tabela para cadastro e verificação de clientes, registrando seus CPFs, nomes, idades, gêneros e cidades. 

Assim, o programa é inciado apresentando os medicamentos e solicitando o CPF do cliente que, caso não esteja cadastro, efetuará seu cadastro inserindo suas informações. Após isso as vendas são iniciadas solicitando os códigos dos produtos desejados e suas quantidades. Após cada código e quantidade inserida é informado o valor respectivo aquele medicamento. Após selecionados todos os medicamentos e suas quantidades é informado o valor final da compra.

Então, o programa gera uma nota fiscal com 6 digitos aleatórios e registra a venda em uma tb_vendas registrando o CPF do cliente, os medicamentos e quantidades compradas e gerando uma data aleatória.

Além disso, iniciando o processo de análise de dados, ao final do programa é possível solicitar visualização das tabelas com filtros específicos, solicitando algum CPF, medicamento, dia ou NF desejada.

Próximos passos:
- Programa integrado ao excel
- Adicionar tabela de vendedores
- Menu de usuário
- Verificação de CPFs de vendedores e de clientes no excel
- Cadastrar novos vendedores, medicamentos e clientes no python e subir para pasta excel
