from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
import threading
from subprocess import Popen, PIPE

class PingApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = MDLabel(text="Ping Analysis Status", halign="center")
        btn = MDRaisedButton(text="Start Multi-IP Ping", pos_hint={"center_x": .5},
                             on_release=self.start_ping)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def start_ping(self, *args):
        # Threading taaki app hang na ho [cite: 2025-12-14]
        threading.Thread(target=self.run_ping).start()

    def run_ping(self):
        ips = ["8.8.8.8", "1.1.1.1"] # Isse test karein [cite: 2025-12-14]
        report = ""
        for ip in ips:
            # Professional 3 Detailed Pings [cite: 2025-12-14]
            process = Popen(['/system/bin/ping', '-c', '3', ip], stdout=PIPE, stderr=PIPE)
            stdout, _ = process.communicate()
            status = "OK" if process.returncode == 0 else "NOT OK"
            report += f"IP: {ip} | Status: {status}\n{'-'*20}\n"
        
        self.label.text = report

if __name__ == "__main__":
    PingApp().run()
