# Máquina de Edição — 6 formatos extras

Este é o complemento da Máquina de Edição. **Instale o pacote principal primeiro.**

| Comando | Como fica |
|---|---|
| `/legenda-encaixada` | Tipografia animada com uma palavra gigante e a frase ao redor |
| `/nuvem-de-imagens` | Grupos de imagens acima da sua cabeça, com visual editorial |
| `/formato-ranking` | Tier list animada que se preenche com suas avaliações |
| `/cortes-de-video-longo` | Seleção e edição de cortes verticais a partir de vídeos longos |
| `/youtube-educativo` | Vídeo horizontal com cards, explicações e animações |
| `/aula-em-tela-dividida` | Você ao lado do documento da aula, com entrega em PDF |

## Instalar

Extraia este ZIP inteiro, incluindo a pasta `.claude`, e abra um terminal na pasta extraída.

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy Bypass -File .\instalar.ps1
```

Mac/Linux:

```bash
bash instalar.sh
```

Se o pacote principal ainda não estiver instalado, o instalador avisa e para antes de copiar qualquer skill. Este complemento adiciona somente as seis skills extras, sem substituir o motor nem os seis formatos da oferta principal. Versões anteriores das mesmas skills vão para backup; preferências e estilos pessoais são preservados.

Feche e abra o Claude Code. Na pasta de um vídeo, use `/maquina-de-edicao` ou um dos comandos acima. Os novos formatos aparecem no painel conforme a orientação da gravação. Todos usam os estilos visuais do pacote principal e os que você criou.

Para atualizar, baixe a nova versão deste complemento e rode o instalador novamente.
