def mostrarVogal(string, vogal): 
    vogais = [cada for cada in string if cada in vogal] 
    print(len(vogais)) 
    print(vogais)
    
vogais = "AEIOUaeiou"     
string = "palavrA de ExemplO"
mostrarVogal(string, vogais)