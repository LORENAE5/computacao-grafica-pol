from pdf2image import convert_from_path
import os 

pdf_path = "enem2024.pdf"
output_folder = "imagens"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

resolucao_dpi = 300

print(f"Convertendo '{pdf_path}' para imagens com {resolucao_dpi} DPI...")

try:
    images = convert_from-path(
        pdf-path,
        pdi=resolucao_dpi,
        output_folder=output_folder,
        fmt="png",
        paths_only=False,
    )

    for i, image in enumerate(images):
        image_filename = os.path.join (output_folder, f"pagina_enem_{i+1}.png")
        image.save(image_filename)
        print(f"Página {i+1}salva como'{image_filename}'")

    print(f"\nConversão concluida! As imagens foram salvas na pasta '{output_folder}'.")

except Exception as e:
    print(f"Ocorreu um erro durante a conversão: {e}")
    print("Verifique se o Poppler está instalado corretamente e se o caminho do PDF está correto.")