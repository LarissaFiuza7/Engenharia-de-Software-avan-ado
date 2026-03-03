

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

- Linguagem principal: **Python**  
- Framework para APIs: **FastAPI**  
- Banco de dados: **MongoDB**  
- Controle de versão: **Git + GitHub**

> Detalhes de instalação, comandos e estrutura de pastas serão adicionados quando a implementação se iniciar.

---

## 11. Equipe

- **Kayky Pires** – Scrum Master  
- **Rafael Dias** – Product Owner  
- **Larissa Santos Fiuza** – Desenvolvedora  
- **Beatriz Cristina** – Desenvolvedora  

---
