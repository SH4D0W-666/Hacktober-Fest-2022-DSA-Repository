import kivy
import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

class Calculator(Screen):

    def bye(self):
        quit()

    def clear(self):
        self.ids.val.text = ''

    def use(self, b):
        x = self.ids.val.text
        if x == '0':
            self.ids.val.text = f'{b}'
        else:
            self.ids.val.text = f'{x}{b}'

    def add(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}+'

    def sub(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}-'

    def mul(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}*'

    def div(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}/'

    def factorial(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}!'

    def exp(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}^'

    def ans(self):
        x = self.ids.val.text
        if '+' in x:
            l = x.split('+')
            a = float(l[0])
            b = float(l[1])
            r = a + b
            r = round(r, 5)
            self.ids.val.text = str(r)

        elif '-' in x:
            l = x.split('-')
            a = float(l[0])
            b = float(l[1])
            r = a - b
            r = round(r, 5)
            self.ids.val.text = str(r)

        elif '*' in x:
            l = x.split('*')
            a = float(l[0])
            b = float(l[1])
            r = a * b
            r = round(r, 5)
            self.ids.val.text = str(r)

        elif '/' in x:
            l = x.split('/')
            a = float(l[0])
            b = float(l[1])
            if b != 0:
                r = a / b
                r = round(r, 5)
                self.ids.val.text = str(r)
            else:
                self.ids.val.text = 'ERROR'

        elif '!' in x:
            y=x.split('!')
            n = int(y[0])
            f = 1
            if n != 0:
                for i in range(1, n + 1):
                    f *= i
                self.ids.val.text = str(f)
            else:
                f = 1
                self.ids.val.text = str(f)

        elif '^' in x:
            l = x.split('^')
            a = float(l[0])
            b = float(l[1])
            r = a ** b
            r=round(r,5)
            self.ids.val.text = str(r)

    def inv(self):
        x = self.ids.val.text
        p = float(x)
        r = p ** -1
        r = round(r, 5)
        self.ids.val.text = (str(r))

    def slice(self):
        x = self.ids.val.text
        y = x[0:len(x) - 1]
        self.ids.val.text = y


class Manager(ScreenManager):
    pass


a = Builder.load_file('Calculator.kv')


class MyGrid(Widget):
    pass


class ØX(App):
    def build(self):
        return a


ØX().run()
