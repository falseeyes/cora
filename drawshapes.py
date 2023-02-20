import turtle as t

t.color('brown', 'yellow')
t.begin_fill()
t.forward (0)
for x in range(360):
    t.forward(1)
    t.left(1)

t.end_fill()
t.done()