import subprocess
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class NetworkMasterPro(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        self.report = Label(text="[📡] Starting Multi-IP Ping Analysis...\n", 
                           size_hint_y=None, halign='left', valign='top', markup=True)
        self.report.bind(texture_size=self.report.setter('size'))
        
        scroll = ScrollView()
        scroll.add_widget(self.report)
        layout.add_widget(scroll)
        
        # 3 Detailed Pings Logic [cite: 2025-12-14]
        self.run_ping_test()
        return layout

    def run_ping_test(self):
        ips = ["8.8.8.8", "1.1.1.1"] 
        summary = "\n[📊] FINAL STATUS SUMMARY\n" + "="*35 + "\n"
        
        for ip in ips:
            try:
                # Performing 3 detailed pings [cite: 2025-12-14]
                subprocess.check_output(['ping', '-c', '3', ip])
                res = "[color=00FF00]OK[/color]"
            except:
                res = "[color=FF0000]NOT OK[/color]"
            summary += f"IP: {ip} | Status: {res}\n"
        
        self.report.text += summary + "="*35

if __name__ == '__main__':
    NetworkMasterPro().run()
