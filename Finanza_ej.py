capital = float(input("Escribe el capital inicial: "))
interes = float(input("Escribe la tasa de interés anual: "))
inflacion = float(input("Escribe la inflación anual : "))
años = int(input("Escribe la cantidad de años a simular: "))
for año in range(1, años + 1):
    
    ganancia = capital * interes 
    
    
    nuevo_capital = capital + ganancia
    
    
    perdida_inflacion = nuevo_capital * inflacion
    
    
    capital_Definitivo = nuevo_capital - perdida_inflacion
    
   
    capital = capital_Definitivo
    
    
    print("En el año", año, "tu capital real es:", capital)
