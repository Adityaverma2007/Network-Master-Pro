import subprocess
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class NetworkMasterPro(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10)
        self.display = Label(text="[🛰️] Network Master Pro: Initializing...\n", 
                            size_hint_y=None, halign='left', valign='top', markup=True)
        self.display.bind(texture_size=self.display.setter('size'))
        
        scroll = ScrollView()
        scroll.add_widget(self.display)
        self.root.add_widget(scroll)
        
        # ओरिजिनल पिंग एनालिसिस शुरू करें [cite: 2025-12-14]
        self.execute_ping_logic()
        return self.root

    def execute_ping_logic(self):
        ips = ["8.8.8.8", "1.1.1.1"] # Google and Cloudflare
        report = "\n[📊] FINAL STATUS SUMMARY\n" + "="*35 + "\n"
        
        for ip in ips:
            try:
                # 3 detailed pings [cite: 2025-12-14]
                subprocess.check_output(['ping', '-c', '3', ip])
                res = "[color=00FF00]OK[/color]"
            except:
                res = "[color=FF0000]NOT OK[/color]"
            report += f"IP: {ip} | Status: {res}\n"
            
        self.display.text += report + "="*35 + "\n[✅] Ready."

if __name__ == '__main__':
    NetworkMasterPro().run()
