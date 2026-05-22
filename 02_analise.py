import pandas as pd

df = pd.read_csv('dados_ti_limpos.csv')

# 1. Salário médio por ocupação
print("=== Salário médio por ocupação ===")
sal_ocupacao = df.groupby('ocupacao')['salario_mensal'].agg(['mean','count']).round(2)
sal_ocupacao.columns = ['salario_medio', 'total_admitidos']
sal_ocupacao = sal_ocupacao.sort_values('salario_medio', ascending=False)
print(sal_ocupacao)
sal_ocupacao.to_csv('resultado_salario_ocupacao.csv')

# 2. Salário médio por estado
print("\n=== Salário médio por estado ===")
sal_uf = df.groupby('sigla_uf')['salario_mensal'].agg(['mean','count']).round(2)
sal_uf.columns = ['salario_medio', 'total_admitidos']
sal_uf = sal_uf.sort_values('salario_medio', ascending=False)
print(sal_uf)
sal_uf.to_csv('resultado_salario_uf.csv')

# 3. Admissões por mês
print("\n=== Admissões por mês ===")
por_mes = df.groupby(['ano','mes']).size().reset_index(name='total_admitidos')
print(por_mes)
por_mes.to_csv('resultado_por_mes.csv', index=False)

# 4. Distribuição por sexo
print("\n=== Distribuição por sexo ===")
print(df['sexo'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%')

# 5. Salário médio por grau de instrução
print("\n=== Salário médio por grau de instrução ===")
sal_instrucao = df.groupby('grau_instrucao')['salario_mensal'].mean().round(2).sort_values(ascending=False)
print(sal_instrucao)
sal_instrucao.to_csv('resultado_salario_instrucao.csv')