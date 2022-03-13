#File.
f = open ("PrimerFile.txt",'w');
try:
    f.write ("Esta es mi primera linea en la file \n ");
    f.write ("Esta es mi segunda linea en la file \n ");
    f.write ("Esta es mi tercera linea en la file \n ");
    f.write ("Esta es mi cuarta linea en la file \n ");
    f.write ("Total de linea escritas 4 \n ");
finally:
    f.close();
#leer
f = open ("PrimerFile.txt",'r');
Lv_Mensaje = f.read();
print(Lv_Mensaje);
f.close();
#Agregar
f = open ("PrimerFile.txt",'a');
f.write ("Esta es una linea nueva, osea en la linia 5");
f.close();
#leer
f = open ("PrimerFile.txt",'r');
Lv_Mensaje = f.read();
print(Lv_Mensaje);
f.close();