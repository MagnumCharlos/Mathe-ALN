from manim import *

class CoordSysExample(Scene):
    def construct(self):

        textwachstum = Text("Beispiel Wachstum:").shift(3*UP)
        textzerfall = Text("Beispiel Zerfall:").move_to(textwachstum.get_center())
        text1 = MathTex(r"5290 = 4000 * 1.15^2")
        text2 =MathTex(r"3240 = 4000 * 0.9^2")

        self.play(Write(textwachstum), run_time = 2)
        self.play(Write(text1), run_time = 3)


        self.wait(2)

        self.play(Unwrite(textwachstum), Unwrite(text1), run_time = 1.5)

        self.play(Write(text2), Write(textzerfall))

        self.wait(2)

        self.play(Unwrite(textzerfall), Unwrite(text2), run_time = 1.5)