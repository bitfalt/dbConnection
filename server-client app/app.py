import tkinter as tk
from tkinter import ttk

# db variables
cname = "Esencial Verde"
pname = "Taco Bell"
address = "Costa Rica Calle 1, San Juan, PR"
WOPTIONS = ["Chemical Waste", "Nuclear Waste", "Paper Waste", "Organic Waste"]
COPTIONS = ["Suli", "Calvo", "Makers", "Quakers"]
NUMBERS = []

# create list of numbers from 1 to 100
for i in range(1, 101):
    NUMBERS.append(str(i))



root = tk.Tk()
root.resizable(False, False)
root.geometry('800x620')

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



# create labels for Waste to pickup and Containers to deliver
wasteLabel = tk.Label(root, text="Waste to pickup:", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
wasteLabel.place(x=10, y=200)

wasteListbox = tk.Listbox(root, bg='white', font=('Helvetica', 14))
wasteListbox.place(x=10, y=260, width=250, height=200)

for i in range(30):
    wasteListbox.insert(tk.END, f"Item {i+1}")

containerLabel = tk.Label(root, text="Containers to deliver:", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
containerLabel.place(x=300, y=200)

containerListbox = tk.Listbox(root, bg='white', font=('Helvetica', 14))
containerListbox.place(x=300, y=260, width=250, height=200)

for i in range(20):
    containerListbox.insert(tk.END, f"Item {i+1}")


# create widgets to add waste

WastePickupLabel = tk.Label(root, text="Waste to pickup", bg='#f2f2f2', font=('Helvetica', 16, 'bold'))
WastePickupLabel.place(x=10, y=460) 

amountLabelW = tk.Label(root, text="Amount:", bg='#f2f2f2', font=('Helvetica', 14))
amountLabelW.place(x=10, y=495)
numberWaste = tk.StringVar(root)
numberWaste.set("")

numberWasteSelection = ttk.Combobox(root, textvariable=numberWaste, values=NUMBERS, font=('Helvetica', 14))
numberWasteSelection["state"] = "readonly"

numberWasteSelection.pack()
numberWasteSelection.place(x=100, y=495, width=80, height=30)

# numberEntry = tk.Entry(root, textvariable=numberWaste, font=('Helvetica', 14))
# numberEntry.place(x=100, y=470, width=80, height=30)


wasteType = tk.StringVar(root)
wasteType.set("Waste Type")

WasteTypeSelection = ttk.Combobox(root, textvariable=wasteType, values=WOPTIONS, font=('Helvetica', 14))
WasteTypeSelection["state"] = "readonly"

WasteTypeSelection.pack()
WasteTypeSelection.place(x=190, y=495, width=180, height=30)

addBtnW = tk.Button(root, text="Add", bg='#f2f2f2', font=('Helvetica', 14))
addBtnW.place(x=380, y=495, width=80, height=30)
submitBtnW = tk.Button(root, text="Submit", bg='#f2f2f2', font=('Helvetica', 14))
submitBtnW.place(x=470, y=495, width=80, height=30)

# create widgets to add container

ContainerDeliverLabel = tk.Label(root, text="Containers to deliver", bg='#f2f2f2', font=('Helvetica', 16, 'bold'))
ContainerDeliverLabel.place(x=10, y=530)

amountLabelC = tk.Label(root, text="Amount:", bg='#f2f2f2', font=('Helvetica', 14))
amountLabelC.place(x=10, y=560)
numberContainers = tk.StringVar(root)
numberContainers.set("")

numberContainersSelection = ttk.Combobox(root, textvariable=numberContainers, values=NUMBERS, font=('Helvetica', 14))
numberContainersSelection["state"] = "readonly"

numberContainersSelection.pack()
numberContainersSelection.place(x=100, y=560, width=80, height=30)


# numberEntry = tk.Entry(root, textvariable=numberContainers, font=('Helvetica', 14))
# numberEntry.place(x=100, y=510, width=80, height=30)


containerModel = tk.StringVar(root)
containerModel.set("Containter model")

containerModelSelection = ttk.Combobox(root, textvariable=containerModel, values=COPTIONS, font=('Helvetica', 14))
containerModelSelection["state"] = "readonly"

containerModelSelection.pack()
containerModelSelection.place(x=190, y=560, width=180, height=30)

addBtnC = tk.Button(root, text="Add", bg='#f2f2f2', font=('Helvetica', 14))
addBtnC.place(x=380, y=560, width=80, height=30)
submitBtnC = tk.Button(root, text="Submit", bg='#f2f2f2', font=('Helvetica', 14))
submitBtnC.place(x=470, y=560, width=80, height=30)

root.mainloop()
