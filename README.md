# SpotifyGenreFinder

🎵 **Organizador Automático de Playlists por Gênero Musical**

Uma ferramenta Python que analisa uma playlist do Spotify e automaticamente cria playlists separadas organizadas por gênero musical, facilitando a descoberta e organização da sua biblioteca musical.

## 📋 Funcionalidades

- **Análise de Gênero**: Extrai informações de gênero de cada música através da API do Spotify
- **Classificação Inteligente**: Sistema de classificação que mapeia múltiplos sub-gêneros para categorias principais
- **Criação Automática**: Gera automaticamente novas playlists nomeadas como "auto - [Gênero]"
- **Processamento em Lote**: Processa grandes playlists de forma eficiente
- **Suporte Multilíngue**: Reconhece gêneros brasileiros (Samba, Pagode, Sertanejo, etc.) e internacionais

## 🎯 Gêneros Suportados

O sistema reconhece e classifica mais de 40 gêneros musicais, incluindo:

- **Rock & Metal**: Rock, Metal, Punk, Grunge, Hardcore
- **Pop & Mainstream**: Pop, Indie, Alternative
- **Hip-Hop & Rap**: Hip-Hop, Rap, Trap
- **Eletrônica**: Electronic, House, Techno, EDM, Dubstep, Drum & Bass
- **Jazz & Blues**: Jazz, Blues, Soul, Funk
- **Brasileiros**: Samba, Pagode, Sertanejo, Forró, Axé, MPB, Bossa Nova
- **Internacionais**: K-Pop, J-Pop, Reggaeton, Latin
- **E muito mais...**

## 🚀 Como Usar

1. **Configure as credenciais do Spotify**:
   - Crie um arquivo `.env` com suas credenciais da API do Spotify:
   ```
   spotifyID=seu_client_id
   spotifySecret=seu_client_secret
   ```

2. **Execute o script**:
   ```bash
   python genreFinder.py
   ```

3. **Cole o link da playlist** quando solicitado

4. **Aguarde o processamento** - o sistema irá:
   - Extrair todas as músicas da playlist original
   - Analisar o gênero de cada música
   - Criar playlists separadas por gênero
   - Adicionar as músicas nas respectivas playlists

## 📦 Dependências

```bash
pip install spotipy pandas python-dotenv
```

## 🔧 Configuração da API Spotify

1. Acesse [Spotify for Developers](https://developer.spotify.com/)
2. Crie uma nova aplicação
3. Configure a Redirect URI como: `http://127.0.0.1:1410`
4. Copie o Client ID e Client Secret para o arquivo `.env`

## 💡 Exemplo de Uso

```
Cole o link da playlist do Spotify: https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M
✅ - Playlist Updated!
25 songs added to playlist 'GenreFinder - Rock' successfully!
✅ - Playlist Updated!
18 songs added to playlist 'GenreFinder - Pop' successfully!
...
```


## 🎨 Estrutura do Projeto

- `genreFinder.py`: Script principal com a classe ConnectSpotify e toda a lógica de integração com Spotify
- `genre_classifier.py`: Módulo dedicado à classificação de gêneros musicais (função classify_genre)
- `README.md`: Documentação do projeto
- `.env`: Arquivo de configuração (não incluído no repositório)

## 🔍 Como Funciona

1. **Conexão**: Estabelece conexão com a API do Spotify usando OAuth
2. **Extração**: Obtém todas as músicas da playlist fornecida
3. **Análise**: Para cada música, busca informações do artista e seus gêneros
4. **Classificação**: Mapeia os gêneros usando um sistema de classificação inteligente
5. **Organização**: Cria playlists separadas e adiciona as músicas correspondentes

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Adicionar novos gêneros ao sistema de classificação
- Melhorar a precisão da detecção de gêneros
- Otimizar o desempenho do processamento
- Adicionar novas funcionalidades

## 📄 Licença

Este projeto é open source e está disponível sob a licença MIT.
