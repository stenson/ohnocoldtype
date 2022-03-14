from coldtype import *

@animation((1080, 1080/2), timeline=60, bg=1, render_bg=1)
def cilati_wave(f:Frame):
    return (Glyphwise("Cilati", lambda g:
        Style("SwearCilatiVariable", 340
            , opsz=f.adj(g.i*-15).e("seio", 1)
            , wght=f.adj(g.i*-15).e("seio", 1)))
        .f(0)
        .align(f.a.r, th=0))

@animation((1080, 1080/2), timeline=60, bg=1, render_bg=1)
def roman_wave(f:Frame):
    return (Glyphwise("Roman", lambda g:
        Style("SwearRomanVariable", 300
            , opsz=f.adj(g.i*15).e("seio", 1)
            , wght=f.adj(g.i*15).e("seio", 1)))
        .f(0)
        .align(f.a.r, th=0))