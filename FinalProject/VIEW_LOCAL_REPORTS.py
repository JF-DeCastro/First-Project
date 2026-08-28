import customtkinter as ctk
import json
import os

class ReportService:
    def __init__(self, filename="local_reports.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def save_report(self, category, subject, description, address):
        reports = self.get_all_reports()
        reports.append({"category": category, "subject": subject, "description": description, "address": address})
        with open(self.filename, 'w') as f:
            json.dump(reports, f, indent=4)

    def get_all_reports(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except Exception:
            return []

    def delete_report(self, index):
        reports = self.get_all_reports()
        if 0 <= index < len(reports):
            reports.pop(index)
            with open(self.filename, 'w') as f:
                json.dump(reports, f, indent=4)
            return True
        return False

class ReportApp(ctk.CTk):
    def __init__(self, service):
        super().__init__()
        self.service = service
        self.title("Local Report Service")
        self.geometry("600x700")

        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Stored Reports")
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.refresh_btn = ctk.CTkButton(self, text="Refresh/View Reports", command=self.display_reports)
        self.refresh_btn.pack(pady=10)

    def handle_delete(self, index):
        if self.service.delete_report(index):
            self.display_reports() # Refresh the list after deleting

    def display_reports(self):
        # Clear existing widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        reports = self.service.get_all_reports()

        if not reports:
            ctk.CTkLabel(self.scrollable_frame, text="No reports found.", font=("Arial", 14)).pack(pady=20)
            return

        for i, report in enumerate(reports):
            # Main Card Container
            card = ctk.CTkFrame(self.scrollable_frame, corner_radius=10)
            card.pack(pady=10, padx=10, fill="x")

            # Content container (Left Side)
            text_frame = ctk.CTkFrame(card, fg_color="transparent")
            text_frame.pack(side="left", fill="both", expand=True, padx=15, pady=10)

            # 1. Category & Subject (Bold Header)
            header_text = f"[{report.get('category', 'N/A')}] {report.get('subject', 'No Subject')}"
            ctk.CTkLabel(text_frame, text=header_text, font=("Arial", 15, "bold"), text_color="#1f538d").pack(anchor="w")

            # 2. Address (With a small label for clarity)
            address_text = f"📍 Location: {report.get('address', 'No address provided')}"
            ctk.CTkLabel(text_frame, text=address_text, font=("Arial", 12, "italic"), text_color="gray").pack(anchor="w", pady=(2, 5))

            # 3. Description
            desc_text = report.get('description', 'No description.')
            ctk.CTkLabel(text_frame, text=desc_text, wraplength=400, justify="left").pack(anchor="w")

            # Delete button (Right Side)
            del_btn = ctk.CTkButton(card,
                                    text="Delete",
                                    width=70,
                                    height=30,
                                    fg_color="#cc3333",
                                    hover_color="#992222",
                                    command=lambda i=i: self.handle_delete(i))
            del_btn.pack(side="right", padx=15)


service = ReportService()
app = ReportApp(service)
app.mainloop()
