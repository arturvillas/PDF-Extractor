# 🧾 Extrator de Dados de Notas Fiscais em PDF para Excel

Este projeto em **Python** foi desenvolvido para **automatizar a extração de dados** de notas fiscais armazenadas em arquivos PDF, organizando as informações em uma **planilha Excel** de forma prática e rápida.

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- [pdfplumber](https://github.com/jsvine/pdfplumber) – Extração de texto de PDFs
- [openpyxl](https://openpyxl.readthedocs.io/) – Criação e manipulação de planilhas Excel
- **Regex** – Expressões regulares para identificação dos dados
- **datetime** – Geração de nome dinâmico do arquivo de saída

## 📁 Estrutura esperada

Crie uma pasta chamada `pdf_extrato` no mesmo diretório do script e coloque dentro dela todos os arquivos PDF que deseja processar.

seu_projeto/
│
├── pdf_extrato/
│ ├── invoice1.pdf
│ ├── invoice2.pdf
│ └── ...
│
├── extrator.py



## ▶️ Como utilizar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
Instale as dependências:


pip install pdfplumber openpyxl
Execute o script:


python extrator.py
Ao final da execução, um novo arquivo .xlsx será gerado com os dados extraídos, contendo as colunas:

Invoice (número da nota)

Date (data da emissão)

File Name (nome do PDF)

Status (sucesso ou erro no processamento)

📌 Observações
O script procura na primeira página de cada PDF pelos padrões:

INVOICE # <número>

DATE: <data no formato DD/MM/AAAA>

Se os padrões não forem encontrados, o PDF será listado com status de erro na planilha final.

Ideal para automatizar o controle de documentos fiscais de forma simples.
