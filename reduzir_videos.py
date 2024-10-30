import os
import time
import subprocess

def reduzir_videos(pasta, nova_resolucao, novo_bitrate, fps, codec="h264_nvenc", excluir=False):
    caminho_ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"

    # Início do temporizador
    start_time = time.time()

    for root, dirs, files in os.walk(pasta):  # Percorre todas as pastas e subpastas
        # Cria uma pasta para os vídeos processados usando o nome da pasta atual
        pasta_saida = os.path.join(root, f"{os.path.basename(root)} - vídeos processados")
        os.makedirs(pasta_saida, exist_ok=True)

        for arquivo in files:
            if arquivo.endswith((".mp4", ".mkv", ".avi", ".mov")):
                caminho_entrada = os.path.join(root, arquivo)
                caminho_saida = os.path.join(pasta_saida, f"{arquivo}")

                try:
                    # Primeiro, obtenha as informações sobre as faixas de áudio
                    probe_cmd = [
                        caminho_ffmpeg,
                        '-i', caminho_entrada
                    ]
                    result = subprocess.run(probe_cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

                    # Contagem de faixas de áudio
                    audio_streams = result.stderr.count('Audio:')
                    print(f"Arquivo {arquivo} tem {audio_streams} faixa(s) de áudio.")

                    if audio_streams > 1:
                        # Comando para mesclar as faixas de áudio
                        cmd = [
                            caminho_ffmpeg,
                            '-i', caminho_entrada,
                            '-filter_complex', 'amerge',
                            '-vcodec', codec,
                            '-b:v', novo_bitrate,
                            '-vf', f'scale={nova_resolucao[0]}:{nova_resolucao[1]}',
                            '-r', fps,  # Usar os FPS definidos pelo usuário
                            '-acodec', 'aac',
                            '-b:a', '192k',
                            '-ac', '2',  # Força 2 canais de áudio
                            '-preset', 'p1',
                            caminho_saida
                        ]
                    else:
                        # Caso haja apenas uma faixa de áudio
                        cmd = [
                            caminho_ffmpeg,
                            '-i', caminho_entrada,
                            '-vcodec', codec,
                            '-b:v', novo_bitrate,
                            '-vf', f'scale={nova_resolucao[0]}:{nova_resolucao[1]}',
                            '-r', fps,  # Usar os FPS definidos pelo usuário
                            '-acodec', 'aac',
                            '-b:a', '192k',
                            '-ac', '2',  # Força 2 canais de áudio
                            '-preset', 'p1',
                            caminho_saida
                        ]

                    # Executa o comando usando subprocess
                    subprocess.run(cmd, check=True)

                    print(f"Vídeo {arquivo} convertido e salvo em {caminho_saida}")

                    # Excluir o vídeo original se a opção estiver ativada
                    if excluir:
                        os.remove(caminho_entrada)
                        print(f"Vídeo original {caminho_entrada} excluído.")

                except subprocess.CalledProcessError as e:
                    print(f"Erro ao processar {caminho_entrada}: {e}")

    # Fim do temporizador
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTempo total para processar todos os vídeos: {total_time:.2f} segundos")

if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta com os vídeos: ")
    
    # Mudando a entrada do codec para opções numéricas
    print("Escolha o codec para o vídeo:")
    print("1 - H.264 (h264_nvenc)")
    print("2 - H.265 (hevc_nvenc)")
    
    escolha_codec = input("Digite o número correspondente ao codec: ")
    codec = "h264_nvenc" if escolha_codec == "1" else "hevc_nvenc"

    # Pergunta ao usuário se deseja excluir os vídeos processados
    excluir_videos = input("Deseja excluir os vídeos originais após o processamento? (s/n): ").strip().lower() == 's'

    # Pergunta ao usuário pela resolução do vídeo
    largura = input("Digite a largura da nova resolução (por exemplo, 1920): ")
    altura = input("Digite a altura da nova resolução (por exemplo, 1080): ")
    nova_resolucao = (int(largura), int(altura))

    # Pergunta ao usuário pelo bitrate do vídeo
    novo_bitrate = input("Digite o bitrate do vídeo (por exemplo, 10000k): ")

    # Pergunta ao usuário pelo FPS do vídeo
    fps = input("Digite os FPS do vídeo (ex: 60). Atenção! Se o vídeo original tiver uma taxa de FPS menor, e o valor inserido for maior, o FPS não será aumentado durante a conversão, isso não causará nenhum problema e o processo será seguido normalmente. O vídeo só mostrará ter uma taxa de quadros maior em suas propriedades: ")

    reduzir_videos(pasta, nova_resolucao, novo_bitrate, fps, codec=codec, excluir=excluir_videos)
