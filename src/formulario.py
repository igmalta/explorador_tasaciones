#!/usr/bin/env python
# -*- coding: utf-8 -*

from PIL import ImageTk
from PIL import Image as PILImage
from tkcalendar import*
from tkinter import filedialog
from tkinter import messagebox
from tkinter import* 
from tkinter.ttk import*
import os

from src.gestionar import*

class Formulario(Frame):
    """
    La clase crea una nueva ventana tipo formulario donde se pueden cargar o editar los datos de 
    las tasaciones. 
    """
    
    def __init__(self, parent, tabla, entrys = [""]*17, ruta_file = [], name_file = [], 
                 directorio_img = None, accion = "nuevo"):
        super().__init__(parent)
        self.parent = parent
        self.tabla = tabla
        self.entrys = entrys
        self.ruta_file = ruta_file
        self.name_file = name_file
        self.ruta_file_op = ruta_file[:]
        self.name_file_op = name_file[:]
        self.directorio_img = directorio_img
        self.accion = accion
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
        self.parent.title("Formulario de Tasaciones")
        self.parent.geometry("980x450")
        self.parent.resizable(False, False)
    
    def __create_style(self):
        """
        Se establecen las configuraciones de estilo de los widgets de la libraría ttk.
        """
        pass
    
    def __create_widgets(self):
        """
        Se crean los widgets de la clase.
        """
        # CONTENEDOR PRINCIPAL 
        # ------------------------------------------------------------------------------------------
        self.contenedor = Frame(self.parent)
        self.contenedor.pack(expand="yes", fill=BOTH)
        
        # SECCIONES PRINCIPALES
        # ------------------------------------------------------------------------------------------
        # Sección de ingreso de datos
        self.seccion_registros = ttk.Frame(self.contenedor)
        self.seccion_registros.grid(row = 0, column = 1)

        # Sección de imágenes
        self.seccion_imagenes = Frame(self.contenedor)
        self.seccion_imagenes.grid(row = 0, column = 2)

        # Sección de botones
        self.seccion_botones = Frame(self.contenedor)
        self.seccion_botones.grid(row = 1, column = 1, sticky = W)

        # ÁREA DE REGISTROS
        # ------------------------------------------------------------------------------------------
        # Contenedor del área
        self.area_registros = ttk.Frame(self.seccion_registros)
        self.area_registros.pack()
        
        # Labelframe
        self.marco_registros = LabelFrame(self.area_registros, 
                                          text = "Editar/Agregar Nueva Tasación")
        self.marco_registros.pack(expand="yes", fill=BOTH, padx = (10,10), pady = (10,10))

        # Labels 
        """ 
        labels_registros = {texto                     : [row, column]} 
        """
        labels_registros = {
                            "Cliente"                 : [1 , 1],
                            "Tipo Propiedad"          : [1 , 2],
                            "Tasador"                 : [3 , 1],
                            "Fecha"                   : [3 , 2],
                            "País"                    : [5 , 1],
                            "Provincia"               : [5 , 2],
                            "Ciudad"                  : [7 , 1],
                            "CP"                      : [7 , 2],
                            "Domicilio"               : [9 , 1],
                            "Nro."                    : [9 , 2],
                            "Sup. Terreno (m2)"       : [11, 1],
                            "Sup. Construída (m2)"    : [11, 2],
                            "Antigüedad (años)"       : [13, 1],
                            "Reformado"               : [13, 2],
                            "Valor de Tasación (ARS)" : [15, 1]
                            }
        # Representación de labels
        for label, prop in labels_registros.items():
            self.label_registro = Label(self.marco_registros, text = label)
            self.label_registro.grid(row = prop[0], column = prop[1], padx = (5,0), pady = (0, 0), 
                                     sticky = W )
        
        # Entradas
        self.entry_cliente = ttk.Entry(self.marco_registros, textvariable = StringVar(), width = 25)
        self.entry_cliente.delete(0, END)
        self.entry_cliente.insert(0, self.entrys[1])
        self.entry_cliente.grid(row = 2, column = 1, padx = (5,0), pady = (0, 5), sticky = W)
        
        self.entry_tasador = ttk.Entry(self.marco_registros, textvariable = StringVar(), width = 25)
        self.entry_tasador.delete(0, END)
        self.entry_tasador.insert(0, self.entrys[3])
        self.entry_tasador.grid(row = 4, column = 1, padx = (5,0), pady = (0, 0), sticky = W)
       
        self.entry_fecha = DateEntry(self.marco_registros, width = 10, background = 'darkblue', 
                                       foreground = 'white', borderwidth = 2, date_pattern ='y-mm-dd')
        self.entry_fecha.delete(0, END)
        self.entry_fecha.insert(0, self.entrys[4])
        self.entry_fecha.grid(row = 4 , column = 2, padx = (5,5), pady = (0,5), sticky = W) 

        self.entry_cp = ttk.Entry(self.marco_registros, textvariable = IntVar()   , width = 10)
        self.entry_cp.delete(0, END)
        self.entry_cp.insert(0, self.entrys[8])
        self.entry_cp.grid(row = 8, column = 2, padx = (5,0), pady = (0, 0), sticky = W)
       
        self.entry_domicilio = ttk.Entry(self.marco_registros, textvariable = IntVar(), width = 25)
        self.entry_domicilio.delete(0, END)
        self.entry_domicilio.insert(0, self.entrys[9])
        self.entry_domicilio.grid(row = 10, column = 1, padx = (5,0), pady = (0, 0), sticky = W)
       
        self.entry_nro = ttk.Entry(self.marco_registros, textvariable = StringVar(), width = 10)
        self.entry_nro.delete(0, END)
        self.entry_nro.insert(0, self.entrys[10])
        self.entry_nro.grid(row = 10, column = 2, padx = (5,0), pady = (0, 0), sticky = W)
      
        self.entry_terreno = ttk.Entry(self.marco_registros, textvariable = DoubleVar(), width = 10)
        self.entry_terreno.delete(0,END)
        self.entry_terreno.insert(0, self.entrys[11])
        self.entry_terreno.grid(row = 12, column = 1, padx = (5,0), pady = (0, 0), sticky = W)

        self.entry_construido = ttk.Entry(self.marco_registros, textvariable = DoubleVar(), width = 10)
        self.entry_construido.delete(0, END)
        self.entry_construido.insert(0, self.entrys[12])
        self.entry_construido.grid(row = 12, column = 2, padx = (5,0), pady = (0, 0), sticky = W)
     
        self.entry_antiguedad = ttk.Entry(self.marco_registros, textvariable = IntVar(), width = 10)
        self.entry_antiguedad.delete(0, END)
        self.entry_antiguedad.insert(0, self.entrys[13])
        self.entry_antiguedad.grid(row = 14, column = 1, padx = (5,0), pady = (0, 0), sticky = W)
      
        self.entry_valor = ttk.Entry(self.marco_registros, textvariable = DoubleVar(), width = 25)
        self.entry_valor.delete(0, END)
        self.entry_valor.insert(0, self.entrys[15])
        self.entry_valor.grid(row = 16, column = 1, padx = (5,0), pady = (0, 10), sticky = W)    
 
        # Comboboxs
        self.cmbbox_tipo = ttk.Combobox(self.marco_registros, textvariable = StringVar(), 
                                        width = 22)
        self.cmbbox_tipo["values"] = ["Casa", "Departamento", "PH", "Terreno"]
        self.cmbbox_tipo.set(self.entrys[2])
        self.cmbbox_tipo.grid(row = 2 , column = 2, padx = (5,5), pady = (0,5), sticky = W)
        
        self.cmbbox_pais = ttk.Combobox(self.marco_registros, textvariable = StringVar(), 
                                        width = 22)
        self.cmbbox_pais["values"] = ["Argentina"]
        self.cmbbox_pais.set(self.entrys[5])
        self.cmbbox_pais.grid(row = 6 , column = 1, padx = (5,5), pady = (0,5), sticky = W)
        
        self.cmbbox_provincia = ttk.Combobox(self.marco_registros, textvariable = StringVar(), 
                                             width = 22)
        self.cmbbox_provincia["values"] = sorted(list(set([x['prv_nombre'] for x in localidades])))
        self.cmbbox_provincia.set(self.entrys[6])
        self.cmbbox_provincia.grid(row = 6 , column = 2, padx = (5,5), pady = (0,5), sticky = W)
        
        self.cmbbox_ciudad = ttk.Combobox(self.marco_registros, textvariable = StringVar(), 
                                          width = 22)
        self.cmbbox_ciudad["values"] = [""] 
        self.cmbbox_ciudad.set(self.entrys[7])
        self.cmbbox_ciudad.grid(row = 8 , column = 1, padx = (5,5), pady = (0,5), sticky = W)
        
        self.cmbbox_reformado = ttk.Combobox(self.marco_registros, textvariable = StringVar(), 
                                             width = 7)
        self.cmbbox_reformado["values"] = ["Si", "No"] 
        self.cmbbox_reformado.set(self.entrys[14])
        self.cmbbox_reformado.grid(row = 14, column = 2, padx = (5,5), pady = (0,5), sticky = W)
        
        # ACCIONES EN LOS COMBOBOXS
        # Se captura la provincia seleccionada para filtrar las localidades
        self.cmbbox_provincia.bind('<<ComboboxSelected>>', 
                                   lambda event:get_localidad(self.cmbbox_ciudad, 
                                   self.cmbbox_provincia))
        # Se captura la ciudad seleccionada para llenar campo "CP"
        self.cmbbox_ciudad.bind('<<ComboboxSelected>>', lambda event:set_cp(self.cmbbox_ciudad, 
                                                                            self.entry_cp))
        
        # ÁREA DE IMÁGENES
        # ------------------------------------------------------------------------------------------
        # Contenedor del área
        self.area_imagenes = ttk.Frame(self.seccion_imagenes)
        self.area_imagenes.pack()
        
        # Labelframe 
        self.marco_imagenes = LabelFrame(self.area_imagenes, text = "Visor de Imágenes")
        self.marco_imagenes.pack(expand="yes", fill=BOTH, pady = (0,0))
           
        # Canvas
        self.canvas_form = Canvas(self.marco_imagenes, width = 350, height = 235, bg= "#BBDEFB")
        self.canvas_form.grid(row = 0, column = 1, columnspan = 2, rowspan = 8, sticky = N, padx = (5,5), pady = (5,5))

        # Label
        self.label_nombre = Label(self.marco_imagenes, text = "Nombre de la imágen: ")
        self.label_nombre.grid(row = 11, column = 1, sticky = W, pady = (0,0), padx = (5,5))

        # Entrada para ingreso del nombre de la imágen
        self.ruta_guardar = Entry(self.marco_imagenes, textvariable = StringVar(), width = 23, font = 11)
        self.ruta_guardar.grid(row = 11, column = 2, pady = (0,0), sticky = W)
       
        # Mensaje de salida con la ruta de la imágen
        self.message_img = Label(self.marco_imagenes, text = '')
        self.message_img.grid(row = 10, column = 1, columnspan = 2, sticky = W, padx = (5,5), pady =(5,5))

        # Tabla de imágenes
        self.tabla_img = Treeview(self.marco_imagenes, columns = "Imagen",  show = 'headings', 
                                  selectmode = "browse")
        self.tabla_img.heading("Imagen", text = "Imagen")
        self.tabla_img.column("Imagen", anchor ='center', width = 150)
        self.tabla_img.grid(row = 0, column = 4, rowspan = 8, sticky = W, padx = (5,5))

        # Botones
        self.btn_cargar = Button(self.marco_imagenes, text = '  Cargar  ', command = self.cargar)
        self.btn_cargar.grid(row = 9, column = 1, sticky = W, padx = (5, 5), pady = (5,5))
        self.btn_renombrar = Button(self.marco_imagenes, text = ' Renombrar ', 
                                    command = self.renombrar_entabla)
        self.btn_renombrar.grid(row = 2, column = 3, sticky = N, padx = (5,5))
        self.btn_agregar = Button(self.marco_imagenes, text = ' Agregar ', 
                                  command = self.agregar_entabla)
        self.btn_agregar.grid(row = 11, column = 3, sticky = W, pady = 10, padx = (5,5))
        self.btn_eliminar = Button(self.marco_imagenes, text = '   Eliminar   ', 
                                   command = self.eliminar_entabla)
        self.btn_eliminar.grid(row = 1, column = 3, sticky = N, padx = (5,5))
    
        # ACCIONES EN LA TABLA DE IMÁGENES
        # Se llena la tabla con las imágenes de la tasación existentes (si hubiese)
        for img in self.name_file:
            self.tabla_img.insert('', "end", text = img , values = img)
        # Cambiar imágen en el canvas al seleccionar en tabla
        self.tabla_img.bind('<<TreeviewSelect>>', self.on_select_img)
    
        # ÁREA BOTONES PRINCIPALES
        # ------------------------------------------------------------------------------------------
        # El boton "Aceptar" ejecuta diferentes métodos según la acción de formulario requerida
        if self.accion == "nuevo":
            self.btn_aceptar = Button(self.seccion_botones, text = '  Aceptar  ', 
                                      command = self.datos_guardar)
            self.btn_aceptar.grid(row = 0, column = 1, sticky = W + E, padx = 7)
        elif self.accion == "editar":
            self.btn_aceptar = Button(self.seccion_botones, text = '  Aceptar  ', 
                                      command = self.datos_modificar)
            self.btn_aceptar.grid(row = 0, column = 1, sticky = W + E, padx = 7)
        self.btn_cancelar = Button(self.seccion_botones, text = '  Cancelar  ', command = self.cancelar)
        self.btn_cancelar.grid(row = 0, column = 2, sticky = W + E, padx=7)

    # ==============================================================================================
    # ACCIONES SOBRE LOS WIDGETS
    # ==============================================================================================
    
    def cargar(self):
        """
        Se abre una ventana de archivos para cargar las imágenes. El código está preparado para 
        trabajar solamente con archivos ".jpg". Al cargar la imágen ésta se visualiza en el canvas
        y se imprime debajo de él un mensaje con la ubicación del archivo.
        """
        # Se abre una ventana para cargar las imágenes
        self.ruta_cargar = filedialog.askopenfilename(title='Subir', 
                                            filetypes = (("jpg files","*.jpg"),("all files","*.*")))                              
        # Se verifica que se haya seleccionado una imágen para cargar
        if len(self.ruta_cargar) < 1:
                self.canvas_form.delete("all")
                messagebox.showinfo("Alerta", "Debe seleccionar una imágen para cargar")
        else:    
            # Se verifica que el formato de imágen sea el correcto
            if not self.ruta_cargar.lower().endswith(('.jpg')):
                messagebox.showwarning("Alerta", 
                                       "Formato de imágen no válido. Cargue un archivo '.jpg'")
            else:
                # Se carga la imágen en el canvas
                self.vista_imagen(self.ruta_cargar, (350,235))
                # Se imprime la ruta de la imágen cargada               
                self.ruta_imagen(self.ruta_cargar)

    def agregar_entabla(self):
        """
        Cuando se carga una imagen desde el directorio se debe definir un nombre para ella en la 
        entrada prevista. Al presionar el botón "Agregar" el nombre elegido se agrega a la lista
        "self.name_file_op "y se visualiza en la tabla. La ubicación del archivo se adiciona a la 
        lista "self.ruta_file_op" en la misma posición que el nombre.
        """
        try:
            # Se verifica que la imágen que se quiere agregar o el nombre establecido no se repitan
            if self.ruta_cargar in self.ruta_file_op:
                messagebox.showinfo("Alerta", "El archivo ya fue cargado. Elija otra imágen")
            elif len(self.ruta_cargar) == 0:
                messagebox.showinfo("Alerta", "Cargue una imágen") 
            elif (self.ruta_guardar.get() + ".jpg") in self.name_file_op:
                messagebox.showinfo("Alerta", "El nombre ya existe. Elija otro nombre")
            elif (self.ruta_guardar.get() + ".jpg") in os.listdir(self.directorio_img):
                messagebox.showinfo("Alerta", "El archivo ya existe. Elija otro nombre")
            else:
                # Se agrega la ruta de la imagen cargada y el nombre establecido a las listas 
                # correspondientes
                if  len(self.ruta_guardar.get()) > 0:
                    # Cuando no hay imágenes guardadas en la tasación
                    if self.name_file_op == [""]:
                        self.ruta_file_op = [self.ruta_cargar]
                        self.name_file_op = [self.ruta_guardar.get() + ".jpg"]
                    # Cuando ya imágenes guardadas para la tasación
                    else:
                        self.ruta_file_op.append(self.ruta_cargar)
                        self.name_file_op.append(self.ruta_guardar.get() + ".jpg") 
                else:
                    messagebox.showinfo("Alerta", "Ingrese un nombre válido", parent = self.parent)     
                # Se actualiza la tabla
                self.actualizar_tabla()
        except:
            # Cuando se cancela la carga de un archivo de imágen
            messagebox.showinfo("Alerta", "Debe cargar una imágen del directorio")

    def on_select_img(self, event):
        """
        Cuando se selecciona una fila en la tabla se recupera el nombre de la imágen elegida 
        y se determina en que posición de la lista "self.name_file_op" se encuentra para obtener la 
        ruta del archivo guardado en el directorio en la misma posición en la lista "self.ruta_file_op".
        """
        # Valores de la fila seleccionados  
        self.seleccion_item = self.tabla_img.selection()
        self.valor_item = self.tabla_img.item(self.seleccion_item)["values"]
        # Posición del item (nombre de la imágen) en la lista "self.name_file"
        self.indice = self.name_file_op.index(self.valor_item[0]) 
        # Se carga la imágen al canvas usando la ruta guardada en la lista "self.ruta_file_op"
        self.vista_imagen(self.ruta_file_op[self.indice], (350,235))
        # Se emite mensaje con la ruta de la imagen
        self.ruta_imagen(self.ruta_file_op[self.indice])
    
    def vista_imagen(self, open, size):
        """
        Este método carga imágenes desde el directorio y las muestra en un canvas, cuando se carga 
        una lista vacía (no hay imágenes para mostar) se elimina la imágen previa cargada en el 
        canvas correspondiente para éste quede vacío.
        """
        try:
            # Se carga el archivo de imágen
            with PILImage.open(open) as abrir_img:
                resize_img = abrir_img.resize(size, PILImage.ANTIALIAS)
                self.imagen = ImageTk.PhotoImage(resize_img)
                self.canvas_form.create_image(0, 0, image = self.imagen, anchor='nw')   
        except:
            # Se elimina la imágen existente en el canvas
            self.canvas_form.delete("all")
   
    def ruta_imagen(self, ruta):
        """
        Imprime un mensaje con la ubicación del archivo, la cual se pasa como argumento. El mensaje
        se limita a 58 caracteres.
        """
        try:
            mensaje ="Ruta: " + str(ruta)
            if len(mensaje) > 58:
                mensaje = mensaje[0:58] + "..."
            self.message_img.config(text = mensaje)
        except:
            self.message_img.config(text = "...")

    def actualizar_tabla(self):
        """
        Recorre la lista de nombres de imágenes y los inserta en la tabla de imágenes.
        """
        records = self.tabla_img.get_children()
        # Se eliminan todos los iteams existentes en la tabla
        for element in records:
            self.tabla_img.delete(element)
        # Se vuelve a llenar la tabla con los valores actualizados en la lista "self.name_file_op"
        for row in self.name_file_op:
            self.tabla_img.insert('', "end", text = row, values = row)
        
    def datos_guardar(self):
        """
        Los cambios realizados al crear un nuevo formulario se ejecutan al apretar el botón 
        "Aceptar". Los valores ingresados en las entradas se guardan en la bd junto con un string 
        que contiene los nombres de las imágenes cargadas, las cuales se se guardan en el directorio 
        establecido.
        """
        # Se capturan los datos ingresados en las entradas
        valores = self.get_entradas()
        # Se define el estado de los campos del formulario
        self.validar_campos(valores)
        # Se verifica que las entradas están llenas
        if self.validar_campos(valores):
            messagebox.showinfo("Alerta", "Complete todos los campos")  
        else:
            consulta =  messagebox.askokcancel('Cerrar', "¿Desea guardar los cambios?")
            if consulta:
                # Se guardan los datos en la base de datos
                alta_tabla(self.tabla, valores)
                # Si no existe, se crea el directorio definido para guardar las imágenes subidas
                directorioParaImgs = os.path.join(self.directorio_img)
                if not os.path.exists(directorioParaImgs):
                    os.mkdir(directorioParaImgs)
                # Se guardan las imágenes cargadas (si hubiese) en el directorio
                for i in range(len(self.ruta_file_op)):
                    name_file = self.name_file_op[i]
                    with PILImage.open(self.ruta_file_op[i]) as abrir_img:
                        guardar_img = os.path.join(directorioParaImgs, name_file)
                        abrir_img.save(guardar_img)
                # Se cierra la ventana
                self.parent.destroy()
            
    def datos_modificar(self):
        """
        Los cambios que se realizan sobre el formulario, ya sea modificando los datos de la tasación 
        en las entradas como las operaciones de carga, renombre y eliminación de imágenes persisten 
        al apretar el botón "Aceptar" y confirmar la acción, donde se actualizan los campos en 
        la bd y el directorio de imágenes.
        Cuando se renombra una imágen (y se confirman los cambios) se hace una copia de la misma en
        el directorio de trabajo con el nuevo nombre y luego se elimina el archivo copiado.
        """
        # Se capturan los datos ingresados en las entradas
        valores = self.get_entradas()
        # Se define el estado de los campos del formulario
        self.validar_campos(valores)
        # Se verifica que las entradas están llenas
        if self.validar_campos(valores):
            messagebox.showinfo("Alerta", "Complete todos los campos")  
        else:
            consulta =  messagebox.askokcancel('Cerrar', "¿Desea guardar los cambios?")
            if consulta:          
                # Se actualiza la base de datos con los valores editados
                update_tabla(self.tabla, valores) 
                # Se guardan primero las imágenes cargadas en el directorio (si hubiese)
                # Ruta del directorio de imágenes
                directorioParaImgs = os.path.join(self.directorio_img)
                # Se guardan las imágenes si "self.name_file_op" no está vacío, o sea, hay imágenes
                if self.name_file_op != [""]:
                    for i in range(len(self.ruta_file_op)):
                        name_file = self.name_file_op[i]
                        with PILImage.open(self.ruta_file_op[i]) as abrir_img:
                            guardar_img = os.path.join(directorioParaImgs, name_file)
                            abrir_img.save(guardar_img)
                # Se obtienen los nombres de las imágenes modificadas
                name_modificado = list(set(self.name_file) - set(self.name_file_op))
                # Si hay imágenes renombradas o eliminadas se crea una lista con su ubicación, sino queda vacía
                if len(name_modificado) != [""]:
                    imagenes_modificadas = [self.directorio_img + i for i in name_modificado]
                else:
                    imagenes_modificadas = []
                # Se eliminan imágenes del directorio (las que fueron eliminadas o renombradas de la 
                # tabla, si hubiese)
                for imagen in sorted(imagenes_modificadas, reverse = True):
                    # Se hace esta verificación para evitar errores cuando la lista está vacía
                    if imagen != self.directorio_img:
                        os.remove(imagen)
                # Se cierra la ventana
                self.parent.destroy()     

    def get_entradas(self):
        """
        Devuelve una lista con los valores de las entradas del formulario. Si es un formulario de
        edición se adiciona el valor del id de la tasación seleccionada.
        """
        # Se capturan los valores de las entradas
        valores = [self.entry_cliente.get(), self.cmbbox_tipo.get(), self.entry_tasador.get(), 
                   self.entry_fecha.get(), self.cmbbox_pais.get(), self.cmbbox_provincia.get(), 
                   self.cmbbox_ciudad.get(), self.entry_cp.get(), self.entry_domicilio.get(), 
                   self.entry_nro.get(), self.entry_terreno.get(), self.entry_construido.get(), 
                   self.entry_antiguedad.get(), self.cmbbox_reformado.get(), self.entry_valor.get(), 
                   str(self.name_file_op)] 
        # Se adiciona el id de la tasación si se edita un registro existente
        if self.accion == "editar":
            valores.append(self.entrys[0]) 
        return valores         
                
    def eliminar_entabla(self):
        """
        Cuando se selecciona una imagen en la tabla y se ejecuta el botón "Eliminar", se elimina su 
        nombre en dicha tabla y en la lista "self.name_file_op". En la misma posición de la lista 
        de nombres se elimina la ruta en "self.ruta_file_op".
        """
        try:
            if self.seleccion_item:
                resultado =  messagebox.askquestion("Alerta", 
                                                    "¿Está seguro que desea eliminar la imágen?")
                if resultado == "yes":
                    # Se borran items de la tabla
                    self.tabla_img.delete(self.seleccion_item)
                    # Se elimina la variable para que no exista si la tabla está vacía y evitar un error
                    del self.seleccion_item 
                    # Se calcula la posición de la imágen en la lista "self.name_file"
                    indice = self.name_file_op.index(self.valor_item[0])
                    # Se elimina la imagen de las correspondientes listas
                    del self.name_file_op[indice]
                    del self.ruta_file_op[indice]
        except:
            messagebox.showinfo("Alerta", "Seleccione una imágen") 
            
    def renombrar_entabla(self):
        """
        Al renombrar una imagen y confirmar se verifica que el nombre nuevo no exista. Los cambios
        se aplican temporalmente sobre la lista "self.name_file_op" y se visualizan en la tabla, pero
        si no se ratifican al apretar el botón "Aceptar" no persisten ya que no se actualizan la bd y
        el directorio donde se guardan los archivos.
        """
        try:
            if self.seleccion_item:
                if len(self.ruta_guardar.get()) == 0:
                    messagebox.showinfo("Alerta", "Ingrese un nombre válido")
                elif (self.ruta_guardar.get() + ".jpg") in os.listdir(self.directorio_img):
                    messagebox.showinfo("Alerta", "El archivo ya existe. Elija otro nombre")
                else:
                    resultado =  messagebox.askquestion("Alerta",
                                                        "¿Está seguro que desea renombrar la imagen?")
                    if resultado == "yes":
                        # valor (nombre) del ítem (imagen) seleccionado
                        self.valor_item = self.tabla_img.item(self.seleccion_item)["values"]
                        # Se obtiene el índice
                        indice = self.name_file_op.index(self.valor_item[0])
                        # Se renombra la imagen
                        if self.ruta_guardar.get() + ".jpg" in self.name_file_op:
                            messagebox.showinfo("Alerta", "El nombre ya existe. Elija otro nombre")
                        else:
                            # Se actualiza la lista "self.name_file_op" con el nuevo nombre ingresado
                            self.name_file_op[indice] = self.ruta_guardar.get() + ".jpg"
                            # Se actualiza la tabla con el nuevo nombre ingresado
                            self.actualizar_tabla() 
                            # Se elimina la variable para que no exista si la tabla está vacía y evitar un error
                            del self.seleccion_item 
        except:
            messagebox.showinfo("Alerta", "Seleccione una imágen")   
      
    def cancelar(self):
        """
        Destruye la ventana del formulario y vuelve a la ventana principal.
        """
        consulta =  messagebox.askokcancel('Cerrar', "¿Desea abandonar la aplicación?")
        if consulta:
            self.parent.destroy()

    def validar_campos(self, valores):
        """
        Se recorre cada campo del formulario, si hay alguno vacío la variable "campos_vacios" se
        configura en "True".
        """
        campos_vacios = False
        # Se verifica que los campos estén llenos
        for v in valores[0:14]:
            if v == "":
                campos_vacios = True      
        return campos_vacios
    



