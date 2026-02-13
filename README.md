<div align="center">
  <img width="400" height="400" alt="ChatGPT Image 6 de fev  de 2026, 20_14_36-Photoroom" src="https://github.com/user-attachments/assets/15c5edbb-8065-4c9f-b1f3-44483db215e1" />
  <h1>MinasMoveVidas</h1>
  <p>Plataforma SOA para aluguel unificado de veículos 🏎️ e casas 🏠</p>
</div>



# MinasMoveVidas

Plataforma SOA para aluguel unificado de veículos 🏎️ e casas 🏠.

**MinasMoveVidas** é uma plataforma unificada para aluguel de veículos e imóveis, desenvolvida em arquitetura orientada a serviços (SOA). O sistema compartilha dados de usuários, localização, pagamentos e avaliações entre serviços, evitando fragmentação de cadastros e múltiplos logins.

---

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Processos de Negócio](#processos-de-negócio)
- [Pontos de Reuso no Sistema](#pontos-de-reuso-no-sistema)
- [Artefatos Reutilizáveis](#artefatos-reutilizáveis)
- [Análise Técnica e Arquitetural do Reuso](#análise-técnica-e-arquitetural-do-reuso)
- [Tecnologias](#tecnologias)
- [Equipe](#equipe)

---

## Visão Geral

**Domínio do Sistema:** aluguel de bens (veículos e casas) em uma única plataforma.

**Problema Resolvido:** hoje, locatários e locadores frequentemente precisam manter contas e cadastros separados em diferentes plataformas (ex.: uma para carros, outra para imóveis). O MinasMoveVidas unifica esses processos com um único login e um modelo de serviços compartilhados.

**Usuários Principais:**

- **Locatário:** busca, filtra, reserva e paga por veículos ou imóveis.
- **Locador:** cadastra e gerencia veículos e/ou imóveis disponíveis para locação.

---

## Funcionalidades

- Cadastro e autenticação de usuários.
- Cadastro e gerenciamento de veículos e imóveis.
- Busca e filtragem por localização, disponibilidade, preço e tipo de bem.
- Realização, cancelamento e gerenciamento de reservas.
- Gerenciamento de pagamentos e histórico de transações.
- Avaliação e feedback de locadores, locatários, veículos e imóveis.

---

## Processos de Negócio

Alguns processos principais modelados no sistema:

- **Cadastro de usuário:** criação de conta única para atuar como locatário e/ou locador.
- **Cadastro de bem:** registro de veículos e imóveis com fotos, descrição, localização e disponibilidade.
- **Busca e reserva:** fluxo de busca por filtros (cidade, data, tipo), seleção do bem e confirmação da reserva.
- **Pagamento:** cálculo do valor total (diárias, taxas) e registro do pagamento.
- **Avaliação pós-uso:** após o término da locação, o usuário pode avaliar o bem e o locador.

---

## Pontos de Reuso no Sistema

O sistema foi desenhado para maximizar o reuso de serviços e componentes entre os domínios de veículos e imóveis. Os principais pontos de reuso são:

- **Cadastramento de Usuário**
  - Serviço único de identidade/autenticação para locadores e locatários.
  - Compartilhado por todos os contextos (carros e casas), evitando múltiplos cadastros.

- **Localização**
  - Modelo de endereço e serviço de localização reutilizado por:
    - Veículos (ex.: endereço da agência ou ponto de retirada).
    - Imóveis (ex.: endereço do imóvel).
  - Uso de CEP e dados geográficos padronizados.

- **Pagamento**
  - Serviço de pagamento genérico capaz de tratar diferentes tipos de bens.
  - Reúso de lógica de cálculo de valor, registro de transação e integração com meios de pagamento.

- **Avaliação**
  - Modelo único de avaliação/feedback:
    - Permite avaliar tanto veículos quanto imóveis, e também locadores/locatários.
  - Mesma estrutura de notas, comentários e histórico para todos os tipos de locação.

Esses serviços são pensados como **serviços de domínio compartilhado** em uma arquitetura orientada a serviços, podendo ser consumidos por diferentes front-ends ou microsserviços.

---

## Artefatos Reutilizáveis

Levantamento de frameworks, bibliotecas e APIs reutilizáveis considerados no projeto:

- **BrasilAPI**
  - API pública brasileira com endpoints para CEP, CNPJ, FIPE (preços de veículos), bancos, entre outros.
  - Possíveis usos:
    - Validação de CEP no serviço de Localização.
    - Validação de CNPJ/CPF no Cadastramento de Usuário.
    - Uso de FIPE para apoiar precificação de veículos.

- **MongoDB**
  - Banco de dados NoSQL orientado a documentos.
  - Possíveis usos:
    - Armazenar usuários, reservas, avaliações e catálogos de bens com esquemas flexíveis.
    - Modelar documentos diferentes para veículos e imóveis, mantendo campos comuns e específicos.

- **FastAPI**
  - Framework Python moderno para criação de APIs REST de alta performance.
  - Possíveis usos:
    - Implementar serviços de Usuário, Localização, Pagamento e Avaliação.
    - Geração automática de documentação (OpenAPI/Swagger).
    - Validação de dados de entrada usando modelos tipados (Pydantic).

Esses artefatos são selecionados por favorecerem reuso, rapidez de desenvolvimento e integração com uma arquitetura SOA.

---

## Análise Técnica e Arquitetural do Reuso

### Benefícios do Reuso de Classes e Artefatos

- **Redução de esforço e tempo de desenvolvimento**
  - Serviços compartilhados (ex.: Usuário, Localização) evitam reimplementações para veículos e imóveis.
- **Consistência e qualidade**
  - Um modelo único de avaliação e pagamento garante comportamento consistente em todo o sistema.
- **Facilidade de manutenção**
  - Correções e melhorias em um serviço compartilhado (por exemplo, validação de CEP) beneficiam todas as partes que o utilizam.
- **Alinhamento com SOA**
  - Serviços independentes e reutilizáveis permitem evolução gradual, substituição e escalabilidade.

### Riscos e Cuidados no Reuso

- **Acoplamento indesejado**
  - Um serviço muito genérico ou com muitas responsabilidades pode criar dependências fortes entre domínios diferentes.
  - Mitigação: separar bem responsabilidades (por exemplo, serviço de Usuário isolado de regras específicas de locação).

- **Dependência de terceiros**
  - APIs externas, como BrasilAPI, podem introduzir riscos de disponibilidade ou mudança de contrato.
  - Mitigação: uso de cache local, tratamento de erros e camadas de abstração no serviço.

- **Complexidade de evolução**
  - Alterar um artefato reutilizado pode impactar múltiplos serviços e funcionalidades.
  - Mitigação: versionamento de APIs, testes automatizados e boa documentação de contratos.

---

## Tecnologias

- **Linguagens/Frameworks**
  - JavaScript (JS)
  - Python
  - FastAPI (para serviços e APIs REST)
- **Banco de Dados**
  - MongoDB (modelagem de documentos para usuários, bens, reservas e avaliações)
- **Arquitetura**
  - SOA (Service-Oriented Architecture) com serviços compartilhados de:
    - Usuário
    - Pagamento
    - Busca/Localização
    - Avaliação

---

## Equipe

- **Kayky Pires** – Scrum Master  
- **Rafael Dias** – Product Owner  
- **Larissa Santos Fiuza** – Desenvolvedora  
- **Beatriz Cristina** – Desenvolvedora  

---
