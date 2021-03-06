from coldtype import *
from coldtype.time.nle.ascii import AsciiTimeline

at = AsciiTimeline(4, """
                                        <
[1   ]    [1       ]
            [0          ]
                [2         ]
                    [wght     ]   [wght]
                        [slnt      ]
                            [tu      ]
""")

@animation((1080, 540), timeline=at)
def ascii(f):
    return (Glyphwise("OHNO", lambda g:
        Style("ObviouslyV", 250
            , wdth=at.ki(g.i).io(8)
            , wght=at.ki("wght").io(10)
            , slnt=at.ki("slnt").io(10)
            , tu=at.ki("tu").io(10, ["eeo", "eeo"], r=(0, 500))))
        .align(f.a.r, tv=1)
        .f(0)) 
