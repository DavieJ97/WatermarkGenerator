import tkinter as tk
from tkinter import filedialog
from pic_diagonal import show_pic_diagonal, show_pic_straight, show_pic_bottem_right
from PIL import Image, ImageTk
import os
import sys

class Main_display:
    def __init__(self, root):
        self.root = root
        self.selected_var = tk.IntVar()
        self.root.title("My WaterMarking App")
        self.root.config(bg="#e2ecec")
        img_path = os.path.join("pics", "Perfect Watermark.png")
        self.img = Image.open(img_path)
        self.root.geometry(f"{self.img.width}x700")
        self.root.wm_state("zoomed")
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.container)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.content_frame = tk.Frame(self.canvas)

        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")
        self.content_frame.config(bg="#e2ecec")

        self.content_frame.bind("<Configure>", self.update_scroll_region)

        img_tk = ImageTk.PhotoImage(self.img)
        self.top_image = tk.Label(self.content_frame, image=img_tk, bg="#e2ecec")
        self.top_image.image = img_tk
        self.top_image.pack()
        self.selected_var = tk.IntVar()
        folder_path = os.path.join("C:", "sample_pics")
        for i, filename in enumerate(os.listdir(folder_path)):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                file_path = os.path.join(folder_path, filename)
                try:
                    img = Image.open(file_path)
                    img.thumbnail((500, 500))  # Resize for display

                    img_tk = ImageTk.PhotoImage(img)

                    button = tk.Radiobutton(
                        self.content_frame,
                        image=img_tk,
                        variable=self.selected_var,
                        value=i,
                        bg="#e2ecec",
                        indicatoron=False  # Makes the button look like a normal button
                    )
                    button.image = img_tk  # Keep a reference to avoid garbage collection
                    button.pack(pady=10)
                except Exception as e:
                    print(f"Error loading image {filename}: {e}")        

        self.watermark_text = tk.Entry(self.content_frame, width=20, fg="grey", font=("Libra Baskerville", 40))
        self.watermark_text.insert(0, "Enter text")
        self.watermark_text.bind("<FocusIn>", self.on_entry_focus_in)
        self.watermark_text.bind("<FocusOut>", self.on_entry_focus_out)
        self.watermark_text.pack(pady=10)

        self.text_size_label = tk.Label(self.content_frame, text="Choose the size of your text.", font=("Libra Baskerville", 30))
        self.text_size_label.pack(pady=10)
        self.text_size_bar = tk.Scale(self.content_frame, from_=11, to=170, orient="horizontal", length=700)
        self.text_size_bar.pack(pady=5)

        self.choose_image_label = tk.Label(self.content_frame, text="Choose an Image", font=("Great Vibes", 40), bg="#e2ecec")
        self.choose_image_label.pack()

        self.choose_image_button = tk.Button(
            self.content_frame, 
            text="Browse for Images",
            activebackground="grey",
            relief="raised",
            bg="#e2ecec",
            fg="black",
            font=("Great Vibes", 30),
            width=40,
            command=self.choose_image
            )
        self.choose_image_button.pack()
        self.choose_image_button.bind("<Enter>", self.on_enter)
        self.choose_image_button.bind("<Leave>", self.on_leave)
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        


    def on_enter(self, event):
        self.choose_image_button.config(bg="#b4cece")

    def on_leave(self, event):
        self.choose_image_button.config(bg="#e2ecec")

    def choose_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files","*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
            )
        if file_path:
            watermark_text = self.watermark_text.get()
            text_size = self.text_size_bar.get()
            self.root.withdraw()
            selected_value = self.selected_var.get()
            if selected_value == 0:
                show_pic_diagonal(root=self.root, pic_url=file_path, text=watermark_text, text_size=text_size) 
            elif selected_value == 1:
                show_pic_straight(root=self.root, pic_url=file_path, text=watermark_text, text_size=text_size)
            elif selected_value == 2:
                show_pic_bottem_right(root= self.root, pic_url=file_path, text=watermark_text, text_size=text_size)
    
    def on_entry_focus_in(self, event):
        if event.widget.get() == "Enter text":  # Placeholder text
            event.widget.delete(0, tk.END)  # Clear the placeholder
            event.widget.config(fg="black")  # Change text colour to black

    def on_entry_focus_out(self, event):
        if not event.widget.get():  # If the entry is empty
            event.widget.insert(0, "Enter text")  # Restore placeholder
            event.widget.config(fg="grey")  # Change text colour to grey
    
    def update_scroll_region(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def close_window(self):
        self.root.destroy() 

    def resource_path(self, relative_path):
        try:
            # Check if we're running as a packaged .exe
            base_path = sys._MEIPASS
        except Exception:
            # If not, use the current directory (for development)
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    root = tk.Tk()            
    app = Main_display(root)
    root.mainloop()    



