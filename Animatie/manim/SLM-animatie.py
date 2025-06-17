from manim import *

class CreateRectangle(Scene):
    def construct(self):
        self.wait(1)
        rect = Rectangle(width= 2.0, height=4.0)
        l1 = Line(start = [-5, -2, 0], end=[-5, -2/3, 0], color = RED)
        l2 = Line(start = [-5, -2/3, 0], end=[-5, 2/3, 0], color = RED)
        l3= Line(start = [-5, 2/3, 0], end=[-5, 2, 0], color = RED)
        l = Group(l1, l2, l3)
        lb = Line(start = [-5,0,0], end = [1,0,0])
        lc = Line(start = [1,0,0], end = [-5,0,0])
        ld = Line(start = [-5,0,0], end = [-1,0,0])
        le_1 = Line(start = [-1,-4/3,0], end = [1,-4/3,0])
        lf_1 = Line(start = [1,-4/3,0], end = [-1,-4/3,0])
        lg_1 = Line(start = [-1,-4/3,0], end = [-5,-4/3,0])
        le_2= Line(start = [-1,0,0], end = [1,0,0])
        lf_2 = Line(start = [1,0,0], end = [-1,0,0])
        lg_2 = Line(start = [-1,0,0], end = [-5,0,0])
        le_3 = Line(start = [-1,4/3,0], end = [1,4/3,0])
        lf_3 = Line(start = [1,4/3,0], end = [-1,4/3,0])
        lg_3 = Line(start = [-1,4/3,0], end = [-5,4/3,0])
        ellipse_1 = Ellipse(width=0.5, height=0.8, color= WHITE)
        ellipse_1.set_fill(color=WHITE, opacity=1)
        ellipse_1.move_to([-0.5, 1, 0])
        ellipse_2 = Ellipse(width=0.5, height=0.8, color= WHITE)
        ellipse_2.set_fill(color=WHITE, opacity=1)
        ellipse_2.move_to([0.5, 1, 0])
        ellipse_3 = Ellipse(width=0.5, height=0.8, color= WHITE)
        ellipse_3.set_fill(color=WHITE, opacity=1)
        ellipse_3.move_to([-0.5, -1, 0])
        ellipse_4 = Ellipse(width=0.5, height=0.8, color= WHITE)
        ellipse_4.set_fill(color=WHITE, opacity=1)
        ellipse_4.move_to([0.5, -1, 0])
        ellipse_5 = Ellipse(width=0.5, height=0.8, color= WHITE)
        ellipse_5.set_fill(color=WHITE, opacity=1)
        ellipse_5.move_to([0.5, 0, 0])
        ellipse_6 = Ellipse(width=0.5, height=0.8, color= WHITE)
        ellipse_6.set_fill(color=WHITE, opacity=1)
        ellipse_6.move_to([-0.5, 0, 0])
        group_ellips = Group(ellipse_1, ellipse_2, ellipse_3, ellipse_4, ellipse_5, ellipse_6)
        # Iets met golven
        self.play(Create(rect))
        self.play(FadeIn(group_ellips))
        self.play(FadeIn(l))
        self.play(MoveAlongPath(l,lb ), rate_func=linear)
        self.play(MoveAlongPath(l,lc))
        self.play(FadeOut(l))
        #Golven
        self.play((Rotate(ellipse_1, angle= (1/6)*PI, about_point= [-0.5, 1, 0])),
                  (Rotate(ellipse_2, angle= (1/6)*PI, about_point= [0.5, 1, 0])))
        
        self.play((Rotate(ellipse_6, angle= (1/2)*PI, about_point= [-0.5, 0, 0])),
                  (Rotate(ellipse_5, angle= (1/2)*PI, about_point= [0.5, 0, 0])))
        
        self.play((Rotate(ellipse_3, angle= (3/8)*PI, about_point= [-0.5, -1, 0])),
                  (Rotate(ellipse_4, angle= (3/8)*PI, about_point= [0.5, -1, 0])))
        self.play(FadeIn(l))
        self.play(MoveAlongPath(l,ld ), rate_func=linear)
        self.play(
            Succession(
                MoveAlongPath(l1,le_1 , rate_func=linear,run_time=1.3),
                MoveAlongPath(l1,lf_1 , rate_func=linear,run_time=1.3),
                MoveAlongPath(l1,lg_1 , rate_func=linear),
                FadeOut(l1)
                ),
            
            Succession(
                MoveAlongPath(l2,le_2 , rate_func=linear,run_time=2),
                MoveAlongPath(l2,lf_2 , rate_func=linear,run_time=2),
                MoveAlongPath(l2,lg_2 , rate_func=linear),
                FadeOut(l2)
                ),
            Succession(
                MoveAlongPath(l3,le_3 , rate_func=linear,run_time=1.8),
                MoveAlongPath(l3,lf_3 , rate_func=linear,run_time=1.8),
                MoveAlongPath(l3,lg_3 , rate_func=linear),
                FadeOut(l3)
                ),
            )
        
        self.wait(1)