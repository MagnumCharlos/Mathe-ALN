from manim import *

class CoordSysExample(Scene):
    def construct(self):

        text = MathTex(r"\log_2 (16) = 4", font_size = 60).move_to(UP)
        #text2 = MarkupText("<span foreground="RED">2</span> = Basiswert").move_to(DOWN)
        #text16 = MarkupText("<span foreground="RED">16</span> = Endergebniss").next_to(text2, DOWN)
        #text4 = MarkupText("<span foreground="RED">4</span> = Exponent").next_to(text16, DOWN)
       
        text2 = MarkupText(' <span foreground="red"> 2 </span> = Basiswert', font_size=40).move_to(DOWN)
        text4 = MarkupText(' <span foreground="red"> 4 </span> = Exponent', font_size=40).next_to(text2, DOWN)
        text16 = MarkupText(' <span foreground="red"> 16 </span> = Endergebnis', font_size=40).next_to(text4, DOWN)
       
        self.wait(0.1)

        self.play(
            Write(text),
            Write(text2),
            Write(text4),
            Write(text16),
        )
        self.wait(5)

        self.play(
            Unwrite(text),
            Unwrite(text2),
            Unwrite(text4),
            Unwrite(text16),
        )

 
        