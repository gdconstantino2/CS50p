months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

while True:
    try:
        x = input("Date: ")
        x = x.strip()
        if(x[0].isnumeric()):
             mes, dia, ano = x.split("/")
             if (int(mes) > 12) or (int(dia) > 31):
                 pass
             elif (mes.isnumeric()) and (dia.isnumeric()):
                ano_n= ano
                dia_n = dia
                mes_n = mes
                print(f"{ano_n}-{int(mes_n):02}-{int(dia_n):02}")
                break
        elif(x[0].isalpha()) and ("," in x):
            escrito = x.replace("," , "")
            mes_e, dia_e, ano_e = escrito.split(" ")
            if (dia_e.isnumeric()) and (mes_e.isalpha()) and (int(dia_e) < 32):
                novo_mes = 0
                for i in months:
                    if i == mes_e.lower():
                        novo_mes = months.index(mes_e.lower())
                        novo_mes = int(novo_mes) + 1
                        print(f"{ano_e}-{int(novo_mes):02}-{int(dia_e):02}")
                break
    except (SyntaxError, ValueError):
        pass
