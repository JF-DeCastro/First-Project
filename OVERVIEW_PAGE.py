import customtkinter

class OverviewPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color='#ebebeb')

        self.show_overview()

    def show_overview(self):
        self.overviewFrame = customtkinter.CTkFrame(self,
                                                    fg_color='#ebebeb')
        self.overviewFrame.pack(fill='both',
                                expand=True)

        self.overview_message = customtkinter.CTkTextbox(self.overviewFrame,
                                                         height=700,
                                                         width=1300,
                                                         corner_radius=10,
                                                         bg_color='#ebebeb',
                                                         font=('Calbiri', 25, 'bold'),
                                                         fg_color='#dcdcdc',
                                                         text_color='black',
                                                         border_width=2,
                                                         border_color='#c0c0c0',
                                                         )
        self.overview_message.pack(pady=50,
                                   padx=50)
        self.overview_message.bind("<Key>", lambda e: "break")
        self.overview_message.bind("<Button-1>", lambda e: "break")
        self.overview_message.bind("<B1-Motion>", lambda e: "break")

        self.text_overview = (
            '1. Check Real-Time Alerts\n'
            'View the homepage dashboard for current disaster warnings (e.g., typhoon signals, earthquake advisories).\n\n'
            '2. Locate Safe Areas\n'
            'Use the interactive map to find evacuation centers, hospitals, and safe routes in your barangay.\n\n'
            '3. Download Preparedness Guides\n'
            'Get bilingual checklists and visual aids for go-bags, family communication plans, and school drills.\n\n'
            '4. Report Local Conditions\n'
            'Submit updates about blocked roads, flooding, or damaged infrastructure to help authorities and neighbors.\n\n'
            '5. Learn and Practice\n'
            'Explore educational modules, reviewer sheets, and gamified learning activities to build disaster readiness skills.\n\n'
            '6. Recover and Rebuild\n'
            'Access post-disaster resources such as relief schedules, counseling services, and rebuilding support programs.')

        self.overview_message.insert('0.0', self.text_overview)

        self.overview_return = customtkinter.CTkButton(self.overviewFrame,
                                                       text='Back',
                                                       text_color='white',
                                                       corner_radius=50,
                                                       bg_color='transparent',
                                                       fg_color='green',
                                                       hover_color='lime green',
                                                       border_width=1,
                                                       border_color='white',
                                                       command=lambda: self.controller.show_frame('MainHome')
                                                       )
        self.overview_return.place(relx=0.5,
                                   rely=0.035,
                                   anchor='center')