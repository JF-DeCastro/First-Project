import customtkinter
from HOME_PAGE import MainHome
from MAP_PAGE import MapPage
from GUIDE_PAGE import GuidePage
from LEARN_PAGE import LearnPage
from RECOVERY_PAGE import RecoveryPage
from OVERVIEW_PAGE import OverviewPage
from LOCAL_REPORTS import ReportApp
from LOCAL_REPORTS import ReportService

class AppManager(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('SafeLink - A Disaster Preparedness Information Portal')
        self.geometry('1300x700')
        self.resizable(False, False)
        self.service = ReportService()

        container = customtkinter.CTkFrame(self)
        container.pack(fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for PageClass in (MainHome, MapPage, GuidePage, LearnPage, RecoveryPage, OverviewPage, ReportApp):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Stack on same spot

        self.show_frame("MainHome")

    def show_frame(self, page_name):
        # switch page
        frame = self.frames[page_name]
        frame.tkraise()

app = AppManager()
app.mainloop()