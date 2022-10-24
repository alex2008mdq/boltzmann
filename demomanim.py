from manim import *


class PrimerScript(Scene):

    def construct(self):
        cuadrado = Square()
        circuloazul = Circle(color=BLUE).shift(LEFT*2)
        self.add(cuadrado)
        self.play(Create(circuloazul))
        self.wait()
        self.play(circuloazul.animate.set_color(GREEN), Rotate(cuadrado))
        self.play(FadeOut(circuloazul))
        self.play(ReplacementTransform(cuadrado, Triangle()))
        self.wait(2)
