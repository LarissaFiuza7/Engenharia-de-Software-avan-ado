
# Componentes de Software – MinasMoveVidas

Este documento descreve, sob a perspectiva de Engenharia de Software Orientada a Serviços e a Componentes, a organização dos componentes implementados em ComponentesSoftware, suas interfaces fornecidas e requeridas, a forma de comunicação entre eles, o uso de Docker Compose e as decisões de projeto adotadas para redução de acoplamento.

---

# 1. Visão Conceitual dos Componentes

Na disciplina, um componente de software pode ser entendido como uma unidade de implementação que:

- Encapsula um conjunto coeso de responsabilidades.
- Expõe interfaces fornecidas formalmente especificadas.
- Declara interfaces requeridas das quais depende para funcionar.
- Pode ser implantado, substituído e evoluído de forma relativamente independente, desde que mantenha seus contratos de interface.

No contexto deste projeto, trabalhamos principalmente com dois grupos de componentes:

## Componentes de serviço (backend)

Implementados em Python e expostos via HTTP:

Componentes/ClienteService  
Componentes/GerenciarBensService  
Componentes/GerenciarReservaService  

## Componente de infraestrutura de dados

Módulo responsável pela conexão com o banco de dados:

conexao/conexao_mongo.py

Também existe um componente de apresentação (frontend) localizado em:

Componentes/FrontendService/app

Ele é responsável pela interação com o usuário e se comporta como cliente das APIs de backend.

---

# 2. Descrição dos Componentes Principais

Embora o sistema tenha mais de um serviço, para fins de relatório de componentes a ênfase está em dois componentes conceituais:

- Componente de Serviço de Domínio
- Componente de Infraestrutura de Dados

---

# 2.1 Componente de Serviço de Domínio (ClienteService)

O componente de serviço de domínio é representado por serviços de backend como:

- ClienteService
- GerenciarBensService
- GerenciarReservaService

## Responsabilidades

- Implementar regras de negócio de um subdomínio específico (clientes, bens ou reservas).
- Orquestrar o acesso ao banco de dados via conexao_mongo.
- Expor APIs REST para consumo por outros componentes.

Arquiteturalmente este componente:

- Não se confunde com o banco de dados (infraestrutura)
- Não se confunde com o frontend (apresentação)
- Fornece operações de alto nível sobre entidades de negócio

Exemplos de entidades:

- Cliente
- Bem
- Reserva

---

# 2.2 Componente de Infraestrutura de Dados (conexao_mongo)

O diretório conexao contém o componente de infraestrutura de dados.

Arquivo principal:

conexao/conexao_mongo.py

## Responsabilidades

- Encapsular configuração e criação da conexão com MongoDB
- Disponibilizar acesso às coleções de dados
- Centralizar políticas de tratamento de erro
- Facilitar o reuso de conexões

Esse componente não contém regras de negócio, apenas serviços de acesso a dados.

---

# 3. Interfaces Fornecidas

## 3.1 Interfaces fornecidas pelos serviços

Cada serviço fornece uma API REST exposta via HTTP.

As operações incluem:

- Consultas
- Criação / Atualização
- Remoção

### ClienteService (porta 8001)

GET /clientes  
POST /clientes  

### GerenciarBensService (porta 8002)

GET /bens  
POST /bens  

### GerenciarReservaService (porta 8003)

GET /reservas  
POST /reservas  

Essas APIs REST constituem a interface fornecida pelos componentes de serviço.

Podem ser consumidas por:

- Frontend
- Outros serviços
- Scripts ou ferramentas HTTP

---

## 3.2 Interface fornecida por conexao_mongo

O componente conexao_mongo fornece uma interface programática em Python.

Ela inclui:

- Funções para criação de clientes MongoDB
- Funções para acesso a bancos e coleções

Essa interface é interna e utilizada apenas pelos serviços de backend.

---

# 4. Interfaces Requeridas

## 4.1 Interfaces requeridas pelos serviços

Os serviços dependem de duas categorias principais:

### Interface de Dados

Fornecida por:

conexao_mongo

Responsável por abstrair a conexão com o MongoDB.

### Interface de Infraestrutura HTTP

Fornecida pelo framework web utilizado (por exemplo FastAPI).

Ela permite que o serviço escute requisições HTTP e responda clientes externos.

---

## 4.2 Interfaces requeridas por conexao_mongo

O módulo de conexão depende de:

- Driver MongoDB instalado via requirements.txt
- Servidor MongoDB em execução

Exemplo no Docker Compose:

mongodb

Assim, conexao_mongo atua como um adaptador entre serviços e banco de dados.

---

# 5. Comunicação entre Componentes

## 5.1 Comunicação Frontend → Serviços

A comunicação segue o padrão cliente-servidor via HTTP.

Fluxo:

1. Usuário interage com a interface web.
2. O JavaScript do frontend envia requisições HTTP.
3. Os serviços processam a requisição.
4. As respostas são retornadas em JSON.
5. O frontend atualiza a interface.

Exemplos de endpoints consumidos:

http://localhost:8001/clientes  
http://localhost:8002/bens  
http://localhost:8003/reservas  

O frontend depende apenas da interface REST, não da implementação interna.

---

## 5.2 Comunicação Serviços → MongoDB

A comunicação ocorre através do módulo conexao_mongo.

Fluxo:

1. Serviço recebe requisição HTTP
2. Serviço solicita acesso ao banco
3. conexao_mongo executa operação no MongoDB
4. Resultado retorna ao serviço
5. Serviço responde em JSON

Essa abordagem desacopla os serviços da infraestrutura de banco.

---

## 5.3 Papel do Docker Compose

O arquivo docker-compose.yml define como os componentes são executados.

Funções:

- Definir serviços Docker
- Configurar portas
- Criar rede interna
- Montar volumes

Exemplo de serviços:

- clientes
- bens
- reservas
- mongodb
- frontend

Cada serviço roda em um contêiner isolado, mas conectado à mesma rede.

---

# 6. Justificativa de Arquitetura

## 6.1 Separação de Responsabilidades

O sistema separa:

- Serviços de domínio
- Infraestrutura de dados
- Camada de apresentação

Isso reduz o acoplamento funcional.

---

## 6.2 Uso de Interfaces

Cada componente possui:

- Interfaces fornecidas
- Interfaces requeridas

Exemplos:

- APIs REST
- módulo conexao_mongo

Isso garante contratos claros entre componentes.

---

## 6.3 Encapsulamento da Infraestrutura

O acesso ao MongoDB foi centralizado em conexao_mongo.

Assim os serviços não precisam conhecer:

- URI de conexão
- credenciais
- detalhes do driver

Isso facilita mudanças futuras na infraestrutura.

---

## 6.4 Isolamento com Docker

Com Docker Compose:

- cada serviço roda em contêiner próprio
- comunicação ocorre via rede
- não existem chamadas diretas entre processos

Isso reduz o acoplamento temporal e espacial e aproxima o sistema de uma arquitetura baseada em microsserviços.

---

# 7. Execução do Projeto

## 7.1 Executar com Docker Compose

Instale:

- Docker
- Docker Compose

Entre no diretório do projeto:

cd ComponentesSoftware

Construa as imagens:

docker compose build

Suba os serviços:

docker compose up

---

## Serviços disponíveis

ClienteService → http://localhost:8001  
GerenciarBensService → http://localhost:8002  
GerenciarReservaService → http://localhost:8003  

O Frontend estará disponível na porta configurada no docker-compose.yml.

---

## Encerrar execução

docker compose down
