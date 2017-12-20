import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
sides = int(turtle.numinput("Les num de les side", "Choicez le num de les side dan votre spirale? ( 2- 6) ", 4, 2 ,6))
colors = ["red", "yellow", "blue", "green", "orange", "purple"]
# , "white", "gray", "pink", "brown"
family = []
name = turtle.textinput("Mon familie", "ENtrez une nom, ou simplement [ENTREZ] pour le finalement:")
while name != "":
   family.append(name)
   name = turtle.textinput("Mon familie", "ENtrez une nom, ou simplement [ENTREZ] pour le finalement:")
for x in range(100):
   t.pencolor(colors[x%len(family)])
   t.penup()
   t.forward(x*4)
   t.pendown()
   t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold"))
   t.left(360/len(family)+2)
#sides = int(turtle.numinput("Num de les sides", "Choizer dan les num 1 - 8 comme les sides ", 4, 1 ,8))
#for x in range(360):
   #t.pencolor(colors[x%sides])
   #t.forward(x*3/sides + 1)
   #t.left(360/sides + 1)
   #t.width(x*sides / 200)
#number_of_circles = int(turtle.numinput("Num de les circles", "Num de les circles dan le votre rosette"))
#for x in range(number_of_circles):
   #t.pencolor(colors[x%sides])
   #t.circle(100)
   #t.left(360/number_of_circles)


