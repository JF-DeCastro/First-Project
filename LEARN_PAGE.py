import customtkinter
from PIL import ImageFilter, ImageTk, Image

class LearnPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self._set_appearance_mode('light')

        self.show_learn()

    def show_learn(self):
        bg_image_path = "illustration-of-people-in-a-boat-in-a-flood.png"
        original_image = Image.open(bg_image_path)
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(2))

        self.bg_image = customtkinter.CTkImage(light_image=blurred_image, dark_image=blurred_image, size=(1700, 1100))
        self.bg_label2 = customtkinter.CTkLabel(self, text="", image=self.bg_image)
        self.bg_label2.place(x=0, y=0, relwidth=1, relheight=1)

        self.header2 = customtkinter.CTkButton(self.bg_label2, fg_color='green', border_color='light green', border_width=1,
                                               text="DISASTER PREPAREDNESS EDUCATION", font=("Courier", 24, "bold"),
                                               text_color="#fef9f3", hover=False, width=1400, height=50)
        self.header2.place(relx=.5,
                           rely=.06,
                           anchor="center")

        self.learn_returnBTN = customtkinter.CTkButton(self.bg_label2,
                                                       text='Back',
                                                       text_color='white',
                                                       corner_radius=50,
                                                       bg_color='transparent',
                                                       fg_color='green',
                                                       hover_color='lime green',
                                                       border_width=1,
                                                       border_color='white',
                                                       command=lambda: self.controller.show_frame("MainHome"))
        self.learn_returnBTN.place(relx=0.1,
                                   rely=0.14,
                                   anchor='center')

        self.tabview = customtkinter.CTkTabview(self.bg_label2, width=1200, height=550, fg_color='#fef9f3', bg_color='#fef9f3',
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

        self.tabview.add("Typhoons")
        self.tabview.add("Bagyo")
        self.tabview.add("Earthquakes")
        self.tabview.add("Lindol")
        self.tabview.add("Flooding")
        self.tabview.add("Baha")
        self.tabview.add("Fire")
        self.tabview.add("Sunog")

        self.setup_typhoonedu_tab()
        self.setup_bagyoedu_tab()
        self.setup_earthquakeedu_tab()
        self.setup_lindoledu_tab()
        self.setup_floodingedu_tab()
        self.setup_bahaedu_tab()
        self.setup_fireedu_tab()
        self.setup_sunogedu_tab()

    def setup_typhoonedu_tab(self):
        text = ("---- HOW TO PREPARE FOR A TYPHOON ----\n"
                "\n\n|• Create an emergency kit (go-bag) in case you need to leave your area or services are cut off.\n\n"
                "|• Store any important documents like ID papers high up or in something that can \nprotect against water damage (like a sealable plastic bag).\n\n"
                "|• If you are in an area that is likely to flood, find an area where you can get to higher ground.\n\n"
                "|• Check your local news or radio station for weather updates and official advice.\n\n"
                "|• If you are advised to evacuate, grab your emergency kit and ID papers and do so immediately.\n\n"
                "|• If you have not been advised to evacuate, stay calm, stay indoors and away from windows.\n\n")
        header_label = customtkinter.CTkLabel(self.tabview.tab("Typhoons"), text=text, font=("Segoe UI", 17, "bold"),
                                              text_color="#3b444b")
        header_label.pack(anchor="center", padx=10, pady=10)

    def setup_bagyoedu_tab(self):
        text = ("---- PAANO MAGHANDA PARA SA BAGYO ----\n"
                "\n\n|• Maghanda ng emergency kit (go-bag) sakaling kailangang lumikas o mawalan ng serbisyo.\n\n"
                "|• Itago ang mahahalagang dokumento tulad ng ID sa mataas na lugar o sa loob ng \nbagay na hindi mababasa (tulad ng sealable plastic bag).\n\n"
                "|• Kung ang inyong lugar ay madalas bahain, maghanap agad ng ligtas at mataas na lugar.\n\n"
                "|• Makinig sa balita sa telebisyon o radyo para sa mga weather update at opisyal na payo.\n\n"
                "|• Kung pinapayuhang lumikas, dalhin ang iyong emergency kit at mga ID at lumikas agad.\n\n"
                "|• Kung hindi naman kailangang lumikas, manatiling mahinahon, manatili sa loob ng bahay \nat lumayo sa mga bintana.\n\n")
        header_label = customtkinter.CTkLabel(self.tabview.tab("Bagyo"), text=text, font=("Segoe UI", 17, "bold"),
                                              text_color="#3b444b")
        header_label.pack(anchor="center", padx=10, pady=10)

    def setup_earthquakeedu_tab(self):
        text = ("---- HOW TO PREPARE FOR AN EARTHQUAKE ----\n"
                "\n\n|• Create an emergency kit (go-bag) in case you need to leave your area or services are cut off.\n\n"
                "|• During an ongoing sudden earthquake Indoors, remember to Duck, Cover, & Hold On.\n\n"
                "|• During an ongoing sudden earthquake Outdoors, move to an open area away from\nbuildings, powerlines, and trees.\n\n"
                "|• Stay on high alert after the ground stops shaking, aftershocks can follow after an earthquake.\n\n"
                "|• Avoid using the elevators and use the stairs instead, power outages and aftershocks\n can trap you in the elevator.\n\n"
                "|• Check your local news or radio station for any earthquake updates and official advice.\n\n")
        header_label = customtkinter.CTkLabel(self.tabview.tab("Earthquakes"), text=text, font=("Segoe UI", 17, "bold"),
                                              text_color="#3b444b")
        header_label.pack(anchor="center", padx=10, pady=10)

    def setup_lindoledu_tab(self):
        text = ("---- PAANO MAGHANDA PARA SA LINDOL ----\n"
                "\n\n|• Maghanda ng emergency kit (go-bag) sakaling kailangang lumikas o mawalan ng serbisyo.\n\n"
                "|• Kapag may nagaganap na lindol at nasa loob ng gusali, tandaan ang: Duck, Cover, & Hold On.\n\n"
                "|• Kung nasa labas naman, pumunta sa isang bukas na lugar malayo sa mga gusali,\nlinya ng kuryente, at mga puno.\n\n"
                "|• Manatiling alerto matapos ang pagyanig dahil maaaring magkaroon ng mga aftershock.\n\n"
                "|• Iwasang gumamit ng elebeytor; gamitin ang hagdan dahil ang brownout at aftershocks\nay maaaring makakulong sa inyo sa loob.\n\n"
                "|• Makinig sa balita o radyo para sa mga update tungkol sa lindol at mga opisyal na payo.\n\n")
        header_label = customtkinter.CTkLabel(self.tabview.tab("Lindol"), text=text, font=("Segoe UI", 17, "bold"),
                                              text_color="#3b444b")
        header_label.pack(anchor="center", padx=10, pady=10)

    def setup_floodingedu_tab(self):
        text = ("---- HOW TO PREPARE FOR A FLOOD ----\n"
                "\n\n|• Create an emergency kit (go-bag) in case you need to leave your area or services are cut off.\n\n"
                "|• Check if you live in a flood-prone zone, if in a flood prone-zone, head to the evacuation sites.\n\n"
                "|• Monitor the local news or PAG-ASA weather updates.\n\n"
                "|• If water enters the house, turn off the electricity at the main breaker.\n\n"
                "|• When indoors and flood is present, move to the highest level of the building and avoid the water.\nThere could be bacteria present in the water that can cause Leptospirosis and infection.\n\n"
                "|• If outside and flooding, do not attempt to travel through the flood water. \nTurn around and don't drown: It only takes 6 inches of moving water to knock you off\nyour feet and 12 inches to sweep away a car.\n\n")
        header_label = customtkinter.CTkLabel(self.tabview.tab("Flooding"), text=text, font=("Segoe UI", 17, "bold"),
                                              text_color="#3b444b")
        header_label.pack(anchor="center", padx=10, pady=10)

    def setup_bahaedu_tab(self):
        text = ("---- PAANO MAGHANDA PARA SA BAHA ----\n"
                "\n\n|• Maghanda ng emergency kit (go-bag) sakaling kailangang lumikas o mawalan ng serbisyo.\n\n"
                "|• Alamin kung ang inyong lugar ay madaling bahain; kung oo, pumunta agad sa evacuation center.\n\n"
                "|• Mag-abang ng mga update sa lokal na balita o mula sa PAG-ASA weather updates.\n\n"
                "|• Kung pumasok na ang tubig sa loob ng bahay, patayin ang kuryente sa main breaker.\n\n"
                "|• Kung nasa loob at may baha, pumunta sa pinakamataas na palapag at iwasang mababad sa tubig.\nMaaaring may mga bacteria sa baha na nagdudulot ng Leptospirosis at iba pang impeksyon.\n\n"
                "|• Kung nasa labas, huwag tangkaing dumaan sa baha. 'Turn around and don't drown':\n6 na pulgada lang ng umaagos na tubig ang kaya kang itumba, at 12 pulgada para inanurin ang kotse.\n\n")
        header_label = customtkinter.CTkLabel(self.tabview.tab("Baha"), text=text, font=("Segoe UI", 17, "bold"),
                                              text_color="#3b444b")
        header_label.pack(anchor="center", padx=10, pady=10)

    def setup_fireedu_tab(self):
        text = ("---- HOW TO PREPARE FOR A FIRE ----\n"
                "\n\n|• Prepare and memorize a fire drill exit in case of a fire.\n\n"
                "|• Make sure to install smoke detectors around the house.\n\n"
                "|• At the first signs of a fire, immediately call an emergency\nhotline (firefighters), and evacuate the building.\n\n"
                "|• Incase of a small fire, learn to use the fire extinguisher.\n PASS: Pull the pin, Aim at the base of the fire,\nSqueeze the handle, and Sweep from side to side\n\n"
                "|• Incase you catch on fire, Stop, Drop, and Roll, to extinguish the flames.\n\n"
                "|• During a fire, crawl low since smoke and toxic gases will rise from the fire.\n\n"
                "|• Before opening a door during a fire, test with the back of your hand to\n double check if it is not hot to avoid burns, incase if it is hot\nit means there's a fire behind the door.\n\n"
                "|• Check your local news or radio station for any earthquake updates and official advice.\n\n")
        header_label = customtkinter.CTkLabel(self.tabview.tab("Fire"), text=text, font=("Segoe UI", 15, "bold"),
                                              text_color="#3b444b")
        header_label.pack(anchor="center", padx=10, pady=0)

    def setup_sunogedu_tab(self):
        text = ("---- PAANO MAGHANDA PARA SA SUNOG ----\n"
                "\n\n|• Maghanda at kabisaduhin ang fire drill exit sakaling magkaroon ng sunog.\n\n"
                "|• Siguraduhing magkabit ng mga smoke detector sa loob ng bahay.\n\n"
                "|• Sa unang senyales ng sunog, tumawag agad sa emergency hotline (bumbero) at lumikas.\n\n"
                "|• Para sa maliliit na apoy, alamin ang paggamit ng fire extinguisher.\n P.A.S.S.: Pull (Hilahin ang pin), Aim (Itutok sa puno ng apoy),\nSqueeze (Pisilin ang handle), at Sweep (I-sway pakaliwa't pakanan).\n\n"
                "|• Kung nag-apoy ang iyong damit, tandaan ang: Stop, Drop, and Roll.\n\n"
                "|• Habang may sunog, gumapang nang mababa dahil ang usok at nakalalasong gas ay umaakyat.\n\n"
                "|• Bago magbukas ng pinto, gamitin ang likod ng iyong kamay para pakiramdaman kung ito ay\nmainit; kung mainit, nangangahulugang may apoy sa likod nito.\n\n"
                "|• Makinig sa balita o radyo para sa mga update at opisyal na payo.\n\n")
        header_label = customtkinter.CTkLabel(self.tabview.tab("Sunog"), text=text, font=("Segoe UI", 15, "bold"),
                                              text_color="#3b444b")
        header_label.pack(anchor="center", padx=10, pady=10)