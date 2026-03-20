from manim import *

class CoordSysExample(Scene):
    def construct(self):

        text1 = Text("Alle Animationen und Quellcodes auf:", font_size = 35).move_to(UP)
        text2 = Text("https://github.com/MagnumCharlos/Mathe-ALN/tree/main", font_size = 20).next_to(text1, DOWN)

        self.play(Write(text1), Write(text2))
        self.wait(5)
        self.play(Unwrite(text1), Unwrite(text2))
        self.wait(1)