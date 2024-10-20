ENGLISH

In this data analysis project, I recreated the sales and customer/vendor registration system for a pharmacy. The system began with a Python project using the Pandas library to create a table where the registrations of medications, their codes, and stock quantities were inserted. Then, a second table was used for customer registration and verification, recording their CPF (Brazilian ID number), names, ages, genders, and cities.

The program starts by displaying the available medications and asking for the customer's CPF. If the customer is not registered, their registration is completed by entering their personal information. After that, the sales process begins by asking for the codes of the desired products and their quantities. After each code and quantity are entered, the corresponding price of the medication is displayed. Once all medications and quantities are selected, the final purchase price is shown.

The program then generates an invoice with a random 6-digit number and records the sale in a "tb_sales" table, registering the customer's CPF, the purchased medications and quantities, and generating a random date.

Furthermore, as part of the data analysis process, the program allows for the visualization of tables with specific filters, such as requesting a particular CPF, medication, date, or invoice number.

To expand the functionality, the program was integrated with Excel, allowing all registered data (such as medications, customers, and sales) to be stored and manipulated using spreadsheets. Additionally, a sellers' table was added to register and manage seller information, making it possible to track sales performance and improve the registration process. A user menu was also created, making the system more interactive and intuitive for users. CPF verification for both sellers and customers was implemented in Excel to ensure the accuracy of the data and avoid duplicate entries. Finally, the system allows the registration of new sellers, medications, and customers directly in Python, with the ability to upload these new records to the Excel folder, ensuring a smooth and seamless workflow between Python and Excel.

Next steps:

Create an executable version accessible via an external web page
Add delivery fee
Implement stock increase functionality
Add branches to the system
Include a customer service rating feature
Develop a symptoms questionnaire with medication suggestions


PORTUGUÊS

Neste projeto de análise de dados, recriei o sistema de vendas e cadastro de clientes e vendedores de uma farmácia. O sistema começou com um projeto em Python utilizando a biblioteca Pandas para criar uma tabela onde foram inseridos os cadastros de medicamentos, seus códigos e quantidades em estoque. Em seguida, uma segunda tabela foi usada para o cadastro e verificação de clientes, registrando seus CPFs, nomes, idades, gêneros e cidades.

O programa é iniciado apresentando os medicamentos disponíveis e solicitando o CPF do cliente. Caso o cliente não esteja cadastrado, o sistema realiza o cadastro inserindo suas informações pessoais. Após isso, o processo de vendas começa solicitando os códigos dos produtos desejados e suas quantidades. Após cada código e quantidade inseridos, o valor correspondente ao medicamento é exibido. Uma vez que todos os medicamentos e suas quantidades são selecionados, o valor final da compra é mostrado.

Então, o programa gera uma nota fiscal com um número de 6 dígitos aleatórios e registra a venda em uma tabela "tb_vendas", registrando o CPF do cliente, os medicamentos comprados, suas quantidades e gerando uma data aleatória.

Além disso, como parte do processo de análise de dados, o programa permite a visualização de tabelas com filtros específicos, como solicitação de um CPF, medicamento, data ou número de nota fiscal.

Para expandir as funcionalidades, o programa foi integrado ao Excel, permitindo que todos os dados registrados (como medicamentos, clientes e vendas) fossem armazenados e manipulados em planilhas. Além disso, foi adicionada uma tabela de vendedores para registrar e gerenciar informações dos vendedores, possibilitando o acompanhamento do desempenho de vendas e aprimorando o processo de cadastro. Um menu de usuário também foi criado, tornando o sistema mais interativo e intuitivo para os usuários. A verificação de CPFs de vendedores e clientes foi implementada no Excel para garantir a precisão dos dados e evitar entradas duplicadas. Por fim, o sistema agora permite o cadastro de novos vendedores, medicamentos e clientes diretamente em Python, com a possibilidade de subir esses novos registros para a pasta do Excel, garantindo um fluxo de trabalho contínuo entre Python e Excel.

Próximos passos:

Criar uma versão executável acessível via página externa
Adicionar taxa de entrega
Implementar a funcionalidade de aumento de estoque
Adicionar filiais ao sistema
Incluir um recurso de classificação de atendimento
Desenvolver um questionário de sintomas com sugestão de remédios
