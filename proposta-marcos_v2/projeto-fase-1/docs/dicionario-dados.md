Leia toda a documentação existente antes de implementar qualquer código.

Documentação existente:

- README.md
- docs/01-analise-dataset.md
- docs/02-limpeza-dados.md

Caso algum documento citado não exista, ignore-o.

Objetivo desta etapa:

Implementar apenas o arquivo:

scripts/01_analise_dataset.py

Requisitos:

- Ler o arquivo:
  data/raw/VIOLBR25.xlsx

- Utilizar pandas para leitura dos dados.

- Utilizar pathlib para manipulação dos caminhos.

- Não utilizar caminhos absolutos.

- Criar automaticamente a pasta "relatorios" caso ela não exista.

O script deve:

1. Exibir no console:

- Quantidade de registros
- Quantidade de colunas
- Lista de todas as colunas

2. Gerar o arquivo:

relatorios/01_colunas.xlsx

contendo todas as colunas do dataset.

3. Gerar o arquivo:

relatorios/02_relatorio_colunas.xlsx

contendo:

- Nome da coluna
- Tipo do dado
- Quantidade de valores nulos
- Percentual de valores nulos
- Quantidade de valores distintos

4. Gerar o arquivo:

relatorios/03_valores_unicos.xlsx

Criar uma aba para cada coluna contendo:

- Valor
- Quantidade de ocorrências

5. Caso exista a coluna CS_SEXO, exibir sua distribuição no console.

6. Adicionar comentários explicando cada etapa do código.

7. Seguir o padrão PEP 8.

Não implemente nenhuma limpeza de dados nesta etapa.

Após concluir a implementação, atualize o arquivo docs/01-analise-dataset.md informando como executar o script e quais arquivos são gerados.

Não altere nenhum outro arquivo.