from manim import *

class CoordSysExample(Scene):
    def construct(self):

        text1 = MathTex(r"f(t) = 5000 * 1.05^3", font_size = 70).move_to(ORIGIN)
        text2 = MathTex(r"t = 5788.125", font_size = 70).next_to(text1, 2*DOWN)
        text3 = MathTex(r"6512.5 = 5000 * 1.05^t", font_size = 70).next_to(text2, 2*DOWN)
        text4 = MathTex(r"1.1025 = 1.05^t", font_size = 70).next_to(text3, 2*DOWN)
        text5 = MathTex(r"t = log_1.05 (1.1025)", font_size = 70).next_to(text4, 2*DOWN)
        text6 = MathTex(r"t = 2", font_size = 70).next_to(text5, 2*DOWN)
        text7 = MathTex(r"| :5000", font_size = 70).shift(5*DOWN, 5*RIGHT)

        texts = Group(text1, text2, text3, text4, text5, text6, text7)

        self.add(texts)

        texts.generate_target()
        texts.target.shift(ORIGIN)
        texts.target.shift(6*UP)

        self.play(
            
            Write(text1),
            Write(text2),
            Write(text3),
            Write(text4),
            Write(text5),
            Write(text6),
            Write(text7),
            run_time = 2
        )

        self.play(MoveToTarget(texts), run_time = 30, rate_func = linear)

        self.wait(1)
        self.play(
            Unwrite(text1),
            Unwrite(text2),
            Unwrite(text3),
            Unwrite(text4),
            Unwrite(text5),
            Unwrite(text6),
            Unwrite(text7),
        )

        self.wait(1)