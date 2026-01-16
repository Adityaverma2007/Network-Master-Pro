import subprocess
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class NetworkMasterPro(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10)
        self.display = Label(text="[📡] Network Master Pro: Initializing...\n")
        self.layout.add_widget(self.display)
        self.run_ping_test()
        return self.layout

    def run_ping_test(self):
        # 3 detailed pings for each IP
        target_ips = ["8.8.8.8", "1.1.1.1"]
        results = ""
        for ip in target_ips:
            try:
                subprocess.check_output(['ping', '-c', '3', ip])
                results += f"IP: {ip} | Status: OK\n"
            except:
                results += f"IP: {ip} | Status: NOT OK\n"
        self.display.text += results

if __name__ == '__main__':
    NetworkMasterPro().run()
