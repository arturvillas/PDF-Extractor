import os
from openpyxl import Workbook
import pdfplumber
import re
from datetime import datetime

def main():
    # Diretório dos PDFs
    directory = 'pdf_extrato'
    files = os.listdir(directory)
    if not files:
        raise Exception("No files found in the directory")

    # Criação do arquivo Excel
    wb = Workbook()
    ws = wb.active
    ws.title = 'Extract Imports'
    ws.append(['Invoice', 'Date', 'File Name', 'Status'])  # Cabeçalho

    for file in files:
        try:
            with pdfplumber.open(os.path.join(directory, file)) as pdf:
                first_page = pdf.pages[0]
                pdf_text = first_page.extract_text()

                # Regex para número da nota e data
                inv_number_re_pattern = r'INVOICE\s*#\s*(\d+)'
                inv_date_re_pattern = r'DATE:\s+(\d{2}/\d{2}/\d{4})'

                match_number = re.search(inv_number_re_pattern, pdf_text)
                match_date = re.search(inv_date_re_pattern, pdf_text)

                if not match_number:
                    raise Exception("Couldn't find invoice number")
                if not match_date:
                    raise Exception("Couldn't find invoice date")

                invoice_number = match_number.group(1)
                invoice_date = match_date.group(1)

                # Escreve no Excel
                ws.append([invoice_number, invoice_date, file, "Completed"])

        except Exception as e:
            print(f"Error processing file '{file}': {e}")
            ws.append(["N/A", "N/A", file, f"Exception: {e}"])

    # Salva planilha Excel
    now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    wb.save(f"Invoices - {now}.xlsx")

if __name__ == "__main__":
    main()
