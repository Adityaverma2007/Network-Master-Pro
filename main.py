from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import subprocess
import os
from datetime import datetime

# --- 3D Style Custom Input ---
class CustomInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_color = (0.12, 0.12, 0.12, 1) # Dark 3D Feel
        self.foreground_color = (1, 1, 1, 1)
        self.padding = [10, 12]
        self.font_size = '15sp'
        self.cursor_color = (0, 1, 0, 1)
        self.multiline = False

class NetworkMasterPro(App):
    def build(self):
        self.title = "Network Master Pro"
        self.main_layout = BoxLayout(orientation='vertical', padding=5, spacing=2) # Zero Gap
        
        # --- 1. Top Section: Details (Scrollable) ---
        self.scroll_input = ScrollView(size_hint=(1, 0.48))
        input_container = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        input_container.bind(minimum_height=input_container.setter('height'))

        # Uniform 3D Boxes for Provider & Client
        details_grid = GridLayout(cols=2, spacing=8, size_hint_y=None, height=420)
        
        self.sp_name = CustomInput(hint_text="Service Provider Co.")
        self.sc_name = CustomInput(hint_text="Service Client Co.")
        self.sp_addr = CustomInput(hint_text="Provider Address")
        self.sc_addr = CustomInput(hint_text="Client Address")
        self.eng_name = CustomInput(hint_text="Engineer Name")
        self.rp_name = CustomInput(hint_text="Responsible Person")
        self.eng_mob = CustomInput(hint_text="Engineer Mobile (9416399442)") #
        self.rp_mob = CustomInput(hint_text="Client Mobile")

        for w in [self.sp_name, self.sc_name, self.sp_addr, self.sc_addr, 
                  self.eng_name, self.rp_name, self.eng_mob, self.rp_mob]:
            details_grid.add_widget(w)

        # Config Box (IPs, Packet, Ping Count)
        config_grid = GridLayout(cols=2, spacing=8, size_hint_y=None, height=180)
        self.start_ip = CustomInput(hint_text="Start IP (e.g. 192.168.1.1)")
        self.end_ip = CustomInput(hint_text="End IP (e.g. 192.168.1.10)")
        self.packet_size = CustomInput(hint_text="Packet Size", text="32")
        self.ping_count = CustomInput(hint_text="Ping Times (Max 5)", text="3") 
        self.date_box = CustomInput(text=datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.dummy = Label(text="", size_hint_y=None, height=40)

        config_grid.add_widget(self.start_ip); config_grid.add_widget(self.end_ip)
        config_grid.add_widget(self.packet_size); config_grid.add_widget(self.ping_count)
        config_grid.add_widget(self.date_box); config_grid.add_widget(self.dummy)

        input_container.add_widget(details_grid)
        input_container.add_widget(config_grid)
        self.scroll_input.add_widget(input_container)

        # --- 2. Buttons Section (Shifted UP) ---
        btn_layout = BoxLayout(size_
