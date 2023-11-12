from pypdf import PdfMerger

try:
    num_pdfs = int(input("Enter the number of PDFs to merge: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

pdfs = []
for i in range(num_pdfs):
    pdf_name = input(f"Enter the name of PDF {i + 1} (.pdf): ")
    pdfs.append(pdf_name)

merger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)


output_pdf_name = input("Enter the name of the output PDF file: ")
merger.write(output_pdf_name)
merger.close()

print(f"Merged PDF saved as {output_pdf_name}")


