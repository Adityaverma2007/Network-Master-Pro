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
        
        self.run_ping_test()
        return layout

    def run_ping_test(self):
        # 3 detailed pings for each IP [cite: 2025-12-14]
        target_ips = ["8.8.8.8", "1.1.1.1"]
        summary = "\n[📊] FINAL STATUS SUMMARY\n" + "="*35 + "\n"
        
        for ip in target_ips:
            try:
                subprocess.check_output(['ping', '-c', '3', ip])
                status = "[color=00FF00]OK[/color]"
            except:
                status = "[color=FF0000]NOT OK[/color]"
            summary += f"IP: {ip} | Status: {status}\n"
        
        self.report.text += summary + "="*35

if __name__ == '__main__':
    NetworkMasterPro().run()
