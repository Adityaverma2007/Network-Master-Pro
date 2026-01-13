from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import platform
import subprocess

class NetworkMasterPro(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # UI Elements
        self.label = Label(text="Network Master Pro - Professional Ping Analysis", size_hint_y=None, height=50)
        self.ip_input = TextInput(hint_text="Enter IP addresses (comma separated)", multiline=False, size_hint_y=None, height=50)
        self.run_btn = Button(text="Start Master Analysis", size_hint_y=None, height=50, background_color=(0, 0.7, 0, 1))
        self.run_btn.bind(on_press=self.run_analysis)
        
        self.result_view = ScrollView()
        self.result_label = Label(text="Results will appear here...", size_hint_y=None, halign='left', valign='top')
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.result_view.add_widget(self.result_label)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.ip_input)
        self.layout.add_widget(self.run_btn)
        self.layout.add_widget(self.result_view)
        
        return self.layout

    def run_analysis(self, instance):
        ips = [ip.strip() for ip in self.ip_input.text.split(',')]
        report = "--- MASTER REPORT ---\n"
        # Adding model info as requested
        report += f"Device Model Info: {platform.machine()} (System Interpretation Active)\n\n"
        
        for ip in ips:
            if not ip: continue
            report += f"Analyzing IP: {ip}\n"
            report += "-" * 30 + "\n"
            
            # Detailed 3 Pings Analysis
            count_param = '-n' if platform.system().lower() == 'windows' else '-c'
            try:
                output = subprocess.check_output(['ping', count_param, '3', ip], stderr=subprocess.STDOUT, universal_newlines=True)
                status = "STATUS: OK" if "0% packet loss" in output or "received, 0% packet loss" in output else "STATUS: NOT OK"
                report += f"{output}\nFinal Summary: {status}\n"
            except:
                report += "Final Summary: STATUS: NOT OK (Host Unreachable)\n"
            
            report += "=" * 30 + "\n\n"
        
        self.result_label.text = report
        self.result_label.height = self.result_label.texture_size[1]

if __name__ == '__main__':
    NetworkMasterPro().run().finish()