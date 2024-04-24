import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataVisualizationApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Data Visualization App")

        self.data = []
        self.chart_type = tk.StringVar()
        self.chart_type.set("Pie Chart")

        self.create_widgets()

    def create_widgets(self):
        # Data input frame
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Data Type:").grid(row=0, column=0, padx=5, pady=5)
        self.data_type_entry = tk.Entry(input_frame)
        self.data_type_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Value:").grid(row=1, column=0, padx=5, pady=5)
        self.value_entry = tk.Entry(input_frame)
        self.value_entry.grid(row=1, column=1, padx=5, pady=5)

        add_button = tk.Button(input_frame, text="Add Data", command=self.add_data)
        add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Chart selection frame
        chart_frame = tk.Frame(self)
        chart_frame.pack(pady=10)

        tk.Label(chart_frame, text="Select Chart Type:").grid(row=0, column=0, padx=5, pady=5)
        chart_types = ["Pie Chart", "Column Chart", "Bar Chart", "Line Chart"]
        for i, chart_type in enumerate(chart_types):
            tk.Radiobutton(chart_frame, text=chart_type, variable=self.chart_type, value=chart_type).grid(row=i+1, column=0, padx=5, pady=2)

        generate_button = tk.Button(chart_frame, text="Generate Chart", command=self.generate_chart)
        generate_button.grid(row=len(chart_types)+1, column=0, padx=5, pady=5)

    def add_data(self):
        data_type = self.data_type_entry.get()
        value = self.value_entry.get()

        if data_type and value:
            try:
                value = float(value)
                self.data.append((data_type, value))
                messagebox.showinfo("Success", "Data added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Invalid value! Please enter a numeric value.")
        else:
            messagebox.showerror("Error", "Please enter data type and value.")

        self.data_type_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)

    def generate_chart(self):
        if not self.data:
            messagebox.showerror("Error", "No data available!")
            return

        chart_type = self.chart_type.get()
        labels, values = zip(*self.data)

        plt.figure(figsize=(8, 6))

        if chart_type == "Pie Chart":
            plt.pie(values, labels=labels, autopct='%1.1f%%')
        elif chart_type == "Column Chart":
            plt.bar(labels, values)
        elif chart_type == "Bar Chart":
            plt.barh(labels, values)
        elif chart_type == "Line Chart":
            plt.plot(labels, values)

        plt.title(chart_type)
        plt.xlabel("Data Type")
        plt.ylabel("Value")

        plt.tight_layout()

        # Embedding the chart in tkinter window
        chart_canvas = FigureCanvasTkAgg(plt.gcf(), self)
        chart_canvas.draw()
        chart_canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = DataVisualizationApp()
    app.mainloop()
