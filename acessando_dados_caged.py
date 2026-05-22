import pandas as pd

# Carregar o arquivo — ajuste o nome se for diferente
df = pd.read_csv('c:/Users/gabri/OneDrive/Documentos/Projetos_Dados/bquxjob_106b51_19e4e5161cf.csv')

# Ver as primeiras linhas e o tamanho
print("Shape:", df.shape)
print(df.head())
print(df.dtypes)

# Mapear CBO para nome da ocupação
ocupacoes = {
    212205: 'Engenheiro de software',
    212210: 'Engenheiro de software sênior',
    212215: 'Arquiteto de software',
    212305: 'Analista de sistemas',
    212310: 'Analista de sistemas sênior',
    212315: 'Analista de negócios',
    212320: 'Analista de suporte',
    212405: 'Analista de TI',
    212410: 'Analista de infraestrutura',
    212415: 'Analista de dados',
    212420: 'Desenvolvedor',
    212425: 'Desenvolvedor sênior',
    212430: 'Desenvolvedor web',
    317205: 'Técnico em informática',
    317210: 'Técnico em suporte'
}

# Mapear sexo
sexo = {1: 'Masculino', 3: 'Feminino'}

# Mapear grau de instrução
instrucao = {
    1: 'Analfabeto',
    3: 'Fundamental incompleto',
    4: 'Fundamental completo',
    5: 'Médio incompleto',
    6: 'Médio completo',
    7: 'Superior incompleto',
    8: 'Superior completo',
    9: 'Mestrado/Doutorado'
}

# Aplicar os mapeamentos
df ['ocupacao'] = df['cbo_2002'].map(ocupacoes)
df ['sexo'] = df['sexo'].map(sexo)
df ['grau_instrucao'] = df['grau_instrucao'].map(instrucao)

# Remover salários zerados ou nulos
df = df[df['salario_mensal'] > 0]
df = df.dropna(subset=['salario_mensal', 'ocupacao'])

# Ver resultado
print("\nApós limpeza:")
print("Shape:", df.shape)
print(df[['ocupacao', 'sigla_uf', 'salario_mensal', 'sexo', 'grau_instrucao']].head(10))

# Salvar CSV limpo
df.to_csv('c:/Users/gabri/OneDrive/Documentos/Projetos_Dados/dados_ti_limpos.csv', index=False)
print("\nArquivo salvo: dados_ti_limpos.csv")

#212405 — Analista de sistemas
#212410 — Analista de suporte
#212415 — Analista de dados
#317110 — Técnico em informática