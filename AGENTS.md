# Repositório da Máquina de Edição

Este é o repositório de instalação da Máquina de Edição com IA e dos 12 estilos prontos. As skills ficam em `.claude/skills/`.

Se a pessoa abriu o Claude Code dentro desta pasta:

- Se ela quer **instalar** ou **atualizar**: rode o instalador (`powershell -ExecutionPolicy Bypass -File .\instalar.ps1` no Windows, `bash instalar.sh` no Mac/Linux). Antes de atualizar, rode `git pull`. Depois, avise que ela precisa fechar e abrir o Claude Code de novo.
- Se ela quer **editar um vídeo**: explique que o vídeo deve ficar numa pasta própria, fora deste repositório. Ela abre o Claude Code nessa pasta e digita `/maquina-de-edicao` ou o nome de um estilo. Se as skills ainda não estiverem instaladas (não existe `~/.claude/skills/maquina-de-edicao`), ofereça rodar o instalador primeiro.
- Se ela quer **ver os estilos**: mostre a tabela do `README.md`.

Não edite os arquivos das skills a pedido de "ajustar meu estilo": ajustes pessoais ficam salvos em `~/.maquina-de-edicao/preferencias.md` pela própria skill. Só edite o repositório se a pessoa disser claramente que quer mudar a skill pra todo mundo.
