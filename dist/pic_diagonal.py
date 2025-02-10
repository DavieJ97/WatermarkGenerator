import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk


def show_pic_diagonal(root, pic_url, text):
    def download_pic():
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
        if save_path:
            # Save the watermarked image
            watermarked_img.save(save_path)
            messagebox.showinfo("Image Saved", f"Image has been saved to {save_path}")
        on_close()
    
    def on_close():
        # Add any cleanup code here if needed
        top.destroy()
        root.deiconify()
    
    def on_enter(event):
        download_button.config(bg="#b4cece")

    def on_leave(event):
        download_button.config(bg="#e2ecec")

    top = tk.Toplevel(root)
    top.title("Image Viewer")
    top.config(bg="#e2ecec")
    top.wm_state("zoomed")
    top.protocol("WM_DELETE_WINDOW", on_close)

    container = tk.Frame(top)
    container.pack(fill="both", expand=True)

    # Add a frame inside the container
    content_frame = tk.Frame(container)
    content_frame.pack(fill="both", expand=True)


    try:
        img = Image.open(pic_url)
    except Exception as e:
        print(f"Error opening image: {e}")
        return
    img_width, img_height = img.size
    text_overlay = Image.new("RGBA", (img_width, img_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_overlay)
    font_path = "C:/Windows/Fonts/arial.ttf"  # Replace with the path to your .ttf font file
    text_size = int(min(img_width, img_height) * 0.5)
    try:
        font = ImageFont.truetype(font_path, text_size)  # Size 36
    except OSError:
        print("Font not found. Using default font.")
        font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (img_width - text_width) // 2
    y = (img_height - text_height) // 2
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
    rotated_text = text_overlay.rotate(45, expand=True)
    rotated_text = rotated_text.resize((img_width, img_height), Image.Resampling.LANCZOS)
    watermarked_img = Image.alpha_composite(img.convert("RGBA"), rotated_text)
    top.update_idletasks()
    height = int(top.winfo_height()/1.5)
    width = int(img_width * (height / img_height))
    resized_watermarked_img = watermarked_img.resize((width, height))

    img_tk = ImageTk.PhotoImage(resized_watermarked_img)
    img_label = tk.Label(content_frame, image=img_tk)
    img_label.image = img_tk
    img_label.pack()
    
    if img.width > 500:
        button_width = "500"
    else:
        button_width = f"{img.width}"
    download_button = tk.Button(content_frame, text="Download", width=button_width, font=("Great Vibes", 40), bg="#e2ecec", command=download_pic, fg="black")
    download_button.pack(pady=5)
    download_button.bind("<Enter>", on_enter)
    download_button.bind("<Leave>", on_leave)
    top.mainloop()


def show_pic_straight(root, pic_url, text):
    def download_pic():
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
        if save_path:
            # Save the watermarked image
            watermarked_img.save(save_path)
            messagebox.showinfo("Image Saved", f"Image has been saved to {save_path}")
        on_close()
    
    def on_close():
        # Add any cleanup code here if needed
        top.destroy()
        root.deiconify()
    
    def on_enter(event):
        download_button.config(bg="#b4cece")

    def on_leave(event):
        download_button.config(bg="#e2ecec")

    top = tk.Toplevel(root)
    top.title("Image Viewer")
    top.config(bg="#e2ecec")
    top.wm_state("zoomed")
    top.protocol("WM_DELETE_WINDOW", on_close)

    container = tk.Frame(top)
    container.pack(fill="both", expand=True)

    # Add a frame inside the container
    content_frame = tk.Frame(container)
    content_frame.pack(fill="both", expand=True)


    try:
        img = Image.open(pic_url)
    except Exception as e:
        print(f"Error opening image: {e}")
        return
    img_width, img_height = img.size
    text_overlay = Image.new("RGBA", (img_width, img_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_overlay)
    font_path = "C:/Windows/Fonts/arial.ttf"  # Replace with the path to your .ttf font file
    text_size = int(min(img_width, img_height) * 0.5)
    try:
        font = ImageFont.truetype(font_path, text_size)  # Size 36
    except OSError:
        print("Font not found. Using default font.")
        font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (img_width - text_width) // 2
    y = (img_height - text_height) // 2
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
    rotated_text = text_overlay
    rotated_text = rotated_text.resize((img_width, img_height), Image.Resampling.LANCZOS)
    watermarked_img = Image.alpha_composite(img.convert("RGBA"), rotated_text)
    top.update_idletasks()
    height = int(top.winfo_height()/1.5)
    width = int(img_width * (height / img_height))
    resized_watermarked_img = watermarked_img.resize((width, height))

    img_tk = ImageTk.PhotoImage(resized_watermarked_img)
    img_label = tk.Label(content_frame, image=img_tk)
    img_label.image = img_tk
    img_label.pack()
    
    if img.width > 500:
        button_width = "500"
    else:
        button_width = f"{img.width}"
    download_button = tk.Button(content_frame, text="Download", width=button_width, font=("Great Vibes", 40), bg="#e2ecec", command=download_pic, fg="black")
    download_button.pack(pady=5)
    download_button.bind("<Enter>", on_enter)
    download_button.bind("<Leave>", on_leave)
    top.mainloop()


def show_pic_bottem_right(root, pic_url, text):
    def download_pic():
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
        if save_path:
            # Save the watermarked image
            img.save(save_path)
            messagebox.showinfo("Image Saved", f"Image has been saved to {save_path}")
        on_close()
    
    def on_close():
        # Add any cleanup code here if needed
        top.destroy()
        root.deiconify()
    
    def on_enter(event):
        download_button.config(bg="#b4cece")

    def on_leave(event):
        download_button.config(bg="#e2ecec")

    top = tk.Toplevel(root)
    top.title("Image Viewer")
    top.config(bg="#e2ecec")
    top.wm_state("zoomed")
    top.protocol("WM_DELETE_WINDOW", on_close)

    container = tk.Frame(top)
    container.pack(fill="both", expand=True)

    # Add a frame inside the container
    content_frame = tk.Frame(container)
    content_frame.pack(fill="both", expand=True)


    try:
        img = Image.open(pic_url)
    except Exception as e:
        print(f"Error opening image: {e}")
        return
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img)
    font_path = "C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/GreatVibes-Regular.ttf"  # Replace with the path to your .ttf font file
    text_size = int(min(img_width, img_height) * 0.15)
    try:
        font = ImageFont.truetype(font_path, text_size)  # Size 36
    except OSError:
        print("Font not found. Using default font.")
        font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # width of the text
    text_height = text_bbox[3] - text_bbox[1]  # height of the text
    x = img_width - text_width - 10  # 10 pixels from the right edge
    y = img_height - text_height - 10  # 10 pixels from the bottom edge
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
    top.update_idletasks()
    height = int(top.winfo_height()/1.5)
    width = int(img_width * (height / img_height))
    resized_watermarked_img = img.resize((width, height))

    img_tk = ImageTk.PhotoImage(resized_watermarked_img)
    img_label = tk.Label(content_frame, image=img_tk)
    img_label.image = img_tk
    img_label.pack()
    
    if img.width > 500:
        button_width = "500"
    else:
        button_width = f"{img.width}"
    download_button = tk.Button(content_frame, text="Download", width=button_width, font=("Great Vibes", 40), bg="#e2ecec", command=download_pic, fg="black")
    download_button.pack(pady=5)
    download_button.bind("<Enter>", on_enter)
    download_button.bind("<Leave>", on_leave)
    top.mainloop()