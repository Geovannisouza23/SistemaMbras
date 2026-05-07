# Sistema de Consulta IPTU (Automacao)

Este projeto automatiza a consulta de proprietario no portal da Prefeitura de Sao Paulo usando Selenium e preenche o resultado em uma planilha Excel.

## Requisitos

- Python 3
- Google Chrome instalado
- Opcional: `make` (apenas para macOS/Linux ou quem preferir usar Makefile)

## Instalar make

Se o comando `make` nao estiver disponivel, instale com um dos comandos abaixo:

### macOS

```bash
xcode-select --install
```

### Ubuntu/Debian

```bash
sudo apt update && sudo apt install -y make
```

### Fedora

```bash
sudo dnf install -y make
```

### Windows (Chocolatey)

```powershell
choco install make
```

## Estrutura

- `iptu - Copia.py`: script principal de automacao
- `Makefile`: comandos para preparar ambiente, instalar dependencias e executar
- `setup_windows.bat`: prepara ambiente no Windows sem `make`
- `run_windows.bat`: executa o sistema no Windows sem IDE

## Uso rapido no Windows (sem IDE)

1. Abra o Prompt de Comando (cmd).
2. Entre na pasta do projeto.
3. Execute o setup:

```bat
setup_windows.bat
```

4. Coloque o arquivo `dados_extraidos.xlsx` na raiz do projeto.
5. Execute:

```bat
run_windows.bat
```

Tambem funciona com duplo clique:

- primeiro em `setup_windows.bat`
- depois em `run_windows.bat`

## Como usar

1. No terminal, entre na pasta do projeto.
2. Execute:

```bash
make setup
```

Esse comando:

- cria a virtualenv (`.venv`) se necessario
- atualiza o `pip`
- instala as dependencias (`selenium` e `openpyxl`)

3. Rode o sistema:

```bash
make run
```

## Alvos do Makefile

- `make help`: lista os comandos disponiveis
- `make setup`: cria ambiente e instala dependencias
- `make install`: instala/atualiza dependencias
- `make run`: executa o script principal
- `make clean`: remove a pasta `.venv`

## Arquivos de entrada e saida

- Entrada esperada: `dados_extraidos.xlsx`
- Saida gerada: `dados_extraidos_IPTU.xlsx`

## Fluxo da automacao

1. Abre o navegador no portal da Prefeitura
2. Aguarda login manual
3. Le os imoveis da planilha
4. Consulta cada cadastro
5. Preenche a coluna de proprietario
6. Salva a planilha final

## Problemas comuns

- Erro de dependencia faltando:
  - No Windows: rode `setup_windows.bat` novamente.
  - Em macOS/Linux: rode `make setup` novamente.
- Erro de navegador/ChromeDriver:
  - Feche janelas antigas do Chrome e rode `run_windows.bat` (Windows) ou `make run` (macOS/Linux).
- Arquivo de entrada nao encontrado:
  - Verifique se `dados_extraidos.xlsx` esta na raiz do projeto.
# SistemaMbras
