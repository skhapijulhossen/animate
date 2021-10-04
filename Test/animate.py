from manim import *


class Animate(Scene):
    def construct(self):
        circle = Circle(color=BLACK)  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen