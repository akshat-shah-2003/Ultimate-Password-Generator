import random
import string
import clipboard
import logging
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.logger import Logger
import sys
sys.setrecursionlimit(1500)
Logger.info("This is an info message")
Logger.warning("This is a warning message")
class MyWidget(Widget):
    input1 = TextInput(multiline=False, size_hint=(None,None), size=(500,50), pos=(300,500), hint_text="Enter Keyword for Password", font_size=30)
    input2 = TextInput(multiline=True, size_hint=(None,None), size=(500,50), pos=(300,400), font_size=30, disabled=True)
    button1 = Button(text='GENERATE', size_hint=(None,None), size=(200,49.5), pos=(790,500), font_size=30)
    button2 = Button(text='COPY', size_hint=(None,None), size=(200,49.5),
                     pos=(790,400), font_size=30)

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.add_widget(self.input1)
        self.add_widget(self.input2)
        self.add_widget(self.button1)
        self.add_widget(self.button2)
        self.button1.bind(on_press=self.gen_pass)
        self.button2.bind(on_press=self.copy_pass)

    def gen_pass(self, length=8):
        self.key = self.input1.text if self.input1.text else "AbCd"
        c1 = random.choice(string.punctuation)
        c2 = random.choice(string.punctuation)
        c3 = self.key
        c4 = random.choice(string.digits)
        c5 = random.choice(string.digits)
        c6 = random.choice(string.digits)
        c7 = random.choice(string.ascii_letters.upper())
        c8 = random.choice(string.ascii_letters.lower())
        c = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8
        c=c.replace(" ","_")
        self.input2.text = c


    def copy_pass(self, instance):
        clipboard.copy(self.input2.text)

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Window.fullscreen = 'auto'
    MyApp().run()
