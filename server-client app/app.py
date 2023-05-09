import tkinter as tk

cname = "Esencial Verde"
pname = "Taco Bell"
address = "Costa Rica - Calle 1, San Juan, PR"

root = tk.Tk()
root.geometry('800x620')

# set background color
root.configure(bg='#f2f2f2')

# create labels and entry widgets for Collector and Producer
collectorLabel = tk.Label(root, text="Collector:", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
collectorLabel.place(x=10, y=10)

producerLabel = tk.Label(root, text="Producer:", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
producerLabel.place(x=300, y=10)

# create labels and entry widgets for Waste to pickup and Containers to deliver
wasteLabel = tk.Label(root, text="Waste to pickup:", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
wasteLabel.place(x=10, y=200)

wasteListbox = tk.Listbox(root, bg='white', font=('Helvetica', 14))
wasteListbox.place(x=10, y=260, width=250, height=200)

for i in range(10):
    wasteListbox.insert(tk.END, f"Item {i+1}")

containerLabel = tk.Label(root, text="Containers to deliver:", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
containerLabel.place(x=300, y=200)

containerListbox = tk.Listbox(root, bg='white', font=('Helvetica', 14))
containerListbox.place(x=300, y=260, width=250, height=200)

for i in range(8):
    containerListbox.insert(tk.END, f"Item {i+1}")

addressLabel = tk.Label(root, text="Address:", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
addressLabel.place(x=10, y=100)


root.mainloop()
