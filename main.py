from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
import platform
import subprocess

# --- Screen 1: Provider Details (End User/Service Provider) ---
class ProviderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="[b]SERVICE PROVIDER (END USER)[/b]", markup=True, size_hint_y=None, height=50))
        
        self.sp_name = TextInput(hint_text="Company Name", multiline=False)
        self.sp_addr = TextInput(hint_text="Address", multiline=False)
        self.eng_name = TextInput(hint_text="Engineer Name", multiline=False)
        self.eng_mob = TextInput(hint_text="Engineer Mobile (9416399442)", multiline=False)
        
        for widget in [self.sp_name, self.sp_addr, self.eng_name, self.eng_mob]:
            layout.add_widget(widget)
        
        btn = Button(text="SAVE & GO BACK", size_hint_y=None, height=80, background_color=(0, 0.7, 0, 1))
        btn.bind(on_press=self.go_back)
        layout.add_widget(btn)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'

# --- Screen 2: Client Details ---
class ClientScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="[b]SERVICE CLIENT DETAILS[/b]", markup=True, size_hint_y=None, height=50))
        
        self.sc_name = TextInput(hint_text="Client Company", multiline=False)
        self.sc_addr = TextInput(hint_text="Client Address", multiline=False)
        self.rp_name = TextInput(hint_text="Responsible Person", multiline=False)
        self.rp_mob = TextInput(hint_text="Client Mobile", multiline=False)
        
        for widget in [self.sc_name, self.sc_addr, self.rp_name, self.rp_mob]:
            layout.add_widget(widget)
        
        btn = Button(text="SAVE & GO BACK", size_hint_y=None, height=80, background_color=(0, 0.7, 0, 1))
        btn.bind(on_press=self.go_back)
        layout.add_widget(btn)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'

# --- Main Screen: IP Inputs & Report ---
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Two Main Entry Buttons
        layout.add_widget(Button(text="SET PROVIDER INFO", on_press=lambda x: self.nav('provider'), background_color=(0.2, 0.6, 1, 1), size_hint_y=None, height=80))
        layout.add_widget(Button(text="SET CLIENT INFO", on_press=lambda x: self.nav('client'), background_color=(0.2, 0.6, 1, 1), size_hint_y=None, height=80))
        
        self.start_ip = TextInput(hint_text="Start IP (e.g. 192.168.1.1)", multiline=False, size_hint_y=None, height=70)
        self.end_ip = TextInput(hint_text="End IP (e.g. 192.168.1.10)", multiline=False, size_hint_y=None, height=70)
        
        layout.add_widget(self.start_ip)
        layout.add_widget(self.end_ip)
        
        self.dl_btn = Button(text="GENERATE & DOWNLOAD REPORT", size_hint_y=None, height=90, background_color=(0.8, 0.3, 0, 1))
        self.dl_btn.bind(on_press=self.generate_report)
        layout.add_widget(self.dl_btn)
        
        self.status = Label(text="Network Master Pro Ready", markup=True)
        layout.add_widget(self.status)
        self.add_widget(layout)

    def nav(self, name):
        self.manager.current = name

    def generate_report(self, instance):
        p = self.manager.get_screen('provider')
        c = self.manager.get_screen('client')
        
        header = f"""
============================================================
                NETWORK MASTER PRO SERVICE REPORT
============================================================
DATE: {datetime.now().strftime('%Y-%m-%d %H:%M')}

SERVICE PROVIDER:                       SERVICE CLIENT:
-----------------                       ---------------
Company: {p.sp_name.text:<30} Company: {c.sc_name.text}
Address: {p.sp_addr.text:<30} Address: {c.sc_addr.text}
Engineer: {p.eng_name.text:<30} Resp. Person: {c.rp_name.text}
Mobile: {p.eng_mob.text:<30} Mobile: {c.rp_mob.text}
============================================================
SCAN RANGE: {self.start_ip.text} TO {self.end_ip.text}
============================================================
"""
        path = "/sdcard/Download/Network_Service_Report.txt"
        try:
            with open(path, "w") as f:
                f.write(header)
            self.status.text = f"[color=00ff00]Report Saved to Download Folder![/color]"
        except Exception as e:
            self.status.text = f"[color=ff0000]Error: {str(e)}[/color]"

class NetworkMasterPro(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ProviderScreen(name='provider'))
        sm.add_widget(ClientScreen(name='client'))
        return sm

if __name__ == '__main__':
    NetworkMasterPro().run()
