arquivo = 'Projeto _ Relatório Automatizado.pdf'
titulo = 'EXEMPLO'

titulo_conteudo = 'Relatório'
subtitulo_conteudo = 'Gerando um teste para modelo de relatório'

conteudo_indice = [
    'Índice: ',
    '',
    '- Critério 1',
    '- Critério 2',
    '- Critério 3'
]

logo = 'apura.jpg'
##################################################

#tamanho do Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch, mm

#área de manipulação de imagem
from reportlab.pdfgen import canvas

pdf = canvas.Canvas(arquivo, pagesize=A4)
pdf.setTitle(titulo)
##################################################

#configurar fontes
print(pdf.getAvailableFonts())

# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont

# pdfmetrics.registerFont(
#     TTFont('OpenSans', 'OpenSans-Regular.ttf')
# )
# pdf.setFont('OpenSans', 36)
##################################################

#inserindo conteúdo
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
from reportlab.lib import colors

texto = pdf.beginText(2 * cm, 24 * cm)
texto.setFont('Courier', 12)
texto.setFillColor(colors.darkred)

for linha in conteudo_indice:
    texto.textLine(linha)

pdf.drawText(texto)
##################################################

#inserir imagens
pdf.drawImage(logo_apura, 2*cm, 10*cm, 17*cm, 9*cm)
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

# desenhar_regua(pdf, A4)
##################################################

#salvando o arquivo
pdf.save()
##################################################