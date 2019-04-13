altura = int(input("Qual a altura da piramide?"))
underlines = int((((1 + ((altura - 1) * 2))-1)/2)) * '_'
count = 1
while count <= altura:
    print(underlines + ((1 + ((count - 1) * 2))* '*') + underlines)
    underlines = underlines.replace('_','',1)
    count += 1