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

# --- 3D Design Input Field ---
class CustomInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_color = (0.15, 0.15, 0.15, 1) 
        self.foreground_color = (1, 1, 1, 1)
        self.padding = [10, 10]
        self.font_size = '16sp'
        self.cursor_color = (0, 1, 0, 1)

class NetworkMasterPro(App):
    def build(self):
        self.title = "Network Master Pro"
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=2)
        
        # 1. DETAILS BOX (Top Section)
        self.scroll_input = ScrollView(size_hint=(1, 0.45))
        input_container = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        input_container.bind(minimum_height=input_container.setter('height'))

        details_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=450)
        
        # Consistent Design for 8 boxes
        self.sp_name = CustomInput(hint_text="Service Provider Co.")
        self.sp_addr = CustomInput(hint_text="Provider Address")
        self.eng_name = CustomInput(hint_text="Engineer Name")
        self.eng_mob = CustomInput(hint_text="Engineer Mobile (9416399442)") [cite: 2026-01-04]
        
        self.sc_name = CustomInput(hint_text="Client Company")
        self.sc_addr = CustomInput(hint_text="Client Address")
        self.rp_name = CustomInput(hint_text="Responsible Person")
        self.rp_mob = CustomInput(hint_text="Client Mobile")

        for widget in [self.sp_name, self.sc_name, self.sp_addr, self.sc_addr, 
                       self.eng_name, self.rp_name, self.eng_mob, self.rp_mob]:
            details_grid.add_widget(widget)

        # 2. CONFIG BOX (IPs, Packet & NEW PING COUNT)
        config_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=180)
        self.start_ip = CustomInput(hint_text="Start IP (192.168.1.1)")
        self.end_ip = CustomInput(hint_text="End IP (192.168.1.10)")
        self.packet_size = CustomInput(hint_text="Packet Size", text="32")
        # Naya Ping Count Box (Max 5)
        self.ping_count = CustomInput(hint_text="Ping Times (Max 5)", text="3") 
        self.date_box = CustomInput(text=datetime.now().strftime("%Y-%m-%d"))
        self.dummy_label = Label(text="", size_hint_y=None, height=40) # Spacing ke liye

        config_grid.add_widget(self.start_ip); config_grid.add_widget(self.end_ip)
        config_grid.add_widget(self.packet_size); config_grid.add_widget(self.ping_count)
        config_grid.add_widget(self.date_box); config_grid.add_widget(self.dummy_label)

        input_container.add_widget(details_grid)
        input_container.add_widget(config_grid)
        self.scroll_input.add_widget(input_container)

        # 3. BUTTONS (Attached to inputs)
        btn_layout = BoxLayout(size_hint_y=None, height=70, spacing=5)
        self.run_btn = Button(text="START SCAN", background_color=(0, 0.8, 0, 1), bold=True)
        self.run_btn.bind(on_press=self.start_analysis)
        self.save_btn = Button(text="SAVE REPORT", background_color=(0, 0.4, 0.9, 1), bold=True)
        self.save_btn.bind(on_press=self.download_report)
        btn_layout.add_widget(self.run_btn); btn_layout.add_widget(self.save_btn)

        # 4. LIVE PING MONITOR
        self.res_scroll = ScrollView(size_hint=(1, 0.45))
        self.result_label = Label(text="[color=00ff00]> System Ready...[/color]", 
                                 markup=True, size_hint_y=None, halign='left', valign='top')
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.res_scroll.add_widget(self.result_label)

        self.main_layout.add_widget(self.scroll_input)
        self.main_layout.add_widget(btn_layout)
        self.main_layout.add_widget(self.res_scroll)
        
        self.full_log = ""
        return self.main_layout

    def start_analysis(self, instance):
        self.result_label.text = "[b]SCANNING...[/b]\n"
        self.full_log = ""
        Clock.schedule_once(self.execute_pings, 0.1)

    def execute_pings(self, dt):
        try:
            base_ip = ".".join(self.start_ip.text.split('.')[:-1])
            start = int(self.start_ip.text.split('.')[-1])
            end = int(self.end_ip.text.split('.')[-1])
            p_size = self.packet_size.text or "32"
            
            # Logic: Input check for Max 5
            try:
                p_count = int(self.ping_count.text)
                if p_count > 5: p_count = 5
                if p_count < 1: p_count = 1
            except:
                p_count = 3 # Default agar user galti kare

            for i in range(start, end + 1):
                ip = f"{base_ip}.{i}"
                self.result_label.text += f"[color=ffffff]Ping {ip} ({p_count} times)...[/color]"
                
                cmd = ['/system/bin/ping', '-c', str(p_count), '-s', p_size, '-W', '1', ip]
                try:
                    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
                    res = f" [color=00ff00]OK[/color]\n"
                except:
                    res = f" [color=ff0000]FAILED[/color]\n"
                
                self.result_label.text += res
                self.full_log += f"IP: {ip} | Pings: {p_count} | Status: {res.strip()}\n"
                self.result_label.height = self.result_label.texture_size[1]
                self.res_scroll.scroll_y = 0

            self.result_label.text += "\n[b][color=ffff00]--- SCAN COMPLETED ---[/color][/b]"
        except Exception as e:
            self.result_label.text += f"\nError: {e}"

    def download_report(self, instance):
        report_content = f"NETWORK SERVICE REPORT - {self.date_box.text}\n" + "="*40 + "\n"
        report_content += f"PROVIDER: {self.sp_name.text} | ENGINEER: {self.eng_name.text}\n"
        report_content += f"CLIENT: {self.sc_name.text} | PERSON: {self.rp_name.text}\n" + "-"*40 + "\n"
        report_content += self.full_log
        
        path = "/sdcard/Documents/NetworkMasterPro_Report.txt"
        try:
            if not os.path.exists("/sdcard/Documents"): os.makedirs("/sdcard/Documents")
            with open(path, "w") as f:
                f.write(report_content)
            self.result_label.text += f"\n\n[u]SAVED TO: {path}[/u]"
        except:
            self.result_label.text += "\n\n[color=ff0000]Error: Permission Denied![/color]"

if __name__ == '__main__':
    NetworkMasterPro().run()
