from coldtype import *

r = Rect(1080, 1080)
ri = r.inset(100)

txt = (StSt("DEMOS", "Beastly-60Point.otf", 500)
    .scaleToRect(ri, True)
    .align(ri, y="S"))

@animation(r, timeline=Timeline(60, 30), bg=0, render_bg=1)
def demos(f):
    return P(
        P().enumerate(range(1, 20), lambda x:
            txt.copy()
                .fssw(-1, 1, f.adj(x.el*5)
                    .e("qeio", 0, r=(0.5, 4)))
                .t(0, 0+f.adj(x.el*5)
                    .e("qeio", 0, r=(0, 1000)))),
        txt.copy().f(1))