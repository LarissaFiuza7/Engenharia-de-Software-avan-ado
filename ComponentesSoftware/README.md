
# Componentes de Software – MinasMoveVidas

Este documento descreve, com base no código atual do repositório, a organização dos componentes implementados em `ComponentesSoftware`, suas interfaces fornecidas e requeridas, a comunicação entre eles e o uso de **Docker Compose**, considerando o estado atual do projeto: serviços em **FastAPI** com conexão ao **MongoDB**, ainda sem frontend funcionando.

---

# Visão Conceitual dos Componentes

Na disciplina, um **componente de software** é entendido como uma unidade de implementação que:

- Encapsula um conjunto coeso de responsabilidades.
- Expõe **interfaces fornecidas** bem definidas (o que o componente oferece).
- Declara **interfaces requeridas** (de que o componente precisa para funcionar).
- Pode ser implantado e evoluído de maneira relativamente independente, desde que mantenha seus contratos de interface.

No projeto **MinasMoveVidas**, o diretório `ComponentesSoftware` concentra, neste momento, principalmente:

- **Componentes de serviço (backend)**, implementados em **Python com FastAPI**, responsáveis pelas regras de negócio ligadas a clientes, bens e reservas.
- **Um componente de infraestrutura de dados**, responsável pela conexão com o banco de dados **MongoDB**.

A parte de **frontend web** existe apenas em nível de intenção/projeto, mas ainda não está integrada nem funcionando; por isso, neste documento o foco permanece nos componentes **FastAPI** e na conexão com o **MongoDB**.

---

# Descrição dos Dois Componentes Principais

Para fins da disciplina, destacam‑se dois componentes principais, que de fato estão presentes no código:

- **Componente de serviço de domínio (FastAPI)**
- **Componente de infraestrutura de dados (conexão com MongoDB)**

---

## 2.1 Componente de Serviço de Domínio (FastAPI)

O componente de serviço de domínio é representado pelos serviços implementados em **FastAPI** dentro de `ComponentesSoftware` (por exemplo, serviços responsáveis por clientes, bens ou reservas, dependendo dos arquivos já criados).

### Responsabilidades

- Implementar as **regras de negócio básicas** previstas para o sistema MinasMoveVidas (como operações sobre entidades de usuários, bens e reservas).
- Expor uma **API REST** por meio de **endpoints HTTP**, utilizando FastAPI.
- Validar e processar os dados recebidos pelas requisições (mesmo que, no momento, os clientes sejam apenas ferramentas como `curl`, navegador ou testes manuais).
- Interagir com o componente de infraestrutura de dados para **salvar e recuperar informações no MongoDB**.

Conceitualmente, esse componente é um **componente de serviço de domínio** porque centraliza as regras de negócio e a lógica de acesso às funcionalidades do sistema via FastAPI, sem tratar diretamente de interface gráfica.

---

## 2.2 Componente de Infraestrutura de Dados (Conexão com MongoDB)

O componente de infraestrutura de dados está representado pelo código em `conexao`, especialmente o arquivo:

```
conexao/conexao_mongo.py
```

### Responsabilidades

- Encapsular os detalhes de criação e configuração da conexão com o banco **MongoDB**.
- Oferecer funções ou objetos que permitem aos serviços FastAPI acessar as coleções necessárias (como coleções de usuários, bens e reservas).
- Servir de **camada de abstração** entre a lógica de negócio e a tecnologia específica de armazenamento.

Desse modo, esse componente é classificado como **componente de infraestrutura**, pois fornece um serviço técnico (persistência de dados) aos componentes de serviço de domínio.

---

# Interfaces Fornecidas

## 3.1 Interfaces Fornecidas pelos Componentes de Serviço (FastAPI)

Os componentes de serviço de domínio fornecem suas funcionalidades por meio de uma **interface REST**, implementada com **FastAPI**.

Essa interface é composta por **endpoints HTTP** que representam operações do sistema.

### Operações típicas

- Consultar entidades (listar ou buscar registros)
- Inserir novas informações (criar registros)
- Atualizar dados existentes
- Remover registros, quando aplicável

Na prática, existem **rotas definidas nos arquivos FastAPI**, expostas em portas configuradas no `docker-compose.yml`.

Cada rota corresponde a uma **operação do domínio**, como:

- operações sobre usuários
- operações sobre bens
- operações sobre reservas

Mesmo sem frontend, qualquer **cliente HTTP** (Postman, navegador ou scripts) pode consumir essa interface.

---

## 3.2 Interface Fornecida pelo Componente de Conexão (MongoDB)

O componente de conexão com o MongoDB fornece uma **interface programática**, utilizada dentro do código Python dos serviços FastAPI.

Essa interface inclui:

- Funções ou classes para **inicializar e obter o cliente de banco de dados**
- Funções de apoio para acessar **bases e coleções específicas**
- Eventualmente, funções que **padronizam operações de leitura e escrita**

Essa interface é **interna ao backend** e evita que cada serviço implemente individualmente a lógica de conexão com o banco.

---

# Interfaces Requeridas

## 4.1 Interfaces Requeridas pelos Componentes de Serviço

Os componentes de serviço de domínio requerem duas interfaces principais.

### a) Interface de acesso a dados (MongoDB)

Fornecida pelo **componente de conexão**.

Os serviços precisam **armazenar e recuperar informações**.  
Em vez de manipular diretamente o driver e a URI do MongoDB em cada serviço, eles utilizam a interface centralizada disponibilizada pelo módulo de conexão.

### b) Interface de infraestrutura de rede (FastAPI)

Os serviços dependem do **servidor HTTP criado pelo FastAPI**, normalmente executado via:

```
uvicorn
```

ou dentro de um contêiner Docker.

Essa interface permite:

- receber requisições HTTP
- enviar respostas adequadas

Assim, os serviços requerem a interface de conexão com o banco e a infraestrutura HTTP sem depender diretamente dos detalhes técnicos.

---

## 4.2 Interfaces Requeridas pelo Componente de Conexão (MongoDB)

O componente de conexão com o MongoDB requer:

- A interface fornecida pelo **driver MongoDB** instalado via `requirements.txt`
- Um **servidor MongoDB em execução**

No cenário com Docker Compose, essa URI aponta para o serviço:

```
mongodb
```

definido no arquivo `docker-compose.yml`.

Assim:

- `conexao_mongo` depende diretamente da tecnologia MongoDB
- os serviços de domínio dependem **apenas desse módulo**, e não do driver do banco

---

# Comunicação entre os Componentes

## 5.1 Comunicação entre Serviços de Domínio e MongoDB

Como ainda não existe frontend funcional, o fluxo principal de comunicação ocorre entre:

- **Serviços FastAPI**
- **Banco MongoDB**

Fluxo conceitual:

1. O serviço FastAPI recebe uma requisição HTTP (ex.: via Postman).
2. O serviço precisa consultar ou alterar dados.
3. O serviço chama funções do módulo `conexao_mongo`.
4. O módulo acessa o MongoDB.
5. O resultado retorna ao serviço FastAPI.
6. O serviço transforma o resultado em **resposta HTTP (JSON)**.

Essa divisão evita repetição de código de conexão com o banco.

---

## 5.2 Papel do Docker Compose na Comunicação

O arquivo:

```
docker-compose.yml
```

é responsável por **orquestrar os contêineres**.

Funções do Docker Compose:

- Definir um serviço para o **MongoDB**
- Definir serviços para os **componentes FastAPI**
- Criar uma **rede Docker comum**
- Permitir acesso ao MongoDB pelo nome do serviço (`mongodb`)
- Mapear volumes com o código fonte

Assim, cada componente roda em **contêiner isolado**, comunicando‑se por interfaces definidas.

---

# Justificativa: Como o Acoplamento Direto Foi Evitado

Mesmo sem frontend, o projeto já evita acoplamento direto por meio de:

### Separação de responsabilidades

- FastAPI → regras de negócio e endpoints
- Conexão → acesso ao MongoDB

### Uso de interfaces

- Rotas HTTP representam a **interface fornecida**
- Funções do módulo de conexão representam a **interface de acesso ao banco**

### Encapsulamento da infraestrutura

Detalhes como:

- URI do banco
- configuração do cliente
- parâmetros do MongoDB

ficam isolados no módulo de conexão.

### Isolamento na implantação

FastAPI e MongoDB executam em **contêineres Docker separados**, comunicando‑se apenas por interfaces formais.

Essas decisões aproximam o projeto dos princípios de:

- **Engenharia de Componentes**
- **Arquitetura Orientada a Serviços**

---

# Instruções para Execução do Projeto

## 7.1 Execução com Docker Compose (Recomendada)

Certifique‑se de possuir:

- Docker
- Docker Compose

No terminal:

```
cd ComponentesSoftware
```

Construir as imagens:

```
docker compose build
```

Subir os serviços:

```
docker compose up
```

Com os contêineres em execução, utilize ferramentas como:

- navegador
- curl
- Postman

para testar os endpoints FastAPI.

Para encerrar os serviços:

```
docker compose down
```

---

## 7.2 Execução Local sem Docker (Alternativa)

1. Garanta que o **MongoDB esteja em execução**
2. No diretório `ComponentesSoftware`, crie um ambiente virtual Python
3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Execute o serviço FastAPI (exemplo):

```
uvicorn main:app --reload --port 8000
```

5. Teste os endpoints usando navegador, curl ou Postman.
