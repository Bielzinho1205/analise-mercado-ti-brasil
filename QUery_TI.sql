SELECT
  cbo2002_ocupacao,
  sigla_uf,
  ROUND(AVG(salario_mensal), 2) AS salario_medio,
  COUNT(*) AS total_admitidos
FROM `basedosdados.br_me_caged.microdados_movimentacao`
WHERE
  ano = 2024
  AND tipo_movimentacao = 1  -- 1 = admissão
  AND SUBSTR(cbo2002_ocupacao, 1, 4) IN (
    '2124',  -- Analistas de TI
    '2123',  -- Analistas de sistemas
    '2122',  -- Engenheiros de software
    '3172'   -- Técnicos em TI
  )
GROUP BY cbo2002_ocupacao, sigla_uf
ORDER BY salario_medio DESC