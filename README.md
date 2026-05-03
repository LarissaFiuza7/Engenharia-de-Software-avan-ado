

<div align="center">

  <img width="700" height="700" alt="ad1c05ef-a7b3-4efe-8b4d-1300bdc7a308 (1)" src="https://github.com/user-attachments/assets/e6580a55-e849-41c9-9011-d5c1915db7ce" />
  <h1>MinasMoveVidas</h1>
  <p>Liberdade para ir, conforto para ficar</p>
</div>


# MinasMoveVidas

Plataforma SOA para aluguel unificado de veículos 🏎️ e imóveis 🏠.

O **MinasMoveVidas** centraliza o aluguel de bens em uma única solução, permitindo que locatários planejem viagens e estadias com mais praticidade e que locadores gerenciem seus bens em um só lugar.

---

## 📌 Sumário

- [1. Objetivo do Projeto](#1-objetivo-do-projeto)
- [2. Domínio e Visão Geral do Sistema](#2-domínio-e-visão-geral-do-sistema)
- [3. Processos de Negócio](#3-processos-de-negócio)
- [4. Casos de Uso (alto nível)](#4-casos-de-uso-alto-nível)
- [5. Pontos de Reuso](#5-pontos-de-reuso)
- [6. Artefatos Reutilizáveis e Tecnologias (ideias iniciais)](#6-artefatos-reutilizáveis-e-tecnologias-ideias-iniciais)
- [7. Análise Técnica e Arquitetural (visão geral)](#7-análise-técnica-e-arquitetural-visão-geral)
- [8. Benefícios e Riscos do Reuso](#8-benefícios-e-riscos-do-reuso)
- [9. Espaços para Diagramas](#9-espaços-para-diagramas)
- [10. Preparação do Ambiente](#10-preparação-do-ambiente)
- [11. Equipe](#11-equipe)

---

## 1. Objetivo do Projeto

Projeto desenvolvido na disciplina de **Engenharia de Software Avançada**, com foco em:

- Compreender o domínio de aluguel de bens.
- Definir um sistema com arquitetura orientada a serviços (SOA).
- Explorar **reuso de serviços, classes e artefatos**.
- Evoluir modelagem (processos, casos de uso, componentes) ao longo dos laboratórios.

---

## 2. Domínio e Visão Geral do Sistema

### 2.1 Domínio do Sistema

- **Domínio:** aluguel de bens (veículos e imóveis).  
- **Problema que resolve:** hoje, quem quer viajar costuma usar mais de uma plataforma (uma para carro, outra para hospedagem). O sistema busca centralizar essa experiência.  
- **Usuários principais:**  
  - Locatários  
  - Locadores  

### 2.2 Visão Geral

- **Nome do sistema:** MinasMoveVidas  
- **Ideia geral:**  
  - Um único ambiente onde o usuário pode:
    - Cadastrar-se.
    - Cadastrar bens (se for locador).
    - Buscar bens.
    - Reservar e pagar.
    - Avaliar experiências.

---

## 3. Processos de Negócio

Modelados inicialmente de forma simplificada:

- **Cadastro de Usuário**
  - Usuário cria uma conta para utilizar a plataforma.
- **Gerenciamento de Bem para Aluguel**
  - Locador registra e gerencia veículos e imóveis.
- **Busca**
  - Locatário busca bens disponíveis conforme filtros (como localização, datas, tipo de bem).
- **Pagamento e Reserva**
  - Locatário seleciona um bem, realiza a reserva e efetua o pagamento.



---

## 4. Casos de Uso (alto nível)

### UC-02 – Gerenciar Bem para Aluguel

Locador cadastra e gerencia bens (veículos ou imóveis) que serão disponibilizados na plataforma.

- Acessar área de gerenciamento.
- Informar dados do bem.
- Salvar/atualizar/remover bem.
- Tornar o bem disponível para busca e reserva.


---

### UC-03 – Pagamento

Locatário realiza o pagamento de uma reserva para concluir a locação.

- Acessar reserva aprovada.
- Visualizar resumo de valores.
- Escolher forma de pagamento.
- Confirmar pagamento.
- Receber confirmação/comprovante.



---

### UC-05 – Gerenciar Reserva

Locatário gerencia reservas desde a escolha do bem até a confirmação.

- Buscar bens por tipo, localização e período.
- Visualizar lista de opções.
- Solicitar reserva.
- Acompanhar aprovação pelo locador.
- Prosseguir para pagamento após aprovação.



---

## 5. Pontos de Reuso

Principais pontos em que o sistema foi pensado para reuso entre diferentes tipos de bens:

- **Cadastramento de Usuário**
  - Serviço de identificação/autenticação comum para locadores e locatários.
- **Localização**
  - Representação e tratamento de endereços, usada tanto em usuários quanto em bens.
- **Pagamento**
  - Mesma lógica/serviço de pagamento para qualquer reserva (veículo ou imóvel).
- **Avaliação**
  - Modelo único de avaliação para bens e usuários, reaproveitado em diferentes fluxos.


---

## 6. Artefatos Reutilizáveis e Tecnologias (ideias iniciais)

Ideias de frameworks, bibliotecas e APIs que podem ser reutilizadas no projeto:

- **BrasilAPI**
  - Para consultas relacionadas a dados brasileiros (ex.: CEP, documentos, FIPE).
- **MongoDB**
  - Banco NoSQL para armazenar informações de usuários, bens, reservas e avaliações.
- **FastAPI**
  - Framework em Python para construção de APIs e serviços.


---

## 7. Análise Técnica e Arquitetural (visão geral)

De forma geral, ao escolher esses artefatos e padrões de reuso, o projeto busca:

- Facilitar a comunicação entre serviços (SOA/APIs).
- Permitir que **serviços compartilhem funcionalidades** (como autenticação, localização, pagamento).
- Manter a arquitetura flexível para mudanças futuras (como adicionar novos tipos de bem).

Os detalhes de implementação (endpoints, modelos de dados, integrações específicas) ainda estão em definição e podem evoluir.

---

## 8. Benefícios e Riscos do Reuso

### Benefícios esperados

- Menos duplicação de lógica entre partes do sistema.
- Consistência maior (mesmo fluxo de cadastro, pagamento, avaliação).
- Facilidade de manutenção: alterar um serviço compartilhado atualiza o comportamento em todo o sistema.

### Riscos a considerar

- Dependência maior de componentes centrais (mudanças impactam vários módulos).
- Uso de APIs externas (como BrasilAPI) introduz dependência de terceiros.
- Necessidade de cuidado com versionamento e contratos de serviços.

---

## 9. Espaços para Diagramas

Arquivos de imagem ainda podem ser adicionados conforme os modelos forem evoluindo:



- Diagramas de casos de uso (UC-02, UC-03, UC-05, etc.)  
  <img width="845" height="513" alt="{589C4A62-707E-4EA1-96DE-45BCB6A698E4}" src="https://github.com/user-attachments/assets/15e81cf6-c352-47d5-aabf-b488c612a1c0" />


- Diagrama de componentes / serviços e interfaces  


---

## 10. Preparação do Ambiente

Decisões iniciais (podem ser ajustadas durante o desenvolvimento):

- Linguagem principal: **Python e JavaScript**  
- Framework para APIs: **FastAPI**  
- Banco de dados: **MongoDB**  
- Controle de versão: **GitHub**

> Detalhes de instalação, comandos e estrutura de pastas serão adicionados quando a implementação se iniciar.

---

## 11. Arquitetura por Componentes (ESBC)

### Descrição dos componentes implementados

O sistema foi dividido em três componentes principais, cada um com uma responsabilidade própria.

#### Cliente

Responsável por armazenar e gerenciar os dados dos usuários do sistema.

Funções principais:

- Cadastrar cliente
- Buscar cliente por CPF
- Buscar cliente por e-mail

#### Bens

Responsável pelo cadastro e controle dos bens disponíveis no sistema.

Funções principais:

- Cadastrar bens
- Vincular um bem a um cliente
- Buscar bem por ID
- Listar bens cadastrados

#### Reserva

Responsável pela criação e gerenciamento das reservas.

Funções principais:

- Criar reserva
- Verificar cliente
- Verificar bem
- Validar datas da reserva
- Buscar e listar reservas

---

### Interfaces fornecidas

Cada componente possui uma interface, que funciona como um contrato dizendo quais ações aquele componente oferece para o restante do sistema.

As interfaces criadas foram:

- `IClienteComponent`
- `IBensComponent`
- `IReservaComponent`

Essas interfaces permitem que os componentes sejam usados sem que seja necessário conhecer todos os detalhes internos da implementação.

---

### Interfaces requeridas

Alguns componentes precisam consultar informações de outros componentes para funcionar corretamente.

#### Componente Bens

Precisa da interface:

- `IClienteComponent`

Isso acontece porque, antes de cadastrar um bem, o sistema precisa verificar se o cliente informado realmente existe.

#### Componente Reserva

Precisa das interfaces:

- `IClienteComponent`
- `IBensComponent`

Isso acontece porque, antes de criar uma reserva, o sistema precisa confirmar se o cliente existe e se o bem informado também está cadastrado.

---

### Como ocorre a comunicação entre os componentes

A comunicação entre os componentes acontece de forma organizada por meio das interfaces.

Um componente não acessa diretamente o funcionamento interno do outro. Ele apenas faz uma solicitação usando a interface disponível.

#### Exemplo: cadastro de um bem

Quando um bem é cadastrado, o componente de Bens precisa saber se o CPF informado pertence a um cliente existente.

Então ele consulta o componente de Cliente por meio da interface `IClienteComponent`.

Se o cliente existir, o bem é cadastrado e vinculado ao CPF informado.

Se o cliente não existir, o cadastro não é realizado.

#### Exemplo: criação de uma reserva

Para criar uma reserva, o componente de Reserva faz algumas verificações:

1. Verifica se o cliente existe
2. Verifica se o bem existe
3. Verifica se a data final não é anterior à data inicial

Depois dessas validações, a reserva é criada.

Assim, o componente de Reserva não precisa saber como o Cliente ou o Bem são salvos no banco de dados. Ele apenas usa as interfaces para pedir as informações necessárias.

---

### Justificativa de como foi evitado o acoplamento direto

O acoplamento direto foi evitado porque os componentes não dependem diretamente das classes de implementação uns dos outros.

Em vez disso, eles dependem das interfaces.

Por exemplo, o componente de Bens não chama diretamente a classe `ClienteComponentImpl`.

Ele usa a interface `IClienteComponent`.

Da mesma forma, o componente de Reserva usa as interfaces `IClienteComponent` e `IBensComponent`, sem depender diretamente das classes concretas.

Isso deixa o sistema mais organizado, pois cada componente mantém sua própria responsabilidade.

Também facilita futuras alterações. Caso seja necessário mudar a forma como um cliente é buscado ou como um bem é cadastrado, a mudança pode ser feita dentro do componente responsável, sem afetar diretamente os demais.

---

### 12 - Execução do Projeto Baseado em Componentes

#### Configuração do MongoDB

  1 - Crie uma conta no MongoDB
  
  2 - Crie um cluster 
  
  3 - Crie 1 Banco de dados nesse cluster.
  
  4 - Crie 3 colletions: bens, clientes e reservas

#### Execução 

  1 - Execute o arquivo MinasmovevidasApplication com os dados desejados.


## 13 - Arquitetura Orientada a Serviços (ESOS)

### Para este modulo criamos serviços que realiza o gerenciamento dos nosso clientes, bens e reservas realizadas, onde cada serviço é responsavel por uma parte dele, mantendo o desacoplamento deles.
### Para isso criamos 3 serviços onde se comunicam via APIs (Dados em formato JSON).

### Serviços
  - clienteService
  - gerenciarBens
  - gerenciarReservas

#### 1. clienteService

  Este serviço é responsal pelo gerenciamento de todos os dados do cliente. Nele realizamos Autenticação(login), registro de usuário e buscas.
  Dados gerenciados pelo serviço: 
  
    - Nome Completo
    - CPF
    - E-mail
    - Senha
    - Data de Nascimento
    - Numero de Telefone

  EndPoints post:
  
    - (/cliente/cadastrar-cliente/) -> Insere no banco de dados o cliente novo.
  Endpoints get:
  
    - (/cliente/login/) -> Realiza a autenticação do usuário com email e senha.
    - (/cliente/id/{id_cliente}/) -> Busca um cliente especifico pelo ID
    - (/cliente/) -> Lista os cliente existentes no banco de dados
    
### 2. gerenciarReservaService

  Este serviço é responsavel pelo gerenciamento das reservas, tanto de imoveis quanto de veiculos, nele podemos realizar os registros das resarvas de imovel e veiculo.
  Dados Gerenciados pelo serviço:

    - CPF do Cliente
    - Nome do Cliente
    - ID Veiculo/Imovel
    - Endereço Veiculo/Imovel
    - Data de inicio e Fim

  Endpoints post: 
  
    - (/gerenciar-reserva/reservar-imovel/) -> Cria o registro da reserva com os dados de cliente, imovel e reserva.
    - (/gerenciar-reserva/reservar-veiculo/) -> Cria o registro da reserva com os dados de cliente, veiculo e reserva.

### 3. gerenciarBensService 

  Este serviço é responsavel por gerenciar os bens cadastrados no banco de dados, nele podemos realizar cadastro do bem (imovel ou veiculo), busca por bem especifico e listagem de bens.
  Dados Gerenciados pelo serviço: 

    Imovel
      - CEP
      - Endereço
      - Bairro
      - Cidade
      - Estado 
      - Numero
      - Complemento
      - Comodos
      - M²
      - Valor 
      - Dados do Proprietario

    Veiculo
      - Marca
      - Modelo
      - Ano 
      - Valor 
      - CEP
      - Endereço
      - Bairro 
      - Cidade
      - Estado
      - Numero
      - Dados do Proprietario

  Endpoints post:

    - (/gerenciar-bens/imoveis/adicionar-imovel/) -> Insere um registro no banco de dados com as informações do imovel
    - (/gerenciar-bens/veiculos/adicionar-veiculo/) -> Insere um registro no banco de dados com as informações do veiculo
    
  Endpoints get:
  
    - (/gerenciar-bens/imoveis/) -> Lista todos os imoveis
    - (/gerenciar-bens/imoveis/filtro/) -> Lista imoveis especificos com base nos filtros inseridos (cidade,estado,qtde_comodos)
    - (/gerenciar-bens/imoveis/{id}/) -> Retorna um imovel especifico pelo ID dele
    - (/gerenciar-bens/veiculos/) -> Lista todos os veiculos
    - (/gerenciar-bens/veiculos/{id}/) -> Retorna um veiculos especifico pelo ID dele
    - (/gerenciar-bens/veiculos/filtro/) -> Retorna uma lista de imvoeis com base nos filtros inseridos (cidade,estado,marca,modelo,ano)

## 14 - Execução do Projeto Orientado a Serviços

### Configuração do MongoDB

  1 - Crie uma conta no MongoDB
  
  2 - Crie um cluster com o nome de "componentSoftware"
  
  3 - Crie 3 Colletions nesse cluster: "ComponentClientes", "ComponentBens" e "ComponentReserva".
  
  4.1 - No ComponentClientes crie a coleção nomeada de "clientes"
  
  4.2 - No ComponentBens crie as coleções nomeadas de : "imoveis" e "veiculos"
  
  4.3 - No ComponentReserva crie as coleçõoes nomeadas de : "reservaImovel" e "reservaVeiculo"

### Execução do Docker

  1 - Copie a URL do MongoDB e passe os paramentos de credenciais dentro de cada componente.

  2 - Crie as imagens do Docker com o comando: docker compose build

  3 - Crie o servidores dos componentes utilizando o comando: docker compose up


