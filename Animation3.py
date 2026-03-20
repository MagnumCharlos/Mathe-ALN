from manim import *

class CoordSysExample(Scene):
    def construct(self):
        
        text = MathTex(r'q = 1 + \frac{5}{\text(p\%)}', font_size=70)
#       text = MathTex(r"q = 1 + \frac{1}{\text{"p%"}}")


        self.play(DrawBorderThenFill(text), run_time = 4)