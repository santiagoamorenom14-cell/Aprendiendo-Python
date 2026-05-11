
# Indice de masa corporal
peso = float(input("¿Cuál es tu peso? "))
estatura = float(input("¿cual es tu estatura?:"))
IMC = peso / (estatura **2)
if IMC >= 18.5 and IMC <= 25.9:
    print("Tu IMC es:", IMC, ". El paciente presenta una relación peso/estatura óptima")
else:
      print("Tu IMC es:", IMC, ". Fuera de parámetros normales. Es necesaria la supervisión de un profesional de la salud.")
