
prendas = {
'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon',
True],
'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester',
True],
'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon',
True],
'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon',
False],
}

bodega = {
'S001': [7990, 12],
'S002': [19990, 0],
'S003': [29990, 3],
'S004': [24990, 6],
'S005': [17990, 8],
'S006': [14990, 2],
}

def leer_opcion():
    print("""
         ========== MENÚ PRINCIPAL ==========
        1. Unidades por categoría
        2. Búsqueda de prendas por rango de precio
        3. Actualizar precio de prenda
        4. Agregar prenda
        5. Eliminar prenda
        6. Salir
        =====================================
          """)
    try : 
        eleccion = int(input("seleccione un opcion del menu: "))
        if 1 <= eleccion <= 6:
            return eleccion
        else :
            print("seleccione un opcion del menu valido")

    except ValueError : 
        print("opcion no valido") 
        

def  unidades_categoria(categoria,prendas,bodega):
    total_unidad = 0
    for codigo,datos in prendas.items():
        if datos[0].lower() == categoria.lower():
            total_unidad += bodega[codigo][1]
    print(f"categoria seleccionado {categoria} : {total_unidad}")        




def busqueda_precio(precio_min, precio_max ,prendas,bodega):
    total_busqueda = []
    prendas_encuentrado = []
    for codigo,datos in prendas.items():
        precio,stock = prendas[codigo]
        if precio_min <= precio <= precio_max and stock > 0:
            print(f"nombre {datos[1]}--{codigo}")
            total_busqueda.append(prendas,bodega)
    print("")        



    if total_busqueda:
        total_busqueda.sort()
        for busqueda in total_busqueda:
            print(busqueda)  
        else :
            print("no hay prenda disponible")            

def buscar_codigo(codigo,prendas,bodega):
    return codigo.upper() in bodega

def actualizar_precio(codigo, nuevo_precio,prendas,bodega):
    if buscar_codigo(codigo):
        bodega[codigo] =[nuevo_precio,bodega[codigo][1]]
        return True
    else :
        return False
    
    
def validar_codigo(codigo,prendas,bodegas):
    return codigo.strip() != "" and not buscar_codigo()
def validar_nombre(nombre,prendas,bodega):
    return nombre.strip() != "" 
def validar_categoria(categoria,prendas,bodega):
    return categoria.strip != ""
def validar_talla(talla,prendas,bodega):
    return talla.strip() != ""
def validar_color(color,prendas,bodega):
    return color.strip() != ""
def validar_material(material,prendas,bodega):
    return material.strip() != ""
def validar_es_unisex(es_unisex,prendas,bodega):
    return es_unisex.lower() in ["s","n"]
def validar_precio(precio,prendas,bodega):
    try:
        precio = int(precio)
        return precio > 0
    except ValueError:
        return False 
        
def validar_stock(stock,prendas,bodega):
    try:
        unidad = int(unidad)
        return stock > 0
    except ValueError:
        return False
    
def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades, prendas,bodega):
    if buscar_codigo(codigo):
        return False
    prendas[codigo] = [nombre, categoria, talla, color, material, es_unisex] 
    bodega [codigo] = [precio,unidades]
    return True

def eliminar_prenda(codigo,prendas,bodega):
    if buscar_codigo(codigo):
        del prendas[codigo]
        del bodega[codigo]
        return True
    else:
        return False

while True:
    opc = leer_opcion()
    if opc == 1:
        categoria = input("ingrese un nombre de la categoria: ")
        unidades_categoria(categoria,prendas,bodega)
    elif opc == 2:
        while True:
            try :
                precio_min = int(input("ingrese el precio minimo: "))
                precio_max = int(input("ingrese el precio maximo: "))
                if precio_min < 0 or precio_max < 0 or precio_max > precio_max:
                    print ("Debe ingresar valores enteros")
                else :
                  busqueda_precio(precio_min,precio_max,prendas,bodega)
                  break
            except ValueError :
                print("ingrese un opcion valido")

    elif opc == 3:
        while True:
            try:
               codigo = input("ingrese prenda que deseas: ")
               if not buscar_codigo(codigo)
               else :
                   nuevo_codigo = int(input("ingrese la nueva prenda que deseas: "))
                   if nuevo_codigo < 0:
                       print("debes ingresesar un numero positivo")
                   else :
                       if actualizar_precio(codigo,prendas,bodega):
                        print("Precio actualizado")
                       else :
                           print("El código no existe")
               pregunta = input("¿Desea actualizar otro precio (s/n)?")  
               if pregunta.lower() != "s":  
                   print() 
            except ValueError:
                print("ingrese un opcion valido")


