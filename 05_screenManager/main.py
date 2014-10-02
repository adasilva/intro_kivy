from kivy.app import App
from kivy.app import Widget

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    def __init__(self,**kwargs):
        super(MainScreen,self).__init__(**kwargs) # implements the features of a GridLayout (the base class of MainScreen)

    def save(self):
        '''Saves the data from the input to a text file.
    It is bound to the save button'''
        status = self.ids.workout1.ids.status.active
        workout = self.ids.workout1.ids.workoutInput.text
        day = self.ids.workout1.ids.dayInput.text
        time = self.ids.workout1.ids.timeInput.text
        with open('workoutData.txt','a') as f:
            f.write('%s, %s, %s, %s\n' %(status, workout, day, time))

        return None

    def totalTime(self):
        '''This function doesn't do anything right now! Add code to compute the total exercise time, and document it in this string'''
        return None

class WorkoutLayout(BoxLayout):
    pass
 
class SecondScreen(Screen):
    pass

class AppScreenManager(ScreenManager):
    pass

class WorkoutApp(App):
    def build(self):
        sm = AppScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='secondary'))
        return sm

if __name__=='__main__':
    WorkoutApp().run()



# NOTE: running is diff on diff platforms
# python main.py
# kivy main.py
