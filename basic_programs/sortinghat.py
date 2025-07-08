#the sorting hat asks you a couple of questions and determines the house you most belong to
grf=0
sly=0
rav=0
huf=0
#question1
ans1=int(input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\nanwer: "))

if ans1==1:
  grf+=1
  rav+=1
elif ans1==2:
  huf+=1
  sly+=1
else:
  print("wrong output")
#question2
ans2=int(input("Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\nanswer: "))

if ans2==1:
  huf+=2
elif ans2==2:
  sly+=2
elif ans2==3:
  rav+=2
elif ans2==4:
  grf+=2
else:
  print("wrong input")
#question3
ans3= int(input("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\nanswer: "))

if ans3==2:
  huf+=4
elif ans3==1:
  sly+=4
elif ans3==3:
  rav+=4
elif ans3==4:
  grf+=4
else:
  print("wrong input")
#printing result
print("")
print("Final score: ")
print(f" huffulpuff={huf}")
print(f" gryfindor={grf}")
print(f" slytherin={sly}")
print(f" ravenclaw={rav}")
