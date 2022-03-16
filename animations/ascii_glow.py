from coldtype import *
from coldtype.time.nle.ascii import AsciiTimeline
from coldtype.fx.skia import phototype

at = AsciiTimeline(4, """
                                        <
[1   ]    [1       ]
            [0          ]
                [2         ]
                    [wght     ]   [wght]
                        [slnt      ]
                            [tu      ]
""")

@animation((1080, 540), timeline=at, bg=0, render_bg=1)
def ascii(f):
    return (Glyphwise("OHNO", lambda g:
        Style("ObviouslyV", 250
            , wdth=at.ki(g.i).io(8)
            , wght=at.ki("wght").io(10)
            , slnt=at.ki("slnt").io(10)
            , tu=at.ki("tu").io(10, ["eeo", "eeo"], r=(0, 500))))
        .align(f.a.r, tv=1)
        .f(1)
        .layer(
            lambda p: p.ch(phototype(f.a.r, blur=5, cut=50, cutw=50, fill=hsl(0.9, 1))),
            lambda p: p.ch(phototype(f.a.r, blur=3, cut=240, cutw=10, fill=1))))