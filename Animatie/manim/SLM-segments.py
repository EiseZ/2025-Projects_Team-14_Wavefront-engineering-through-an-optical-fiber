from manim import *

scalar = 2

class SLM(Scene):
    def construct(self):
        # Create SLM screen
        screen = Rectangle(width = (1.92 * scalar), height = (1.2 * scalar))
        screen.set_stroke(color = "white", width = (2 * scalar))
        self.wait()
        self.play(Create(screen))
        
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

        self.play(FadeIn(pixels))
        self.wait()

        # Make laser beam 

        # Create translucent outer rings to simulate blur
        laser = VGroup()  # Group for all blurry layers
        for i in range(0, 15):
            fade_circle = Circle(radius=1.0 + i * 0.02)
            fade_circle.set_fill(color = "red", opacity=0.1)  # More transparent in outer layers
            fade_circle.set_stroke(opacity=0)
            laser.add(fade_circle)

        # Fade in the whole "laser"
        self.play(FadeIn(laser, run_time=2))
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


        dim_pixels = NumberPlane(
            x_range=[-width_scaled / 2, width_scaled / 2, 0.05],  # 0.4 units per square
            y_range=[-height_scaled / 2, height_scaled / 2, 0.05],
            x_length=width_scaled,
            y_length=height_scaled,
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 0.5,
                "stroke_opacity": 0.2,})
        
        # Make center axes match the background lines
        dim_pixels.x_axis.set_stroke(color=WHITE, width=0.3, opacity = 0.15)
        dim_pixels.y_axis.set_stroke(color=WHITE, width=0.3, opacity = 0.15)

        dim_pixels.move_to(screen.get_center())
        dim_pixels.z_index = -1

        self.play(FadeIn(segments))
        self.wait()

        # SLM window
        window = Square(side_length = 3, stroke_width = 1)
        window.move_to(screen.get_center())

        not_window = Difference(screen, window, color = BLACK, fill_opacity = 0.5)
        not_window.set_stroke(color = WHITE, width = 1)
        self.play(FadeIn(window), FadeIn(not_window))
        self.wait()
