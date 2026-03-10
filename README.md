# Automação de Download de Matérias Legislativas

## Descrição

Esta é uma aplicação desktop com interface gráfica (GUI) desenvolvida em Python para automatizar a busca, o download e a compilação de matérias legislativas do SAPL - Sistema de Apoio Legislativo da Câmara Municipal de Artur Nogueira. O projeto foi criado para resolver um problema real, eliminando um processo manual, demorado e sujeito a erros.

## Funcionalidades Principais

- **Interface Gráfica Intuitiva:** Permite que qualquer usuário filtre matérias por autor, ano e tipo.
- **Coleta de Dados Web:** Extrai informações diretamente do portal do SAPL.
- **Download em Lote:** Baixa todos os PDFs correspondentes à busca de forma automática.
- **Compilação de Relatórios:** Unifica centenas de arquivos PDF em um único documento final, organizado e pronto para uso.
- **Versão Portátil (.exe):** Empacotado para rodar nativamente no Windows sem necessidade de instalação do Python.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:**
  - **Pandas:** Para manipulação e filtragem dos dados.
  - **Requests:** Para a comunicação com a fonte de dados web.
  - **PyPDF2:** Para a fusão dos documentos PDF.
  - **CustomTkinter:** Para a criação da interface gráfica.
  - **PyInstaller:** Para compilação do executável final.

## Como Utilizar (Usuários Finais)

Para utilizar a ferramenta sem precisar configurar um ambiente de desenvolvimento:
1. Acesse a aba [Releases].
2. Faça o download do arquivo `Downloader_SAPL.exe`.
3. Dê um duplo clique para abrir a interface gráfica e começar a usar. Não é necessário instalar o Python.

## Como Executar o Projeto (Desenvolvedores)

1. Clone o repositório: `git clone https://github.com/ds-nava/downloader-sapl-artur-nogueira`
2. Navegue até a pasta do projeto: `cd downloader-sapl-artur-nogueira`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute a aplicação: `python guipdfsapl.py`

## Capturas de tela
<img width="617" height="393" alt="Interface de Seleção" src="https://github.com/user-attachments/assets/741a21df-84b9-4153-ae88-62a6b04f887a" />
<img width="618" height="389" alt="Processo de Download" src="https://github.com/user-attachments/assets/561d5994-9832-4510-bdff-22ec0a3c3c06" />