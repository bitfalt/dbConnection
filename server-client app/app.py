import tkinter as tk
from tkinter import ttk
import pyodbc

server = 'localhost'
database = 'esenVerde'
username = "user"
password = "123456"

connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# db variables
cname = "Esencial Verde"
pname = "Taco Bell"
address = "Costa Rica Calle 1, San Juan, PR"
WOPTIONS = ["Chemical Waste", "Nuclear Waste", "Paper Waste", "Organic Waste"]
COPTIONS = ["Suli", "Calvo", "Makers", "Quakers"]
NUMBERS = []

# crear dos listas para almacenar los datos de los contenedores y los desechos
containersList = []
wastesList = []

# función para agregar los datos ingresados por el usuario a la lista waste
def addDataWaste():
    # obtener los datos ingresados por el usuario
    tipoWaste = wasteType.get()
    cantidadWaste = numberWaste.get()

    # validar que se ingresaron datos válidos
    if tipoWaste and cantidadWaste:
        # agregar los datos a la lista correspondiente
        wastesList.append([tipoWaste, int(cantidadWaste)])

# función para agregar los datos ingresados por el usuario a la lista container
def addDataContainer():
    # obtener los datos ingresados por el usuario
    modeloContainer = containerModel.get()
    cantidadContainer = numberContainers.get()

    # validar que se ingresaron datos válidos
    if modeloContainer and cantidadContainer:
        # agregar los datos a la lista correspondiente
        containersList.append([modeloContainer, int(cantidadContainer)])

# función para enviar los datos del waste a la base de datos mediante un TVP
def sendDataWaste():
    # crear una tabla de valor de parámetro para los desechos
    wastesTVP = pyodbc.TableValuedParameter('[dbo].[WastesTVP]')
    wastesTVP.add_rows(wastesList)

    # crear un cursor para ejecutar el stored procedure
    cursor = connection.cursor()

    # ejecutar el stored procedure con los parámetros adecuados
    # cursor.execute('EXEC canjear_residuos ?, ?, ?, ?', productor_id, transportista_id, tipo_residuo, cantidad_recipientes)

    # guardar los cambios en la base de datos
    connection.commit()

# función para enviar los datos del container a la base de datos mediante un TVP
def sendDataContainer():
    # crear una tabla de valor de parámetro para los contenedores
    containersTVP = pyodbc.TableValuedParameter('[dbo].[ContainersTVP]')
    containersTVP.add_rows(containersList)

    # crear un cursor para ejecutar el stored procedure
    cursor = connection.cursor()

    # ejecutar el stored procedure con los parámetros adecuados
    cursor.execute("EXEC exchangeContainer @ContainersTVP=?", containersTVP)

    # guardar los cambios en la base de datos
    connection.commit()



# create list of numbers from 1 to 100
for i in range(1, 101):
    NUMBERS.append(str(i))



root = tk.Tk()
root.resizable(False, False)
root.geometry('800x500')

# set background color
root.configure(bg='#f2f2f2')


# create labels for Driver, Collector, Producer and Address
driverLabel = tk.Label(root, text="Driver: Manuel Granados", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
driverLabel.place(x=10, y=10)

addressLabel = tk.Label(root, text=f"Destination: {address}", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
addressLabel.place(x=10, y=40)

collectorLabel = tk.Label(root, text=f"Collector: {cname}", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
collectorLabel.place(x=10, y=100)

producerLabel = tk.Label(root, text=f"Producer: {pname}", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
producerLabel.place(x=10, y=130)



# create widgets to add waste

WastePickupLabel = tk.Label(root, text="Waste to pickup", bg='#f2f2f2', font=('Helvetica', 16, 'bold'))
WastePickupLabel.place(x=10, y=200) 

amountLabelW = tk.Label(root, text="Amount:", bg='#f2f2f2', font=('Helvetica', 14))
amountLabelW.place(x=10, y=235)
numberWaste = tk.StringVar(root)
numberWaste.set("")

numberWasteSelection = ttk.Combobox(root, textvariable=numberWaste, values=NUMBERS, font=('Helvetica', 14))
numberWasteSelection["state"] = "readonly"

numberWasteSelection.pack()
numberWasteSelection.place(x=100, y=235, width=80, height=30)

# numberEntry = tk.Entry(root, textvariable=numberWaste, font=('Helvetica', 14))
# numberEntry.place(x=100, y=470, width=80, height=30)


wasteType = tk.StringVar(root)
wasteType.set("Waste Type")

WasteTypeSelection = ttk.Combobox(root, textvariable=wasteType, values=WOPTIONS, font=('Helvetica', 14))
WasteTypeSelection["state"] = "readonly"

WasteTypeSelection.pack()
WasteTypeSelection.place(x=190, y=235, width=180, height=30)

addBtnW = tk.Button(root, text="Add", bg='#f2f2f2', font=('Helvetica', 14), command=addDataWaste)
addBtnW.place(x=380, y=235, width=80, height=30)
submitBtnW = tk.Button(root, text="Submit", bg='#f2f2f2', font=('Helvetica', 14), command=sendDataWaste)
submitBtnW.place(x=470, y=235, width=80, height=30)

# create widgets to add container

ContainerDeliverLabel = tk.Label(root, text="Containers to deliver", bg='#f2f2f2', font=('Helvetica', 16, 'bold'))
ContainerDeliverLabel.place(x=10, y=280)

amountLabelC = tk.Label(root, text="Amount:", bg='#f2f2f2', font=('Helvetica', 14))
amountLabelC.place(x=10, y=310)
numberContainers = tk.StringVar(root)
numberContainers.set("")

numberContainersSelection = ttk.Combobox(root, textvariable=numberContainers, values=NUMBERS, font=('Helvetica', 14))
numberContainersSelection["state"] = "readonly"

numberContainersSelection.pack()
numberContainersSelection.place(x=100, y=310, width=80, height=30)


# numberEntry = tk.Entry(root, textvariable=numberContainers, font=('Helvetica', 14))
# numberEntry.place(x=100, y=510, width=80, height=30)


containerModel = tk.StringVar(root)
containerModel.set("Containter model")

containerModelSelection = ttk.Combobox(root, textvariable=containerModel, values=COPTIONS, font=('Helvetica', 14))
containerModelSelection["state"] = "readonly"

containerModelSelection.pack()
containerModelSelection.place(x=190, y=310, width=180, height=30)

addBtnC = tk.Button(root, text="Add", bg='#f2f2f2', font=('Helvetica', 14), command=addDataContainer)
addBtnC.place(x=380, y=310, width=80, height=30)
submitBtnC = tk.Button(root, text="Submit", bg='#f2f2f2', font=('Helvetica', 14), command=sendDataContainer)
submitBtnC.place(x=470, y=310, width=80, height=30)

root.mainloop()


# cerrar la conexión con la base de datos
connection.close()