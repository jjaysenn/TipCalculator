#Tip Calculator

print("Bienvenidos a la calculadora de propinas")

total = float(input("Digite el total de la factura con el impuesto incluido: "))

porciento = float(input("Cuanto porciento de propina desea dejar: "))

personas = int(input("Digite entre cuantas personas quiere dividir la factura: "))

porciento_total = total * porciento

total_final = total + porciento_total

total_por_persona = total_final / personas

print(f"Total = ${total}\nPropina Porciento = % {round(porciento,2)}\nTotal Final = ${round(total_final,2)}\nPersonas a pagar = {personas}\nPago por Persona = ${round(total_por_persona,2)}")