from manim import *

class LargeCoordinateSystem(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 20, 2],          # start, end, step
            y_range=[0, 15000, 1000],   # start, end, step
            x_length=5,                # visual width
            y_length=5,                 # visual height
            axis_config={"include_numbers": True},
            tips=False
        )

        # Optional: axis labels
        x_label = axes.get_x_axis_label("x - Jahre")
        y_label = axes.get_y_axis_label("y - Geld")




        exgraph = axes.plot(
            lambda x: 5000 * (1.05 ** x),
            color=YELLOW
        )

        lingraph = axes.plot(
            lambda x: 5000 + x*(250),
            color=RED
        )

        




        x_tracker = ValueTracker(0)

        # Moving point
        dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    x_tracker.get_value(),
                    5000 * (1.05 ** x_tracker.get_value())
                ),
                color=RED
            )
        )

        # Coordinate label that follows the point
        coord_label = always_redraw(
            lambda: VGroup(
                MathTex(
                    f"x = {x_tracker.get_value():.1f}",
                    font_size=28
                ),
                MathTex(
                    f"y = {5000 * (1.05 ** x_tracker.get_value()):.0f}",
                    font_size=28
                )
            ).arrange(DOWN).next_to(dot, DOWN)
        )



        # Draw everything
        self.play(Create(axes))
        self.play(Create(exgraph))
        self.add(dot, coord_label)

        # Animate movement
        self.play(x_tracker.animate.set_value(20), run_time=6, rate_func=linear)

        self.wait(1)

        self.play(Write(lingraph), run_time = 3)

        self.wait(5)
        self.play(
            Unwrite(axes),
            Unwrite(lingraph),
            Unwrite(exgraph),
            Unwrite(coord_label),
            Unwrite(dot),
            run_time = 3
        )