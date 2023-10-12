from manim import *

class Test(Scene):
    def construct(self):
        rectangle1 = Rectangle().shift(UP * 2) 
        rectangle2 = Rectangle().shift(DOWN * 2)

        self.add(rectangle1, rectangle2)
