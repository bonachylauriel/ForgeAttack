
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(vulnerabilities, filename='report.pdf'):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)
    y = height - 40
    c.drawString(30, y, "Rapport de vulnérabilités")
    y -= 30
    for vuln in vulnerabilities:
        c.drawString(30, y, f"- {vuln}")
        y -= 20
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 40
    c.save()
