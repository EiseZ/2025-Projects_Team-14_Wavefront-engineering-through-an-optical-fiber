from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(GREEN, opacity= 1) # filling
        circle.set_stroke(BLUE, opacity=1) # line
        self.play(Create(circle)) # animate

class CreateSquare(Scene):
    def construct(self):
        square = Square()  # create a square
        square.set_fill(GREEN, opacity= 1) # filling
        square.set_stroke(BLUE, opacity=1) # line
        self.play(Create(square)) # animate


class CreateTriangle(Scene):
    def construct(self):
        triangle = Triangle()  # create a triangle
        triangle.set_fill(GREEN, opacity= 1) # filling
        triangle.set_stroke(BLUE, opacity=1) # line 
        self.play(Create(triangle)) # animate

class CreateCircleAndSquare(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(GREEN, opacity= 1) # filling
        circle.set_stroke(BLUE, opacity=1) # line
        self.play(Create(circle)) # animate
        self.clear() # delete circle
        square = Square()  # create a square
        square.set_fill(PINK, opacity= 1) # filling
        square.set_stroke(RED, opacity=1) # line
        self.play(Create(square)) # animate
