from manim import *

class Test(Scene):
    def construct(self):
        rectangle1 = Rectangle().shift(UP * 2) 
        rectangle2 = Rectangle().shift(DOWN * 2)

        self.add(rectangle1, rectangle2)
        self.play(rectangle1.animate.set_fill(color= [TEAL, GREEN], opacity= 1), run_time=2)
        self.play(rectangle2.animate.scale(1.2), run_time=2)
        self.wait(1)
