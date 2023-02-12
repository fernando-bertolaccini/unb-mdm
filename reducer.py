
# Imports
import sys
 
# Dicionário para gravar o resultado
resultado = {}

# Função para gravar o resultado no dicionário
def geraResultado(resultado, hospital, total_atendimentos):
    
    # Verifica se o nome do hospital ainda não está na lista de reseultados
    if hospital not in resultado:
        
        # Se não estiver, inclui pela primeira vez
        resultado[hospital] = total_atendimentos
    else:
        # Se já estiver, adiciona ao que já está lá e grava na própria variável
        resultado[hospital] = resultado[hospital] + total_atendimentos

        
# Loop para ler o resultado do processo de mapeamento
for line in sys.stdin:
    
    # Separa as linhas
    linha = line.strip()
    
    # Separa as colunas
    hospital, total_atendimentos = line.split('\t', 1)
    
    # Chama a função de gravação do resultado
    geraResultado(resultado, hospital, int(total_atendimentos))
    
# Imprime o resultado que será gravado em um arquivo txt
# As colunas serão separadas pelo caracter pipe |
for (x, y) in resultado.items():
    print("%s|%s" % (x, y))
