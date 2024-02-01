import tkinter as tk
from tkinter import filedialog
import subprocess 

class TextEditorAndCompiler(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fantastic IDE")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
       # self.logo = tk.PhotoImage(file="logo.png")
        #self.logo_label = tk.Label(self, image=self.logo)
        #self.logo_label.pack()

        self.open_button = tk.Button(self, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(self, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        self.run_button = tk.Button(self, text="Run", command=self.run_code)
        self.run_button.pack(side=tk.LEFT)

        self.code_input = tk.Text(self, wrap=tk.WORD)
        self.code_input.pack(expand=True, fill=tk.BOTH)

        self.code_output = tk.Text(self, wrap=tk.WORD)
        self.code_output.pack(expand=True, fill=tk.BOTH)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".py")
        if file_path:
            with open(file_path, "r") as file:
                self.code_input.delete("1.0", tk.END)
                self.code_input.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".py")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.code_input.get("1.0", tk.END))

    def run_code(self):
        try:
            code = self.code_input.get("1.0", tk.END)
            with open("temp.py", "w") as f:
                f.write(code)
            output = subprocess.check_output(["python", "temp.py"], stderr=subprocess.STDOUT).decode()
            self.code_output.delete("1.0", tk.END)
            self.code_output.insert(tk.END, output)
        except subprocess.CalledProcessError as e:
            self.code_output.delete("1.0", tk.END)
            self.code_output.insert(tk.END, f"Error: {str(e.output)}")
        

if __name__ == "__main__":
    app = TextEditorAndCompiler()
    app.mainloop()