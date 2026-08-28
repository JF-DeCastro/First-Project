import customtkinter
from PIL import ImageFilter, ImageTk, Image

class GuidePage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.show_guide()

    def show_guide(self):
        bg_image_path = "illustration-of-people-in-a-boat-in-a-flood.png"
        original_image = Image.open(bg_image_path)
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(2))

        self.bg_image = customtkinter.CTkImage(light_image=blurred_image, dark_image=blurred_image, size=(1700, 1100))

        self.bg_flood = customtkinter.CTkLabel(self, text="", image=self.bg_image)
        self.bg_flood.place(x=0, y=0, relwidth=1, relheight=1)

        self.guide_returnBTN = customtkinter.CTkButton(self.bg_flood,
                                                           text='Back',
                                                           text_color='white',
                                                           corner_radius=50,
                                                           bg_color='transparent',
                                                           fg_color='green',
                                                           hover_color='lime green',
                                                           border_width=1,
                                                           border_color='white',
                                                           command=lambda :self.controller.show_frame("MainHome"))
        self.guide_returnBTN.place(relx=0.1,
                                       rely=0.14,
                                       anchor='center')

        self.header = customtkinter.CTkButton(self.bg_flood, fg_color='green', border_color='light green', border_width=1,
                                        text="DISASTER PREPAREDNESS GUIDES", font=("Courier", 24, "bold"),
                                        text_color="#fef9f3", hover=False, width=1400, height=50)
        self.header.place(relx=.5,
                              rely=.06,
                              anchor="center")

        self.tabview = customtkinter.CTkTabview(self.bg_flood, width=1200, height=550, fg_color='#fef9f3', bg_color='#fef9f3',
                                          border_color='light gray',
                                          border_width=1, corner_radius=20,
                                          segmented_button_selected_color="#365899",
                                            segmented_button_unselected_color='#fef9f3',
                                          segmented_button_unselected_hover_color="#365899",
                                            segmented_button_fg_color='#fef9f3',
                                            text_color="black")

        self.tabview.place(relx=.5,
                               rely=.57,
                               anchor="center")

        self.tabview.add("Emergency Checklist")
        self.tabview.add("Family Plan")
        self.tabview.add("Emergency Drills")
        self.setup_checklist_tab()
        self.setup_family_plan_tab()
        self.setup_school_drills_tab()

    def setup_checklist_tab(self):
            checklist_items = [
                "Bottled drinkable water",
                "Non-perishable food (Canned goods, nuts, crackers, etc.)",
                "First-Aid kit (Bandages, Antiseptics)",
                "Personal items (Hygiene, Important Documents, Cash, Clothing)",
                "Battery-powered / hand-crank radio",
                "Flashlight",
                "Powerbank & Extra batteries",
                "Multi-purpose tool (Swiss Army Knife / Leatherman Wave)",
                "Emergency whistle"]

            self.go_bag_sticker2 = Image.open('go-bag.png')
            self.go_bag_sticker_resize = self.go_bag_sticker2.resize((500, 520))
            self.go_bag_sticker3 = ImageTk.PhotoImage(self.go_bag_sticker_resize)

            self.go_bag_sticker_main = customtkinter.CTkLabel(self.tabview.tab('Emergency Checklist'), image=self.go_bag_sticker3,
                                                    text='')
            self.go_bag_sticker_main.place(relx=0.75,
                                           rely=0.55,
                                           anchor='center')

            self.header_label = customtkinter.CTkLabel(
                self.tabview.tab("Emergency Checklist"),
                text="Essential Emergency Kit (Go-Bag):",
                font=("Segoe UI", 27, "bold"),
                text_color="#4267B2")
            self.header_label.pack(anchor="w", padx=20, pady=(15, 10))

            for item in checklist_items:
                checkbox = customtkinter.CTkCheckBox(
                    self.tabview.tab("Emergency Checklist"),
                    text=item,
                    font=("Segoe UI", 20, "bold"),
                    hover_color="lime green",
                    text_color="#3b444b",
                    fg_color="green",
                    border_width=2)
                checkbox.pack(anchor="w", padx=40, pady=6)

    def setup_family_plan_tab(self):
            """Content for the Communication Plan"""
            text = (
                "Family Communication Plan:\n\n"
                "1. Identify an out-of-town contact person.\n\n"
                "2. Establish a primary 'Safe Room' in the house.\n\n"
                "3. Designate a meeting place outside the neighborhood.\n\n"
                "4. Ensure every member has printed contact cards.")
            label = customtkinter.CTkLabel(
                self.tabview.tab("Family Plan"),
                text=text,
                justify="left",
                text_color="#3b444b",
                font=("Segoe UI", 26, "bold"),
                anchor="nw")
            label.pack(expand=True, fill="both", padx=20, pady=20)

    def setup_school_drills_tab(self):
            self.current_lang = "EN"

            self.drills_content = {
                "EN": (
                    "Standard Drill Procedures:\n\n"
                    "  ---Fire---\n: Evacuate immediately to designated zone.\n [On Fire]: Stop, Drop, and Roll to extinguish flames\n\n"
                    "  ---Earthquake---\n [During]: Drop, Cover, and Hold on.\n Evacuate to designated area\n\n"
                    "  ---Flood---\n: [Before]: Unplug all electrical appliances and prepare Go-Bag\n [During]: Avoid flooded areas\n: Safely evacuate to designated areas."
                ),
                "FIL": (
                    "Mga Pamamaraan sa Drill:\n\n"
                    "---Sunog---\n: Lumikas agad papunta sa itinalagang zone.\n [Nasusunog]: Tumigil, Dumapa, at Gumulong para mapatay ang apoy\n\n"
                    "---Lindol---\n [Habang May Lindol]: Dumapa, Sumuklong, at Kumapit.\n : Lumikas sa itinalagang lugar\n\n"
                    "---Baha---\n[Bago ang Baha]: Hugutin ang lahat ng de-kuryenteng kagamitan\n                            at ihanda ang Go-Bag.\n[Habang Bumabaha]: Iwasan ang mga lugar na may baha\n: Lumikas nang ligtas sa mga itinalagang lugar."
                )
            }

            tab = self.tabview.tab("Emergency Drills")

            self.lang_btn = customtkinter.CTkButton(tab,
                                          text="Switch to Filipino", command=self.toggle_language, width=150, height=32,
                                          fg_color="#4a4a4a", hover_color="#365899")
            self.lang_btn.pack(anchor="nw", padx=20, pady=(10, 0))

            self.drills_label = customtkinter.CTkLabel(tab, text=self.drills_content["EN"], justify="left",
                                             font=("Segoe UI", 19, "bold"), anchor="nw", text_color="#3b444b")
            self.drills_label.pack(expand=True, fill="both", padx=20, pady=20)

    def toggle_language(self):
            if self.current_lang == "EN":
                self.current_lang = "FIL"
                self.drills_label.configure(text=self.drills_content["FIL"])
                self.lang_btn.configure(text="Translate to English")
            else:
                self.current_lang = "EN"
                self.drills_label.configure(text=self.drills_content["EN"])
                self.lang_btn.configure(text="Translate to Filipino")