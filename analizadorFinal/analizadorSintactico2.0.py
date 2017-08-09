from getpass import getpass
while (1):
    print ('Menu')
    print ('1.- Agregar una palabra')
    print ('2.- Validar una palabra definida')
    print ('3.- Imprimir archivo')
    print ('4.- Palabras reservadas')
    print ('5.- Operaciones')
    print ('6.- Salir')
    opcion=input('Elige una opcion\n')
    if opcion == '1':
        while (1):
            lineas = len(open('reservadas.csv').readlines())
            conteo=(int)(lineas)
            archivo2=open('reservadas.csv')
            # print(conteo)
            buscar=input('Ingresa la palabra que desee ingresar,si desea regresar solo presione enter:\n')
            buscar2=buscar+'\n'
            if buscar == "":
                break
            else:

                #le concateno un salto de linea porque se lee con uno integrado desde el archivo
                suma=0
                encontrado=0
                for i in range(0,conteo):
                    linea=archivo2.readline()
                    # linea1=(str)(linea)
                    if linea == buscar2:
                        encontrado=1
                    else:
                        cantidad=len(linea)
                        cantidad1=(int)(cantidad)
                        suma=suma+cantidad1
                        archivo2.seek(suma)

                if encontrado == 1:
                    print('La palabra '+buscar+' ya existe en palabras reservadas')
                    archivo2.close()


                else:
                    lineas = len(open('analizadorS.csv').readlines())
                    conteo=(int)(lineas)
                    archivo2=open('analizadorS.csv')
                    # print(conteo)
                    # buscar=input('Ingresa la palabra que desees agregar, si deseas salir presione enter:\n')
                    # buscar2=buscar+'\n'
                    #le concateno un salto de linea porque se lee con uno integrado desde el archivo
                    suma=0
                    encontrado=0
                    for i in range(0,conteo):
                        linea=archivo2.readline()
                        # linea1=(str)(linea)
                        if linea == buscar2:
                            encontrado=1
                        else:
                            cantidad=len(linea)
                            cantidad1=(int)(cantidad)
                            suma=suma+cantidad1
                            archivo2.seek(suma)

                    if encontrado == 1:
                        print('La palabra '+buscar+' ya existe')
                        break
                    else:
                        archivo=open('analizadorS.csv','a')
                        # archivo.write("numero")
                        # archivo.write("\n")
                        # archivo.write("formula")
                        # archivo.write("\n")
                        # archivo.write("coordenada")
                        # archivo.write("\n")
                        # archivo.write("parrafo")
                        # archivo.write("\n")
                        # archivo.write("Hombre")
                        # archivo.write("\n")
                        # archivo.write("Mujer")
                        # archivo.write("\n")
                        # archivo.write("Tecnologico")
                        # archivo.write("\n")
                        # archivo.write("HueTAMO")
                        # archivo.write("\n")
                        # archivo.write("Comunidad")
                        # archivo.write("\n")



                        # nuevaP=input('Ingresa la nueva palabra, si desea regresar solo presione enter \n')
                        if buscar == "":
                            print("")
                            break
                        else:
                            archivo.write(buscar)
                            archivo.write("\n")
                            archivo.close()
                            print("La palabra "+buscar+" se ha agregado exitosamente")
                            regre=input('¿Desea regresar? (si/no)\n')
                            if regre in ('s','Si','si','SI','sI'):
                                break

    elif opcion == '2':
        while(1):
            lineas = len(open('analizadorS.csv').readlines())
            conteo=(int)(lineas)
            archivo2=open('analizadorS.csv')
            # print(conteo)
            buscar=input('Ingresa la palabra que deseas validar:\n')
            if buscar == "":
                break
            else:
                buscar2=buscar+'\n'
                #le concateno un salto de linea porque se lee con uno integrado desde el archivo
                suma=0
                encontrado=0
                for i in range(0,conteo):
                    linea=archivo2.readline()
                    # linea1=(str)(linea)
                    if linea == buscar2:
                        print('si')
                        encontrado=1
                    else:
                        cantidad=len(linea)
                        cantidad1=(int)(cantidad)
                        suma=suma+cantidad1
                        archivo2.seek(suma)

                if encontrado == 1:
                    print('La palabra '+buscar+" esta escrita correctamente")
                else:
                    print('La palabra no esta escrita correctamente, intenta de nuevo')
            regreRes=input('¿Desea regresar al menu principal? (si/no)\n')
            if regreRes in ('s','Si','si','SI','sI'):
                break

    elif opcion == '3':
        archivoPaLeer=open('analizadorS.csv')
        print(archivoPaLeer.read())
        archivoPaLeer.close()
    elif opcion == '4':
        while(1):
            print("1.- Agregar palabra reservada")
            print("2.- Mostrar palabras reservadas")
            print("3.- Regresar")
            opcionRes=input("Elige una opcion \n")
            if opcionRes == '1':
                decremento=2
                for i in range(0,3):
                    print('Ingresa la contraseña\n')
                    password=getpass()
                    contraLeer=open('contra.csv')
                    contraLeer1=contraLeer.readline()
                    password=password+'\n'
                    if password == contraLeer1:
                        print('correcto')
                        fallo=0
                        break
                    else:
                        if decremento == 0:

                            fallo=1
                        else:
                            incremento=(str)(decremento)
                            print("Prueba otra vez, te quedan: "+incremento+" intentos")
                            decremento=decremento-1
                if fallo == 0:
                    lineas = len(open('reservadas.csv').readlines())
                    conteo=(int)(lineas)
                    archivo2=open('reservadas.csv')
                    # print(conteo)
                    buscar=input('Ingresa la palabra que desee ingresar,si desea regresar solo presione enter:\n')
                    buscar2=buscar+'\n'
                    if buscar == "":
                        break
                    else:

                        #le concateno un salto de linea porque se lee con uno integrado desde el archivo
                        suma=0
                        encontrado=0
                        for i in range(0,conteo):
                            linea=archivo2.readline()
                            # linea1=(str)(linea)
                            if linea == buscar2:
                                encontrado=1
                            else:
                                cantidad=len(linea)
                                cantidad1=(int)(cantidad)
                                suma=suma+cantidad1
                                archivo2.seek(suma)

                        if encontrado == 1:
                            print('La palabra '+buscar+' ya existe')
                            archivo2.close()
                            break

                        else:
                            archivo2.close()
                            lineas1 = len(open('analizadorS.csv').readlines())
                            conteo2=(int)(lineas1)
                            archivo3=open('analizadorS.csv')
                            # print(conteo)
                            buscar3=buscar+'\n'
                            #le concateno un salto de linea porque se lee con uno integrado desde el archivo
                            suma1=0
                            encontrado1=0
                            for i in range(0,conteo2):
                                linea1=archivo3.readline()
                                # linea1=(str)(linea)
                                if linea1 == buscar3:
                                    print('si')
                                    encontrado1=1
                                else:
                                    cantidad1=len(linea1)
                                    cantidad2=(int)(cantidad1)
                                    suma1=suma1+cantidad2
                                    archivo3.seek(suma1)

                            if encontrado1 == 1:
                                print('La palabra '+buscar+' ya existe en el archivo Analizador')
                                regreRes=input('¿Desea eliminar el dato del archivo del analizador? (si/no)\n')
                                if regreRes in ('s','Si','si','SI','sI'):
                                    f = open("analizadorS.csv","r")
                                    lineas4 = f.readlines()
                                    f.close()
                                    f = open("analizadorS.csv","w")
                                    for linea in lineas4:
                                        if linea!=buscar+"\n":
                                            f.write(linea)
                                    f.close()
                                    print('Dato eliminado')
                                else:
                                    break
                            else:
                                archivoRes=open('reservadas.csv','a')
                                archivoRes.write(buscar)
                                archivoRes.write("\n")
                                archivoRes.close()
                                print("La palabra "+buscar+" ha sido registrada exitosamente")
                                regreRes=input('¿Desea regresar al menu principal? (si/no)\n')
                                if regreRes in ('s','Si','si','SI','sI'):
                                    break
                else:
                    print('Ha superado el maximo de intentos, bye')
                    break
            elif opcionRes == '2':
                archivoPaLeerRes=open("reservadas.csv")
                print(archivoPaLeerRes.read())
                archivoPaLeerRes.close()
            elif opcionRes == '3':
                break
    elif opcion == '5':
        while(1):
            print('1.- Ayuda')
            print('2.- Realizar una operacion')
            print('3.- Regresar')
            opcionsita=input('Elige una opcion\n')
            if opcionsita == '1':
                while(1):
                    print('1.- Como operar una suma')
                    print('2.- Como operar una resta')
                    print('3.- Como operar una division')
                    print('4.- Como operar una multiplicacion')
                    print('5.- Regresar')
                    opcionsita2=input('Ingrese el numero de ayuda que desee obtener, presione enter para salir\n')
                    if opcionsita2 == "":
                        break
                    else:
                        if opcionsita2 == '1':
                            print('Para operar una operacion de suma, primero ingrese un valor, por ejemplo: 5, y despues ingrese el siguiente valor, por ejemplo: 4. El resultado se expresara al final en digitos')
                        elif opcionsita2 == '2':
                            print('Para operar una operacion de resta, primero ingrese un valor, por ejemplo: 5, y despues ingrese el siguiente valor, por ejemplo: 4. El resultado se expresara al final en digitos')
                        elif opcionsita2 == '3':
                            print('Para operar una operacion de division, primero ingrese un valor, por ejemplo: 5, y despues ingrese el siguiente valor, por ejemplo: 4. El resultado se expresara al final en digitos')
                        elif opcionsita2 == '4':
                            print('Para operar una operacion de multiplicacion, primero ingrese un valor, por ejemplo: 5, y despues ingrese el siguiente valor, por ejemplo: 4. El resultado se expresara al final en digitos')
                        elif opcionsita2 == '5':
                            break
            elif opcionsita == '2':
                lineas = len(open('reservadas.csv').readlines())
                conteo=(int)(lineas)
                archivo2=open('reservadas.csv')
                    # print(conteo)
                buscar=input("Ingrese la palabra reservada de operacion, presione enter para volver \n")
                if buscar == "":
                    print("")
                else:
                    buscar2=buscar+'\n'
                        #le concateno un salto de linea porque se lee con uno integrado desde el archivo
                    suma=0
                    encontrado=0
                    for i in range(0,conteo):
                        linea=archivo2.readline()
                            # linea1=(str)(linea)
                        if linea == buscar2:
                            encontrado=1
                        else:
                            cantidad=len(linea)
                            cantidad1=(int)(cantidad)
                            suma=suma+cantidad1
                            archivo2.seek(suma)

                    if encontrado == 1:
                        if buscar == 'suma':
                            numOp1=input("Ingrese el primer numero: \n")
                            numOp2=input("Ingrese el segundo numero: \n")
                            numSum=(int)(numOp1)
                            numSum2=(int)(numOp2)
                            resulSum=numSum + numSum2
                            resulSumaS=(str)(resulSum)
                            print("El resultado de tu operacion es: "+resulSumaS)
                        elif buscar == 'resta':
                            numOp1=input("Ingrese el primer numero: \n")
                            numOp2=input("Ingrese el segundo numero: \n")
                            numRes=(int)(numOp1)
                            numRes2=(int)(numOp2)
                            resulRes=numRes - numRes2
                            resulResS=(str)(resulRes)
                            print("El resultado de tu operacion es: "+resulResS)
                        elif buscar == 'multiplicacion':
                            numOp1=input("Ingrese el primer numero: \n")
                            numOp2=input("Ingrese el segundo numero: \n")
                            numRes=(int)(numOp1)
                            numRes2=(int)(numOp2)
                            resulRes=numRes * numRes2
                            resulResS=(str)(resulRes)
                            print("El resultado de tu operacion es: "+resulResS)
                        elif buscar == 'division':
                            numOp1=input("Ingrese el primer numero: \n")
                            numOp2=input("Ingrese el segundo numero: \n")
                            numRes=(int)(numOp1)
                            numRes2=(int)(numOp2)
                            resulRes=numRes / numRes2
                            resulResS=(str)(resulRes)
                            print("El resultado de tu operacion es: "+resulResS)
                        else:
                            print("La palabra "+buscar+" se encuentra registrada como una palabra reservada pero aun no tiene un tipo de operacion asignada")
                    else:
                        print('La palabra '+buscar+' no se reconoce como una palabra reservada')
                        archivo2.close()
                        break
            elif opcionsita == '3':
                break


    elif opcion == '6':
        break
