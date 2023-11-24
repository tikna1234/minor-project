#import pickle
#from joblib import load
from model import Printpred
eng = 57
math = 60
sci = 59
sst = 57
logical = 60
cmp = 62

diploma = {
	"Computer Science and Information Technology":

	["Diploma in Computer Science",
	"Diploma in Digital Marketing",
	"Diploma in Mobile App Development",
	"Diploma in Cybersecurity",
	"Diploma in Web Development"
	],

	"Mechanical and Electrical":

	["Diploma in Mechanical Engineering",
	"Diploma in Electrical Engineering",
	"Diploma in Automobile Engineering",
	"Diploma in Chemical Engineering",
	"Diploma in Mechatronics"
	],

	"Electronics and Communication":

	["Diploma in Electronics and Communication Engineering"
	],

	"Construction and Design":

	[
	"Diploma in Architecture",
	"Diploma in Civil Engineering",
	"Diploma in Interior Design"
	],

	"Hospitality and Event Management":

	[
	"Diploma in Hotel Management",
	"Diploma in Event Management",
	"Diploma in Aviation and Hospitality Management"
	],

	"Life Sciences and Environment":
	[
	"Diploma in Biotechnology",
	"Diploma in Environmental Science",
	"Diploma in Veterinary Science"
	],
	
	"Arts and Media":
	[
	"Diploma in Animation and Multimedia",
	"Diploma in Film Making and Direction",
	"Diploma in Photography"
	],

	"Physical Education and Wellness":
	[
	"Diploma in Early Childhood Education",
	"Diploma in Yoga and Wellness"
	],

	"Finance, Business and Marketing":
	[
	"Diploma in Financial Accounting"
	]

	}



iti = {
	"Computer Science and Information Technology ":

	[
	"ITI in Computer Hardware and Networking",
	"ITI in Information Technology",
	"ITI in Mobile Repair and Maintenance"
	],

	"Mechanical and Electrical":
	[
	 "ITI in Mechanical",
	"ITI in Automotive Technology",
	"ITI in Welding and Fabrication",
	" ITI in Fitter and Turner",
	"ITI in Machinist",
	"ITI in Foundry and Pattern Making",
	"ITI in CNC Operator"
	],

	"Electronics and Communication":
	[
	"ITI in Electronics and Communication",
	"ITI in Instrumentation and Control",
	],

	"Construction and Design":
	[
	"ITI in Plumbing and Pipefitting",
	"ITI in Carpentry and Woodworking"
	],
	
	"Physical Education and Wellness":
	[
	"ITI in Beauty and Wellness"
	]

	}
	


vocational = {"Computer Science and Information Technology ":

	[
	"Vocational Training in Data Entry and Office Automation",
	"Vocational Training in Computer Programming",
	"Vocational Training in Mobile App Development",
	"Vocational Training in Web Development",
	"Vocational Training in Computer Hardware and Networking",
	"Vocational Training in Mobile Phone Repair Technician"
	],

	"Mechanical and Electrical":
	[
	"Vocational Training in Welding Technician",
	"Vocational Training in Automotive Technician",
	"Vocational Training in Electrician",
	"Vocational Training in AutoCAD and Drafting Certification",
	"Vocational Training in Robotics and Automation Workshop",
	"Vocational Training in Machinist and CNC Operator",
	" Vocational Training in HVAC Technician"
	],
	
	"Construction and Design":
	[
	"Vocational Training in Welding Technician",
	"Vocational Training in Plumbing and Pipefitting",
	"Vocational Training in Carpentry and Woodworking"
	],

	"Hospitality and Event Management":
	[
	"Vocational Training in Hospitality and Customer Service",
	"Vocational Training in Healthcare Assistant Training",
	"Vocational Training in Basic First Aid and Safety Training",
	"Vocational Training in Retail Sales and Customer Service"
	],

	"Arts and Media":
	[
	"Vocational Training in Graphic design Essentials",
	"Vocational Training in Digital Marketing Certification",
	"Vocational Training in Photography and Videography Course",
	"Vocational Training in Fashion Design and Tailoring",
	"Vocational Training in Language Proficiency Course"
	],
	
	"Physical Education and Wellness":
	[
	"Vocational Training in Beauty and Makeup Artistry"
	],

	"Finance, Business and Marketing":
	[
	"Vocational Training in Digital Marketing Certification",
	"Vocational Training in Entrepreneurship and Business Skills"
	],

	"Culinary Studies and Cooking":
	[
	"Vocational Training in Culinary arts and Cooking",
	"Vocational Training in Baking and Pastry Arts",
	"Vocational Training in Food Safety and Hygiene Certification"
	]
             }
# Choosing branch (diploma = 0 , iti = 1, vocational = 2) according to average

avg = (eng+math+sci+sst+logical+cmp)/6*100
if avg>=75:
    branch = 0
elif avg>=55:
    branch = 1
else:
    branch = 2


#model = load(r'C:\Users\HP\Documents\GitHub\minor-project\jupyter files\model_filename.joblib')    
recommend = Printpred(eng, math, sci, sst, logical, cmp, branch)

print(recommend)

if branch == 0:
    if recommend == "Computer Science and Information Technology":
        for i in diploma['Computer Science and Information Technology']:
            print(i)
    elif recommend == "Mechanical and Electrical":
        for i in diploma['Mechanical and Electrical']:
            print(i)
    elif recommend == "Electronics and Communication":
        for i in diploma['Electronics and Communication']:
            print(i)
    elif recommend == "Construction and Design":
        for i in diploma['Construction and Design']:
            print(i)
    elif recommend == "Hospitality and Event Management":
        for i in diploma['Hospitality and Event Management']:
            print(i)
    elif recommend == "Life Sciences and Environment":
        for i in diploma['Life Sciences and Environment']:
            print(i)
    elif recommend == "Arts and Media":
        for i in diploma['Arts and Media']:
            print(i)
    elif recommend == "Physical Education and Wellness":
        for i in diploma['Physical Education and Wellness']:
            print(i)
    elif recommend == "Finance, Business and Marketing":
        for i in diploma['Finance, Business and Marketing']:
            print(i)

elif branch == 1:
    if recommend == "Computer Science and Information Technology":
        for i in diploma['Computer Science and Information Technology']:
            print(i)
    elif recommend == "Mechanical and Electrical":
        for i in diploma['Mechanical and Electrical']:
            print(i)
    elif recommend == "Electronics and Communication":
        for i in diploma['Electronics and Communication']:
            print(i)
    elif recommend == "Construction and Design":
        for i in diploma['Construction and Design']:
            print(i)
    elif recommend == "Physical Education and Wellness":
        for i in diploma['Physical Education and Wellness']:
            print(i)

else:
    if recommend == "Computer Science and Information Technology":
        for i in diploma['Computer Science and Information Technology']:
            print(i)
    elif recommend == "Mechanical and Electrical":
        for i in diploma['Mechanical and Electrical']:
            print(i)
    elif recommend == "Construction and Design":
        for i in diploma['Construction and Design']:
            print(i)
    elif recommend == "Hospitality and Event Management":
        for i in diploma['Hospitality and Event Management']:
            print(i)
    elif recommend == "Arts and Media":
        for i in diploma['Arts and Media']:
            print(i)
    elif recommend == "Physical Education and Wellness":
        for i in diploma['Physical Education and Wellness']:
            print(i)
    elif recommend == "Finance, Business and Marketing":
        for i in diploma['Finance, Business and Marketing']:
            print(i)
    elif recommend == "Culinary Studies and Cooking":
        for i in diploma['Culinary Studies and Cooking']:
            print(i)
           


