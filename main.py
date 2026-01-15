from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import subprocess
import threading
from datetime import datetime

class ProviderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="[b]SERVICE PROVIDER DETAILS[/b]", markup=True, size_hint_y=None, height=50))
        self.sp_name = TextInput(hint_text="Company Name", multiline=False)
        self.sp_addr = TextInput(hint_text="Address", multiline=False)
        self.eng_name = TextInput(hint_text="Engineer Name", multiline=False)
        self.eng_mob = TextInput(hint_text="Engineer Mobile (9416399442)", multiline=False)
        for w in [self.sp_name, self.sp_addr, self.eng_name, self.eng_mob]: layout.add_widget(w)
        btn = Button(text="SAVE & BACK", size_hint_y=None, height=80, background_color=(0, 0.7, 0, 1))
        btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(btn)
        self.add_widget(layout)

class ClientScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="[b]SERVICE CLIENT DETAILS[/b]", markup=True, size_hint_y=None, height=50))
        self.sc_name = TextInput(hint_text="Client Company", multiline=False)
        self.sc_addr = TextInput(hint_text="Client Address", multiline=False)
        self.rp_name = TextInput(hint_text="Responsible Person", multiline=False)
        self.rp_mob = TextInput(hint_text="Client Mobile", multiline=False)
        for w in [self.sc_name, self.sc_addr, self.rp_name, self.rp_mob]: layout.add_widget(w)
        btn = Button(text="SAVE & BACK", size_hint_y=None, height=80, background_color=(0, 0.7, 0, 1))
        btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(btn)
        self.add_widget(layout)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.final_report = ""
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Navigation
        nav_box = BoxLayout(size_hint_y=None, height=80, spacing=10)
        nav_box.add_widget(Button(text="Provider Info", on_press=lambda x: self.nav('provider')))
        nav_box.add_widget(Button(text="Client Info", on_press=lambda x: self.nav('client')))
        layout.add_widget(nav_box)

        # IP Inputs
        self.start_ip = TextInput(hint_text="Start IP (192.168.1.1)", multiline=False, size_hint_y=None, height=60)
        self.end_ip = TextInput(hint_text="End IP (192.168.1.10)", multiline=False, size_hint_y=None, height=60)
        layout.add_widget(self.start_ip); layout.add_widget(self.end_ip)

        # Config: Count & Size
        config_box = BoxLayout(size_hint_y=None, height=60, spacing=10)
        self.p_count = TextInput(hint_text="Count", text="3", multiline=False)
        self.p_size = TextInput(hint_text="Size", text="32", multiline=False)
        config_box.add_widget(self.p_count); config_box.add_widget(self.p_size)
        layout.add_widget(config_box)

        # Action Buttons
        self.run_btn = Button(text="START LIVE SCAN", size_hint_y=None, height=80, background_color=(0, 0.8, 0, 1))
        self.run_btn.bind(on_press=self.start_thread)
        self.dl_btn = Button(text="DOWNLOAD REPORT", size_hint_y=None, height=80, background_color=(0.2, 0.2, 0.8, 1))
        self.dl_btn.bind(on_press=self.save_report)
        layout.add_widget(self.run_btn); layout.add_widget(self.dl_btn)

        # Log View
        self.scroll = ScrollView()
        self.log = Label(text="Ready...", size_hint_y=None, markup=True, halign='left', valign='top')
        self.log.bind(size=self.log.setter('text_size'))
        self.scroll.add_widget(self.log)
        layout.add_widget(self.scroll)
        self.add_widget(layout)

    def nav(self, name): self.manager.current = name

    def start_thread(self, instance):
        self.log.text = "[b]Scan Started...[/b]\n"
        threading.Thread(target=self.run_ping).start()

    def run_ping(self):
        try:
            start_base = ".".join(self.start_ip.text.split('.')[:3])
            s_num = int(self.start_ip.text.split('.')[3])
            e_num = int(self.end_ip.text.split('.')[3])
            
            report_body = ""
            for i in range(s_num, e_num + 1):
                target = f"{start_base}.{i}"
                Clock.schedule_once(lambda dt, t=target: self.update_log(f"Testing {t}... "))
                
                cmd = ['/system/bin/ping', '-c', self.p_count.text, '-s', self.p_size.text, target]
                try:
                    subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
                    res = "[color=00ff00]OK[/color]\n"
                    status_text = "OK"
                except:
                    res = "[color=ff0000]FAILED[/color]\n"
                    status_text = "FAILED"
                
                report_body += f"{target} : {status_text}\n"
                Clock.schedule_once(lambda dt, r=res: self.update_log(r, append=True))
            
            self.final_report = report_body
            Clock.schedule_once(lambda dt: self.update_log("\n[b][color=00ff00]SCAN COMPLETED![/color][/b]", append=True))
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_log(f"\nError: {str(e)}", append=True))

    def update_log(self, text, append=False):
        if append: self.log.text += text
        else: self.log.text = text
        self.log.height = self.log.texture_size[1]

    def save_report(self, instance):
        p = self.manager.get_screen('provider')
        c = self.manager.get_screen('client')
        header = f"DATE: {datetime.now()}\nPROVIDER: {p.sp_name.text}\nCLIENT: {c.sc_name.text}\n" + "="*20 + "\n"
        path = "/sdcard/Download/NetworkMaster_Report.txt"
        with open(path, "w") as f: f.write(header + self.final_report)
        self.log.text += f"\n[b]Saved: {path}[/b]"

class NetworkMasterPro(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main')); sm.add_widget(ProviderScreen(name='provider')); sm.add_widget(ClientScreen(name='client'))
        return sm

if __name__ == '__main__':
    NetworkMasterPro().run()
