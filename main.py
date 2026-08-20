import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.animation import Animation

class WalkingApp(App):
    def build(self):
        self.layout = FloatLayout()
        self.char = Label(text="🙋", font_size="60sp", size_hint=(None, None), size=(80, 80))
        self.char.pos = (100, 100)
        self.layout.add_widget(self.char)
        Clock.schedule_interval(self.move_char, 3)
        return self.layout

    def move_char(self, dt):
        new_x = random.randint(0, max(0, self.layout.width - 80))
        new_y = random.randint(0, max(0, self.layout.height - 80))
        anim = Animation(x=new_x, y=new_y, duration=2)
        anim.start(self.char)

if __name__ == "__main__":
    WalkingApp().run()