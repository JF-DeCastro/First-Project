import customtkinter
import json
import os
from datetime import datetime
from tkinter import messagebox

# --- Data Layer ---
class ReportService:
    def __init__(self, filename="local_reports.json"):
        self.filename = filename
        # Ensure the file exists
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def save_report(self, category, subject, description, address):
        if not subject or not description:
            raise ValueError("Subject and Description cannot be empty.")

        new_report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "category": category,
            "subject": subject,
            "description": description,
            "address": address
        }

        with open(self.filename, 'r+') as f:
            data = json.load(f)
            data.append(new_report)
            f.seek(0)
            json.dump(data, f, indent=4)

        return True


# --- UI Layer ---
class ReportApp(customtkinter.CTkFrame):
    def __init__(self, parent, controller, service=None):
        super().__init__(parent)
        self.controller = controller
        self.service = service

        self.configure(fg_color="#ebebeb")
        self.grid_columnconfigure(0, weight=1)
        self.setup_ui()

    def setup_ui(self):
        # Header
        self.header = customtkinter.CTkLabel(self, text="Submit Local Condition Report", text_color='black', font=("Arial", 24, "bold"))
        self.header.grid(row=0, column=0, pady=(30, 20))

        # Category Selection (Row 1-2)
        self.cat_label = customtkinter.CTkLabel(self, text="Report Category", text_color='black')
        self.cat_label.grid(row=1, column=0, padx=40, sticky="w")
        self.cat_option = customtkinter.CTkOptionMenu(self, values=["Dirty Air, Water, and Land (Pollution)", " Trash and Garbage Problems", "Harming Nature and Trees", "Running Out of Resources and Bad Weather"], height=40)
        self.cat_option.grid(row=2, column=0, padx=40, pady=(5, 15), sticky="ew")

        # Subject Input (Row 3-4)
        self.sub_label = customtkinter.CTkLabel(self, text="Subject", text_color='black')
        self.sub_label.grid(row=3, column=0, padx=40, sticky="w")
        self.sub_entry = customtkinter.CTkEntry(self, text_color='black', placeholder_text="Enter brief summary...", fg_color='#dcdcdc', border_width=2, border_color='gray', height=40)
        self.sub_entry.grid(row=4, column=0, padx=40, pady=(5, 15), sticky="ew")

        # --- ADDRESS INPUT (New Section - Row 5-6) ---
        self.addr_label = customtkinter.CTkLabel(self, text="Address / Location", text_color='black')
        self.addr_label.grid(row=5, column=0, padx=40, sticky="w")
        self.addr_entry = customtkinter.CTkEntry(self, text_color='black', placeholder_text="Street, City, or Landmark...", fg_color='#dcdcdc', border_width=2, border_color='gray', height=40)
        self.addr_entry.grid(row=6, column=0, padx=40, pady=(5, 15), sticky="ew")

        # Description Input (Row 7-8)
        self.desc_label = customtkinter.CTkLabel(self, text="Description", text_color='black')
        self.desc_label.grid(row=7, column=0, padx=40, sticky="w")
        self.desc_text = customtkinter.CTkTextbox(self, text_color='black', height=150, fg_color='#dcdcdc', border_width=2, border_color='gray')
        self.desc_text.grid(row=8, column=0, padx=40, pady=(5, 20), sticky="ew")

        # Submit Button (Row 9)
        self.submit_btn = customtkinter.CTkButton(self, text="Submit Report", command=self.handle_submit)
        self.submit_btn.grid(row=9, column=0, pady=20)

        # Back Button (Remains placed relatively)
        self.report_returnBTN = customtkinter.CTkButton(self, text='Back', text_color='white', corner_radius=50, bg_color='transparent', fg_color='green', hover_color='lime green', border_width=1, border_color='white', command=lambda: self.controller.show_frame("MainHome"))
        self.report_returnBTN.place(relx=0.1, rely=0.06, anchor='center')

    def handle_submit(self):
        category = self.cat_option.get()
        subject = self.sub_entry.get()
        description = self.desc_text.get("1.0", "end-1c")
        address = self.addr_entry.get() # Updated to get from addr_entry

        try:
            if self.controller.service:
                self.controller.service.save_report(category, subject, description, address)
                messagebox.showinfo("Success", "Report saved successfully.")
                self.clear_form()
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def clear_form(self):
        """Resets the UI fields."""
        self.sub_entry.delete(0, 'end')
        self.addr_entry.delete(0, 'end') # Clear address
        self.desc_text.delete("1.0", "end")



