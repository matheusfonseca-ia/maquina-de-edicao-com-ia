# Repositório da Máquina de Edição

Fonte de instalação da Máquina de Edição com IA. Cada um dos 12 formatos tem sua skill própria. A oferta principal inclui seis formatos em `.claude/skills/`, junto do motor. Os outros seis ficam em `order-bump/.claude/skills/` e são entregues em um ZIP separado. A divisão completa e o critério de seleção estão no `README.md`; os manifestos `pacote.json` de cada pacote definem quais skills entram na instalação.

Os estilos visuais (Pixelado, Noite Laranja, Claro Tecnológico) continuam incluídos no principal, em `.claude/skills/maquina-de-edicao/estilos-visuais/`. Para criar outro, use `_modelo.md` dessa pasta.

Se a pessoa abriu o Claude Code dentro desta pasta:

- **Instalar ou atualizar:** rode o instalador do pacote recebido (`powershell -ExecutionPolicy Bypass -File .\instalar.ps1` no Windows, `bash instalar.sh` no Mac/Linux). No repositório de desenvolvimento, o padrão instala somente o principal; para adicionar os extras, use `-Pacote order-bump` ou `bash instalar.sh order-bump`. O complemento requer o motor já instalado. Depois, peça para fechar e abrir o Claude Code. Alunos atualizam baixando o novo ZIP do pacote comprado; no repositório de desenvolvimento, use `git pull` antes de atualizar.
- **Gerar entregas:** rode `preparar-pacotes.ps1`. Entregue o ZIP principal na compra principal e o ZIP do complemento apenas a quem comprou o order bump. Não distribua o repositório completo como download do principal, pois ele contém os dois pacotes.
- **Editar vídeo:** a gravação deve ficar numa pasta própria, fora deste repositório. A pessoa abre o Claude Code nessa pasta e digita `/maquina-de-edicao` ou o comando de um formato instalado. Se não houver `~/.claude/skills/maquina-de-edicao/SKILL.md`, ofereça instalar primeiro o principal.
- **Ver formatos ou estilos visuais:** consulte o README e mostre os formatos do pacote instalado. A ausência dos seis extras é esperada sem o complemento; não é erro de instalação.

Não edite as skills a pedido de "ajustar meu estilo": ajustes pessoais ficam em `~/.maquina-de-edicao/preferencias.md`. Só altere o repositório quando a pessoa disser que quer mudar a skill para todo mundo.
