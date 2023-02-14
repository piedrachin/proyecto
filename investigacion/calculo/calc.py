#from proyecto import PI   #aca importamos la constante PI creada en mi otra variable


def suma(num1, num2):# Esto me ayudara a realizar la suma entre dos numeros
    return num1 + num2

def area_circulo(radio):
    return radio*radio*PI

continuar= True  
while continuar:
   opcion=int(input("Que accion deseas realizar:\n"+"\n1. Sumar \t"+"\n2. Calcular Area Circulo \t"))
 
if(opcion==1): 
   print("Introdusca el valor del primer numero: ")
   num1=int(input())
   
   print("Introdusca el valor del segundo numero: ")
   num2=int(input()) 
   
   suma=num1+num2
   print(f"La suma de los dos numeros es: {str(suma)}")
      
elif(opcion==2): 
   print("Digite el numero perteneciente al radio: ")
   radio=int(input())
   area= radio*radio*PI
  
   print(f"El area del circulo es: {area}")
elif(opcion==3):
       print("Gracias....")
else:
       print("Opcion no encontrada, intente de nuevo.")  
            
if(opcion!=3):# a partir de este if, es para que me  vuelva a hacer la peticion al usuario
         respuesta=input("\nDesea volver al menu de opciones? "+"\n Si es si presione Y\" o y\""+"\n Si es no precione N\" o n\"")
         
         if (respuesta== 'Y' or respuesta== 'y'):
               pass
         #elif(respuesta=='N' or respuesta =='n'):
               
         else:
               continuar = False 
 
   
 