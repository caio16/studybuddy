from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER


# Função para gerar o PDF
def generate_pdf(final_sum_of_time, file_name):
    # Estilos
    styles = getSampleStyleSheet()
    style_normal = styles["Normal"]
    style_normal.alignment = TA_CENTER  # Adicionando alinhamento central

    # Estilo para a matéria em negrito
    style_subject = ParagraphStyle(
        name='BoldSubject',
        parent=style_normal,
        fontName='Helvetica-Bold',
    )
    pdf_filename = file_name
    # Criar um PDF
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    elements = []

    # Adicionar título
    title_text = "<b>Cronograma de Estudos</b>"
    elements.append(Paragraph(title_text, styles['Title']))
    elements.append(Spacer(1, 24))

    # Adicionar texto centralizado
    text_centered = "Para saber mais sobre seus estudos, consulte a parte de 'Rendimento' no início do programa. <br/>"
    elements.append(Paragraph(text_centered, style_normal))  # Não é mais necessário especificar alignment
    elements.append(Spacer(1, 12))

    # Adicionar os dados ao PDF
    for subject, time in final_sum_of_time:
        subject_text = f"<b>Recomendação:</b> {time} horas semanais"
        recommendation_text = f"{subject}"

        # Adicionar a recomendação e a matéria ao PDF
        elements.append(Paragraph(recommendation_text, style_subject))
        elements.append(Paragraph(subject_text, style_normal))
        elements.append(Spacer(1, 12))



    # Construir o PDF
    doc.build(elements)

    print(f"PDF gerado com sucesso: {file_name}")
