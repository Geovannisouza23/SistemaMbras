# Sistema de Consulta IPTU (Automacao)

Este projeto automatiza a consulta de proprietario no portal da Prefeitura de Sao Paulo usando Selenium e preenche o resultado em uma planilha Excel.

## Requisitos

- macOS, Linux ou Windows com `make` instalado
- Python 3
- Google Chrome instalado

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
  - Rode `make setup` novamente.
- Erro de navegador/ChromeDriver:
  - Feche janelas antigas do Chrome e rode `make run` outra vez.
- Arquivo de entrada nao encontrado:
  - Verifique se `dados_extraidos.xlsx` esta na raiz do projeto.
# SistemaMbras
