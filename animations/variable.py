from coldtype import *

at = AsciiTimeline(4, 30, """
                                <
[w             ]
       [s           ]
                        [w  ]
            [ss01     ]
""")

txt = "VARIABLE"

@animation((1080, 540), tl=at, bg=1, render_bg=1)
def variable(f):
    return (StSt(txt, "IrregardlessV", 300
        , ss01=at.ki("ss01").on()
        , wght=at.ki("w").io(10)
        , slnt=at.ki("s").io(10))
        .align(f.a.r, th=0)
        .f(0))
