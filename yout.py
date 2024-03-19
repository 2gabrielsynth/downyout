import streamlit as st
from pytube import YouTube
import os

def main():
    st.title("Download de Vídeo do YouTube")
    st.write("Cole o link do vídeo do YouTube abaixo:")

    # Campo de entrada para o link do vídeo
    video_url = st.text_input("URL do vídeo do YouTube")

    # Verifica se o link foi inserido e se o usuário clicou no botão "Download"
    if st.button("Download"):
        if video_url:
            try:
                yt = YouTube(video_url)

                # Exibe informações sobre o vídeo
                st.write("Título:", yt.title)
                st.write("Duração:", yt.length, "segundos")

                # Obtém a melhor resolução disponível para o vídeo
                video_stream = yt.streams.get_highest_resolution()

                # Baixa o vídeo
                st.write("Baixando...")
                file_path = os.path.join(os.getcwd(), f"{yt.title}.mp4")
                video_stream.download(filename=file_path)

                st.success("Download completo!")
                
                # Abre o arquivo de vídeo para streaming
                with open(file_path, 'rb') as f:
                    video_bytes = f.read()

                # Exibe o vídeo para o usuário
                st.video(video_bytes)

            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")
        else:
            st.warning("Por favor, insira o link do vídeo do YouTube.")

if __name__ == "__main__":
    main()
