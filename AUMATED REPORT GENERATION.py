import csv
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def read_data(file_path):
    with open(file_path, newline='') as txtfile:
        reader = csv.reader(txtfile)
        data = list(reader)
        return data

def generate_pdf_report(data, output_filename):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(output_filename, pagesize=LETTER)
    elements = []
    # Title
    elements.append(Paragraph("Automated Report", styles['Title']))
    elements.append(Spacer(1, 20))
    # Table
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)
    elements.append(table)
    doc.build(elements)

if __name__ == "__main__":
    # Step 1: Read the data from Task2.txt
    data = read_data('C:\\Users\\admin\\Task2.txt')
    # Step 2: Generate the PDF report
    generate_pdf_report(data, 'C:\\Users\\admin\\sample_report.pdf')
    print("Report generated: sample_report.pdf")
