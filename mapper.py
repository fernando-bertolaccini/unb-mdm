
# Imports
import csv
import sys
from io import StringIO

# Variável que determina o tipo de causa de atendimento médico de emergência que estamos buscando
ID_CAUSA = '1'

# Loop pelo arquivo de entrada
for line in sys.stdin:
    
    # Separa as linhas
    linha_bytes = line.strip()
    
    # O resultado anterior é em bytes, então convertemos para string
    linha_string = StringIO(linha_bytes)
    
    # Agora separamos as colunas pelo caracter separador vírgula
    colunas_arquivo = csv.reader(linha_string, delimiter = ',')
    
    # Para cada coluna de cada linha...
    for coluna in colunas_arquivo:
        
        # ...checamos a condição de causa (índice 2) e ...
        causa = coluna[2]
        
        # ...se verdadeiro, extraímos as duas colunas que nos interessam 
        # Nome_Estabelecimento (índice 1) e Total_Pessoas_Atendidas (índice 4)
        if causa == ID_CAUSA:
            
            # O resultado é gerado em duas colunas separadas por tab (\t)
            print("%s\t%s" % (coluna[1], coluna[4]))
