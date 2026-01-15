from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import subprocess
import threading
from datetime import datetime

# --- Screen 1: Provider Details ---
class ProviderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="[b]SERVICE PROVIDER DETAILS[/b]", markup=True, size_hint_y=None, height=50))
        self.sp_name = TextInput(hint_text="Company Name", multiline=False)
        self.sp_addr = TextInput(hint_text="Address", multiline=False)
        self.eng_name = TextInput(hint_text="Engineer Name", multiline=False)
        self.eng_mob = TextInput(hint_text="Engineer Mobile (9416399442)", multiline=False)
        for w in [self.sp_name, self.sp_addr, self.eng_name, self.eng_mob]: layout.add_widget(w)
        btn = Button(text="SAVE & BACK", size_hint_y=None, height=60, background_color=(0, 0.7, 0, 1))
        btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(btn)
        self.add_widget(layout)

# --- Screen 2: Client Details ---
class ClientScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="[b]SERVICE CLIENT DETAILS[/b]", markup=True, size_hint_y=None, height=50))
        self.sc_name = TextInput(hint_text="Client Company", multiline=False)
        self.sc_addr = TextInput(hint_text="Client Address", multiline=False)
        self.rp_name = TextInput(hint_text="Responsible Person", multiline=False)
        self.rp_mob = TextInput(hint_text="Client Mobile", multiline=False)
        for w in [self.sc_name, self
