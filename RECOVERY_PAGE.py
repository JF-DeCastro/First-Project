import customtkinter
from datetime import datetime
import calendar

class RecoveryPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="#ebebeb")
        self.show_recovery()

    def show_recovery(self):
        self.main_recoverframe = customtkinter.CTkFrame(self, fg_color="#ebebeb")
        self.main_recoverframe.pack(fill="both", expand=True)

        # Call setup functions
        self.setup_sidebar()
        self.setup_main_container()
        self.create_relief_page()
        self.create_counselling_page()
        self.create_support_page()

        self.update_time()
        self.build_view_only_calendar()

        # Initial view
        self.show_frame("relief")

    def setup_sidebar(self):
        # Sidebar: Left side, 20% width, full height
        self.sidebar = customtkinter.CTkFrame(self.main_recoverframe, corner_radius=0, fg_color='#ebebeb')
        self.sidebar.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        self.recover_returnBTN = customtkinter.CTkButton(self.sidebar,
                                                         text='Back',
                                                         text_color='white',
                                                         corner_radius=50,
                                                         bg_color='transparent',
                                                         fg_color='green',
                                                         hover_color='lime green',
                                                         border_width=1,
                                                         border_color='white',
                                                         height=20,
                                                         width=20,
                                                         command=lambda: self.controller.show_frame("MainHome"))
        self.recover_returnBTN.place(relx=0.075, rely=0.035)


        # Logo: Top center of sidebar
        self.logo = customtkinter.CTkLabel(self.sidebar, text="SafeLink", font=("Arial", 20, "bold"), text_color="black")
        self.logo.place(relx=0.5, rely=0.05, anchor="center")

        # Navigation Buttons: Stacked vertically
        self.btn_relief = customtkinter.CTkButton(self.sidebar, text="Relief Schedules",
                                                  command=lambda: self.show_frame("relief"), text_color="black")
        self.btn_relief.place(relx=0.5, rely=0.15, anchor="center", relwidth=0.8)

        self.btn_counsel = customtkinter.CTkButton(self.sidebar, text="Counselling Services",
                                                   command=lambda: self.show_frame("counsel"), text_color="black")
        self.btn_counsel.place(relx=0.5, rely=0.22, anchor="center", relwidth=0.8)

        self.btn_support = customtkinter.CTkButton(self.sidebar, text="Support Programs",
                                                   command=lambda: self.show_frame("support"), text_color="black")
        self.btn_support.place(relx=0.5, rely=0.29, anchor="center", relwidth=0.8)

        # Time Label: Bottom of sidebar
        self.time_label = customtkinter.CTkLabel(self.sidebar, text="", font=("Arial", 15, "bold"), text_color="black")
        self.time_label.place(relx=0.5, rely=0.85, anchor="center")

    def setup_main_container(self):
        # Main View: Right side, starting from 20%, taking rest of width
        self.main_view = customtkinter.CTkFrame(self.main_recoverframe, width=990, height=600, corner_radius=15,
                                                border_width=1, fg_color="#fef9f3")
        self.main_view.place(relx=0.22, rely=0.05)

        # Title: Top of main view
        self.title_label = customtkinter.CTkLabel(self.main_view, text="POST DISASTER RESOURCES",
                                                  font=("Arial Black", 30, "bold"), text_color="black")
        self.title_label.place(relx=0.5, rely=0.06, anchor="center")

        # Content Frames: These will be toggled in show_frame
        # We give them a specific spot inside main_view
        self.relief_frame = customtkinter.CTkFrame(self.main_view, fg_color="transparent")
        self.counsel_frame = customtkinter.CTkFrame(self.main_view, fg_color="transparent")
        self.support_frame = customtkinter.CTkFrame(self.main_view, fg_color="transparent")

    def create_relief_page(self):
        # 1. Define the Data (Location: Schedule)
        self.schedules = {
            'Agoncillo': "No relief schedule for this area yet.",
            'Alitagtag': "No relief schedule for this area yet.",
            'Balayan': "No relief schedule for this area yet.",
            'Balete': "No relief schedule for this area yet.",
            'Bauan': "Location: Barangay Sta. Maria, Bauan:\n- May 10, 2026\n- 1:00 PM at Brgy. Sta.Maria \nCovered Court",
            'Calatagan': "No relief schedule for this area yet.",
            'Cuenca': "No relief schedule for this area yet.",
            'Ibaan': "No relief schedule for this area yet.",
            'Laurel': "No relief schedule for this area yet.",
            'Lemery': "No relief schedule for this area yet.",
            'Lian': "No relief schedule for this area yet.",
            'Lobo': "No relief schedule for this area yet.",
            'Mabini': "No relief schedule for this area yet.",
            'Malvar': "No relief schedule for this area yet.",
            'Mataasnakahoy': "No relief schedule for this area yet.",
            'Nasugbu': "No relief schedule for this area yet.",
            'Padre': "No relief schedule for this area yet.",
            'Garcia': "No relief schedule for this area yet.",
            'Rosario': "No relief schedule for this area yet.",
            'San Jose': "No relief schedule for this area yet.",
            'San Juan': "No relief schedule for this area yet.",
            'San Luis': "No relief schedule for this area yet.",
            'San Nicolas': "No relief schedule for this area yet.",
            'San Pascual': "Location: Barangay Sambat, San Pascual:\n- May 10, 2026\n- 9:00 PM at Brgy. Sambat \nCovered Court\n\n"
                           "Location: Barangay Mataas na Lupa, San Pascual:\n- May 10, 2026\n- 3:00 PM at Brgy. Mataas na Lupa \nEvent Center\n\n",
            'Santa Teresita': "No relief schedule for this area yet.",
            'Taal': "No relief schedule for this area yet.",
            'Talisay': "No relief schedule for this area yet.",
            'Taysan': "No relief schedule for this area yet.",
            'Tingloy': "No relief schedule for this area yet.",
            'Tuy': "No relief schedule for this area yet.",
        }

        self.loc_scroll_frame = customtkinter.CTkScrollableFrame(self.relief_frame, width=200, height=350,
                                                                 label_text="Locations", fg_color="#fef9f3")
        self.loc_scroll_frame.place(relx=0.03, rely=0.45, anchor="w")

        for loc in self.schedules.keys():
            btn = customtkinter.CTkButton(
                self.loc_scroll_frame,
                text=loc,
                fg_color="transparent",
                text_color="black",
                hover_color="#8E94F2",
                anchor="w",
                command=lambda l=loc: self.update_schedule_display(l)
            )
            btn.pack(fill="x", pady=2)

        # 2. Right Side: The Display Area (NOW A SCROLLABLE FRAME)
        self.header_label = customtkinter.CTkLabel(self.relief_frame, text="RELIEF SCHEDULES",
                                                   font=("Arial Black", 30, "bold"), text_color="black")
        self.header_label.place(relx=0.65, rely=0.02, anchor="center")

        # Replaced CTkTextbox with CTkScrollableFrame
        self.display_scroll = customtkinter.CTkScrollableFrame(self.relief_frame, width=620, height=300,
                                                               corner_radius=15, border_width=1,
                                                               fg_color="#fef9f3", label_text="Schedule Details")
        self.display_scroll.place(relx=0.6255, rely=0.5, anchor="center")

        # Initialize with the first location's data
        self.update_schedule_display(list(self.schedules.keys())[0])

    def update_schedule_display(self, selected_location):
        """Clears the scrollable frame and adds new labels based on selection"""

        # 1. Clear all existing widgets inside the display scroll
        for widget in self.display_scroll.winfo_children():
            widget.destroy()

        # 2. Get data from dictionary
        info = self.schedules.get(selected_location, "No data available.")

        # 3. Create a new label inside the scrollable frame
        # We use wraplength so the text doesn't go off the edge
        schedule_label = customtkinter.CTkLabel(
            self.display_scroll,
            text=info,
            font=("Segoe UI", 20),
            text_color="black",
            justify="left",
            anchor="nw",
            wraplength=650  # Ensures text wraps inside the 700px width
        )
        schedule_label.pack(fill="both", expand=True, padx=20, pady=20)

    def create_counselling_page(self):
        customtkinter.CTkLabel(self.counsel_frame, text="Available Counselling Services", font=("Arial", 25), text_color='black').pack(
            pady=20)
        customtkinter.CTkLabel(self.counsel_frame, text_color='black',text="\n"
                                                        "Jesus of Nazareth Hospital  -  Gov. Antonio Carpio Rd, Batangas City, Batangas |  0437234144\n\n\n"
                                                        "Batangas Medical Center  -  Bihi Road, Batangas City, 4200 Batangas |  0437408307\n\n\n"
                                                        "Mvisions Psychological Center  -  C&N Calangi Building, P.Canlapan, Poblacion 9, Batangas City, Batangas |  09153848486\n\n\n"
                                                        "PowerMinds Psychological Wellness Center  -  Barbosa Residences, Shilling St, Hilltop Rd, Batangas City |  09204374184\n\n\n"
                                                        "Southwest Therapy Center  -  Batangas Healthcare Specialist Medical Center, Diversion Road, Batangas City |  09672288132\n\n\n"
                                                        "HealSpace Psychological Clinic  -  Jiao Medical Clinic, Lobrin Subdivision, Sico, Lipa City, 4217 Batangas |  09270349050\n\n\n"
                                                        "Philippine Mental Health Association Batangas Chapter  -  A. Bonifacio St., Brgy. 10, Lipa City, Batangas |  09676423610\n\n\n"
                                                        "Psych Counseling and Health Support Services (Tanauan City Branch)  -  Filenvest, Darasa, Tanauan City, Batangas |  09542517813\n\n\n"
                               ).pack()

    def create_support_page(self):
        customtkinter.CTkLabel(self.support_frame, text="Community Support Programs", font=("Arial", 25), text_color='black').pack(pady=20)
        customtkinter.CTkLabel(self.support_frame, text_color='black',text="\n"
                                                        "Philippine Red Cross (Batangas Chapter)  -  Capitol Site, Batangas City, 4200 Batangas |  0437233027\n\n\n"
                                                        "Philippine Red Cross Lipa Branch  -  D.P. Laygo St, Lipa City, 4217 Batangas |  0437400768\n\n\n"
                                                        "Philippine Mental Health Association Batangas Chapter  -  A. Bonifacio St., Brgy. 10, Lipa City, Batangas |  09676423610\n\n\n"
                                                        "Provincial Social Welfare and Development Office  -  Capitol Hills, Batangas City, 4200 Batangas |  0437234024\n\n\n"
                                                        "Philippine Mental Health Association Batangas Chapter  -  A. Bonifacio St., Brgy. 10, Lipa City, Batangas |  09676423610\n\n\n"
                                                        "Batangas Lions Club INC.  -  Rafael Road, Nazareth Compound, Barangay Gulod Itaas, Batangas City, Batangas |  09456011942\n\n\n"
                               ).pack()

    def show_frame(self, page_name):
        # Hide current pages
        self.relief_frame.place_forget()
        self.counsel_frame.place_forget()
        self.support_frame.place_forget()

        inactive_color = "#BDBDBD"
        active_color = "#8E94F2"
        self.btn_relief.configure(fg_color=inactive_color)
        self.btn_counsel.configure(fg_color=inactive_color)
        self.btn_support.configure(fg_color=inactive_color)

        # Show selected page at the standard content position
        if page_name == "relief":
            self.relief_frame.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)
        elif page_name == "counsel":
            self.counsel_frame.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)
        elif page_name == "support":
            self.support_frame.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)

    def update_time(self):
        # Update the label with real-time date and time
        now = datetime.now().strftime("%B %d, %Y\n%I:%M:%S %p")
        self.time_label.configure(text=f"{now}\n📍 San Pascual, Batangas")

        # Schedule the next update in 1000ms (1 second)
        self.after(1000, self.update_time)

    def build_view_only_calendar(self):
        # 1. Prepare calendar data
        now = datetime.now()
        year, month = now.year, now.month
        cal_data = calendar.monthcalendar(year, month)
        month_name = calendar.month_name[month]

        # 2. Create the container frame (placing it in sidebar for this example)
        self.cal_container = customtkinter.CTkFrame(self.sidebar, fg_color="white", corner_radius=10)
        self.cal_container.place(relx=0.15, rely=0.4)

        # 3. Header with Month and Year
        header = customtkinter.CTkLabel(self.cal_container, text=f"{month_name} {year}",
                                        font=("Arial", 14, "bold"), fg_color="#3498db", text_color="white",
                                        corner_radius=5)
        header.pack(fill="x", pady=(0, 5))

        # 4. Grid for Days
        days_frame = customtkinter.CTkFrame(self.cal_container, fg_color="transparent")
        days_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Day of the week headers
        for i, day in enumerate(["M", "T", "W", "T", "F", "S", "S"]):
            customtkinter.CTkLabel(days_frame, text=day, font=("Arial", 10, "bold"),
                                   text_color="gray").grid(row=0, column=i, sticky="nsew")

        # 5. Populate the days
        for r, week in enumerate(cal_data):
            for c, day in enumerate(week):
                if day != 0:
                    # Highlight current day with emergency orange or your theme's blue
                    is_today = (day == now.day)
                    bg = "#f1c40f" if is_today else "transparent"
                    txt_color = "black" if is_today else "gray20"

                    (customtkinter.CTkLabel(days_frame, text=str(day), fg_color=bg,
                               text_color=txt_color, corner_radius=5, width=25).grid(row=r + 1, column=c, pady=2))

        # Ensure grid is responsive
        for i in range(7): days_frame.grid_columnconfigure(i, weight=1)