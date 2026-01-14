from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import platform
import subprocess
import os

class NetworkMasterPro(App):
    def build(self):
        self.title = "Network Master Pro"
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # --- UI Header ---
        self.layout.add_widget(Label(text="[b]IP RANGE ANALYZER[/b]", markup=True, size_hint_y=None, height=40))

        # --- Inputs Section ---
        self.start_ip = TextInput(hint_text="Start IP (e.g. 192.168.1.1)", multiline=False, size_hint_y=None, height=80)
        self.end_ip = TextInput(hint_text="End IP (e.g. 192.168.1.10)", multiline=False, size_hint_y=None, height=80)
        self.packet_size = TextInput(hint_text="Packet Size (Bytes) - Default 32", multiline=False, size_hint_y=None, height=80)
        
        self.layout.add_widget(self.start_ip)
        self.layout.add_widget(self.end_ip)
        self.layout.add_widget(self.packet_size)

        # --- Buttons ---
        btn_layout = BoxLayout(size_hint_y=None, height=80, spacing=10)
        self.run_btn = Button(text="START SCAN", background_color=(0, 0.7, 0, 1))
        self.run_btn.bind(on_press=self.start_analysis)
        
        self.download_btn = Button(text="DOWNLOAD REPORT", background_color=(0.2, 0.2, 0.8, 1))
        self.download_btn.bind(on_press=self.download_report)
        
        btn_layout.add_widget(self.run_btn)
        btn_layout.add_widget(self.download_btn)
        self.layout.add_widget(btn_layout)

        # --- Results View ---
        self.result_view = ScrollView()
        self.result_label = Label(text="Ready to Scan...", size_hint_y=None, halign='left', valign='top', markup=True)
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.result_view.add_widget(self.result_label)
        self.layout.add_widget(self.result_view)
        
        self.final_report = "" # रिपोर्ट स्टोर करने के लिए
        return self.layout

    def start_analysis(self, instance):
        self.result_label.text = "Initializing Range Scan..."
        Clock.schedule_once(self.run_range_ping, 0.1)

    def run_range_ping(self, dt):
        try:
            start_parts = list(map(int, self.start_ip.text.split('.')))
            end_parts = list(map(int, self.end_ip.text.split('.')))
            p_size = self.packet_size.text if self.packet_size.text else "32"
            
            base_ip = ".".join(map(str, start_parts[:3]))
            report = f"[b]MASTER REPORT (Contact: 9416399442)[/b]\n"
            report += f"Packet Size: {p_size} Bytes\n"
            report += "="*30 + "\n"

            for i in range(start_parts[3], end_parts[3] + 1):
                current_ip = f"{base_ip}.{i}"
                report += f"Analyzing: {current_ip}...\n"
                
                # Android-Specific Ping Command
                cmd = ['/system/bin/ping', '-c', '2', '-s', p_size, current_ip]
                try:
                    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
                    if "0% packet loss" in output:
                        report += f"[color=00ff00]STATUS: OK[/color]\n"
                    else:
                        report += f"[color=ffcc00]STATUS: PARTIAL LOSS[/color]\n"
                except:
                    report += f"[color=ff0000]STATUS: NOT OK[/color]\n"
                report += "-"*20 + "\n"
                self.result_label.text = report # Real-time update
            
            self.final_report = report
            self.result_label.text = report + "\n[b]SCAN COMPLETE[/b]"
            self.result_label.height = self.result_label.texture_size[1]
        except Exception as e:
            self.result_label.text = f"Error: Check IP Format\n{str(e)}"

    def download_report(self, instance):
        if not self.final_report:
            self.result_label.text = "No report to download!"
            return
        
        # Android Download Folder Path
        path = "/sdcard/Download/NetworkMaster_Report.txt"
        try:
            with open(path, "w") as f:
                f.write(self.final_report.replace('[color=00ff00]', '').replace('[/color]', ''))
            self.result_label.text += f"\n\n[color=00ff00]REPORT SAVED TO: {path}[/color]"
        except:
            # Fallback if permission issues
            self.result_label.text += "\n\n[color=ff0000]Permission Error: Enable Storage Access[/color]"

if __name__ == '__main__':
    NetworkMasterPro().run()
