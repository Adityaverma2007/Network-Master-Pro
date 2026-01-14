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

class NetworkMasterPro(App):
    def build(self):
        self.title = "Network Master Pro - Professional Mode"
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=5) # Spacing kam ki hai
        
        # --- Top Section: Service Details (Scrollable to save space) ---
        input_scroll = ScrollView(size_hint=(1, 0.45)) # Input area ko thoda chhota kiya taaki gap kam ho
        details_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        details_layout.bind(minimum_height=details_layout.setter('height'))

        # Two Column Grid for Provider & Client
        grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=400)
        
        # Left: Provider
        p_box = BoxLayout(orientation='vertical', spacing=2)
        p_box.add_widget(Label(text="[b]PROVIDER[/b]", markup=True, size_hint_y=None, height=30))
        self.sp_name = TextInput(hint_text="Company Name", multiline=False)
        self.sp_addr = TextInput(hint_text="Address", multiline=False)
        self.eng_name = TextInput(hint_text="Engineer Name", multiline=False)
        self.eng_mob = TextInput(hint_text="Mobile: 9416399442", multiline=False) # Contextual Number
        p_box.add_widget(self.sp_name); p_box.add_widget(self.sp_addr)
        p_box.add_widget(self.eng_name); p_box.add_widget(self.eng_mob)

        # Right: Client
        c_box = BoxLayout(orientation='vertical', spacing=2)
        c_box.add_widget(Label(text="[b]CLIENT[/b]", markup=True, size_hint_y=None, height=30))
        self.sc_name = TextInput(hint_text="Client Company", multiline=False)
        self.sc_addr = TextInput(hint_text="Client Address", multiline=False)
        self.rp_name = TextInput(hint_text="Responsible Person", multiline=False)
        self.rp_mob = TextInput(hint_text="Client Mobile", multiline=False)
        c_box.add_widget(self.sc_name); c_box.add_widget(self.sc_addr)
        c_box.add_widget(self.rp_name); c_box.add_widget(self.rp_mob)

        grid.add_widget(p_box); grid.add_widget(c_box)
        details_layout.add_widget(grid)

        # IP Config Section
        ip_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=120)
        self.start_ip = TextInput(hint_text="Start IP (e.g. 192.168.1.1)", multiline=False)
        self.end_ip = TextInput(hint_text="End IP (e.g. 192.168.1.10)", multiline=False)
        self.packet_size = TextInput(hint_text="Packet Size (Bytes)", text="32", multiline=False)
        self.report_date = TextInput(text=datetime.now().strftime("%Y-%m-%d %H:%M"), multiline=False)
        ip_grid.add_widget(self.start_ip); ip_grid.add_widget(self.end_ip)
        ip_grid.add_widget(self.packet_size); ip_grid.add_widget(self.report_date)
        
        details_layout.add_widget(ip_grid)
        input_scroll.add_widget(details_layout)

        # --- Middle Section: Buttons (Gap kam karne ke liye position change) ---
        btn_layout = BoxLayout(size_hint_y=None, height=60, spacing=10)
        self.run_btn = Button(text="START SCAN", background_color=(0, 0.6, 0, 1), bold=True)
        self.run_btn.bind(on_press=self.start_analysis)
        self.save_btn = Button(text="SAVE REPORT", background_color=(0.1, 0.1, 0.6, 1), bold=True)
        self.save_btn.bind(on_press=self.download_report)
        btn_layout.add_widget(self.run_btn); btn_layout.add_widget(self.save_btn)

        # --- Bottom Section: Live Results (Khali jagah bharne ke liye) ---
        self.res_scroll = ScrollView(size_hint=(1, 0.45))
        self.result_label = Label(text="[color=888888]System Ready for Analysis...[/color]", 
                                 markup=True, size_hint_y=None, halign='left', valign='top')
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.res_scroll.add_widget(self.result_label)

        self.root.add_widget(input_scroll)
        self.root.add_widget(btn_layout)
        self.root.add_widget(self.res_scroll)
        
        self.current_report_text = ""
        return self.root

    def start_analysis(self, instance):
        self.result_label.text = "[b]Initializing Master Scan...[/b]\n"
        self.current_report_text = ""
        Clock.schedule_once(self.run_scan_logic, 0.5)

    def run_scan_logic(self, dt):
        try:
            start = self.start_ip.text.strip()
            end = self.end_ip.text.strip()
            p_size = self.packet_size.text.strip() or "32"
            
            # Simple Range Logic
            base = ".".join(start.split('.')[:-1])
            s_num = int(start.split('.')[-1])
            e_num = int(end.split('.')[-1])

            self.current_report_text = f"--- SERVICE REPORT: {self.report_date.text} ---\n\n"
            
            for i in range(s_num, e_num + 1):
                ip = f"{base}.{i}"
                # Live Update Animation taaki user ko pata chale kaam ho raha hai
                self.result_label.text += f"Checking {ip}... "
                
                cmd = ['/system/bin/ping', '-c', '2', '-s', p_size, '-W', '1', ip]
                try:
                    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
                    # Extract Latency (ms)
                    ms = output.split('/')[-3] if '/' in output else "N/A"
                    res = f"[color=00ff00]OK ({ms}ms)[/color]\n"
                except:
                    res = "[color=ff0000]FAILED[/color]\n"
                
                self.result_label.text += res
                self.current_report_text += f"IP: {ip} | Status: {res.strip()}\n"
                self.result_label.height = self.result_label.texture_size[1]
                self.res_scroll.scroll_y = 0 # Auto-scroll to bottom
            
            self.result_label.text += "\n[b][color=00ff00]SCAN COMPLETED SUCCESSFULLY![/color][/b]"
        except Exception as e:
            self.result_label.text = f"[color=ff0000]Error: {str(e)}[/color]"

    def download_report(self, instance):
        if not self.current_report_text:
            self.result_label.text += "\n[color=ff0000]Run Scan first![/color]"
            return

        # Android path fix
        folder = "/sdcard/Documents/NetworkMasterReports"
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        filename = f"Report_{datetime.now().strftime('%H%M%S')}.txt"
        full_path = os.path.join(folder, filename)
        
        with open(full_path, "w") as f:
            f.write(self.current_report_text)
            
        self.result_label.text += f"\n\n[b]SAVED:[/b] [ref={full_path}][color=00aaff]{full_path}[/color][/ref]"
        self.result_label.bind(on_ref_press=self.open_file)

    def open_file(self, instance, value):
        # File par click karne par open karne ki koshish (Android Intent)
        try:
            os.system(f"am start -a android.intent.action.VIEW -d file://{value} -t text/plain")
        except:
            self.result_label.text += "\nCould not open directly. Check Documents folder."

if __name__ == '__main__':
    NetworkMasterPro().run()
