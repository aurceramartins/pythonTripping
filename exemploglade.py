from gi.repository import Gtk
import sqlite3 as dbapi

# version de api
print(dbapi.apilevel)
# nivel de seuridade de fios de 0 a 3
print(dbapi.threadsafety)
# insercion de param
print(dbapi.paramstyle)
try:
    bbdd = dbapi.connect("basedatos.dat")
except (ConnectionError, dbapi.DatabaseError):
    print("Error de conexion")
else:
    print("Conexion establecida")
finally:
    print("Conexion lista")

cursor = bbdd.cursor()
sql = """
create table if not exists existenciasPorPersona(
cod integer primary key autoincrement not null,
 nombre text not null,
  producto text)
  """
sqlDomotica = """create table if not exists domotica(
cliente text primary key not null,
apellido text not null,data text not null,
raspberry text not null,
leds text not null,
cortinas text not null,
alarma text not null,
camaras text not null)
"""

# Ejecutamos la consulta
cursor.execute(sqlDomotica)

# cursor.execute(datos)






cliente = "ninguno"
apellido = "ninguno"
fecha = "ninguno"
rasp = "niguno"
led = "niguno"
cort = "niguno"
alarm = "niguno"
cam = "niguno"
tripp = "niguno"


def registrar(Button):
    nombre = entryNombre.get_text();
    contraseña = entryContraseña.get_text();

    if nombre == "alejandro" and contraseña == "contraseña":
        lblprueba.set_text(" %s" % "Peritas estas dentro")
        ventana2 = builder2.get_object("ventana2")
        ventana2.show_all()
        window.hide();

        Gtk.main()

    else:
        lblprueba.set_text("Prueba otra vez")


def raspberry(Button):
    global rasp
    rasp = "raspberry pi"


def leds(Button):
    global led
    led = "luds LEMONS"


def cortinas(Button):
    global cort
    cort = "Persianas"


def alarma(Button):
    global alarm
    alarm = "Alarma Seguridad"


def camaras(Button):
    global cam
    cam = "Camaras Seguridad"


def tripping(Button):
    lblTitulo.set_text(" %s" % "TRIPPDAWORLDDDDD")


def compras(Button):
    cliente = entry1.get_text()
    apellido = entry2.get_text()
    fecha = entry3.get_text()
    print(cliente + " " + apellido + " " + fecha + " " + rasp + " " + led + " " + cort + " " + alarm + " " + cam)
    datosDomoticos = """insert into domotica values(
    '""" + cliente + """',
    '""" + apellido + """',
    '""" + fecha + """',
    '""" + rasp + """',
    '""" + led + """',
    '""" + cort + """',
    '""" + alarm + """',
    '""" + cam + """'
    )"""
  
    cursor.execute(datosDomoticos)
    bbdd.commit()
    cursor.execute("""select * from domotica""")
    for result in cursor:
        print("Cliente:" + str(result[0]) + " fecha:" + result[1] + " producto1:" + result[2])


handlers = {
    # Ventana 1
    "onButtonPressed": registrar,
    "onDeleteWindow": Gtk.main_quit,

    # Ventana 2

    "rasp": raspberry,
    "leds": leds,
    "cortinas": cortinas,
    "alarma": alarma,
    "camaras": camaras,
    "trippdaworld": tripping,
    "comprar": compras
}

builder = Gtk.Builder()
# Primera ventana
builder.add_from_file("exemplo_glade.glade")
builder.connect_signals(handlers)
lblNombre = builder.get_object("lblNombre")
lblContraseña = builder.get_object("lblContraseña")
entryNombre = builder.get_object("entryNombre")
entryContraseña = builder.get_object("entryContraseña")
lblprueba = builder.get_object("lblprueba")
window = builder.get_object("ventanaPrincipal")
window.show_all()

# Segunda Ventana
builder2 = Gtk.Builder()
builder2.add_from_file("fichero2.glade")
builder2.connect_signals(handlers)
lblTitulo = builder2.get_object("lblTitulo")
entry1 = builder2.get_object("entry1")
entry2 = builder2.get_object("entry2")
entry3 = builder2.get_object("entry3")

Gtk.main()

bbdd.commit()
# cerramos la conexion
bbdd.close()
