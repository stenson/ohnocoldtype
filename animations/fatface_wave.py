from coldtype import *

@animation((1080, 1080/2), timeline=50)
def fatface_wave(f):
    return (Glyphwise("WAVEFORM", lambda g:
        (Style("OhnoFatfaceVariable"
            , fontSize=f.adj(g.i*4).e("seio", 1, r=(100, 250))
            , wdth=f.adj(g.i*4).e("seio", 1)
            , opsz=f.adj(g.i*4).e("seio", 1)
            , rotate=f.adj(g.i*4).e("seio", 1, r=(-20, 20)))))
        .align(f.a.r, h=200)
        .f(0))