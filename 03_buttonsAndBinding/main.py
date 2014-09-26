from kivy.app import App
from kivy.app import Widget

from kivy.uix.gridlayout import GridLayout


class MainScreen(GridLayout):
    def __init__(self,**kwargs):
        super(MainScreen,self).__init__(**kwargs) # implements the features of a GridLayout (the base class of MainScreen)

    def save(self):
        '''Saves the data from the input to a text file.
    It is bound to the save button'''
        status1 = self.ids.checkbox1.active  #active is boolean (True or False)
        workout1 = self.ids.workoutInput1.text
        day1 = self.ids.dayInput1.text
        time1 = self.ids.timeInput1.text

        status2 = self.ids.checkbox2.active
        workout2 = self.ids.workoutInput2.text
        day2 = self.ids.dayInput2.text
        time2 = self.ids.timeInput2.text

        status3 = self.ids.checkbox3.active
        workout3 = self.ids.workoutInput3.text
        day3 = self.ids.dayInput3.text
        time3 = self.ids.timeInput3.text
        with open('workoutData.txt','a') as f:
            f.write('%s, %s, %s, %s\n' %(status1, workout1, day1, time1))
            f.write('%s, %s, %s, %s\n' %(status2, workout2, day2, time2))
            f.write('%s, %s, %s, %s\n' %(status3, workout3, day3, time3))

        return None
        

class WorkoutApp(App):
    def build(self):
        return MainScreen()


if __name__=='__main__':
    WorkoutApp().run()



# NOTE: running is diff on diff platforms
# python main.py
# kivy main.py
