from manim import *

class CoordSysExample(Scene):
    def construct(self):

        uberschrift = Text("Beispiel Zeitpunkt berechnen:").move_to(2*UP)
        text1 = MathTex("2361,96 = 4000 * 0.9^t").move_to(1*UP)
        text2 = MathTex("0,59049 = 0.9^t")#.move_to(1*UP)
        text3 = MathTex("\log_0,9 (0,59049) = 5").move_to(1*DOWN)
        text4 = MathTex("| :4000").next_to(text1, DR, -0.03*UP)

        self.play(
            Write(uberschrift)
        )
        self.wait(1.5)

        self.play(
            Write(text1)
        )
        self.wait(1.5)

        self.play(
            Write(text4)
        )
        self.wait(1.5)

        self.play(
            Write(text2)
        )
        self.wait(1.5)

        self.play(
            Write(text3)
        )
        self.wait(1.5)

        self.play(
            Unwrite(uberschrift),
            Unwrite(text1),
            Unwrite(text2),
            Unwrite(text3),
            Unwrite(text4),
        )