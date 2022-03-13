def Fnc_Calculo(In_Valor1,In_Valor2,Iv_proceso):
    if (Iv_proceso=="1"):
        print(In_Valor1 + In_Valor2);
    elif (Iv_proceso=="2"):
        print(In_Valor1 + In_Valor2);
    elif (Iv_proceso=="3"):
        print(In_Valor1 + In_Valor2);
    else:
        print(In_Valor1 / In_Valor2);

Ln_Valor1 = int(input("Ingrese valor #1:"));
Ln_Valor2 = int(input("Ingrese valor #2:"));
print("¿Que calculo desea realizar?");
print ("1.-Suma");
print ("2.-Resta");
print ("3.-Multiplicacion");
print ("4.-Divicion");
Lv_Proceso = (input("Digite su opcion:"));
Fnc_Calculo(Ln_Valor1, Ln_Valor2, Lv_Proceso)