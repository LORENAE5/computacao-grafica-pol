from PIL import Image
import os

# Configurações
pasta_imagens = "metades-recortadas"
pasta_saida = "concatenadas"
os.makedirs(pasta_saida, exist_ok=True)

# Lista para armazenar os pares de imagens
pares_imagens = []

# Coletar todas as imagens e organizar por número
for numero in range(2, 28):  # 2 a 27
    esquerda_path = os.path.join(pasta_imagens, f"pagina_enem_{numero}_esquerda.png")
    direita_path = os.path.join(pasta_imagens, f"pagina_enem_{numero}_direita.png")
    
    if os.path.exists(esquerda_path) and os.path.exists(direita_path):
        pares_imagens.append((esquerda_path, direita_path, numero))

# Verificar se encontramos pares
if not pares_imagens:
    print("Nenhum par de imagens encontrado!")
    exit()

# Carregar o primeiro par para obter dimensões
primeira_esquerda = Image.open(pares_imagens[0][0])
primeira_direita = Image.open(pares_imagens[0][1])

# Obter dimensões (assumindo que todas as imagens têm o mesmo tamanho)
largura = primeira_esquerda.width
altura = primeira_esquerda.height

# Criar imagem final (altura total = altura * número de pares * 2)
imagem_final = Image.new('RGB', (largura, altura * len(pares_imagens) * 2))

# Posicionar as imagens
y_pos = 0
for esquerda_path, direita_path, numero in pares_imagens:
    try:
        # Carregar imagens
        img_esquerda = Image.open(esquerda_path)
        img_direita = Image.open(direita_path)
        
        # Colocar imagem esquerda (em cima)
        imagem_final.paste(img_esquerda, (0, y_pos))
        y_pos += altura
        
        # Colocar imagem direita (embaixo)
        imagem_final.paste(img_direita, (0, y_pos))
        y_pos += altura
        
        print(f"Par {numero} adicionado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao processar par {numero}: {e}")

# Salvar imagem final
caminho_final = os.path.join(pasta_saida, "paginas_concatenadas_final.png")
imagem_final.save(caminho_final)
print(f"Imagem final salva em: {caminho_final}")
print(f"Dimensões da imagem final: {imagem_final.width}x{imagem_final.height}")