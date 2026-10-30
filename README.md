# Máquina de Edição com IA — oferta principal + complemento

Repositório de desenvolvimento dos 12 formatos. Cada formato tem uma skill própria e um comando. A entrega comercial tem **dois pacotes separados**: seis formatos na oferta principal e seis no order bump.

## Oferta principal — 6 formatos

| Skill / comando | Como fica |
|---|---|
| `/reels-de-negocio` | Alterna câmera cheia, tela dividida e animação em tela cheia |
| `/reels-com-broll` | Cortes rápidos, clipes de apoio e frases-chave empilhadas |
| `/tela-dividida-explicativa` | Você embaixo e explicações animadas em cima |
| `/ensaio-visual` | Você recortado com notícias, números e provas visuais |
| `/recorte-com-imagens` | Você na frente de imagens que mudam com a fala |
| `/telas-em-profundidade` | Interfaces animadas atrás de você, com profundidade |

A seleção prioriza variedade de composição, impacto visual e uso recorrente em conteúdo curto: venda, explicação, comentário e demonstração de ferramentas. É uma escolha editorial baseada nas especificações dos formatos, sem comparação de novos vídeos renderizados.

O pacote inclui o motor `/maquina-de-edicao`, os seis formatos acima e os estilos visuais **Pixelado, Noite Laranja e Claro Tecnológico**. São sete skills no total. Os seis formatos são verticais (9:16); a edição **Do zero** continua aceitando gravações horizontais.

## Order bump — 6 formatos extras

| Skill / comando | Como fica |
|---|---|
| `/legenda-encaixada` | Tipografia animada, com uma palavra gigante e a frase encaixada ao redor |
| `/nuvem-de-imagens` | Grupos de imagens acima da cabeça, com visual editorial |
| `/formato-ranking` | Tier list animada que se preenche conforme as avaliações |
| `/cortes-de-video-longo` | Seleção e edição de cortes verticais de um vídeo longo |
| `/youtube-educativo` | Vídeo horizontal com cards, tela dividida e animações explicativas |
| `/aula-em-tela-dividida` | Documento da aula ao lado da câmera, com entrega em PDF |

O complemento amplia as possibilidades com tipografia, colagens, listas, reaproveitamento de vídeos longos, YouTube e aulas. Ele requer o pacote principal e adiciona seis skills; não inclui outra cópia do motor. Após instalar os dois, são 13 skills (motor + 12 formatos).

## Formato e estilo visual

**Formato** define estrutura, layouts e ritmo. **Estilo visual** define cores, fontes, materiais, aparência das legendas e música. Cada formato pode usar seu visual original, Pixelado, Noite Laranja, Claro Tecnológico ou um estilo pessoal. Os estilos visuais continuam incluídos no principal; a divisão 6 + 6 é dos formatos.

A pessoa pode pedir para analisar o visual de um vídeo de referência ou descrever um visual novo. Os estilos pessoais ficam em `~/.maquina-de-edicao/estilos-visuais/`. Preferências e ajustes ficam em `~/.maquina-de-edicao/preferencias.md`, fora das skills.

## Estrutura de desenvolvimento

- `.claude/skills/`: motor e seis formatos do principal.
- `pacote.json`: lista exata das sete skills do principal.
- `order-bump/.claude/skills/`: seis formatos extras.
- `order-bump/pacote.json`: lista exata das seis skills do complemento.
- `LEIA-ME.md` e `order-bump/LEIA-ME.md`: instruções que acompanham cada entrega.
- `instalar.ps1` e `instalar.sh`: instaladores compartilhados, que seguem o manifesto do pacote.
- `preparar-pacotes.ps1`: gera os dois ZIPs, cada um com manifesto, instaladores e instruções próprios.
- `dist/`: entregas geradas, ignoradas no Git.

## Gerar as entregas

Na raiz deste repositório, execute:

```powershell
powershell -ExecutionPolicy Bypass -File .\preparar-pacotes.ps1
```

Saídas:

- `dist/maquina-de-edicao-principal.zip`: motor + seis formatos; sem arquivos das seis skills extras.
- `dist/maquina-de-edicao-order-bump.zip`: somente as seis skills extras.

Para gerar outra versão sem substituir os ZIPs anteriores, use `-Saida <outra-pasta>`.

Entregue o primeiro ZIP na oferta principal e o segundo apenas a quem comprou o order bump. **O repositório completo contém os dois pacotes** e não deve ser usado como download da oferta principal. Não há licença ou bloqueio por checkout: a separação é feita pelos arquivos entregues. Preço e configuração comercial do complemento não são definidos por este repositório.

## Instalação pelo aluno

A pessoa extrai seu ZIP inteiro, incluindo `.claude`, abre um terminal na pasta extraída e roda:

Windows:

```powershell
powershell -ExecutionPolicy Bypass -File .\instalar.ps1
```

Mac/Linux:

```bash
bash instalar.sh
```

Cada ZIP instala somente as skills do próprio manifesto em `~/.claude/skills/`. O complemento verifica a presença do motor antes de copiar qualquer arquivo. As versões anteriores das mesmas skills vão para `~/.claude/skills-backup/`; preferências, estilos pessoais e outras skills já instaladas são preservados. Atualizar o principal mantém os extras de quem já instalou o complemento. Instalações antigas com os 12 formatos também são preservadas.

Para atualizar, o aluno baixa o novo ZIP do pacote comprado e roda seu instalador. Depois de instalar ou atualizar, fecha e abre o Claude Code.

Para testar diretamente a partir deste repositório de desenvolvimento:

```powershell
.\instalar.ps1
.\instalar.ps1 -Pacote order-bump
```

```bash
bash instalar.sh
bash instalar.sh order-bump
```

## Como usar

1. Crie uma pasta própria para o vídeo, fora da pasta de instalação, e coloque a gravação nela.
2. Abra o Claude Code nessa pasta e digite `/maquina-de-edicao` ou o comando de um formato instalado.
3. Na primeira edição, o Claude verifica Node.js, FFmpeg, Python e HyperFrames e orienta a instalação do que faltar.
4. Escolha o formato e o visual no painel local do navegador. O painel só oferece formatos instalados e compatíveis com a orientação da gravação. Sem formato compatível, use **Do zero**.
5. Assista à montagem no HyperFrames Studio e peça ajustes pelo chat.
6. Diga **pode exportar** para gerar `edit/final.mp4`.

Arquivos próprios são opcionais: imagens em `imagens/`, clipes em `broll/`, roteiro na pasta do vídeo. Sem imagens ou clipes, a skill busca material conforme as regras de origem. Cortes de Vídeo Longo pede aprovação do ranking de trechos antes de editar. O documento da Aula em Tela Dividida fica mais fiel quando há roteiro.

## Verificação das entregas

No ambiente de desenvolvimento Windows com Python, Node, PowerShell e Git Bash, rode `python tests/verificar-entregas.py`. O teste gera e extrai os ZIPs em uma pasta temporária, instala cada pacote em perfis isolados, verifica backups e preferências e confere o catálogo pelo servidor local. O Bash é testado pelo Git Bash; esse teste não equivale a uma execução nativa no macOS.

## Problemas comuns

- **O comando não aparece:** feche e abra o Claude Code; confira se a skill existe em `~/.claude/skills/`.
- **Formato extra não aparece:** instale o ZIP do complemento depois do principal. Reinstalar só o principal não adiciona os extras.
- **Complemento pede o motor:** instale o pacote principal primeiro.
- **Gravação horizontal sem formatos disponíveis:** o principal tem seis formatos verticais. Use Do zero ou, se comprou o complemento, instale-o para obter YouTube, aulas e cortes.
- **PowerShell bloqueia scripts:** use o comando completo com `-ExecutionPolicy Bypass` acima.

### Enquadramento em todos os vídeos

A Máquina mantém o centro da cabeça da pessoa exatamente no centro horizontal da imagem ou da janela da câmera, em todos os formatos e estilos. Ajusta o enquadramento por tomada e durante movimentos, e verifica a centralização antes da revisão e na exportação final. Essa configuração é automática e também vale ao reutilizar preferências antigas.
