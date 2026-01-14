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

# --- 3D Style Input ---
class CustomInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_color = (0.15, 0.15, 0.15, 1)
        self.foreground_color = (1, 1, 1, 1)
        self.padding = [10, 12]
        self.font_size = '15sp'
        self.cursor_color = (0, 1, 0, 1)
        self.multiline = False

class NetworkMasterPro(App):
    def build(self):
        self.title = "Network Master Pro"
        self.main_layout = BoxLayout(orientation='vertical', padding=5, spacing=2)
        
        # 1. Input Area
        self.scroll_input = ScrollView(size_hint=(1, 0.48))
        container = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        container.bind(minimum_height=container.setter('height'))

        grid = GridLayout(cols=2, spacing=8, size_hint_y=None, height=600)
        self.sp_name = CustomInput(hint_text="Service Provider Co.")
        self.sc_name = CustomInput(hint_text="Service Client Co.")
        self.sp_addr = CustomInput(hint_text="Provider Address")
        self.sc_addr = CustomInput(hint_text="Client Address")
        self.eng_name = CustomInput(hint_text="Engineer Name")
        self.rp_name = CustomInput(hint_text="Responsible Person")
        self.eng_mob = CustomInput(hint_text="Engineer Mobile (9416399442)")
        self.rp_mob = CustomInput(hint_text="Client Mobile")
        self.start_ip = CustomInput(hint_text="Start IP (e.g. 192.168.1.1)")
        self.end_ip = CustomInput(hint_text="End IP (e.g. 192.168.1.10)")
        self.packet_size = CustomInput(hint_text="Packet Size", text="32")
        self.ping_count = CustomInput(hint_text="Ping Times (Max 5)", text="3")

        for w in [self.sp_name, self.sc_name, self.sp_addr, self.sc_addr, 
                  self.eng_name, self.rp_name, self.eng_mob, self.rp_mob,
                  self.start_ip, self.end_ip, self.packet_size, self.ping_count]:
            grid.add_widget(w)

        container.add_widget(grid)
        self.scroll_input.add_widget(container)

        # 2. Buttons (Zero Gap)
        btn_layout = BoxLayout(size_hint_y=None, height=65, spacing=5)
        self.run_btn = Button(text="START SCAN", background_color=(0, 0.7, 0.2, 1), bold=True)
        self.run_btn.bind(on_press=self.start_analysis)
        self.save_btn = Button(text="SAVE REPORT", background_color=(0.1, 0.4, 0.8, 1), bold=True)
        self.save_btn.bind(on_press=self.download_report)
        btn_layout.add_widget(self.run_btn); btn_layout.add_widget(self.save_btn)

        # 3. Live Monitor
        self.res_scroll = ScrollView(size_hint=(1, 0.42))
        self.result_label = Label(text="[color=00ff00]> Ready to scan...[/color]", 
                                 markup=True, size_hint_y=None, halign='left', valign='top')
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.res_scroll.add_widget(self.result_label)

        self.main_layout.add_widget(self.scroll_input)
        self.main_layout.add_widget(btn_layout)
        self.main_layout.add_widget(self.res_scroll)
        
        self.final_report_text = ""
        return self.main_layout

    def start_analysis(self, instance):
        self.result_label.text = "[b]SCANNING...[/b]\n"
        self.final_report_text = ""
        Clock.schedule_once(self.run_pings, 0.2)

    def run_pings(self, dt):
        try:
            base = ".".join(self.start_ip.text.split('.')[:-1])
            s_num = int(self.start_ip.text.split('.')[-1])
            e_num = int(self.end_ip.text.split('.')[-1])
            p_size = self.packet_size.text or "32"
            p_count = max(1, min(int(self.ping_count.text or 3), 5))

            for i in range(s_num, e_num + 1):
                target = f"{base}.{i}"
                self.result_label.text += f"Checking {target}... "
                
                cmd = ['/system/bin/ping', '-c', str(p_count), '-s', p_size, '-W', '1', target]
                try:
                    subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
                    res = "[color=00ff00]OK[/color]\n"
                except:
                    res = "[color=ff0000]FAIL[/color]\n"
                
                self.result_label.text += res
                self.final_report_text += f"IP: {target} | Pings: {p_count} | Status: {res.strip()}\n"
                self.result_label.height = self.result_label.texture_size[1]
                self.res_scroll.scroll_y = 0

            self.result_label.text += "\n[b][color=ffff00]--- SCAN COMPLETED ---[/color][/b]"
        except Exception as e:
            self.result_label.text += f"\n[color=ff0000]Error: {str(e)}[/color]"

    def download_report(self, instance):
        if not self.final_report_text:
            self.result_label.text += "\n[color=ff0000]Run Scan First![/color]"
            return

        # --- Professional Report Format ---
        header = f"""========================================
        NETWORK MASTER PRO REPORT
========================================
DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

SERVICE PROVIDER:       SERVICE CLIENT:
{self.sp_name.text:<20}    {self.sc_name.text}
Engineer: {self.eng_name.text:<15} Person: {self.rp_name.text}
Mobile: {self.eng_mob.text:<17} Mobile: {self.rp_mob.text}
----------------------------------------
RESULTS:
{self.final_report_text}
========================================
"""
        # Android Save Path (Documents Folder)
        from android.storage import primary_external_storage_path
        primary_path = primary_external_storage_path()
        save_folder = os.path.join(primary_path, "Download") # Download folder is easiest to find
        
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            
        filename = f"NetworkReport_{datetime.now().strftime('%H%M%S')}.txt"
        full_path = os.path.join(save_folder, filename)

        try:
            with open(full_path, "w") as f:
                f.write(header)
            self.result_label.text += f"\n\n[b][color=00aaff]SAVED: {full_path}[/color][/b]"
        except Exception as e:
            self.result_label.text += f"\n[color=ff0000]Save Failed: {str(e)}[/color]"

if __name__ == '__main__':
    NetworkMasterPro().run()
