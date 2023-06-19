# POC do Robo

Este robo tem por obtivo copiar algumas informações linha por linha de um arquivo
txt e colar nas linhas do Libre Office.
Para fazer isso ele questiona o usuário quantas linhas existe no arquivo.
Caso ele encontre o texo <i>=== eof ===</i> ou chegue no número de linhas informado pelo usuário
o robo encerra o script.

## Pré-requisitos

- Python (versão 3+)
- Windows
- Libre Office

## Instalação

1. Clone o repositório ou faça o download dos arquivos.
2. Instale as dependências executando o seguinte comando:

```
pip install -r requirements.txt
```

3. Dentro do diretório do script execute:

```
python script.py
```
