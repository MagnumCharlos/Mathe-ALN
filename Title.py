from manim import *


class CoordSysExample(Scene):
    def construct(self):
        Over = Text("Mathe ALN", font_size=40, font="0xProto Nerd Font").move_to(2*UP)
        Mid = Text("Exponentialrechnung", font_size=80, font="0xProto Nerd Font")
        Under = Text("Matthis Brach ---- 10r3", font_size=40, font="0xProto Nerd Font").move_to(2*DOWN)


        #self.add(Over, Mid, Under)
        self.play(
            Write(Over),
            Write(Mid),
            Write(Under),
            run_time = 3
            )
        
        self.wait(2)

        self.play(
            Unwrite(Over),
            Unwrite(Mid),
            Unwrite(Under),
            run_time = 2)
        

        self.wait(0.1)