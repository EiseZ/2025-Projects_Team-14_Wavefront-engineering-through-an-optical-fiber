from manim import *

# <<<<<<< HEAD
# =======
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

class FiberAnimation(Scene):
    def construct(self):
        outer_rect = Rectangle(width=10.0, height=2.5)
        outer_rect.set_fill("#FFFFFF", opacity=1)
        inner_rect = Rectangle(width=10.0, height=2.0)
        inner_rect.set_fill("#B9D9EB", opacity=1)
        fiber = Group(outer_rect, inner_rect)

        br1 = MathTex("n_1").move_to([4, -1.3, 0])
        br2 = MathTex("n_2").move_to([4, -0.7, 0])
        breq = MathTex("n_1 < n_2").move_to([4, -2.5, 0])

        screen = Ellipse(width=1, height=2, color=GRAY)
        screen.set_fill("#FFFFFF", opacity=1)

        setup = Group(fiber, screen).arrange(buff=2.0)
    

        p1 = [-7, 0, 1]
        p2 = [-5, 1, 1]
        p3 = [-1, -1, 1]
        p4 = [3, 1, 1]
        p5 = [6, -0.5, 1]
        laser1 = Line(p1, p2, color=RED).append_points(Line(p2, p3).points).append_points(Line(p3, p4).points).append_points(Line(p4, p5).points)

        p6 = [-8, -1, 1]
        p7 = [-3, 1, 1]
        p8 = [2, -1, 1]
        p9 = [6, 0.6, 1]
        laser2 = Line(p6, p7, color=RED).append_points(Line(p7, p8).points).append_points(Line(p8, p9).points)

        p10 = [-8, 1, 1]
        p11 = [-3, -1, 1]
        p12 = [2, 1, 1]
        p13 = [6, -0.6, 1]
        laser3 = Line(p10, p11, color=RED).append_points(Line(p11, p12).points).append_points(Line(p12, p13).points)


        self.play(FadeIn(fiber))
        self.play(Write(br1))
        self.play(Write(br2))
        self.play(Write(breq))
        self.play(FadeIn(screen))
        self.play(Create(laser1))
        self.play(Create(laser2))
        self.play(Create(laser3))
        # self.play(FadeOut(screen))

        speckle = ImageMobject("./speckle.png").set_width(1)
        Group(fiber, speckle).arrange(buff=2.0)
        self.play(FadeTransform(screen, speckle))
# >>>>>>> 467e44515f39fbc4b24b6571dd5ada284b8d237d
