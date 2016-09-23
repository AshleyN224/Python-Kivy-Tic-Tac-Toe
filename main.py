from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.config import Config
from ai import Ai
from random import randint

class TicTacToe(App):

    title = 'Tic Tac Toe'
    states = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    choices = ["X","O"]

    def build(self):
        Config.set('graphics', 'width', '600')
        Config.set('graphics', 'height', '600')
        layout = StackLayout()
        for x in range(9): # range() explanation: http://pythoncentral.io/pythons-range-function-explained/
            bt = Button(text=' ', font_size=200, width=200, height=200, size_hint=(None, None), id=str(x+1))
            bt.bind(on_release=self.btn_pressed)
            layout.add_widget(bt)
        return layout

    def on_start(self):
        self.init_players();
        greeting = "Hello Player! You are playing with \"" + self.player + "\""
        popup = Popup(title="Welcome!",
                content=Label(text=greeting),
                size=(300, 100),
                size_hint=(None, None))
        popup.open()

    def btn_pressed(self, button):
        button.text="X"
        self.states[int(button.id)-1] = "X"

    def init_players(self):
        rand_choice = randint(0,1);
        self.bot = Ai(self.choices[rand_choice]);
        self.player = self.choices[0] if rand_choice == 1 else self.choices[1]

if __name__ == '__main__':
    TicTacToe().run()
