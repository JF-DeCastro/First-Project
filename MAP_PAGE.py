import customtkinter
import requests
from tkintermapview import TkinterMapView
import sqlite3
import geocoder


class MapPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="#ebebeb")

        self.show_mappage()

    def show_mappage(self):
        self.frame_cmd = customtkinter.CTkFrame(self,
                                                bg_color='#ebebeb',
                                                fg_color='light gray',
                                                height=675,
                                                corner_radius=30,
                                                border_width=1,
                                                border_color='light gray')
        self.frame_cmd.grid(row=0,
                            column=1,
                            sticky="nsew",
                            padx=10,
                            pady=10)

        self.map = TkinterMapView(self,
                                  height=675,
                                  width=1300,
                                  corner_radius=50)
        self.map.grid(row=0,
                      column=2,
                      sticky="nsew",
                      padx=10,
                      pady=10)
        self.map_returnBTN = customtkinter.CTkButton(self.frame_cmd,
                                                     text='Back',
                                                     text_color='white',
                                                     corner_radius=50,
                                                     bg_color='transparent',
                                                     fg_color='green',
                                                     hover_color='lime green',
                                                     border_width=1,
                                                     border_color='white',
                                                     command=lambda: self.controller.show_frame('MainHome'))
        self.map_returnBTN.place(relx=0.15,
                                 rely=0.03)

        self.legend_title = customtkinter.CTkLabel(self.frame_cmd, text="📍 Map Legends",
                                                   font=("Arial Black", 14), text_color="#333333")
        self.legend_title.place(relx=0.1, rely=0.15)

        # Danger Legend
        self.line_danger = customtkinter.CTkFrame(self.frame_cmd, width=40, height=5, fg_color="red",
                                                  border_width=0)
        self.line_danger.place(relx=0.1, rely=0.22)
        self.lbl_danger = customtkinter.CTkLabel(self.frame_cmd, text_color='black', text="Danger / Closed",
                                                 font=("Arial", 12))
        self.lbl_danger.place(relx=0.35, rely=0.21)

        # Caution Legend
        self.line_caution = customtkinter.CTkFrame(self.frame_cmd, width=40, height=5, fg_color="orange",
                                                   border_width=0)
        self.line_caution.place(relx=0.1, rely=0.27)
        self.lbl_caution = customtkinter.CTkLabel(self.frame_cmd, text_color='black', text="Caution / Traffic",
                                                  font=("Arial", 12))
        self.lbl_caution.place(relx=0.35, rely=0.26)

        # Safe Legend
        self.line_safe = customtkinter.CTkFrame(self.frame_cmd, width=40, height=5, fg_color="green",
                                                border_width=0)
        self.line_safe.place(relx=0.1, rely=0.32)
        self.lbl_safe = customtkinter.CTkLabel(self.frame_cmd, text_color='black', text="Safe Route",
                                               font=("Arial", 12))
        self.lbl_safe.place(relx=0.35, rely=0.31)

        self.update()
        self.map.draw_move()

        self.current_path = None
        self.update_navigation()

    def get_road_route(self, start, end):
        # routes from OSRM API
        url = f"https://router.project-osrm.org/route/v1/driving/{start[1]},{start[0]};{end[1]},{end[0]}?overview=full&geometries=geojson"
        try:
            response = requests.get(url).json()
            if response.get("routes"):
                coords = response["routes"][0]["geometry"]["coordinates"]
                return [[p[1], p[0]] for p in coords]
        except Exception as e:
            print(f"Routing Error: {e}")
        return [start, end]

    def update_navigation(self):
        #Live GPS
        g = geocoder.ip('me')
        if not g.latlng:
            self.after(5000, self.update_navigation)
            return

        current_gps = tuple(g.latlng)

        if not hasattr(self, 'active_paths'):
            self.active_paths = []
        if not hasattr(self, 'active_markers'):
            self.active_markers = []

    # markers input from database (emergency_system.db)
        try:
            conn = sqlite3.connect("emergency_system.db")
            cursor = conn.cursor()

            # CHANGE: Select all markers instead of LIMIT 1
            cursor.execute("SELECT name, lat, lon, status FROM markers")
            destinations = cursor.fetchall()
            conn.close()

            # Clear previous paths and markers from the map
            for path in self.active_paths:
                path.delete()
            for marker in self.active_markers:
                marker.delete()

            self.active_paths.clear()
            self.active_markers.clear()

            # 2. Loop through every location in the database
            for dest in destinations:
                name, d_lat, d_lon, status = dest
                dest_coords = (d_lat, d_lon)

                # Fetch road-snapped route for this specific destination
                road_points = self.get_road_route(current_gps, dest_coords)

                # Determine color
                color = "green" if status == "safe" else "red" if status == "danger" else "orange"

                # Draw the path and save reference
                path = self.map.set_path(road_points, color=color, width=4)
                marker = self.map.set_marker(d_lat, d_lon, text=name)

                self.active_paths.append(path)
                self.active_markers.append(marker)

            # 3. Center map on user
            self.map.set_position(current_gps[0], current_gps[1])
            self.map.set_zoom(10)

        except Exception as e:
            print(f"System Error: {e}")



