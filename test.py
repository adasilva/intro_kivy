from kivy.app import App
from kivy.app import Widget

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class UserInfoScreen(FloatLayout):
    def __init__(self,**kwargs):
        super(UserInfoScreen,self).__init__(**kwargs)
        self.add_widget(Label(text='Test was a success!'))

class TodoApp(App):
    def build(self):
        return UserInfoScreen()


if __name__=='__main__':
    TodoApp().run()

