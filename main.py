from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock # Android पर स्मूथ अपडेट के लिए
import platform
import subprocess

class NetworkMasterPro(App):
    def build(self):
        # 'self.title' सेट करना ज़रूरी है ताकि ऊपर नाम दिखे
        self.title = "Network Master Pro"
        
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # UI Elements
        self.label = Label(text="Network Master Pro\nProfessional Ping Analysis", 
                           size_hint_y=None, height=100, halign='center')
        
        self.ip_input = TextInput(hint_text="Enter IP addresses (e.g. 8.8.8.8, 1.1.1.1)", 
                                  multiline=False, size_hint_y=None, height=100)
        
        self.run_btn = Button(text="Start Master Analysis", size_hint_y=None, height=100, 
                              background_color=(0, 0.6, 0.2, 1), font_size='20sp')
        self.run_btn.bind(on_press=self.run_analysis)
        
        self.result_view = ScrollView(size_hint=(1, 1))
        self.result_label = Label(text="Results will appear here...", size_hint_y=None, 
                                 halign='left', valign='top', markup=True)
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.result_view.add_widget(self.result_label)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.ip_input)
        self.layout.add_widget(self.run_btn)
        self.layout.add_widget(self.result_view)
        
        return self.layout

    def run_analysis(self, instance):
        self.result_label.text = "Analyzing... Please wait..."
        # छोटी सी देरी ताकि UI अपडेट हो सके
        Clock.schedule_once(self.perform_ping, 0.1)

    def perform_ping(self, dt):
        ips = [ip.strip() for ip in self.ip_input.text.split(',')]
        report = "[b]--- MASTER REPORT ---[/b]\n"
        report += f"Contact: 9416399442\n"
        report += f"Model Arch: {platform.machine()}\n\n"
        
        for ip in ips:
            if not ip: continue
            report += f"Analyzing IP: {ip}\n"
            report += "-" * 20 + "\n"
            
            # Android पर पिंग करने का सही तरीका
            try:
                # Android में पिंग का पाथ अक्सर /system/bin/ping होता है
                cmd = ['/system/bin/ping', '-c', '3', ip]
                output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
                
                if "3 packets transmitted, 3 received" in output or "0% packet loss" in output:
                    status = "[color=00ff00]STATUS: OK[/color]"
                else:
                    status = "[color=ff0000]STATUS: NOT OK[/color]"
                
                report += f"{output}\n{status}\n"
            except Exception as e:
                report += f"Final Summary: [color=ff0000]STATUS: NOT OK[/color]\n(Unreachable or System Blocked)\n"
            
            report += "=" * 20 + "\n\n"
        
        self.result_label.text = report
        # हाइट अपडेट करना ताकि स्क्रॉल काम करे
        self.result_label.height = max(self.result_label.texture_size[1], self.result_view.height)

if __name__ == '__main__':
    NetworkMasterPro().run() # .finish() हटा दिया गया है
