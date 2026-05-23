capital = 1000
interes = 0.10
inflacion = 0.04
años = 5

# Aquí abrimos la "caja" del ciclo for
for año in range(1, años + 1):
    
    ganancia = capital * interes 
    
    
    nuevo_capital = capital + ganancia
    
    
    perdida_inflacion = nuevo_capital * inflacion
    
    
    capital_Definitivo = nuevo_capital - perdida_inflacion
    
   
    capital = capital_Definitivo
    
    
    print("En el año", año, "tu capital real es:", capital)
