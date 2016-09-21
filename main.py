from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.config import Config


class TicTacToe(StackLayout):

    states = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, **kwargs):
        super(TicTacToe, self).__init__(**kwargs)
        for x in range(1,10):
            bt = Button(text=' ', font_size=200, width=200, height=200, size_hint=(None, None), id=str(x))
            bt.bind(on_release=self.btn_pressed)
            self.add_widget(bt)

    def btn_pressed(self, button):
        button.text="X"
        self.states[int(button.id)-1] = "X"
        print(self.states)

class MyApp(App):

    title = 'Tic Tac Toe'

    def build(self):
        Config.set('graphics', 'width', '600')
        Config.set('graphics', 'height', '600')
        return TicTacToe()


if __name__ == '__main__':
    MyApp().run()
