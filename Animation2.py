from manim import *

class CoordSysExample(Scene):
    def construct(self):

        extext = MathTex(r"f(t) = a*b^{t}",  font_size = 60).move_to(2*UP)

        atext = MathTex(r"a = Anfangswert", font_size = 50).shift(4*LEFT, 1*DOWN)
        btext = MathTex(r"b = Wachstumsfaktor", font_size = 50).next_to(atext, DOWN)

        iftext = MathTex(r"Wenn: b > 1= Wachstum",  font_size = 50).shift(3*RIGHT, 1*DOWN)
        ifnottext = MathTex(r"Wenn: b < 1= Zerfall",  font_size = 50).next_to(iftext, DOWN)

        self.play(
            Write(extext),
        )

        self.wait(3)

        self.play(Write(atext))
        self.wait(3)
        self.play(Write(btext))
        self.wait(3)
        self.play(Write(iftext), Write(ifnottext))
        
        self.wait(3)

        self.play(
            Unwrite(extext),
            Unwrite(atext),
            Unwrite(btext),
            Unwrite(iftext),
            Unwrite(ifnottext)
        )
        self.wait(1)