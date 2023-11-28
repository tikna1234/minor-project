eng = , maths = , sci = , sst = , log = , comp =
weak[]
if branch == 0:
    min_marks = 80
elif branch ==1:
    min_marks = 60
else:
    min_marks = 45
if interest == "Computer Science and Information Technology (IT)":
    if(comp>=min_marks and log >=min_marks and maths >=min_marks):
        print("No weakness")
    else:
        if(comp<min_marks):
            weak.append(comp)
        elif(log<min_marks):
            weak.append(log)
        elif(maths<min_marks):
            weak.append(maths)
        print("weak subjects : ")
        for i in weak:
            print(i)
            
if interest == "Mechanical and Electrical":
    if(sci >= min_marks and maths >=min_marks and comp >=min_marks):
        print("No weakness")
    else:
        if(sci<min_marks):
            weak.append(sci)
        elif(maths<min_marks):
            weak.append(maths)
        elif(comp<(min_marks - 5)):
            weak.append(comp)
        print("weak subjects : ")
        for i in weak:
            print(i)

if interest == "Electronics and Communication":
    if(sci >= min_marks and maths >=(min_marks - 5) and comp >=min_marks):
        print("No weakness")
    else:
        if(sci<min_marks):
            weak.append(sci)
        elif(comp<min_marks):
            weak.append(comp)
        elif(maths<(min_marks - 5)):
            weak.append(maths)
        print("weak subjects : ")
        for i in weak:
            print(i)

if interest == "Construction and Design":
    if(sci >= min_marks and maths >=min_marks and comp >=(min_marks - 5) and log >= (min_marks - 5)):
        print("No weakness")
    else:
        if(sci<min_marks):
            weak.append(sci)
        elif(comp<(min_marks - 5)):
            weak.append(comp)
        elif(maths<min_marks):
            weak.append(maths)
        elif(log<(min_marks - 5)):
            weak.append(log)
        print("weak subjects : ")
        for i in weak:
            print(i)


if interest == "Hospitality and Event Management":
    if(eng >= min_marks and sst >=(min_marks - 5)):
        print("No weakness")
    else:
        if(eng<min_marks):
            weak.append(eng)
        elif(sst<(min_marks - 5)):
            weak.append(sst)
        print("weak subjects : ")
        for i in weak:
            print(i)


if interest == "Life Sciences and Environment":
    if(sci >= min_marks and maths >=(min_marks - 5) and eng >=min_marks):
        print("No weakness")
    else:
        if(sci<min_marks):
            weak.append(sci)
        elif(eng<min_marks):
            weak.append(eng)
        elif(maths<(min_marks - 5)):
            weak.append(maths)
        print("weak subjects : ")
        for i in weak:
            print(i)


if interest == "Physical Education and Wellness":
    if(sci >= min_marks and  sst>=(min_marks - 5) and eng >=(min_marks - 5)):
        print("No weakness")
    else:
        if(sci<min_marks):
            weak.append(sci)
        elif(sst<(min_marks - 5)):
            weak.append(sst)
        elif(eng<(min_marks - 5)):
            weak.append(eng)
        print("weak subjects : ")
        for i in weak:
            print(i)



if interest == "Finance, Business and Marketing":
    if(sst >= min_marks and  maths>=(min_marks - 5) and eng >=(min_marks - 5)):
        print("No weakness")
    else:
        if(sst<min_marks):
            weak.append(sst)
        elif(maths<(min_marks - 5)):
            weak.append(maths)
        elif(eng<(min_marks - 5)):
            weak.append(eng)
        print("weak subjects : ")
        for i in weak:
            print(i)


if interest == "Arts and Media":
    if(comp >= min_marks and  maths>=(min_marks - 5) and eng >=(min_marks - 5)):
        print("No weakness")
    else:
        if(comp<min_marks):
            weak.append(comp)
        elif(maths<(min_marks - 5)):
            weak.append(maths)
        elif(eng<(min_marks - 5)):
            weak.append(eng)
        print("weak subjects : ")
        for i in weak:
            print(i)

