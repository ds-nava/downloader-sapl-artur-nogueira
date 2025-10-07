# Automação de Relatórios Legislativos

# Descrição

Esta é uma aplicação desktop com interface gráfica (GUI) desenvolvida em Python para automatizar a busca, o download e a compilação de matérias legislativas do SAPL - Sistema de Apoio Legislativo da Câmara Municipal de Artur Nogueira. O projeto foi criado para resolver um problema real, eliminando um processo manual, demorado e sujeito a erros.

# Funcionalidades Principais

- **Interface Gráfica Intuitiva:** Permite que qualquer usuário filtre matérias por autor, ano e tipo.
- **Coleta de Dados Web:** Extrai informações diretamente do portal do SAPL.
- **Download em Lote:** Baixa todos os PDFs correspondentes à busca de forma automática.
- **Compilação de Relatórios:** Unifica centenas de arquivos PDF em um único documento final, organizado e pronto para uso.

# Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:**
  - **Pandas:** Para manipulação e filtragem dos dados.
  - **Requests:** Para a comunicação com a fonte de dados web.
  - **PyPDF2:** Para a fusão dos documentos PDF.
  - **CustomTkinter:** Para a criação da interface gráfica.

# Como Executar o Projeto

1.  Clone o repositório: `git clone https://github.com/ds-nava/downloader-sapl-artur-nogueira`
2.  Navegue até a pasta do projeto: `cd [nome-da-pasta]`
3.  Instale as dependências: `pip install -r requirements.txt`
4.  Execute a aplicação: `guipdfsapl.py`
