# Instala a Maquina de Edicao e os 12 formatos prontos no Claude Code (Windows).
# Uso, dentro da pasta do repositorio:
#   powershell -ExecutionPolicy Bypass -File .\instalar.ps1
#
# Copia cada pasta de .claude\skills\ deste repositorio para %USERPROFILE%\.claude\skills\.
# Se ja existir uma skill com o mesmo nome, a versao antiga vai para
# %USERPROFILE%\.claude\skills-backup\<data>\ antes de ser substituida.
# Suas preferencias e estilos salvos (%USERPROFILE%\.maquina-de-edicao\) nao sao tocados.

$ErrorActionPreference = 'Stop'

$origem = Join-Path $PSScriptRoot '.claude\skills'
$destino = Join-Path $env:USERPROFILE '.claude\skills'
$carimbo = Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'
$backup = Join-Path $env:USERPROFILE ".claude\skills-backup\$carimbo"

if (-not (Test-Path $origem)) {
    Write-Host "Nao achei a pasta .claude\skills ao lado deste script. Rode o instalador de dentro da pasta do repositorio." -ForegroundColor Red
    exit 1
}

New-Item -ItemType Directory -Force -Path $destino | Out-Null

$skills = Get-ChildItem -Path $origem -Directory
$fezBackup = $false

foreach ($skill in $skills) {
    $alvo = Join-Path $destino $skill.Name
    if (Test-Path $alvo) {
        New-Item -ItemType Directory -Force -Path $backup | Out-Null
        Move-Item -Path $alvo -Destination (Join-Path $backup $skill.Name)
        $fezBackup = $true
    }
    Copy-Item -Path $skill.FullName -Destination $alvo -Recurse
    Write-Host "  ok  /$($skill.Name)"
}

Write-Host ""
Write-Host "Pronto! $($skills.Count) skills instaladas em $destino" -ForegroundColor Green
if ($fezBackup) {
    Write-Host "As versoes antigas foram guardadas em $backup"
}
Write-Host ""
Write-Host "Feche e abra o Claude Code de novo. Depois, na pasta do seu video, digite:"
Write-Host "  /maquina-de-edicao      (escolhe entre editar do zero ou com um formato pronto)"
Write-Host "  /reels-de-negocio       (ou o nome de qualquer formato, pra ir direto)"
