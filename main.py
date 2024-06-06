import kivy
import math as m
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
kivy.require('1.0.7')

class MainApp(App):
    def build(self):
        self.sm = ScreenManager(transition=NoTransition())

        ############################################################
        main_screen = Screen(name="main")
        main_layout = BoxLayout(orientation="vertical")
        label_comp = Label(text="sar&a", pos_hint={"center_x": .5, "center_y": 1}, font_size=35)
        top_anch = AnchorLayout(anchor_x="center", anchor_y="top")
        top_anch.add_widget(label_comp)
        main_layout.add_widget(top_anch)
        label_name = Label(text="Welcome to Python Calc", pos_hint={"center_x": .5, "center_y": 1}, font_size=50)
        main_layout.add_widget(label_name)
        menu_gr = GridLayout(cols=2, height=.5, spacing=30)
        bool_btn = Button(text="Bool Calc", size_hint=(.5, 1))
        bool_btn.bind(on_release=self.tobool)
        bool_gui_btn = Button(text="Bool Guide", size_hint=(.5, 1))
        bool_gui_btn.bind(on_release=self.tobooltut)
        math_btn = Button(text="Math Calc", size_hint=(.5, 1))
        math_btn.bind(on_release=self.tomath)
        math_gui_btn = Button(text="Math Guide", size_hint=(.5, 1))
        math_gui_btn.bind(on_release=self.tomathtut)
        menu_gr.add_widget(bool_btn)
        menu_gr.add_widget(math_btn)
        menu_gr.add_widget(bool_gui_btn)
        menu_gr.add_widget(math_gui_btn)
        main_layout.add_widget(menu_gr)
        choose_label = Label(text="Choose and Check", font_size=55)
        main_layout.add_widget(choose_label)
        main_screen.add_widget(main_layout)
        self.sm.add_widget(main_screen)

        ############################################################
        bool_screen = Screen(name="bool")
        bool_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.solutionBool = TextInput(multiline=False, readonly=False, halign="right",
                                      font_size=55, input_filter="float")
        bool_layout.add_widget(self.solutionBool)
        buttons_bool = [
            ["1", "2", "3", "/", "=="],
            ["4", "5", "6", "*", "!="],
            ["7", "8", "9", "-", ">="],
            ["(", "0", ")", "+", "<="],
            [".", "<", ">", "%", "C"]
        ]
        for row in buttons_bool:
            hb_layout = BoxLayout()
            for label in row:
                if label == "C":
                    button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    font_size=22, background_color=(1, 0, 0, 1))
                else:
                    button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=22)
                button.bind(on_press=self.on_button_press_bool)
                hb_layout.add_widget(button)
            bool_layout.add_widget(hb_layout)
        equals_button_bool = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    background_color=(0, 1, 0, 1))
        equals_button_bool.bind(on_press=self.on_solution_bool)
        bool_layout.add_widget(equals_button_bool)
        menu_button_bool = Button(text="Menu", pos_hint={"center_x": 0.5, "center_y": 0.5},
                                  background_color=(0, 0, 1, 1))
        menu_button_bool.bind(on_release=self.tomain)
        bool_layout.add_widget(menu_button_bool)
        bool_screen.add_widget(bool_layout)
        self.sm.add_widget(bool_screen)

        ############################################################
        math_screen = Screen(name="math")
        math_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.solution = TextInput(multiline=False, readonly=False, halign="right", font_size=55, input_filter="float")
        math_layout.add_widget(self.solution)
        buttons_math = [
            ["1", "2", "3", "/", "m.log", "m.sin"],
            ["4", "5", "6", "*", "m.log10", "m.cos"],
            ["7", "8", "9", "-", "m.sqrt", "m.tan"],
            ["(", "0", ")", "+", "m.tau", "m.pi"],
            [".", "!=", "==", "C", "m.gcd", "m.e"]
        ]
        for row in buttons_math:
            h_layout = BoxLayout()
            for label in row:
                if label == "C":
                    button_math = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5},
                                         font_size=22, background_color=(1, 0, 0, 1))
                else:
                    button_math = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=22)
                button_math.bind(on_press=self.on_button_press)
                h_layout.add_widget(button_math)
            math_layout.add_widget(h_layout)
        equals_button_math = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    background_color=(0, 1, 0, 1))
        equals_button_math.bind(on_press=self.on_solution)
        math_layout.add_widget(equals_button_math)
        menu_button_math = Button(text="Menu", pos_hint={"center_x": 0.5, "center_y": 0.5},
                                  background_color=(0, 0, 1, 1))
        menu_button_math.bind(on_release=self.tomain)
        math_layout.add_widget(menu_button_math)
        math_screen.add_widget(math_layout)
        self.sm.add_widget(math_screen)

        ############################################################
        bool_tut_screen = Screen(name="bool_tut")
        bool_tut_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        bool_tut_top_anch = AnchorLayout(anchor_x="center", anchor_y="top")
        bool_tut_top_anch.add_widget(Label(text="sar&a", font_size=35))
        bool_tut_layout.add_widget(bool_tut_top_anch)
        bool_tut_text = Label(text="")
        bool_tut_layout.add_widget(bool_tut_text)
        bool_tut_menu_button = Button(text="Menu", pos_hint={"center_x": 0.5, "center_y": 0.5},
                                      background_color=(0, 0, 1, 1))
        bool_tut_menu_button.bind(on_release=self.tomain)
        bool_tut_layout.add_widget(bool_tut_menu_button)
        bool_tut_screen.add_widget(bool_tut_layout)
        self.sm.add_widget(bool_tut_screen)

        # Math guide screen
        math_tut_screen = Screen(name="math_tut")
        math_tut_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        math_tut_top_anch = AnchorLayout(anchor_x="center", anchor_y="top")
        math_tut_top_anch.add_widget(Label(text="sar&a", font_size=35))
        math_tut_layout.add_widget(math_tut_top_anch)
        math_tut_text = Label(text="", font_size=20)
        math_tut_layout.add_widget(math_tut_text)
        math_tut_menu_button = Button(text="Menu", pos_hint={"center_x": 0.5, "center_y": 0.5},
                                      background_color=(0, 0, 1, 1))
        math_tut_menu_button.bind(on_release=self.tomain)
        math_tut_layout.add_widget(math_tut_menu_button)
        math_tut_screen.add_widget(math_tut_layout)
        self.sm.add_widget(math_tut_screen)

        self.sm.current = "main"
        return self.sm

    def on_button_press(self, instance):
        if instance.text == "C":
            self.solution.text = ""
        else:
            self.solution.text += instance.text

    def on_button_press_bool(self, instance):
        if instance.text == "C":
            self.solutionBool.text = ""
        else:
            self.solutionBool.text += instance.text

    def on_solution(self, instance):
        if self.solution.text:
            try:
                self.solution.text = str(eval(self.solution.text))
            except:
                self.solution.text = "Error"

    def on_solution_bool(self, instance):
        if self.solutionBool.text:
            try:
                self.solutionBool.text = str(eval(self.solutionBool.text))
            except:
                self.solutionBool.text = "Error"

    def tobool(self, instance):
        self.sm.current = "bool"

    def tomain(self, instance):
        self.sm.current = "main"

    def tomath(self, instance):
        self.sm.current = "math"

    def tobooltut(self, instance):
        self.sm.current = "bool_tut"

    def tomathtut(self, instance):
        self.sm.current = "math_tut"

if __name__ == '__main__':
    MainApp().run()
