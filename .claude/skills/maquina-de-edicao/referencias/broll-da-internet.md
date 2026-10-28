# B-roll da internet

Quando um formato usa clipes de apoio (B-roll) e a pessoa não trouxe os dela, você busca sozinho em bancos de vídeo gratuitos. A pessoa não precisa criar pasta nem juntar arquivo nenhum.

Vale quando:

- a escolha de B-roll foi "Buscar clipes na internet" (é o padrão quando a pasta `broll/` não existe);
- ou a pasta `broll/` tem menos clipes que os pontos de B-roll do vídeo: complete com clipes da internet.

## De onde baixar (nesta ordem)

Só bancos com licença que permite usar em vídeo, inclusive comercial. **Nunca** baixe de YouTube, Instagram, TikTok, Google Imagens ou qualquer site sem licença clara: é conteúdo de outra pessoa.

1. **Pexels** (licença Pexels: uso livre, crédito opcional). Precisa de uma chave gratuita: procure `PEXELS_API_KEY` nas variáveis de ambiente e no arquivo `~/.maquina-de-edicao/chaves.env` (linhas `NOME=valor`).

   ```bash
   curl -s -H "Authorization: $PEXELS_API_KEY" \
     "https://api.pexels.com/videos/search?query=woman%20typing%20laptop&orientation=portrait&size=medium&per_page=15"
   ```

   Em `videos[].video_files[]`, pegue o arquivo `video/mp4` com o lado menor ≥ 1080 px (ou o maior que houver, se nenhum chegar a 1080). Crédito: `videos[].user.name` e `videos[].url`.

2. **Pixabay** (licença Pixabay: uso livre, crédito opcional). Chave gratuita em `PIXABAY_API_KEY` (mesmos lugares).

   ```bash
   curl -s "https://pixabay.com/api/videos/?key=$PIXABAY_API_KEY&q=woman+typing+laptop&per_page=15&safesearch=true"
   ```

   Use `hits[].videos.large.url` (ou `medium`). Crédito: `hits[].user` e `hits[].pageURL`.

3. **Wikimedia Commons** (sem chave). Aceite só as licenças CC0, domínio público, CC BY e CC BY-SA. As duas últimas exigem crédito: autor, licença e link no relatório e na sugestão de descrição do post.

   ```bash
   curl -s -A "MaquinaDeEdicao/1.0" "https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch=filetype:video%20laptop%20typing&gsrnamespace=6&gsrlimit=15&prop=videoinfo&viprop=url|size|mime|extmetadata&viextmetadatafilter=LicenseShortName|Artist"
   ```

   Os arquivos costumam ser `.webm`/`.ogv`: converta com FFmpeg pra H.264 antes de usar.

4. **Sem clipe que sirva** pra uma frase: use imagem no lugar (ordem de origem de `formatos-prontos.md`) com aproximação lenta (escala 1 → 1,06 no trecho todo), como na opção "Usar só imagens".

Sem chave do Pexels nem do Pixabay, siga direto pro Commons e avise a pessoa uma vez, no fim, em uma linha: "Pra clipes melhores nas próximas edições, crie uma chave grátis em pexels.com/api e me mande: eu guardo em `~/.maquina-de-edicao/chaves.env`." Não pare a edição por isso.

## Como buscar

1. Depois da transcrição e dos cortes, marque os pontos de B-roll do formato (ex: Reels com B-roll: a cada 3–6 s, nas frases que dá pra mostrar). Em `edit/plano.md`, monte a tabela **"frase → o que mostrar → busca"**.
2. A busca é em **inglês**, com 2 a 4 palavras concretas do que aparece na tela, não do conceito: "vender mais no direct" vira `phone notification shopping`; "trabalhar de madrugada" vira `laptop night desk`.
3. Pra vídeo vertical, peça orientação retrato quando o banco deixar (`orientation=portrait` no Pexels). Clipe horizontal também serve: o formato tem layout pra ele.
4. Baixe 2 ou 3 candidatos por ponto pra uma pasta temporária, extraia 3 quadros de cada (início, meio, fim) e olhe. Descarte:
   - marca d'água, logo ou texto queimado;
   - pessoa olhando pra câmera ou falando (parece outro vídeo);
   - qualidade baixa (lado menor < 720 px), tremida forte, cortes no meio;
   - qualquer coisa que contradiga a fala.
5. Copie o escolhido pra `broll/` com nome descritivo (`notificacao-celular-01.mp4`) e corte só o trecho que vai usar, com 0,5 s de folga em cada lado.
6. Registre cada clipe em `broll/creditos.md`: arquivo, banco, autor, licença, link. Leve essa lista pro relatório.
7. A partir daqui, siga "Como escolher os clipes" do formato como se a pasta tivesse vindo da pessoa.

## Imagens enviadas pela pessoa

Se a pessoa subiu imagens pelo painel (pasta `imagens/`), elas valem mais que qualquer coisa buscada: use primeiro, casando o nome do arquivo e o conteúdo com a fala.
