# hello
import turtle as trtl

t = trtl.Turtle()
t.color("yellow")
#t.shape("hallow.gif")
t.forward(50)
t.stamp()
t.right(90)
t.forward(50)


wn = trtl.Screen()
wn.addshape("hallow.gif")
t.shape("hallow.gif")
#wn.bgpic("hallow.gif")
wn.mainloop()