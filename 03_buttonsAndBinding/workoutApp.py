from kivy.app import App
from kivy.app import Widget

from kivy.uix.gridlayout import GridLayout


class MainScreen(GridLayout):
    def __init__(self,**kwargs):
        super(MainScreen,self).__init__(**kwargs) # implements the features of a GridLayout (the base class of MainScreen)

    def save(self):
        '''Saves the data from the input to a text file.
    It is bound to the save button'''
        workout = self.ids.workoutInput.text
        day = self.ids.dayInput.text
        time = self.ids.timeInput.text

        workout2 = self.ids.workoutInput2.text
        day2 = self.ids.dayInput2.text
        time2 = self.ids.timeInput2.text

        workout3 = self.ids.workoutInput3.text
        day3 = self.ids.dayInput3.text
        time3 = self.ids.timeInput3.text
        with open('workoutData.txt','a') as f:
            f.write('%s, %s, %s\n' %(workout, day, time))
            f.write('%s, %s, %s\n' %(workout2, day2, time2))
            f.write('%s, %s, %s\n' %(workout3, day3, time3))

        return None
        

class WorkoutApp(App):
    def build(self):
        return MainScreen()


if __name__=='__main__':
    WorkoutApp().run()



# NOTE: running is diff on diff platforms
# python main.py
# kivy main.py
