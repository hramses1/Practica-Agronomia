print("-------------Variables------------");
Lv_Nombre='';
print("Hola, ingrese su nombre:")
Lv_Nombre= input();
print("Gusto en conocerte, "+ Lv_Nombre);
print("Hola, ingrese su apellido:")
Lv_Apellido= input();
print(f"Gusto en conocerte,{ Lv_Apellido}");
Lv_Usuario= input("Ingrese su Usuario:")
print(f"Ingreso exitoso,{Lv_Usuario}");
print("-------------------------");
print("-------------------------");
print("------------Funciones-------------");
Lst_Temp1=['Lunes','Martes','Miercoles','Jueves','Perro'];
print(Lst_Temp1);
print("-------------------------");
Lst_Temp1.remove('Perro');
print(Lst_Temp1);
print("-------------------------");
Lst_Temp1.append('Viernes');
Lst_Temp1.append('Viernes');
Lst_Temp1.append('Viernes');
Lst_Temp1.append('Viernes');
print(Lst_Temp1);
print("-------------------------");
Lst_Temp1.remove('Viernes');
print(Lst_Temp1);
print("-------------------------");
Lst_Temp2=['Luis','Marco','Pedro','Juan','Jose'];
Lst_Temp2.sort();
Lst_Temp2.pop();
print(Lst_Temp2);
print("-------------------------");
if 'Luan' in Lst_Temp2:
    print("Si existe Luan");
elif 'Juan' in Lst_Temp2:
    print("Si existe Juan");
else:
    print("No existe los nombres buscados");
print("-------------------------");