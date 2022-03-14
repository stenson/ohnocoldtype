from coldtype import *

@animation((1080, 540), tl=50, bg=0, render_bg=1)
def wdth(f):
    return (Glyphwise("WHOA", lambda g:
        Style("ObviouslyV", 160
            , wght=f.adj(-g.i*5).e("ceio", r=(1, 0))
            , wdth=f.adj(-g.i*5).e("seio")))
        .align(f.a.r)
        .f(1))
