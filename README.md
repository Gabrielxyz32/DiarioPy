# Diário Pessoal em Python

Projeto de um diário pessoal desenvolvido em Python para praticar os principais conceitos da linguagem.

A aplicação funciona pelo terminal e permite criar, visualizar, pesquisar e excluir entradas. As informações são armazenadas em um arquivo JSON para que continuem disponíveis quando o programa for executado novamente.

## Funcionalidades

* Adicionar entradas ao diário
* Registrar automaticamente a data da entrada
* Exibir as entradas do dia
* Exibir todas as entradas
* Pesquisar entradas pelo título ou pelo texto
* Excluir entradas pelo índice
* Salvar as entradas em um arquivo JSON
* Carregar as entradas salvas ao iniciar o programa

## Tecnologias

* Python 3.10+
* `datetime`
* `json`

## Estrutura

Cada entrada é armazenada como um dicionário:

```python
{
    "Titulo": "Meu dia",
    "Texto": "Hoje estudei Python.",
    "Data": "25/09/2026"
}
```

As entradas são armazenadas em uma lista:

```python
entradas = [
    {
        "Titulo": "Meu dia",
        "Texto": "Hoje estudei Python.",
        "Data": "25/09/2026"
    }
]
```

## Persistência dos dados

O projeto utiliza o arquivo `diario.json` para armazenar as entradas.

Quando uma nova entrada é adicionada ou uma entrada é excluída, os dados são salvos no arquivo. Ao iniciar o programa, as informações salvas são carregadas novamente para a lista `entradas`.

Para isso, o projeto utiliza as funções `json.dump()` e `json.load()`.

## Como executar

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd diario-python
```

Execute o programa:

```bash
python main.py
```

No Windows, também pode ser necessário utilizar:

```bash
py main.py
```

## Menu

O programa possui as seguintes opções:

```text
Diário Pessoal no Python

1 - Inserir nota neste dia
2 - Exibir notas neste dia
3 - Exibir todas as notas
4 - Pesquisar entradas
5 - Excluir entradas
6 - Sair
```

## Conceitos praticados

O projeto está sendo desenvolvido como forma de praticar:

* Variáveis e tipos de dados
* Funções
* Listas
* Dicionários
* Estruturas de repetição
* Condicionais
* `match/case`
* `enumerate()`
* Manipulação de strings
* Manipulação de arquivos
* `try/except`
* JSON
* Persistência de dados

## Objetivo

Este projeto foi criado para estudar Python na prática, evoluindo a aplicação conforme novos conceitos da linguagem são aprendidos.
