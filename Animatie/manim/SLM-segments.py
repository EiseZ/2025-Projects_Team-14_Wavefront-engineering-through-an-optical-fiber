from manim import *

scalar = 2

class SLM(Scene):
    def construct(self):
        self.wait()

        # Create SLM screen
        screen = Rectangle(width = (1.92 * scalar), height = (1.2 * scalar))
        screen.set_stroke(color = "white", width = (2 * scalar))

        slm_tex = Text("SLM").shift(UP * 3)

        self.play(Create(screen), Write(slm_tex))
        
        self.wait()

        # Zoom in
        zoom = 2
        self.play(screen.animate.scale(zoom))
        self.wait()

        # Compute scaled dimensions
        width_scaled = 1.92 * scalar * zoom
        height_scaled = 1.2 * scalar * zoom

        # Make pixel grid
        pixels = NumberPlane(
            x_range=[-width_scaled / 2, width_scaled / 2, 0.05],  # 0.4 units per square
            y_range=[-height_scaled / 2, height_scaled / 2, 0.05],
            x_length=width_scaled,
            y_length=height_scaled,
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 0.5,
                "stroke_opacity": 0.5,})
        
        # Make center axes match the background lines
        pixels.x_axis.set_stroke(color=WHITE, width=0.3, opacity = 0.4)
        pixels.y_axis.set_stroke(color=WHITE, width=0.3, opacity = 0.4)

        pixels.move_to(screen.get_center())

        pixels_tex = Text("Pixels").shift(DOWN * 3)


        self.play(FadeIn(pixels), Write(pixels_tex))
        self.wait()

        # Make laser beam 

        # Create translucent outer rings to simulate blur
        laser = VGroup()  # Group for all blurry layers
        for i in range(0, 15):
            fade_circle = Circle(radius=1.0 + i * 0.02)
            fade_circle.set_fill(color = "red", opacity=0.1)  # More transparent in outer layers
            fade_circle.set_stroke(opacity=0)
            laser.add(fade_circle)

        laser_tex = Text("Laser").shift(DOWN * 3)


        # Fade in the whole "laser"
        self.play(FadeIn(laser), Unwrite(pixels_tex))
        self.play(Write(laser_tex))
        self.wait()

        # Opdelen in segments
        segments = NumberPlane(
            x_range=[-width_scaled / 2, width_scaled / 2, 0.5],  # 0.4 units per square
            y_range=[-height_scaled / 2, height_scaled / 2, 0.5],
            x_length=width_scaled,
            y_length=height_scaled,
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1.5,
                "stroke_opacity": 0.5,})
        
        # Make center axes match the background lines
        segments.x_axis.set_stroke(color=WHITE, width=1.3, opacity = 0.3)
        segments.y_axis.set_stroke(color=WHITE, width=1.3, opacity = 0.3)

        segments.move_to(screen.get_center())

        segments_tex = Text("Segments").shift(DOWN * 3)


        self.play(FadeIn(segments), Unwrite(laser_tex))
        self.play(Write(segments_tex))
        self.wait(2)

        # SLM window
        window = Square(side_length = 3, stroke_width = 1)
        window.move_to(screen.get_center())

        not_window = Difference(screen, window, color = BLACK, fill_opacity = 0.5)
        not_window.set_stroke(color = WHITE, width = 1)
        self.play(FadeIn(window), FadeIn(not_window))
        self.wait()

        seg1 = Square(side_length= 0.5, color = "white", fill_opacity = 0.5)
        seg1.set_stroke(color = WHITE, width = 1)
        seg1.shift(UP * 1.25)
        seg1.shift(LEFT * 1.25)

        seg2 = Square(side_length= 0.5, color = "white", fill_opacity = 0.5)
        seg2.set_stroke(color = WHITE, width = 1)
        seg2.shift(UP * 1.25)
        seg2.shift(LEFT * 0.75)

        seg3 = Square(side_length= 0.5, color = "white", fill_opacity = 0.5)
        seg3.set_stroke(color = WHITE, width = 1)
        seg3.shift(UP * 1.25)
        seg3.shift(LEFT * 0.25)

        self.play(FadeIn(seg1))
        self.play(FadeOut(seg1), FadeIn(seg2))
        self.play(FadeOut(seg2), FadeIn(seg3))       
        self.wait()


