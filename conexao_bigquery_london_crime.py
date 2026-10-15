"""
Estabelecendo conexão com o BigQuery 
Realizando Queries simples apenas para teste

Autor: Gabriel Araujo
Finalidade: Análise e entendimento de dados relacionados aos crimes de Londres de 2011 até 2016
"""

# Importando bibliotecas necessárias
from google.cloud import bigquery
import pandas as pd
import os
import sys

# Configurando conexão com o BigQuery
project_id = 'london-crimes-495314' 
client = bigquery.Client(project=project_id)

# Debug: Verificando se a conexão foi estabelecida
print("Conexão com BigQuery estabelecida com sucesso!")
print(f"Projeto atual: {client.project}")

# Realizando Query de validação 
sql_valida = f"""
SELECT 
    year, 
    COUNT(*) as total_registros,
    SUM(value) as total_crimes
FROM `bigquery-public-data.london_crime.crime_by_lsoa`
WHERE year >= 2011
GROUP BY year
ORDER BY year DESC
"""

print(">>> Validando dados de 2011 até 2016...")
df_valida = client.query(sql_valida).to_dataframe()

# Verificando tipos e nulos 
print("\n--- Informações da Tabela ---")
print(df_valida.info())
print("\n--- Resumo por Ano ---")
print(df_valida)