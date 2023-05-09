import tkinter as tk

cname = "Esencial Verde"
pname = "Taco Bell"
address = "Costa Rica Calle 1, San Juan, PR"
OPTIONS = ["Chemical Waste", "Nuclear Waste", "Paper Waste", "Organic Waste"]

root = tk.Tk()
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

amountLabel = tk.Label(root, text="Amount:", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
amountLabel.place(x=10, y=470)
numberWaste = tk.StringVar(root)
numberWaste.set("")
numberEntry = tk.Entry(root, textvariable=numberWaste, font=('Helvetica', 14))
numberEntry.place(x=100, y=470, width=80, height=30)


wasteType = tk.StringVar(root)
wasteType.set("Waste Type")
WasteTypeSelection = tk.OptionMenu(root, wasteType, *OPTIONS)
WasteTypeSelection.pack()
WasteTypeSelection.place(x=190, y=470, width=150, height=30)

addBtn = tk.Button(root, text="Add", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
addBtn.place(x=350, y=470, width=80, height=30)



root.mainloop()
