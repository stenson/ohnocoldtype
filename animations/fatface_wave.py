from coldtype import *

@animation((1080, 1080/2), timeline=50)
def fatface_wave(f):
    return (Glyphwise("WAVEFORM", lambda g:
        (Style("OhnoFatfaceVariable",
            100+(fa:=f.adj(g.i*4)).e(ease:="seio", 1)*150,
            wdth=fa.e(ease, 1),
            opsz=fa.e(ease, 1),
            rotate=-15+30*fa.e(ease, 1))))
        .align(f.a.r, h=200)
        .f(0))