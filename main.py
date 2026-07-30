from kivy.app import App
from kivy.uix.label import Label
import os

class HelloArabicApp(App):
    def build(self):
        # استخدم الخط العربي إذا كان موجودًا، وإلا استخدم الخط الافتراضي
        font_path = 'arabic_font.ttf'
        if not os.path.exists(font_path):
            font_path = None  # قد لا يظهر النص العربي في هذه الحالة

        return Label(
            text='مرحباً بالعالم',
            font_name=font_path,
            font_size='40sp',
            halign='center',
            valign='middle'
        )

if __name__ == '__main__':
    HelloArabicApp().run()