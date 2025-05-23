# SizeReducer
SizeReducer é um projeto que desenvolvi utilizando IA e meu conhecimento em programação a fim de otimizar o armazenamento dos meus clipes de jogos.
Este código permite reduzir o tamanho dos vídeos em uma pasta específica (incluindo suas subpastas), ajudando a liberar espaço no seu armazenamento,
podendo diminuir o espaço em até 10x ou mais!

Em meus testes consegui diminuir uma pasta de 377GB para apenas 32GB!

Os vídeos processados são organizados em uma nova pasta, que recebe o nome da pasta original, facilitando a gestão dos arquivos.

Antes:
![Screenshot 2024-10-30 174227](https://github.com/user-attachments/assets/18f4ee41-316f-4c8a-8ec9-f3634a1a4837)

Depois:
![Screenshot 2024-10-30 193147](https://github.com/user-attachments/assets/d8633afa-8928-4a56-9dd2-7e9e284b4492)


## Funcionalidades:
+ **Escolha de Codecs:** Suporte para H.264 e H.265.
+ **Eficiência:** Opção de excluir automaticamente os vídeos já processados.
+ **Escolha de Resolução:** Personalize a resolução dos vídeos.
+ **Escolha de Bitrate:** Ajuste o bitrate conforme sua necessidade.
+ **Escolha da Taxa de Quadros:** Defina a taxa de quadros desejada.



## Observações importantes:
Para utilizar o SizeReducer, você precisa instalar o FFmpeg. Acesse o site oficial "https://www.gyan.dev/ffmpeg/builds/" e faça o download da versão FULL. 
Extraia o conteúdo em seu sistema e coloque na unidade "C:".
Se o seu drive tiver um nome diferente ou se preferir colocar a pasta em outro diretório, modifique a string na linha 6 do código para o caminho correto do arquivo "ffmpeg.exe".
Para fazer isso, navegue até a pasta extraída, entre na pasta "bin", clique com o botão direito em "ffmpeg.exe" e selecione "Copy as path".

Ao atualizar a string na linha 6, lembre-se de adicionar uma barra invertida extra ao lado de cada barra invertida existente. Por exemplo:
Antes: C:\ffmpeg\bin\ffmpeg.exe
Depois: C:\\ffmpeg\\bin\\ffmpeg.exe

### Recomendação
Comece com uma pasta contendo dois ou três pequenos vídeos para testar, especialmente se você optar por excluir automaticamente os vídeos já processados.
Isso permite ajustar as configurações de bitrate e resolução conforme suas preferências, além de minimizar o risco de perder arquivos em caso de erros.

Para executar o projeto, basta fazer o download do arquivo, abrir o terminal, ir até o local do arquivo e executar o comando "python reduzir_videos.py".

(python deve estar instalado em seu computador)

Se houver dúvidas ou sugestões, sinta-se à vontade para entrar em contato comigo pelo e-mail pablosfranco201812@gmail.com. Ficarei feliz em ajudá-lo!
