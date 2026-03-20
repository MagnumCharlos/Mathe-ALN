from manim import *

class CoordSysExample(Scene):
    def construct(self):
                # the location of the ticks depends on the x_range and y_range.
        grid = NumberPlane(
            x_range=[0, 15, 1],  # step size determines num_decimal_places.
            y_range=[0, 15, 1],
            x_length=7,
            y_length=7,
            axis_config={
                "numbers_to_include": np.arange(0, 15 + 1, 1),
                "font_size": 24,
            },
            tips=False,
        ).move_to(ORIGIN)


        l1 = Line(1.5*UP, ORIGIN, stroke_opacity = 0)
        l1.reverse_points()


        exgraph = grid.plot(lambda x: x ** 2/10, x_range=[0.001, 12.3], use_smoothing=False)


        self.play(
            Write(grid), Write(l1))
        
        self.wait(0.5)

        self.play(
            Write(exgraph), run_time=5)
        
        self.wait(2)
        
        extext = MathTex(r"f(t) = a*b^{t}", stroke_color=RED).move_to(DOWN)

        group = Group(grid, exgraph)

        self.play(
            ScaleInPlace(group, 0.5),
            MoveAlongPath(group, l1)
            )
        
        self.play(FadeToColor(exgraph, color=RED))

        #self.wait(0.5)

        extext = MathTex(r"f(t) = a*b^{t}", stroke_color=RED).move_to(DOWN)

        extext.generate_target()
        extext.target.shift(ORIGIN)
        extext.target.shift(3*LEFT)

        lintext = MathTex(r"f(t) = x", stroke_color=GREEN).move_to(DOWN)

        lintext.generate_target()
        lintext.target.shift(ORIGIN)
        
        lintext.target.shift(3*RIGHT)

        lingraph = grid.plot(lambda x: x *1, x_range=[0.001, 15], use_smoothing=False)

        #self.wait(2)
        self.play(Write(extext))
        self.wait(7)
        self.play(MoveToTarget(extext))

        self.wait(2)

        self.play(Write(lingraph))
        self.play(FadeToColor(lingraph, color=GREEN))

        self.play(Write(lintext))
        self.play(MoveToTarget(lintext))

        self.play(
            Unwrite(grid),
            Unwrite(exgraph),
            Unwrite(lingraph),
            Unwrite(extext),
            Unwrite(lintext),
            run_time = 3
            )

        self.wait(1)



        

