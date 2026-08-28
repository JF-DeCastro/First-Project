import customtkinter
from PIL import ImageFilter, ImageTk, Image
import requests
from datetime import datetime


class MainHome(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller


        self.bg_photo = Image.open('bg_ambulance.jpeg')
        self.blurred_photo = self.bg_photo.filter(ImageFilter.GaussianBlur(30)).resize((1700,1100))
        self.final_bg = ImageTk.PhotoImage(self.blurred_photo)

        self.bg_label = customtkinter.CTkLabel(self,
                                               text='',
                                               image=self.final_bg)
        self.bg_label.place(relx=-0.017,
                            rely=-0.13)

        self.main_frame = customtkinter.CTkButton(self.bg_label,
                                                  corner_radius=30,
                                                  fg_color='#fef9f3',
                                                  bg_color='transparent',
                                                  width=1100,
                                                  height=600,
                                                  hover=False)
        self.main_frame.place(relx=0.5,
                              rely=0.5,
                              anchor='center')


        self.main_widgets()

    def main_widgets(self):
        self.dashboards()
        self.map_widget()
        self.guide_widget()
        self.local_widgets()
        self.learn_widgets()
        self.recover_widgets()

        self.safelink = customtkinter.CTkLabel(self.main_frame,
                                               text='Safe Link',
                                               font=('Segoe UI Black', 30, 'bold'),
                                               text_color='black')
        self.safelink.place(relx=0.2,
                            rely=0.08,
                            anchor='center')



        self.dialogue2 = customtkinter.CTkLabel(self.main_frame,
                                                text='Be ready. Keep safe.\n\n\n\n\n\n\n\n'
                                                     'Be Alert.',
                                                justify='left',
                                                font=('Nirmala UI', 19,  'roman'),
                                                text_color='#414a4c',
                                                bg_color='transparent')
        self.dialogue2.place(relx=0.13,
                             rely=0.29)

        self.dialogue = customtkinter.CTkLabel(self.main_frame,
                                               text='YOUR PORTAL LINKED\n'
                                                    'TO SAFETY AND\n'
                                                    'READINESS',
                                               justify='left',
                                               font=('Arial Black', 40, 'bold'),
                                               text_color='black')
        self.dialogue.place(relx=0.36,
                            rely=0.48,
                            anchor='center')

        self.overview = customtkinter.CTkButton(self.main_frame,
                                                text='Overview',
                                                font=('Arial Black', 12),
                                                bg_color='transparent',
                                                fg_color='blue',
                                                border_color='blue',
                                                border_width=0,
                                                corner_radius=10,
                                                height=50,
                                                width=100,
                                                command=lambda :self.controller.show_frame('OverviewPage'))
        self.overview.place(relx=0.83,
                            rely=0.083,
                            anchor='center')

    def dashboards(self):
        self.alert_label = customtkinter.CTkButton(self.main_frame,
                                                   text="Checking for alerts...",
                                                   font=('Arial Black', 25, 'bold'),
                                                   text_color='black',
                                                   fg_color="#fef9f3",
                                                   bg_color="#fef9f3",
                                                   border_width=5,
                                                   corner_radius=20,
                                                   border_color='gray',
                                                   height=90,
                                                   width=20,
                                                   hover=False)


        self.alert_label.place(relx=0.65,
                               rely=0.3)


        try:
            data = requests.get("https://usgs.gov").json()
            self.alert_label.configure(text=f"Latest Event: {data['features'][0]['properties']['title']}",
                                       font=('Arial Black', 25, 'bold'),
                                       text_color='black',
                                       fg_color="#fef9f3",
                                       bg_color="#fef9f3",
                                       border_width=5,
                                       corner_radius=20,
                                       border_color='red',
                                       height=90,
                                       width=20,
                                       hover=False)
            pass
        except Exception:
            self.alert_label.configure(text="Typhoon Warning",
                                       font=('Arial Black', 25, 'bold'),
                                       text_color='black',
                                       fg_color="white",
                                       bg_color="#fef9f3",
                                       border_width=5,
                                       corner_radius=20,
                                       border_color='red',
                                       height=90,
                                       width=20,
                                       hover=False
                                       )
        self.after(300000, self.dashboards)

        self.info_frame = customtkinter.CTkFrame(self.main_frame,
                                                 height=250,
                                                 width=300,
                                                 corner_radius=10,
                                                 border_width=4,
                                                 border_color='#e7decc',
                                                 bg_color='#fef9f3',
                                                 fg_color='#fdf6e4')
        self.info_frame.place(relx=0.6,
                              rely=0.5)

        self.location_label = customtkinter.CTkLabel(self.info_frame, text="Auto-detecting...", font=("Arial", 14, "italic"), text_color='black')
        self.location_label.place(relx=0.5, rely=0.1, anchor="center")

        # 2. Date/Time Label - Upper middle
        self.date_label = customtkinter.CTkLabel(self.info_frame, text="", font=("Arial", 24, "bold"), text_color='black')
        self.date_label.place(relx=0.5, rely=0.25, anchor="center")

        # 3. Weather Stats - Middle
        self.temp_label = customtkinter.CTkLabel(self.info_frame, text="Temp: --", font=("Arial", 18), text_color='black')
        self.temp_label.place(relx=0.5, rely=0.45, anchor="center")

        self.hum_label = customtkinter.CTkLabel(self.info_frame, text="Humidity: --", font=("Arial", 18), text_color='black')
        self.hum_label.place(relx=0.5, rely=0.55, anchor="center")

        # 4. Manual City Entry - Lower middle
        self.city_entry = customtkinter.CTkEntry(self.info_frame, text_color='black', placeholder_text="Enter City (e.g. Batangas)", fg_color='#f5fefd', border_color='#fff1e6')
        self.city_entry.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.7)

        # 5. Refresh Button - Bottom
        self.refresh_btn = customtkinter.CTkButton(self.info_frame, text="Refresh Weather", border_color='white', fg_color='#63c5da', text_color='#1f201f',border_width=2, command=self.update_weather)
        self.refresh_btn.place(relx=0.5, rely=0.85, anchor="center")

        self.update_clock()
        self.update_weather()

    def map_widget(self):
        self.map_button = customtkinter.CTkButton(self.main_frame,
                                                  font=('Calbiri', 13),
                                                  text='Map',
                                                  text_color='black',
                                                  height=50,
                                                  width=60,
                                                  border_width=0,
                                                  border_color='black',
                                                  bg_color='transparent',
                                                  fg_color='transparent',
                                                  hover_color='light gray',
                                                  command=lambda :self.controller.show_frame("MapPage"))
        self.map_button.place(relx=0.34,
                              rely=0.083,
                              anchor='center')

    def guide_widget(self):
        self.guide_button = customtkinter.CTkButton(self.main_frame,
                                                    font=('Calbiri', 13),
                                                    text='Guide',
                                                    text_color='black',
                                                    height=50,
                                                    width=60,
                                                    border_width=0,
                                                    border_color='black',
                                                    bg_color='transparent',
                                                    fg_color='transparent',
                                                    hover_color='light gray',
                                                    command=lambda :self.controller.show_frame("GuidePage"))
        self.guide_button.place(relx=0.4,
                                rely=0.083,
                                anchor='center')

    def local_widgets(self):
        self.local_button = customtkinter.CTkButton(self.main_frame,
                                                    font=('Calbiri', 13),
                                                    text='Local Reports',
                                                    text_color='black',
                                                    height=50,
                                                    width=60,
                                                    border_width=0,
                                                    border_color='black',
                                                    bg_color='transparent',
                                                    fg_color='transparent',
                                                    hover_color='light gray',
                                                    command=lambda :self.controller.show_frame("ReportApp"))
        self.local_button.place(relx=0.475,
                                rely=0.083,
                                anchor='center')

    def learn_widgets(self):
        self.learn_button = customtkinter.CTkButton(self.main_frame,
                                                    font=('Calbiri', 13),
                                                    text='Learn',
                                                    text_color='black',
                                                    height=50,
                                                    width=60,
                                                    border_width=0,
                                                    border_color='black',
                                                    bg_color='transparent',
                                                    fg_color='transparent',
                                                    hover_color='light gray',
                                                    command=lambda :self.controller.show_frame("LearnPage"))
        self.learn_button.place(relx=0.55,
                                rely=0.083,
                                anchor='center')

    def recover_widgets(self):
        self.recover_button = customtkinter.CTkButton(self.main_frame,
                                                      font=('Calbiri', 13),
                                                      text='Recover',
                                                      text_color='black',
                                                      height=50,
                                                      width=60,
                                                      border_width=0,
                                                      border_color='black',
                                                      bg_color='transparent',
                                                      fg_color='transparent',
                                                      hover_color='light gray',
                                                      command=lambda :self.controller.show_frame("RecoveryPage"))
        self.recover_button.place(relx=0.61,
                                  rely=0.083,
                                  anchor='center')

    def update_clock(self):
        self.date_label.configure(text=datetime.now().strftime("%B %d, %Y\n%H:%M:%S"))
        self.after(1000, self.update_clock)

    def update_weather(self):
        # Check if user typed a city, otherwise use empty string for auto-detection
        city = self.city_entry.get().strip()
        self.location_label.configure(text="Fetching from Web...")

        try:
            # wttr.in format: ?format=j1 gives easy-to-parse JSON
            url = f"https://wttr.in{city}?format=j1"
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                current = data['current_condition'][0]

                # Update Labels
                area = data['nearest_area'][0]['areaName'][0]['value']
                country = data['nearest_area'][0]['country'][0]['value']

                self.location_label.configure(text=f"Location: {area}, {country}")
                self.temp_label.configure(text=f"Temperature: {current['temp_C']}°C")
                self.hum_label.configure(text=f"Humidity: {current['humidity']}%")
            else:
                self.location_label.configure(text="Web Service Busy (Try again)")

        except Exception as e:
            self.location_label.configure(text="Connection Error")
            print(f"Error details: {e}")

        # Auto-refresh every 20 minutes
        self.after(1200000, self.update_weather)
