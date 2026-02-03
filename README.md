# Teste Técnico – Consolidação de Despesas (ANS)
# Sobre o projeto
Este projeto foi desenvolvido como parte do Teste Técnico para Estágio.
O objetivo é consolidar os dados de despesas relacionadas a Eventos/Sinistros a partir das demonstrações contábeis trimestrais disponibilizadas pela ANS.

O codigo realiza a extração automática de arquivos ZIP (quando presentes),
processa os arquivos CSV e gera um arquivo consolidado contendo as informações
padronizadas dos últimos três trimestres.

# Objetivo
- Processar dados contábeis trimestrais da ANS
- Identificar e filtrar despesas relacionadas a Eventos/Sinistros
- Consolidar os dados em um único arquivo CSV
- Garantir organização, clareza e reprodutibilidade do processo

# Estrutura do projeto

IntuitiveCare/
│
├── data/
│ ├── 1T2025.csv
│ ├── 2T2025.csv
│ ├── 3T2025.csv
│ └── consolidado_despesas.csv
│
├── etapa1.py
└── README.md

# Tecnologias utilizadas
- Python 3.13
- Pandas
- Pathlib
- Zipfile

# Pré-requisitos
Antes de executar o projeto, é necessário ter instalado na máquina:
- Python 3.9 ou superior

# Como executar o projeto

## Opção A — Clonar o repositório com Git 
- No terminal, execute:
- git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
- Em seguida, entre na pasta do projeto:
- cd SEU_REPOSITORIO

## Opção B — Download manual (sem usar Git)
- No GitHub, clique em Code > Download ZIP
- Extraia o arquivo ZIP em qualquer pasta do computador
- Abra a pasta extraída (essa será a pasta raiz do projeto)
- Instalar dependências
- No terminal, dentro da pasta do projeto, execute:
- pip install pandas
- Caso não funcione, tente:
- pip3 install pandas
- Preparar os dados
- Na raiz do projeto, utilize (ou crie) a pasta chamada data/
- Coloque dentro dessa pasta:
- Os arquivos ZIP dos trimestres ou os arquivos CSV já extraídos (exemplo: 1T2025.csv, 2T2025.csv, 3T2025.csv)

O pipeline identifica automaticamente arquivos ZIP e realiza a extração quando necessário.

## Como Executar o script: 

Ainda no terminal, dentro da pasta do projeto, execute: 
- python etapa1.py
Caso o comando acima não funcione, tente:
- python3 etapa1.py

# Resultado

Após a execução, o arquivo consolidado será gerado no seguinte caminho:
data/consolidado_despesas.csv

Ao final do processo, uma mensagem de sucesso será exibida no terminal.
