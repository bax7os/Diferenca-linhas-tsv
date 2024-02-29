import os
import re

# modelo do nome do arquivo: nº - frames - tipo - nome_paciente


# Generalizando arquivos 
def listar_arquivos_com_extensao(diretorio, extensao):
    arquivos = []
    for arquivo in os.listdir(diretorio):
        if re.search(r'\.' + extensao + r'$', arquivo):
            arquivos.append(os.path.join(diretorio, arquivo))
    return arquivos


# Conta a quantidade de linhas dos arquivos
def contar_linhas_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        '''
        if arquivo == tsv:
            new = len(linhas)
        else:
            new = len(linhas)
        '''
    return len(linhas)

#Diferença entre a quantidade de linhas dos arquivos
def diferenca_linhas(arquivo_tsv, arquivo_csv):
    linhas_tsv = contar_linhas_arquivo(arquivo_tsv)
    linhas_csv = contar_linhas_arquivo(arquivo_csv)
    diferenca = linhas_tsv - linhas_csv
    return diferenca

#Escreve resultado em um arquivo de saída
def salvar_resultado_arquivo(arquivo, diferenca, nome_arquivo):
    with open(arquivo, 'a') as f:  # Modo 'a' para adicionar ao final do arquivo
        f.write(str(diferenca) + " " + nome_arquivo + '\n')  # Adiciona uma quebra de linha após o resultado


diretorio = '.'  # Diretório atual, pode ser alterado para o diretório desejado
arquivos_tsv = listar_arquivos_com_extensao(diretorio, 'tsv')
arquivos_csv = listar_arquivos_com_extensao(diretorio, 'csv')
arquivo_resultado = 'saida/resultado.tsv'

# Verificar se há pelo menos um arquivo TSV e um arquivo CSV
if not arquivos_tsv or not arquivos_csv:
    print("Não foram encontrados arquivos TSV ou CSV no diretório.")
else:
    for tsv, csv in zip(arquivos_tsv, arquivos_csv):
        diferenca = diferenca_linhas(tsv, csv)
        nome_arquivo = str(csv)
        salvar_resultado_arquivo(arquivo_resultado, diferenca, nome_arquivo)

#Confirma arquivo de destino
print("Diferenças entre linhas salvas em", arquivo_resultado)
