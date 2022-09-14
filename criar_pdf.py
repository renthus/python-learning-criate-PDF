from reportlab.lib.pagesizes import A4 # (210*mm,297*mm)
from reportlab.lib.units import cm, inch, mm #Padrão = Points
from reportlab.pdfgen import canvas # desenho do PDF
from reportlab.lib import colors #trabalhar com cores

#Criando o arquivo
arquivo = 'Projeto _ Relatório Automatizado.pdf'
titulo = 'EXEMPLO'
pdf = canvas.Canvas(arquivo, pagesize=A4)
pdf.setTitle(titulo)
##################################################

#inserindo conteúdo
titulo_conteudo = 'Esboço de Relatório'
subtitulo_conteudo = 'Gerando um teste para modelo de relatório'

pdf.setFont('Courier', 18)
pdf.drawCentredString((210*mm)/2, (28) * cm, titulo_conteudo)

pdf.setFillColorRGB(0, 0, 1.0)
pdf.setFont('Courier-Bold', 14)
pdf.drawString(2*cm, (26) * cm, subtitulo_conteudo)
##################################################

#criando linha
pdf.line(2 * cm, 25.5 * cm, 19 * cm, 25.5 * cm)
##################################################

#textos longos
conteudo_indice = [
    'Índice: ',
    '',
    '- Critério 1',
    '- Critério 2',
    '- Critério 3'
]

texto = pdf.beginText(2 * cm, 24 * cm)
texto.setFont('Courier', 12)
texto.setFillColor(colors.darkred)

for linha in conteudo_indice:
    texto.textLine(linha)

pdf.drawText(texto)
##################################################

#inserir imagens
logo = 'python.jpg'
pdf.drawImage(logo, 2*cm, 10*cm, 17*cm, 9*cm)
##################################################

#inserindo conteúdo na pagina 2
pdf.showPage()
pdf.setFont('Courier', 18)
pdf.drawCentredString((210*mm)/2, (28) * cm, titulo_conteudo)

pdf.setFillColorRGB(0, 0, 1.0)
pdf.setFont('Courier-Bold', 14)
pdf.drawString(2*cm, (26) * cm, subtitulo_conteudo)
##################################################

#criando linha
pdf.line(2 * cm, 25.5 * cm, 19 * cm, 25.5 * cm)
##################################################

#inserindo conteúdo na pagina 3
pdf.showPage()
pdf.setFont('Courier', 18)
pdf.drawCentredString((210*mm)/2, (28) * cm, titulo_conteudo)

pdf.setFillColorRGB(0, 0, 1.0)
pdf.setFont('Courier-Bold', 14)
pdf.drawString(2*cm, (26) * cm, subtitulo_conteudo)
##################################################

#criando linha
pdf.line(2 * cm, 25.5 * cm, 19 * cm, 25.5 * cm)
##################################################

#conversor de tamanhos
def mostrar_tamanho():
    print(f'1mm vale {mm} pontos')
    print(f'1cm vale {cm} pontos')
    print(f'1polegada vale {inch} pontos')

mostrar_tamanho()
##################################################

#desenhar uma regua
def desenhar_regua(pdf, pagina):
    pdf.setFontSize(8)
    pdf.setFillColor(colors.gray)
    pagina_y = int(pagina[1] / cm)
    pagina_x = int(pagina[0] / cm)

    for y in range(pagina_y):
        pdf.drawString(0 * cm, y * cm, f'y{y}')

    for x in range(pagina_x):
        pdf.drawString(x * cm, (pagina_y + 0.2) * cm, f'x{x}')

desenhar_regua(pdf, A4)
##################################################

#salvando o arquivo
pdf.save()
##################################################