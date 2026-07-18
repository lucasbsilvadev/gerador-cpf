# gen_cpf (handmade)

gerador de cpf feito a mão, pra exercitar lógica e algoritmos em python.

## por que gastar tempo com isso?

estudar já é parte da rotina, então, porque não usar da aplicação prática pra estudar né...
é interessante manipular variáveis, listas e vários valores lógicos sem as libs que automatizam tudo
mesmo assim, o python continua simples e muito prático

## funcionamento

o algoritmo é orientado pelo padrão oficial:

1. gera 8 números aleatórios (0-9)
2. escolhe um 9º número baseado na região (tabela da Receita)
3. calcula D1 e D2 usando os pesos (10,9,8... e 11,10,9...)
4. se o resto da divisão por 11 for 0 ou 1, o dígito é 0
5. senão, é 11 - resto

### sample
=== GERADOR DE CPF ===

Dígitos gerados: [7, 3, 9, 1, 5, 8, 2, 4]
Região selecionada: Minas Gerais (MG)
D1 calculado: 6
D2 calculado: 3

CPF gerado: 739.158.246-63

text

## Estrutura do código
main.py
├── gerar_digitos_aleatorios() # os 8 primeiros
├── escolhe_id_regiao() # define o 9º dígito
├── calcular_d1() # primeiro verificador
├── calcular_d2() # segundo verificador
├── montar_cpf() # formata com pontos e traço
└── main() # orquestra tudo

text

## conhecimentos que obtive

- que a geração de identificadores pode ser mais matemática do que sintaxe
- relacionar pares chave valor com uso dos dicionários
- montagem de funções e indexação dos dígitos dos valores aleatórios

## como rodar

```bash
python main.py
caso tenha mais versões python:

bash
python3 main.py
