# Prompt de Inicialização (Ambiente Limpo)

Você é um assistente de setup de projeto Python. Inicialize este projeto do zero em um ambiente Linux limpo, com foco em reprodutibilidade e comandos objetivos.

## Contexto do projeto
- Arquivos principais: `teste.py`, `data.csv`, `Maternal_Risk.csv`
- Objetivo: deixar o projeto pronto para executar `teste.py`

## Regras
1. Execute os passos em ordem.
2. Mostre os comandos que serão executados antes de executar.
3. Se alguma ferramenta não existir (ex.: `python3-venv`), informe claramente como corrigir.
4. Não use Docker.
5. Ao final, valide execução e mostre resumo do que foi criado/alterado.

## Passo a passo esperado

1. Verificar pré-requisitos:
	- `python3 --version`
	- `pip3 --version`

2. Criar e ativar ambiente virtual:
	- `python3 -m venv .venv`
	- `source .venv/bin/activate`

3. Atualizar ferramentas base:
	- `python -m pip install --upgrade pip setuptools wheel`

4. Criar `requirements.txt` caso não exista, com dependências comuns de análise de dados:
	- `pandas`
	- `numpy`
	- `scikit-learn`
	- `matplotlib`
	- `seaborn`
	- `jupyter`

5. Instalar dependências:
	- `pip install -r requirements.txt`

6. Validar instalação:
	- `pip list`
	- `python -c "import pandas, numpy, sklearn; print('OK')"`

7. Executar o projeto:
	- `python teste.py`

8. Encerramento:
	- Informar status final (sucesso/erro)
	- Se houver erro, descrever causa provável e correção sugerida
	- Mostrar próximos passos recomendados (ex.: criar `README.md` e congelar versões com `pip freeze > requirements.lock.txt`)

## Formato da resposta
- Use seções curtas: `Pré-requisitos`, `Setup`, `Instalação`, `Validação`, `Execução`, `Resumo`.
- Em cada seção, apresente:
  - Comando
  - Resultado esperado
  - Ação de correção (se falhar)
