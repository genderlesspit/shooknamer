import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF
from PIL import Image, ImageTk

class PDFViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Viewer")
        self.master.geometry("800x600")

        self.canvas = tk.Canvas(master, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.btn_frame = tk.Frame(master)
        self.btn_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.open_button = tk.Button(self.btn_frame, text="Open PDF", command=self.open_pdf)
        self.open_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.next_button = tk.Button(self.btn_frame, text="Next Page", command=self.next_page)
        self.next_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.prev_button = tk.Button(self.btn_frame, text="Previous Page", command=self.prev_page)
        self.prev_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.current_page = 0
        self.pdf_document = None

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_document = fitz.open(file_path)
            self.current_page = 0
            self.show_page()

    def show_page(self):
        if self.pdf_document is not None and 0 <= self.current_page < len(self.pdf_document):
            page = self.pdf_document[self.current_page]
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            self.img_tk = ImageTk.PhotoImage(img)

            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
            self.master.title(f"PDF Viewer - Page {self.current_page + 1}")

    def next_page(self):
        if self.pdf_document and self.current_page < len(self.pdf_document) - 1:
            self.current_page += 1
            self.show_page()

    def prev_page(self):
        if self.pdf_document and self.current_page > 0:
            self.current_page -= 1
            self.show_page()

if __name__ == "__main__":
    root = tk.Tk()
    viewer = PDFViewer(root)
    root.mainloop()
