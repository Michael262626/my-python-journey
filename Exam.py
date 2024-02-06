total_pass = 0
total_fail= 0
count = 0
fail = 0
pass_score = 0
score = int(input("Enter your score or -1to end: "))
while(score != -1):
 score = int(input("Enter your score or -1 to end: "))
 if(score < 45):
   fail+=1
 if(score>=45):
   pass_score+=1

print("total fail is:", fail)
print("total pass is:", pass_score)

