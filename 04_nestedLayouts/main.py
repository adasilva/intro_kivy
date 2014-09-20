from kivy.app import App
from kivy.app import Widget

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class MainScreen(BoxLayout):
    def __init__(self,**kwargs):
        super(MainScreen,self).__init__(**kwargs) # implements the features of a GridLayout (the base class of MainScreen)

    def save(self):
        '''Saves the data from the input to a text file.
    It is bound to the save button'''
        workout = self.ids.workout1.ids.workoutInput.text
        day = self.ids.workout1.ids.dayInput.text
        time = self.ids.workout1.ids.timeInput.text
        with open('workoutData.txt','a') as f:
            f.write('%s, %s, %s\n' %(workout, day, time))

        return None

    

class WorkoutLayout(BoxLayout):
    pass
        

class WorkoutApp(App):
    def build(self):
        return MainScreen()


if __name__=='__main__':
    WorkoutApp().run()



# NOTE: running is diff on diff platforms
# python main.py
# kivy main.py
