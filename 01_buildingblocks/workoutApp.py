from kivy.app import App
from kivy.app import Widget

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class UserInfoScreen(GridLayout):
    def __init__(self,**kwargs):
        super(UserInfoScreen,self).__init__(**kwargs) # implements the features of a GridLayout
        self.cols=3
        
        l1=Label(text='Workout')
        l2=Label(text='Day')
        l3=Label(text='Time')

        in1=TextInput(multiline=False)
        in2=TextInput(multiline=False)
        in3=TextInput(multiline=False)

        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(in1)
        self.add_widget(in2)
        self.add_widget(in3)
        

class TodoApp(App):
    def build(self):
        return UserInfoScreen()


if __name__=='__main__':
    TodoApp().run()



# NOTE: running is diff on diff platforms
# python main.py
# kivy main.py
