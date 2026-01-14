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
        self.title = "Network Master Pro - Service Report Mode"
        # मुख्य लेआउट (Vertical)
        self.root = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # --- सर्विस डिटेल्स सेक्शन (Two Columns) ---
        details_grid = GridLayout(cols=2, spacing=15, size_hint_y=None)
        details_grid.bind(minimum_height=details_grid.setter('height'))

        # Left Side: Service Provider Details
        provider_box = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None, height=450)
        provider_box.add_widget(Label(text="[b]SERVICE PROVIDER[/b]", markup=True, size_hint_y=None, height=30))
        self.sp_name = TextInput(hint_text="Company Name", multiline=False)
        self.sp_addr = TextInput(hint_text="Address", multiline=False)
        self.eng_name = TextInput(hint_text="Engineer Name", multiline=False)
        self.eng_mob = TextInput(hint_text="Engineer Mobile", multiline=False)
        provider_box.add_widget(self.sp_name); provider_box.add_widget(self.sp_addr)
        provider_box.add_widget(self.eng_name); provider_box.add_widget(self.eng_mob)

        # Right Side: Service Client Details
        client_box = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None, height=450)
        client_box.add_widget(Label(text="[b]SERVICE CLIENT[/b]", markup=True, size_hint_y=None, height=30))
        self.sc_name = TextInput(hint_text="Client Company", multiline=False)
        self.sc_addr = TextInput(hint_text="Client Address", multiline=False)
        self.rp_name = TextInput(hint_text="Responsible Person", multiline=False)
        self.rp_mob = TextInput(hint_text="Client Mobile", multiline=False)
        client_box.add_widget(self.sc_name); client_box.add_widget(self.sc_addr)
        client_box.add_widget(self.rp_name); client_box.add_widget(self.rp_mob)

        details_grid.add_widget(provider_box)
        details_grid.add_widget(client_box)

        # --- IP & Scan Section ---
        scan_box = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None, height=250)
        self.start_ip = TextInput(hint_text="Start IP (192.168.1.1)", multiline=False)
        self.end_ip = TextInput(hint_text="End IP (192.168.1.10)", multiline=False)
        self.packet_size = TextInput(hint_text="Packet Size (Bytes)", multiline=False)
        self.report_date = TextInput(text=datetime.now().strftime("%Y-%m-%d %H:%M"), hint_text="Date", multiline=False)
        
        scan_box.add_widget(self.start_ip); scan_box.add_widget(self.end_ip)
        scan_box.add_widget(self.packet_size); scan_box.add_widget(self.report_date)

        # --- ScrollView for all inputs ---
        input_scroll = ScrollView(size_hint=(1, 0.6))
        main_input_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        main_input_layout.bind(minimum_height=main_input_layout.setter('height'))
        main_input_layout.add_widget(details_grid)
        main_input_layout.add_widget(scan_box)
        input_scroll.add_widget(main_input_layout)

        # --- Buttons ---
        btn_layout = BoxLayout(size_hint_y=None, height=70, spacing=10)
        self.run_btn = Button(text="START SCAN", background_color=(0, 0.7, 0, 1))
        self.run_btn.bind(on_press=self.start_analysis)
        self.download_btn = Button(text="SAVE REPORT", background_color=(0.2, 0.2, 0.8, 1))
        self.download_btn.bind(on_press=self.download_report)
        btn_layout.add_widget(self.run_btn); btn_layout.add_widget(self.download_btn)

        # --- Display Result ---
        self.result_label = Label(text="Fill details and start scan...", size_hint_y=None, markup=True, halign='left')
        self.result_label.bind(size=self.result_label.setter('text_size'))
        res_scroll = ScrollView(size_hint=(1, 0.4))
        res_scroll.add_widget(self.result_label)

        # Add everything to root
        self.root.add_widget(input_scroll)
        self.root.add_widget(btn_layout)
        self.root.add_widget(res_scroll)
        
        return self.root

    def start_analysis(self, instance):
        self.result_label.text = "Starting Analysis..."
        Clock.schedule_once(self.run_scan, 0.1)

    def run_scan(self, dt):
        # पिंग लॉजिक (जैसा पिछला था)
        report = f"[b]NETWORK SERVICE REPORT[/b]\nDate: {self.report_date.text}\n"
        report += "-"*40 + "\n"
        report += f"PROVIDER: {self.sp_name.text} | CLIENT: {self.sc_name.text}\n"
        report += f"ENGINEER: {self.eng_name.text} | PERSON: {self.rp_name.text}\n"
        report += "-"*40 + "\n"
        # यहाँ पिंग लूप चलेगा और रिपोर्ट अपडेट होगी...
        self.final_full_report = report # इसे डाउनलोड के लिए सुरक्षित करें
        self.result_label.text = report + "\nScan details will appear here..."

    def download_report(self, instance):
        # रिपोर्ट फाइल में डिटेल्स को प्रोफेशनली लिखना
        header = f"""
============================================================
                NETWORK MASTER PRO SERVICE REPORT
============================================================
DATE: {self.report_date.text}

SERVICE PROVIDER:                       SERVICE CLIENT:
-----------------                       ---------------
Company: {self.sp_name.text:<30} Company: {self.sc_name.text}
Address: {self.sp_addr.text:<30} Address: {self.sc_addr.text}
Engineer: {self.eng_name.text:<30} Resp. Person: {self.rp_name.text}
Mobile: {self.eng_mob.text:<30} Mobile: {self.rp_mob.text}
============================================================
"""
        # फाइल सेव करने का लॉजिक (जैसा पिछला था)
        path = "/sdcard/Download/Service_Report.txt"
        with open(path, "w") as f:
            f.write(header)
        self.result_label.text = f"Report Saved to {path}"

if __name__ == '__main__':
    NetworkMasterPro().run()
