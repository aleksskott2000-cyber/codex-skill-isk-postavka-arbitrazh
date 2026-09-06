# Установка скилла на другом компьютере

## Требования

- установлен Codex;
- установлен Git или GitHub CLI;
- у пользователя есть доступ к приватному репозиторию;
- для визуальной проверки DOCX установлен LibreOffice либо Microsoft Word на Windows.

## Windows PowerShell с GitHub CLI

```powershell
gh auth login
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex\skills' }
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
gh repo clone aleksskott2000-cyber/codex-skill-isk-postavka-arbitrazh (Join-Path $skillRoot 'isk-postavka-arbitrazh')
```

## Windows PowerShell с Git

```powershell
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex\skills' }
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
git clone https://github.com/aleksskott2000-cyber/codex-skill-isk-postavka-arbitrazh.git (Join-Path $skillRoot 'isk-postavka-arbitrazh')
```

Для приватного репозитория Git запросит авторизацию. Не вставляйте токен в команду или URL; используйте менеджер учетных данных Git либо GitHub CLI.

## macOS или Linux

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
gh auth login
gh repo clone aleksskott2000-cyber/codex-skill-isk-postavka-arbitrazh "${CODEX_HOME:-$HOME/.codex}/skills/isk-postavka-arbitrazh"
```

После установки перезапустите Codex. Скилл можно вызвать явно:

```text
$isk-postavka-arbitrazh Подготовь иск по документам в папке <путь к делу>.
```

Обычные запросы о подготовке иска по поставке также могут подключать скилл автоматически.
