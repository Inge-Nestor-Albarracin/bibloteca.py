libros=[] #Lista que almacenara los libros
usuarios=[]
contadoridlibros=0 #nuestas id autoincrement
contadoridusuarios=0

def menu():
    
    def registarlibro(): #Nuestro registro de libros
        print("Entiendo vamos a registar un libro")
        
       
        while True: #se mantendra hasta nuestro break
            ingresplibros={} # el diccionario vacio que almacenara todos los libros dentro del while para reiniciarlo cada iteracion
            ingresplibros["titulo"]=input("Ingrese un titulo o escriba salir para salir: ")

            if ingresplibros["titulo"].lower()=="salir": #Validacion del break
                break
            
            elif ingresplibros["titulo"]=="": #verifica que no este vacio
                print("Ingrese UN TITULO")
            else:
                ingresplibros["autor"]=input("Ingrese un autor o escriba salir para salir: ")
                if ingresplibros["autor"].lower()=="salir":
                    break
                elif ingresplibros["autor"]=="": #verifica que no este vacio
                    print("ingrese un AUTOR valido")
                else:
                    ingresplibros["genero"]=input("Ingrese el genero del su libro o escriba salir: ")
                    if ingresplibros["genero"].lower()=="salir":
                        break
                    elif ingresplibros["genero"]=="": #verifica que no este vacio
                        print("Ingrese un autor valido")
                    else:
                        global contadoridlibros #solucionamos bug pues asi la volvemos una variable global y no solo local
                        contadoridlibros+=1 #añadimos 1 al id
                        ingresplibros["id"]=contadoridlibros #nuesto id sera el numero del contador de libros
                        ingresplibros["disponible"]=True
                        libros.append(ingresplibros) #agregamos este diccionario a la lista 

    def registrarusuario():
        print("Entendido vamos a registrar un usuario")

        while True:
            ingresousuarios={}  # el diccionario vacio que almacenara todos los usuarios dentro del while para reiniciarlo cada iteracion
            ingresousuarios["nombre"]=input("Ingrese un nombre o escriba salir para salir: ")
            
            if ingresousuarios["nombre"].lower()=="salir":
                break
            elif ingresousuarios["nombre"]=="":
                print("Ingrese un nombre valido")
            else:
                ingresousuarios["email"]=input("Ingrese un email o escriba salir para salir:")
                if ingresousuarios["email"].lower=="salir":
                    break
                elif ingresousuarios["email"]=="":
                    print("Ingrese un correo valido")
                
                else:
                    global contadoridusuarios #solucionamos bug pues asi la volvemos una variable global y no solo local
                    contadoridusuarios+=1
                    ingresousuarios["id"]=contadoridusuarios
                    usuarios.append(ingresousuarios)

            
             
            




    while True: #para romper con un break
        
        print("Bienvenido a tu bibloteca de confianza Bibloteca.py")
        print("------------------------------------")
        print("Selecione una opcion para empezar")
        print("1 para registar un libro")
        print("2 para registar un usuario")
        print("3 para pedir prestado un libro")
        print("4 para devolver un libro")
        print("5 para ver los reportes de los libros")
        print("6 para salir")
        
        opcion=int(input("Digite una opcion: ")) #Variable opcion
        print("----------------------------------------")
        if opcion==1:
            registarlibro()
            print(libros)
        elif opcion==2:
            registrarusuario()
            print(usuarios)
        else:
            print("si")

menu()
