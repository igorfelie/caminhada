import streamlit as st
from PIL import Image
import io

def process_image(uploaded_image):
    # Caminho da imagem base (agora no repositório)
    try:
        # A imagem editavel.png está na pasta "images"
        base_image = Image.open("images/editavel.png")  # Certifique-se de que você tenha a imagem no repositório
        
        if uploaded_image is not None:
            user_image = Image.open(uploaded_image)

            # Coordenadas do quadrado onde a imagem será colocada
            left = 214   # Distância da borda esquerda do quadrado
            top = 718    # Distância da borda superior do quadrado
            right = 865  # Distância da borda direita do quadrado
            bottom = 1465 # Distância da borda inferior do quadrado

            # Dimensões do quadrado branco onde a imagem será colocada
            box_width = right - left
            box_height = bottom - top

            # Redimensionar a imagem para caber no quadrado branco, mantendo a proporção
            user_image.thumbnail((box_width, box_height))  # Mantém a proporção da imagem

            # Calcular a posição para centralizar a imagem no quadrado branco
            x_offset = left + (box_width - user_image.width) // 2 + 50  # Deslocamento para a direita
            y_offset = top + (box_height - user_image.height) // 2

            # Colocar a imagem do usuário dentro do quadrado branco da imagem base
            base_image.paste(user_image, (x_offset, y_offset))  # Coloca a imagem no quadrado branco

            return base_image
        else:
            return base_image  # Se não houver upload, exibe a imagem base sem alterações

    except Exception as e:
        st.error(f"Erro ao processar a imagem: {e}")
        return None

def save_image(image):
    """Converte a imagem para um formato que possa ser baixado."""
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

def main():
    st.title("Envio de Imagem")

    # Carregar o arquivo da imagem do usuário
    uploaded_image = st.file_uploader("Carregue sua imagem", type=["png", "jpg", "jpeg"])

    # Processar a imagem conforme as opções
    final_image = process_image(uploaded_image)

    if final_image is not None:
        # Exibir a imagem final com o parâmetro width='stretch'
        st.image(final_image, caption="Imagem Final", width='stretch')

        # Botão para baixar a imagem (sem customização adicional)
        img_byte_arr = save_image(final_image)
        st.download_button(
            label="Baixar Imagem",
            data=img_byte_arr,
            file_name="imagem_final.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
