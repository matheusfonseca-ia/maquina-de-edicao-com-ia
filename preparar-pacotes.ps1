# Gera dois ZIPs de entrega contendo apenas as skills de cada compra.
param([string]$Saida = (Join-Path $PSScriptRoot 'dist'))
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
New-Item -ItemType Directory -Force -Path $Saida | Out-Null
$saidaResolvida = (Resolve-Path -LiteralPath $Saida).Path
$temporario = Join-Path ([IO.Path]::GetTempPath()) ('maquina-pacotes-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $temporario | Out-Null
try {
    foreach ($id in @('principal', 'order-bump')) {
        $fonte = $PSScriptRoot
        if ($id -eq 'order-bump') { $fonte = Join-Path $PSScriptRoot 'order-bump' }
        $manifesto = Get-Content -LiteralPath (Join-Path $fonte 'pacote.json') -Raw -Encoding UTF8 | ConvertFrom-Json
        $nome = "maquina-de-edicao-$id"
        $pasta = Join-Path $temporario $nome
        $skills = Join-Path $pasta '.claude/skills'
        New-Item -ItemType Directory -Force -Path $skills | Out-Null
        foreach ($skill in $manifesto.skills) {
            if ($skill -notmatch '^[a-z0-9]+(-[a-z0-9]+)*$') { throw "Nome de skill invalido: $skill" }
            $origem = Join-Path $fonte ".claude/skills/$skill"
            if (-not (Test-Path -LiteralPath (Join-Path $origem 'SKILL.md'))) { throw "Skill ausente: $skill" }
            Copy-Item -LiteralPath $origem -Destination (Join-Path $skills $skill) -Recurse
        }
        Copy-Item -LiteralPath (Join-Path $fonte 'pacote.json') -Destination $pasta
        foreach ($arquivo in @('instalar.ps1', 'instalar.sh')) {
            Copy-Item -LiteralPath (Join-Path $PSScriptRoot $arquivo) -Destination $pasta
        }
        Copy-Item -LiteralPath (Join-Path $fonte 'LEIA-ME.md') -Destination (Join-Path $pasta 'README.md')
        $zip = Join-Path $saidaResolvida "$nome.zip"
        if (Test-Path -LiteralPath $zip) { throw "Ja existe $zip. Use -Saida com outra pasta para gerar uma nova versao." }
        [IO.Compression.ZipFile]::CreateFromDirectory($pasta, $zip)
        Write-Host "Gerado: $zip ($($manifesto.skills.Count) skills)"
    }
} finally {
    $tempResolvido = [IO.Path]::GetFullPath($temporario)
    $tempRaiz = [IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd([IO.Path]::DirectorySeparatorChar) + [IO.Path]::DirectorySeparatorChar
    if ($tempResolvido.StartsWith($tempRaiz, [StringComparison]::OrdinalIgnoreCase) -and
        [IO.Path]::GetFileName($tempResolvido) -match '^maquina-pacotes-[a-f0-9]{32}$') {
        Remove-Item -LiteralPath $tempResolvido -Recurse -Force
    }
}
