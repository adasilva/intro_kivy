from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MainScreen(GridLayout):
    def __init__(self,**kwargs):
        # add widgets...

        super(MainScreen,self).__init__(**kwargs) # implements the features of a GridLayout (the base class of MinScreen)
        self.cols=3
        
        l1=Label(text='Workout')
        l2=Label(text='Day')
        l3=Label(text='Time')

        in1=TextInput(multiline=False)  # multiline determines if more than one line of text is allowed
        in2=TextInput(multiline=False)
        in3=TextInput(multiline=False)

        self.add_widget(l1)  # Adds widgets to the layout
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(in1)
        self.add_widget(in2)
        self.add_widget(in3)
        

class WorkoutApp(App):
    def build(self):
        return MainScreen()


if __name__=='__main__':
    WorkoutApp().run()


