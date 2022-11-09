'''{Author:Kolawole Andrew
    Date: Wednesday, ‎August ‎31, ‎2022, ‏‎6:53:19 AM}'''
    
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.image import Image
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.graphics.instructions import Canvas
import sys
import Matrix

class WindowManager(ScreenManager):
    pass

class SelectOperation(Screen):
    pass

class EquationWindows(Screen):
    def quit_app(self):
        print('I am linked..')
    
class SolveBy2(Screen):
    def __init__(self,**kwargs):
        super(SolveBy2,self).__init__(**kwargs)
        
    def solve_eqn(self):
        a = float(self.ids.a.text)
        b = float(self.ids.b.text)
        c = float(self.ids.c.text)
        d = float(self.ids.d.text)
        e = float(self.ids.e.text)
        f = float(self.ids.f.text)
        soln = Matrix.solve_by2(a, b, c, d, e, f)
        self.ids.ans_label.text = 'Answer: ' + str(soln)
        print(self.ids.some)
            
        
class SolveBy3(Screen):
    
    def __init__(self,**kwargs):
        super(SolveBy3,self).__init__(**kwargs)
      
    def solve_eqn(self):

        l = []
        for i in range(12):
            b = self.ids['b_'+str(i)].text
            l.append(b)

        eqn1 = str(l[0]) + ','+ str(l[1])+ ','+ str(l[2]) + ','+ str(l[3])
        eqn2 = str(l[4]) + ','+ str(l[5])+ ','+ str(l[6]) + ','+ str(l[7])
        eqn3 = str(l[8]) + ','+ str(l[9])+ ','+ str(l[10]) + ','+ str(l[11])
        soln = Matrix.solve_by3(eqn1,eqn2,eqn3)
        self.ids.by3_ans.text = self.ids.by3_ans.text+ '\n' +str(soln)
        
        

class Quadratic(Screen):
    def __init__(self,**kwargs):
        super(Quadratic,self).__init__(**kwargs)  
    def solve_eqn(self):
    
        a = float(self.ids['a'].text)
        b = float(self.ids['b'].text)
        c = float(self.ids['c'].text)
        soln = Matrix.quadratic(a, b, c)
        if len(soln) > 30:
            self.ids.quad_ans.font_size = dp(12)
            self.ids.quad_ans.text = str(soln)
        else:
            self.ids.quad_ans.text = self.ids.quad_ans.text + '\n' + str(soln)


class MatrixWindow(Screen):
    def __init__(self,**kwargs):
        super(MatrixWindow,self).__init__(**kwargs)

class By2Determinant(Screen):
    def __init__(self,**kwargs):
        super(By2Determinant,self).__init__(**kwargs)
        def solve_eqn(self):
            print('Hello World')

class By3Determinant(Screen):
    def __init__(self,**kwargs):
        super(By3Determinant,self).__init__(**kwargs)

    

class InverseCofactor(Screen):
    def __init__(self,**kwargs):
        super(InverseCofactor,self).__init__(**kwargs)


class VectorWindow(Screen):
    def __init__(self,**kwargs):
        super(VectorWindow,self).__init__(**kwargs)

class Vector2D(Screen):
    def __init__(self,**kwargs):
        super(Vector2D,self).__init__(**kwargs)
            
class Vector3D(Screen):
    def __init__(self,**kwargs):
        super(Vector3D,self).__init__(**kwargs)
                
class Calculator(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        bck_img = Image(source = 'light.jpg',allow_stretch = True, keep_ratio = False)
        self.add_widget(bck_img)
        main_box = BoxLayout(orientation = 'vertical')
        self.add_widget(main_box)
        child_box = BoxLayout(orientation = 'vertical',spacing=dp(5),padding=dp(5),size_hint = (1,.3))
        main_box.add_widget(child_box)
        grid_lay = GridLayout(cols = 5,spacing = dp(3))
        main_box.add_widget(grid_lay)


       

        ''' list_obj = [i for i in range(10)]# + ['X','/','+','-']
        self.box_1 = BoxLayout(orientation = 'vertical',spacing = dp(5), padding= dp(3))
        
        self.grid = GridLayout(cols = 5,spacing=dp(3),padding=dp(2))
        self.add_widget(self.grid)

        for i in list_obj:
            btn = Button(text = str(list_obj[i]),size_hint = (None,None),width=dp(40),height=dp(40))
            self.grid.add_widget(btn)
            #self.add_widget(btn)'''

    
class About(Screen):
    
    text = StringProperty('')
    def __init__(self,**kwargs):
        super(About,self).__init__(**kwargs)
        with open('About.txt','r') as f:
            About.text = f.read()
            f.close()




kv = Builder.load_file('main.kv')
class CalcApp(App):
    def build(self):
        Window.size = [250,300]
        return kv


if __name__ == '__main__':
    CalcApp().run()