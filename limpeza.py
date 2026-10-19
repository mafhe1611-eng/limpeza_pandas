import pandas as pd

caminho_arquivo = 'lista.csv'
df = pd.read_csv(caminho_arquivo)

print("--- Dados originais lidos do seu CSV ---")
print(df[['ID', 'Data']])
print("\n" + "="*50 + "\n")

df['Data_Limpa'] = pd.to_datetime(df['Data'], format='mixed', errors='coerce')
print("--- Resultado da limpeza  ---")
print(df[['ID', 'Data', 'Data_Limpa']])

df_limpo = df.dropna(subset=['Data_Limpa'])
print(f"Linhas restantes no mesmo DataFrame: {len(df_limpo)}")

print("Tipo da coluna de data ANTES:")
print(df['Data'].dtype)

df['Data'] = pd.to_datetime(df['Data'], format='mixed', errors='coerce')

print("\nTipo da coluna de data DEPOIS:")
print(df['Data'].dtype)

#Valores irreais na coluna de idade
df_limpo = df_limpo.copy()
df_limpo['Idade_Alternativa'] = [35] * 106 + [300]

indice_suspeito = df_limpo[df_limpo['Idade_Alternativa'] == 300].index[0]
df_limpo.loc[indice_suspeito, 'Idade_Alternativa'] = 30
print(f"Valor corrigido no índice {indice_suspeito}!")
print(df_limpo.loc[[indice_suspeito], ['ID', 'Nome', 'Idade_Alternativa']])

limite_teto = 100
for indice in df_limpo.index:
    if df_limpo.loc[indice, 'Idade'] > limite_teto:
        df_limpo.loc[indice, 'Idade'] = limite_teto

print("--- Correção por Regra de Corte Concluída! ---")
print(df_limpo[['ID', 'Nome', 'Idade']].head(10))

limite_teto = 100
print(f"Linhas antes de remover as idades absurdas: {len(df_limpo)}")
for indice in df_limpo.index:
    if df_limpo.loc[indice, 'Idade'] > limite_teto:
        df_limpo = df_limpo.drop(indice)
print(f"Linhas restantes após a remoção por regra de corte: {len(df_limpo)}")

print("--- INICIANDO DESAFIO: DOIS PROBLEMAS DE UMA VEZ ---\n")
df_limpo['Data'] = pd.to_datetime(df_limpo['Data'], format='mixed', errors='coerce')
df_limpo = df_limpo.dropna(subset=['Data'])
print(f"Passo 1 Concluído: Datas padronizadas e NaT removidos. Linhas: {len(df_limpo)}")
limite_teto = 110
for indice in df_limpo.index:
    if df_limpo.loc[indice, 'Idade'] > limite_teto:
        df_limpo = df_limpo.drop(indice)
print(f"Passo 2 Concluído: Idades absurdas (> {limite_teto} anos) removidas. Linhas finais: {len(df_limpo)}")
print("\n" + "="*50 + "\n")
print("--- DataFrame Final Tratado e Pronto ---")
print(df_limpo[['ID', 'Nome', 'Data', 'Idade']].head(10))