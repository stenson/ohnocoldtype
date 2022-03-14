from coldtype import *

at = AsciiTimeline(6, 30, """
                                              <
[0   ][1   ][2     ][3  ][4         ]
  [0w                                  ]
        [1w                            ]
               [2w                     ]
                      [3w              ]
                              [4w      ]
                                      [z    ]
                                      [o   ]
""")

@animation((1080, 1080), timeline=at, bg=1, render_bg=1)
def casual1(f):
    letter = at.ki(list("012345"))
    li, lidx = letter.e(find=1)
    
    z = at.ki("z")
    o = at.ki("o")

    return (Glyphwise("Swear", lambda g:
        Style("SwearCilatiV", 100
            , opsz=o.e("eeo", 1)
                if o.on()
                    else at.ki(g.i).e("eeio", 1)
            , wght=z.e("eeo", 0, r=(1, 0))
                if z.on()
                    else at.ki(f"{g.i}w").io([8, 8], "eeo")))
        .align(f.a.r)
        .centerPoint(f.a.r, (lidx, "thtvC"), i=li)
        .cond(True,
            lambda p: p
                .scale(letter.io([15, 5], r=(1, 12)), pt=(lidx, "tvC"))
                .scale(z.io([10, 15], ["eeo", "ceio"], r=(1, 4))),
            lambda p: p
                .scale(letter.e(r=(1,12)), pt=(lidx, "tvC"))
                .scale(z.e("eeio", r=(1, 3))))
        .f(0))

release = casual1.export("h264", loops=3)