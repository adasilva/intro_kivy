from kivy.app import App
from kivy.app import Widget

from kivy.uix.gridlayout import GridLayout


class MainScreen(GridLayout):
    def __init__(self,**kwargs):
        super(MainScreen,self).__init__(**kwargs) # implements the features of a GridLayout (the base class of MainScreen)
        

class WorkoutApp(App):
    def build(self):
        return MainScreen()


if __name__=='__main__':
    WorkoutApp().run()



# NOTE: running is diff on diff platforms
# python main.py
# kivy main.py
