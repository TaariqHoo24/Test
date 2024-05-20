import tkinter as tk

class ticket_booking_system:
    def __init__(self, master):
        self.master = master
        master.title('Ticket Booking System')

        self.adult_price = 15
        self.child_price = 5
        self.student_price = 10

        self.create_booking_system()

    def create_booking_system(self): 
        self.adult_label = tk.Label(self.master, text = 'Adult $15', font = ('Arial', 15))
        self.adult_label.grid(row = 0, column = 0, pady = 10, padx = 10, sticky = 'w')
        self.adult_entry = tk.Entry(root, font = ('Arial', 15))
        self.adult_entry.grid(row = 0, column = 1, pady = 10, padx = 10)

        self.child_label = tk.Label(self.master, text = 'Child $5', font = ('Arial', 15))
        self.child_label.grid(row = 1, column = 0, pady = 10, padx = 10, sticky = 'w')
        self.child_entry = tk.Entry(root, font = ('Arial', 15))
        self.child_entry.grid(row = 1, column = 1, pady = 10, padx = 10)

        self.student_label = tk.Label(self.master, text = 'Student/Senior $10', font = ('Arial', 15))
        self.student_label.grid(row = 2, column = 0, pady = 10, padx = 10, sticky = 'w')
        self.student_entry = tk.Entry(self.master, font = ('Arial', 15))
        self.student_entry.grid(row = 2, column = 1, pady = 10, padx = 10)

        self.total_price_button = tk.Button(self.master, text = 'Total Price:', font = ('Arial', 15, 'bold'), command = self.calc_total_price)
        self.total_price_button.grid(row = 3, column = 0, pady = 10, padx = 10, sticky = 'w')
        self.total_price_output_label = tk.Label(self.master, font = ('Arial', 15, 'bold'))
        self.total_price_output_label.grid(row = 3, column = 1, pady = 10, padx = 10)

    def calc_total_price(self):
        self.adult_quantity = int(self.adult_entry.get())
        self.child_quantity = int(self.child_entry.get())
        self.student_quantity = int(self.student_entry.get())

        total_price = (self.adult_quantity * self.adult_price) + (self.child_quantity * self.child_price) + (self.student_quantity * self.student_price)

        if self.adult_quantity + self.child_quantity + self.student_quantity > 100:
            self.total_price_output_label.config(text = 'Erorr: Only 100 tickets are available.')
        else:
            self.total_price_output_label.config(text = f'Total Price: ${total_price}')

root = tk.Tk()
booking_system = ticket_booking_system(root)
root.mainloop()