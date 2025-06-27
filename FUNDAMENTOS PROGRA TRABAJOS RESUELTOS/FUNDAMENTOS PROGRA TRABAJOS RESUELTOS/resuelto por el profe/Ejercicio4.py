tasa_aud_a_clp = 599   #1 Dolar Australiano equivale a $599 clp
tasa_arg_a_clp = 1     #1 Peso Argentino equivale a $1 clp
tasa_yen_a_clp = 6     #1 Yen equivale a $6 clp

monto = int(input("Ingrese Monto a convertir: "))
moneda = str(input("Ingrese Tipo de Moneda [Aud/Arg/Yen]: "))

def convertir_a_clp(monto, moneda):
    if moneda == "Aud":
        return monto * tasa_aud_a_clp
    elif moneda == "Arg":
        return monto * tasa_arg_a_clp
    elif moneda == "Yen":
        return monto * tasa_yen_a_clp
    else:
        return "Moneda no válida"


print(convertir_a_clp(monto,moneda))

'''print("AUD a CLP :",convertir_a_clp(100,"Aud"))
print("ARG a CLP :",convertir_a_clp(1000,"Arg"))
print("YEN a CLP :",convertir_a_clp(500,"Yen"))'''