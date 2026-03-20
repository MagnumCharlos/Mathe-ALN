from manim import *

class CoordSysExample(Scene):
    def construct(self):

        gtext = MathTex(r"G_0 = 5000", font_size = 60)
        ptext = MathTex(r"p\% = 5000", font_size = 60)

        gtext.generate_target()
        gtext.target.shift(ORIGIN)
        gtext.target.shift(3*LEFT)

        ptext.generate_target()
        ptext.target.shift(ORIGIN)
        ptext.target.shift(3*RIGHT)
        
        
        self.play(Write(gtext))
        self.play(MoveToTarget(gtext))

        self.play(Write(ptext))
        self.play(MoveToTarget(ptext))