#!/usr/bin/env python
# -*- coding: utf-8 -*
# Python Version: 3.7.4

import os

from src.formulario import Formulario
from src.gestionar import*
from src.muestra import crear_muestra

class Aplicacion(Frame):
    """
    La clase genera una ventana principal donde se pueden explorar los datos de las tasaciones
    cargadas en la bd definida.
    """

    def __init__(self, parent = None, directorio_img = None):
        super().__init__(parent)
        self.parent = parent
        self.directorio_img = directorio_img
        self.__configure()
        self.__create_style()
        self.__create_widgets()

    # ==============================================================================================
    # CONFIGURACIÓN DE LOS WIDGETS
    # ==============================================================================================
    
    def __configure(self):
        """
        Se establecen las configuraciones de la ventana emergente.
        """
        self.parent.title("Explorador de Tasaciones")
        self.parent.geometry("1024x710")
        self.parent.resizable(False, False)
    
    def __create_style(self):
        """
        Se establecen las configuraciones de estilo de los widgets de la libraría ttk.
        """
        self.style = Style()
        self.style.configure("area_imagen.TFrame", relief="sunken")
        self.style.configure("tabla.Treeview", rowheight = 24)
    
    def __create_widgets(self):
        """
        Se crean los widgets de la clase.
        """
        # CONTENEDOR PRINCIPAL 
        # ------------------------------------------------------------------------------------------
        self.contenedor = Frame(self.parent, style = "test.TFrame")
        self.contenedor.pack(expand="yes", fill=BOTH)
        
        # SECCIONES PRINCIPALES
        # ------------------------------------------------------------------------------------------
        # Sección de áreas de datos
        self.seccion_datos = Frame(self.contenedor,style = "test.TFrame")
        self.seccion_datos.pack(side=TOP, expand="yes", fill=BOTH, padx= 0, pady= 0)

        # Sección de botones
        self.seccion_botones = Frame(self.contenedor)
        self.seccion_botones.pack(side = TOP, expand = "yes", fill = BOTH, padx = 10, pady = 10)

        # ÁREA IMÁGEN
        # ------------------------------------------------------------------------------------------
        # Contenedor del área
        self.area_imagen = Frame(self.seccion_datos, style = "area_imagen.TFrame")
        self.area_imagen.grid(row = 0, column = 1, padx = 10, pady =  10, sticky= N )
        
        # Canvas
        self.canvas_app = Canvas(self.area_imagen, bg= "#BBDEFB", width = 330, height = 200)
        self.canvas_app.pack(side = "top") 
        self.canvas_ant = Button(self.area_imagen, text = '<<', command = lambda: self.anterior())
        self.canvas_ant.pack(side = LEFT)
        self.canvas_sig = Button(self.area_imagen, text = '>>', command = lambda: self.siguiente())
        self.canvas_sig.pack(side = RIGHT)
        
        # ÁREA BUSCAR / FILTRAR
        # ------------------------------------------------------------------------------------------
        # Contenedor del área
        self.area_buscar =Frame(self.seccion_datos)
        self.area_buscar.grid(row = 0, column = 2, padx = 10, pady = 0, sticky = W)
        
        # Labelframe
        self.marco_buscar = LabelFrame(self.area_buscar, text = "Buscar tasación")
        self.marco_buscar.pack()
        
        # Labels
        """ 
        labels_buscar = {text               : [row, column, padx]} 
        """
        labels_buscar = {
                        "Cliente"           : [1, 1, (10,0)],
                        "Tasador"           : [1, 2, (0 ,0)],
                        "Tipo Propiedad"    : [1, 3, (0 ,0)],
                        "Provincia"         : [3, 1, (10,0)],
                        "Ciudad"            : [3, 2, (0 ,0)],
                        "CP"                : [3, 3, (0 ,0)],
                        "Domicilio"         : [3, 4, (0 ,0)],
                        "Nro."              : [3, 5, (0 ,0)],
                        "Sup. terr. desde"  : [5, 1, (10,0)],
                        "Sup. terr. hasta"  : [5, 2, (0 ,0)],
                        "Sup. const. desde" : [5, 3, (0 ,0)],
                        "Sup. const. hasta" : [5, 4, (0 ,0)],
                        "Antigüedad desde"  : [7, 1, (10,0)],
                        "Antigüedad hasta"  : [7, 2, (0 ,0)],
                        "Reformado"         : [5, 5, (0 ,0)],
                        "Valor desde"       : [7, 3, (0 ,0)],
                        "Valor hasta"       : [7, 4, (0 ,0)]
                        }
        ## Representación de labels
        for label, prop in labels_buscar.items():
            self.label_buscar = Label(self.marco_buscar, text = label)
            self.label_buscar.grid(row = prop[0], column = prop[1], padx = prop[2], pady = (2, 0), 
                                   sticky = W )
        
        # Entradas
        """ 
        entrys_buscar = {referencia         : [textvariable, row, column, padx, pady, width]}
        """
        entrys_buscar = {
                        "Cliente"           : [StringVar(), 2, 1, (10,10), (0 , 0), 20],
                        "Tasador"           : [StringVar(), 2, 2, (0 ,10), (0 , 0), 20],
                        "CP"                : [IntVar()   , 4, 3, (0 ,10), (0 , 0), 10],
                        "Domicilio"         : [StringVar(), 4, 4, (0 ,10), (0 , 0), 20],
                        "Nro."              : [IntVar()   , 4, 5, (0 ,10), (0 , 0), 12],
                        "Sup. terr. desde"  : [DoubleVar(), 6, 1, (10,10), (0 , 0), 10],
                        "Sup. terr. hasta"  : [DoubleVar(), 6, 2, (0 ,10), (0 , 0), 10],
                        "Sup. const. desde" : [DoubleVar(), 6, 3, (0 ,10), (0 , 0), 10],
                        "Sup. const. hasta" : [DoubleVar(), 6, 4, (0 ,10), (0 , 0), 10],
                        "Antigüedad desde"  : [IntVar()   , 8, 1, (10,10), (0 ,10), 10],
                        "Antigüedad hasta"  : [IntVar()   , 8, 2, (0 ,10), (0 ,10), 10],
                        "Valor desde"       : [DoubleVar(), 8, 3, (0 ,10), (0 ,10), 20],
                        "Valor hasta"       : [DoubleVar(), 8, 4, (0 ,10), (0 ,10), 20]
                        }
        ## Representación de entradas
        self.entry_buscar = []
        cnt_entry  = 0
        for entry in entrys_buscar.values():
            self.entry_buscar.append(Entry(self.marco_buscar, textvariable = entry[0], 
                                           width = entry[5]))
            self.entry_buscar[cnt_entry].grid(row = entry[1], column = entry[2], padx = entry[3], 
                                              pady = entry[4], sticky = W)
            cnt_entry += 1
     
        # Comboboxs       
        self.cmbbox_tipo = Combobox(self.marco_buscar, textvariable = StringVar(), width = 17)
        self.cmbbox_tipo["values"] = ["Casa", "Departamento", "PH", "Terreno"]
        self.cmbbox_tipo.grid(row = 2 , column = 3, padx = (0,10), pady = (0, 0), sticky = W)
        
        self.cmbbox_provincia = Combobox(self.marco_buscar, textvariable = StringVar(), 
                                         width = 17)
        self.cmbbox_provincia["values"] = sorted(list(set([x['prv_nombre'] for x in localidades])))
        self.cmbbox_provincia.grid(row = 4 , column = 1, padx = (10,10), pady = (0, 0), sticky = W)
        
        self.cmbbox_ciudad = Combobox(self.marco_buscar, textvariable = StringVar(), 
                                      width = 17)
        self.cmbbox_ciudad["values"] = [""] 
        self.cmbbox_ciudad.grid(row = 4 , column = 2, padx = (0,10), pady = (0, 0), sticky = W)
        
        self.cmbbox_reformado = Combobox(self.marco_buscar, textvariable = StringVar(), 
                                         width = 9)
        self.cmbbox_reformado["values"] = ["Si", "No"] 
        self.cmbbox_reformado.grid(row = 6, column = 5, padx = (0,10), pady = (0, 0), sticky = W)

        # Botones
        self.btn_buscar = Button(self.area_buscar, text = '  Buscar  ', command = self.buscar)
        self.btn_buscar.pack(side = LEFT, pady = (10,10), padx = (0,10))
        self.btn_limpiar = Button(self.area_buscar, text = '  Limpiar  ', command = self.buscar_limpiar)
        self.btn_limpiar.pack(side = LEFT, pady = (10,10))
        
        # ACCIONES EN LOS COMBOBOXS
        # Se captura la provincia seleccionada para filtrar las localidades
        self.cmbbox_provincia.bind('<<ComboboxSelected>>', 
                                   lambda event:get_localidad(self.cmbbox_ciudad, 
                                   self.cmbbox_provincia))
        # Se captura la ciudad seleccionada para llenar campo "CP"
        self.cmbbox_ciudad.bind('<<ComboboxSelected>>', 
                                lambda event:set_cp(self.cmbbox_ciudad, self.entry_buscar[2]))
        
        # ÁREA INFORMACIÓN DE LA TASACIÓN
        # ------------------------------------------------------------------------------------------
        # Contenedor del área
        self.area_informacion = Frame(self.seccion_datos)
        self.area_informacion.grid(row = 1, column = 1, sticky = N)
        
        # Labelframe
        self.marco_informacion = LabelFrame(self.area_informacion, text = "Datos de la tasación")
        self.marco_informacion.pack(side = LEFT)
 
        # Labels y entradas
        """ 
        campos_informacion = {texto / referencia         : [row, column, width]} 
        """
        campos_informacion = {
                              "Cliente"                 : [1 , 1, 25],
                              "Tipo Propiedad"          : [1 , 2, 25],
                              "Tasador"                 : [3 , 1, 25],
                              "Fecha"                   : [3 , 2, 10],
                              "País"                    : [5 , 1, 25],
                              "Provincia"               : [5 , 2, 25],
                              "Ciudad"                  : [7 , 1, 25],
                              "CP"                      : [7 , 2, 10],
                              "Domicilio"               : [9 , 1, 25],
                              "Nro."                    : [9 , 2, 10],
                              "Sup. Terreno (m2)"       : [11, 1, 10],
                              "Sup. Construída (m2)"    : [11, 2, 10],
                              "Antigüedad (años)"       : [13, 1, 10],
                              "Reformado"               : [13, 2, 10],
                              "Valor de Tasación (ARS)" : [15, 1, 25]
                             }
        # Representación de labels
        for label, prop in campos_informacion.items():
            self.label_informacion = Label(self.marco_informacion, text = label)
            self.label_informacion.grid(row = prop[0], column = prop[1], padx = (5,0), 
                                        pady = (0, 0), sticky = W )
        # Representación de entradas
        self.entry_informacion = []
        cnt_info = 0
        for entry in campos_informacion.values():
            self.entry_informacion.append(Entry(self.marco_informacion, width = entry[2], 
                                                state='disabled'))
            self.entry_informacion[cnt_info].grid(row = entry[0] + 1, column = entry[1], 
                                                  padx = (5,5), pady = (0, 5), sticky = W)
            cnt_info += 1
  
        # ÁREA TABLA DE CLIENTES
        # ------------------------------------------------------------------------------------------
        # Contenedor del área
        self.area_tabla = Frame(self.seccion_datos, style = "test.TFrame")
        self.area_tabla.grid(row = 1 , column = 2, sticky = N, padx = (0,100) , pady = 10)     

        # Lista con todas las columnas de la bd
        cols_tabla = ["Id","Cliente", "Tipo", "Tasador", "Fecha", "País", "Provincia", "Ciudad", 
                      "CP", "Domicilio", "Nro.", "Sup. terreno", "Sup. construida", "Antigüedad",
                      "Reformado", "Valuación", "imagenes"]
        # Lista de las columnas que se van a mostrar en la tabla
        cols_mostrar = ["Id", "Cliente", "Tipo", "Fecha", "Provincia", "Ciudad", "Domicilio", "Nro."]
        # Anchos de las columnas
        width_cols = [30, 100, 80, 1, 70, 1, 80, 100, 1, 80, 50, 1, 1, 1, 1, 1, 1]
        # Se crea la tabla con todas las columnas.
        # Se limita la selección en la tabla a una sola fila (selectmode = "browse")
        self.tabla = Treeview(self.area_tabla, columns = cols_tabla, height = 15,  
                              show = "headings", selectmode = "browse", style = "tabla.Treeview")
        # Se muestran solamente las columnas elegidas
        self.tabla["displaycolumns"] = cols_mostrar
        # Se crean las columnas en la tabla
        for col in range(len(cols_tabla)):
            self.tabla.heading(cols_tabla[col], text = cols_tabla[col])
            self.tabla.column(cols_tabla[col], anchor = "center", width = width_cols[col])
        self.tabla.grid(padx = 10)

        # Scrollbar vertical para la tabla   
        ysb = Scrollbar(self.area_tabla, orient = "vertical", command = self.tabla.yview)
        ysb.grid(row = 0, column = 1, sticky = "ns")
        self.tabla.configure(yscroll=ysb.set)

        # ACCIONES EN LA TABLA
        # Se llena la tabla con los datos (tasaciones) existentes en la bd
        self.vista_tasacion = vista_tasacion(self.tabla)
        # Al seleccionar una fila se llenan las entradas del área de información de la tasación
        self.tabla.bind('<<TreeviewSelect>>', self.on_select)
       
        # ÁREA BOTONES PRINCIPALES
        # ------------------------------------------------------------------------------------------   
        # Botones
        self.btn_nuevo = Button(self.seccion_botones, text = "  Nuevo  ", 
                                command = self.nuevo_formulario)
        self.btn_nuevo.grid(row = 0, column = 1, sticky = W + E, padx = (0,10), pady = (0,10))
        
        self.btn_editar = Button(self.seccion_botones, text = "  Editar  ", 
                                 command = self.editar_formulario)
        self.btn_editar.grid(row = 0, column = 2, sticky = W + E, padx = (0,10), pady = (0,10))
        
        self.btn_eliminar = Button(self.seccion_botones, text = "  Eliminar  ", 
                                   command = self.eliminar_fila)
        self.btn_eliminar.grid(row = 0, column = 3, sticky = W + E, padx = (0,10), pady = (0,10))
        self.btn_eliminar_todo = Button(self.seccion_botones, text = " Eliminar Todo ", 
                                        command = self.eliminar_todo)
        self.btn_eliminar_todo.grid(row = 0, column = 4, sticky = W + E, padx = (95,0),
                                    pady = (0,10))
        
        # CREAR UNA MUESTRA PARA PROBAR EL PROGRAMA
        # ------------------------------------------------------------------------------------------ 
        # Se agrega un botón adicional para crear una muestra de registros (tasaciones) predefinidas
        self.btn_muestra = Button(self.seccion_botones, text = "  Muestra  ", 
                                  command = lambda:crear_muestra(self.tabla))
        self.btn_muestra.grid(row = 0, column = 5, sticky = E, padx = (10,10), pady = (0,10))

        # ACCIONES EN LOS BOTONES
        # Si no hay acceso a la bd los botones se desactivan
        self.estado_botones()

    # ==============================================================================================
    # ACCIONES SOBRE LOS WIDGETS
    # ==============================================================================================
    
    def on_select(self, event):
        """
        Cuando se selecciona una fila en la tabla se recupera del widget Treeview toda la información 
        de la tasación correspondiente al cliente (incluídos los datos de las columnas ocultas en la 
        tabla) la cual se utiliza para completar los campos de las entradas del área de información 
        y mostrar las imágenes guardadas en el directorio en el área de imágenes.
        """
        # Valores de la fila seleccionada (lista con datos de la tasación)
        self.seleccion_item_app = self.tabla.selection()
        self.lista_items = self.tabla.item(self.seleccion_item_app)["values"]
        # El último item que corresponde a los nombres de las imágenes guardades en el directorio
        self.string_imagenes = self.lista_items[-1]
        # Se transforma el string en una lista de nombres de imágenes
        self.lista_imagenes  = [i[1:-1] for i in list(self.string_imagenes[1:-1].split(", "))]
        # Se define la ubicación de las imágenes en el directorio
        self.ruta_imagenes   = [self.directorio_img + i for i in self.lista_imagenes]
        # Se llenan los campos del área de información con los valores de la selección
        for v in range(len(self.entry_informacion)-1):
            # Se cambia el estado de las entradas
            self.entry_informacion[v].configure(state='normal')
            self.entry_informacion[v].delete(0, END)
            self.entry_informacion[v].insert(0, self.lista_items[v+1])
            # Se cambia nuevamente el estado de las entradas
            self.entry_informacion[v].configure(state='readonly')
        # Se cambia el formato del valor de tasación
        self.entry_informacion[14].configure(state='normal')
        self.entry_informacion[14].delete(0, END)
        self.entry_informacion[14].insert(0, "${:,.2f}".format(float(self.lista_items[15])))
        self.entry_informacion[14].configure(state='readonly')
        # La función vista_imagenes muestra la primer imágen guardada en el directorio (si hubiera)
        self.vista_imagen(self.directorio_img +  self.lista_imagenes[0], (330,200))
        # Cada vez que se selecciona una fila en la tabla el contador vuelve a cero
        self.cnt = 0
 
    def buscar(self):
        """
        Se selecciona una columna de la tabla de tasaciones con todas sus filas. En cada cada fila 
        se evalúa la condición establecida en la entrada perteneciente a la variable elegida y si no 
        cumple dicha condición se elimina la fila completa (todas las columnas) de la tabla. Cuando
        se verifican todas las filas de una columna se pasa a la siguiente columna donde se evalúan 
        los registros que no se eliminaron y así susecivamente se van filtrando las filas.
        La condición puede incluir texto o valores numéricos.
        """
        # Se llena la tabla con los datos de la bd
        vista_tasacion(self.tabla)
        # Lista de indices de columnas con valores de tipo string en la tabla
        cols_string  = [1, 3, 2, 6, 7, 8, 9, 10, 14]
        # Lista de entradas correspondientes a las columnas e tipo string en el área buscar
        entry_string = [self.entry_buscar[0], self.entry_buscar[1], self.cmbbox_tipo, 
                        self.cmbbox_provincia, self.cmbbox_ciudad, self.entry_buscar[2],
                        self.entry_buscar[3], self.entry_buscar[4], self.cmbbox_reformado]
        # Lista de índices de columnas con valores numéricos en la tabla
        cols_num  = [11, 12, 13, 15]
        # Lista de entradas correspondientes a las columnas numéricas en el área buscar
        entry_num = [[self.entry_buscar[5], self.entry_buscar[6]], [self.entry_buscar[7], 
                      self.entry_buscar[8]], [self.entry_buscar[9], self.entry_buscar[10]], 
                      [self.entry_buscar[11], self.entry_buscar[12]]]
        # Se filtran las filas si se ingresa texto
        for col in range(len(cols_string)):
            # Toma todas las filas de la tabla existentes para la columna "col"
            children = self.tabla.get_children()
            for child in children:
                # Toma una fila de la columna, la convierte en string y minúscula
                texto = str(list(self.tabla.item(child)["values"])[cols_string[col]]).lower()
                # Si no hay coincidencia con la búsqueda se elimina la fila completa
                if not texto.startswith(entry_string[col].get().lower()):
                    self.tabla.delete(child)
        # Se filtran las filas cuando se ingresan valores numéricos
        for col in range(len(cols_num)):
        # Para cada columna se toman todas las filas
            children = self.tabla.get_children()
            for child in children:
                # Se convierten los valores a tipo "float"
                valor = float(list(self.tabla.item(child)["values"])[cols_num[col]])
                # Si no hay coincidencia con la búsqueda se elimina la fila
                # Si se ingresa solo en campo "desde"
                if entry_num[col][0].get() != "" and entry_num[col][1].get() == "":
                    if valor < float(entry_num[col][0].get()):
                        self.tabla.delete(child)
                # Si se ingresa solo en campo "hasta"
                elif entry_num[col][0].get() == "" and entry_num[col][1].get() != "":
                    if valor > float(entry_num[col][1].get()):
                        self.tabla.delete(child)
                # Si se ingresan en campos "desde" y "hasta"    
                elif entry_num[col][0].get() != "" and entry_num[col][1].get() != "":
                    if valor < float(entry_num[col][0].get()) or valor > float(entry_num[col][1].get()):
                        self.tabla.delete(child)
    
    def buscar_limpiar(self):
        """
        Se elimina el texto ingresado en las entradas para realizar una nueva búsqueda y se vuelven
        a mostrar todas las filas.
        """
        # Se limpian las entradas
        for entry in self.entry_buscar:
            entry.delete(0, END)
        # Se limpian los comboboxs
        self.cmbbox_tipo.delete(0, END)
        self.cmbbox_ciudad.delete(0, END)
        self.cmbbox_provincia.delete(0, END)
        self.cmbbox_reformado.delete(0, END)
        # Se llena la tabla con los datos de la bd
        vista_tasacion(self.tabla)
        
    def vista_imagen(self, open, size):
        """
        Este método carga imágenes desde el directorio y las muestra en un canvas, cuando se carga 
        una lista vacía (no hay imágenes para mostar) se elimina la imágen previa cargada en el 
        canvas correspondiente para que éste quede vacío.
        """
        try:
            # Se carga el archivo de imágen
            with PILImage.open(open) as abrir_img:
                resize_img = abrir_img.resize(size, PILImage.ANTIALIAS)
                self.imagen = ImageTk.PhotoImage(resize_img)
                self.canvas_app.create_image(0, 0, image = self.imagen, anchor='nw') 
        except:
            # Se elimina la imágen existente en el canvas
            self.canvas_app.delete("all")
    
    def siguiente(self):
        """
        Muestra la imágen siguiente de la lista de imágenes guardadas en el directorio 
        pertenecientes a una tasación (o a un cliente) seleccionada en la tabla. Si la tasación no 
        tiene imágenes guardadas, si hay una sola imágen o es la última imágen de la lista no se 
        genera ningún cambio en el canvas. Se utiliza un contador para indicar la posición en 
        la lista.
        """
        try:
            # Mientras no sea la última imágen de la lista
            if self.cnt < len(self.lista_imagenes) - 1:
                self.cnt += 1
            # Se carga la imágen al canvas
            self.vista_imagen(self.directorio_img + self.lista_imagenes[self.cnt], (330,200))
        except:
            # Es necesario seleccionar una fila en la tabla
             messagebox.showinfo("Alerta", "Seleccione una Tasación")
    
    def anterior(self):
        """
        Muestra la imágen anterior de la lista de imágenes guardadas en el directorio 
        pertenecientes a una tasación (o a un cliente) seleccionada en la tabla. Si la tasación no 
        tiene imágenes guardadas, si hay una sola imágen o es la primera imágen de la lista no se 
        genera ningún cambio en el canvas. Se utiliza un contador para indicar la posición en 
        la lista.
        """
        try:
            if self.cnt > 0:
                self.cnt -= 1
            self.vista_imagen(self.directorio_img + self.lista_imagenes[self.cnt], (330,200))
        except:
            messagebox.showinfo("Alerta", "Seleccione una Tasación")

    def nuevo_formulario(self):
        """
        Al ajecutar el botón "Nuevo" se abre una ventana que contiene un formulario para cargar los 
        datos de una nueva tasación. 
        """
        popupFormulario = Toplevel()
        # Instanciación de la clase Formulario
        Formulario(popupFormulario, tabla = self.tabla,  directorio_img = self.directorio_img)
        # Restricciones en la ventana principal
        popupFormulario.grab_set()
        popupFormulario.focus_set()
        popupFormulario.wait_window()
        # Se eliminan los datos cargados previamente al seleccionar una tasación en la tabla
        self.limpiar_datos() 
    
    def editar_formulario(self):
        """
        Al seleccionar una tasación en la tabla y al ejecutar el botón "Editar" se abre una ventana 
        con un formulario que contiene los datos cargados previamente al crear dicha tasación. 
        Los valores de la tasación seleccionada se pasan como argumento a la clase (como "entrys") 
        y se utilizan para setear las entradas respectivas. También se pasan como argumento la tabla 
        completa y las listas de imágenes (nombres de las mismas y ubicación en el directorio) para
        visualizar los archivos guardados en la bd y en el directorio en la tabla del formulario.
        """
        try:
            # Se verifica que se haya seleccionado una fila
            if self.seleccion_item_app:
                popupFormulario = Toplevel()
                # Instanciación de la clase Formulario
                Formulario(popupFormulario, tabla = self.tabla, entrys = self.lista_items, 
                           ruta_file = self.ruta_imagenes, name_file = self.lista_imagenes, 
                           directorio_img = self.directorio_img, accion = "editar")
                # Restricciones en la ventana principal
                popupFormulario.grab_set()
                popupFormulario.focus_set()
                popupFormulario.wait_window()
                # Se eliminan los datos cargados previamente al seleccionar una tasación en la tabla
                self.limpiar_datos() 
                # Se elimina la selección vigente para obligar a seleccionar nuevamente una fila
                del self.seleccion_item_app
        except:
            messagebox.showinfo("Alerta", "Seleccione una fila")               

    def eliminar_fila(self):
        """
        Al seleccionar una fila y ejecutar el botón "Eliminar" se elimina el registro de la tabla en 
        la bd. El método llama a la función "eliminar_registro" del módulo "gestionar.py" la cual se 
        conecta a la bd a través de la clase "Abmc" y realiza la tarea requerida.
        """
        try:
            # Se verifica que se haya seleccionado una fila
            if self.seleccion_item_app:
                resultado =  messagebox.askquestion("Eliminar", 
                                                    "¿Está seguro que desea eliminar el registro?")
                if resultado == "yes":
                    # Se elimina la fila de la tabla en la base de datos
                    # Se pasan como argumentos la tabla de tasaciones con el id de la que se debe eliminar
                    eliminar_registro(self.tabla, self.lista_items[0])
                    # Se elimina la variable para que no exista si la tabla está vacía y evitar un error
                    del self.seleccion_item_app 
                    # Se eliminan las imágenes correspondientes en el directorio de trabajo (si hubiese)
                    if self.ruta_imagenes != [self.directorio_img]:
                        for imagen in sorted(self.ruta_imagenes, reverse = True):
                                os.remove(imagen) 
        except:
           messagebox.showinfo("Alerta", "Seleccione una fila")  

    def eliminar_todo(self):
        """
        Al ejecutar el botón "Eliminar Todo" se eliminan los registros de la tabla en la bd.
        El método llama a la función "eliminar_todo" del módulo "gestionar.py" la cual se conecta a 
        la bd a través de la clase "Abmc" y realiza la tarea requerida.
        """
        # Se verifica que se haya seleccionado una fila
        resultado =  messagebox.askquestion("Eliminar", 
                                            "¿Está seguro que desea eliminar todos los registros?")
        if resultado == "yes":
            # Se eliminan todas las filas de la tabla en la base de datos
            # Se pasa como argumentos la tabla de tasaciones
            eliminar_todo(self.tabla)
            # Se eliminan todos los archivos en el directorio de trabajo (si hubiese)
            list(map( os.remove, (os.path.join(self.directorio_img,f)
                                               for f in os.listdir(self.directorio_img))))
       
    def limpiar_datos(self):
        """
        Se eliminan los datos cargados en las entradas del área de información de la tasación y la 
        imagen existente en el canvas del área de imágenes
        """
        # Se elimina la imágen existente 
        self.canvas_app.delete("all")
        # Se eliminan los datos en las entradas 
        for v in range(len(self.entry_informacion)):
            self.entry_informacion[v].configure(state='normal')
            self.entry_informacion[v].delete(0, END)
            self.entry_informacion[v].configure(state='disable')

    def estado_botones(self):
        """
        Si no hay conexión con MySQL los botones se desactivan para no permitir ejecutarlos.
        Para activarlos será necesario entonces reiniciar el programa con MySQL iniciado.
        """
        if not self.vista_tasacion:
            self.btn_nuevo.configure(state = DISABLED)
            self.btn_editar.configure(state = DISABLED)            
            self.btn_eliminar.configure(state = DISABLED)
            self.btn_eliminar_todo.configure(state = DISABLED)
            self.btn_muestra.configure(state=  DISABLED)
            self.btn_buscar.configure(state=  DISABLED)
            self.btn_limpiar.configure(state=  DISABLED)
            
# ==================================================================================================  
# EJECUTAR APLICACIÓN
# ==================================================================================================                       
if __name__ == '__main__':
    directorio_imagenes = "img/imagenes/"
    root = Tk()
    Aplicacion(root, directorio_imagenes)
    root.mainloop()
