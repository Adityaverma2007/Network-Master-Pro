from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
import threading
from subprocess import Popen, PIPE
import platform

class PingMasterApp(MDApp):
    def build(self):
        # Professional UI Setup [cite: 2026-01-06]
        self.theme_cls.primary_palette = "Blue"
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

        self.status_label = MDLabel(
            text="Multi-IP Ping Analysis Ready",
            halign="center",
            theme_text_color="Primary",
            font_style="H6"
        )

        # Result area with scrolling for long reports [cite: 2025-12-14]
        scroll = MDScrollView()
        self.result_text = MDLabel(
            text="Results will appear here...",
            halign="left",
            size_hint_y=None
        )
        self.result_text.bind(texture_size=self.result_text.setter('size'))
        scroll.add_widget(self.result_text)

        btn = MDRaisedButton(
            text="Start Detailed Ping",
            pos_hint={"center_x": .5},
            on_release=self.start_analysis
        )

        layout.add_widget(self.status_label)
        layout.add_widget(btn)
        layout.add_widget(scroll)
        screen.add_widget(layout)
        return screen

    def start_analysis(self, *args):
        # Threading taaki UI freeze na ho [cite: 2025-12-14]
        self.result_text.text = "Analyzing Latency...\n"
        threading.Thread(target=self.run_ping_logic).start()

    def run_ping_logic(self):
        # Aapki perfect Multi-IP list [cite: 2025-12-14]
        target_ips = ["8.8.8.8", "1.1.1.1", "192.168.0.1"]
        final_report = ""
        
        for ip in target_ips:
            try:
                # 3 Detailed pings as requested [cite: 2025-12-14]
                ping_cmd = ['/system/bin/ping', '-c', '3', ip]
                process = Popen(ping_cmd, stdout=PIPE, stderr=PIPE)
                stdout, _ = process.communicate()
                
                status = "OK" if process.returncode == 0 else "NOT OK"
                
                # Report with divider lines [cite: 2025-12-14]
                final_report += f"{'='*30}\n"
                final_report += f"Target IP: {ip}\nStatus: {status}\n"
                final_report += f"Details: {stdout.decode('utf-8') if stdout else 'No Data'}\n"
                
            except Exception as e:
                final_report += f"Error pinging {ip}: {str(e)}\n"

        # Update UI with Final Summary [cite: 2025-12-14]
        self.result_text.text = final_report
        self.status_label.text = "Analysis Complete"

if __name__ == "__main__":
    PingMasterApp().run()
