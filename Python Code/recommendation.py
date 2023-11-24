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

ITI = {
    'ITI in Computer Hardware and Networking': [
        'Computer Hardware Technician',
        'Network Technician',
        'IT Support Technician',
        'Field Service Technician',
        'System Administrator'
    ],
    'ITI in Information Technology': [
        'IT Support Specialist',
        'Computer Operator',
        'Data Entry Operator',
        'IT Assistant',
        'Desktop Support Technician'
    ],
    'ITI in Mobile Repair and Maintenance': [
        'Mobile Phone Technician',
        'Cellphone Repair Technician',
        'Mobile Service Technician',
        'Mobile Hardware Specialist',
        'Cellphone Diagnostic Technician'
    ],
    'ITI in Mechanical': [
        'Mechanical Technician',
        'Machinist',
        'Maintenance Technician',
        'Production Assistant',
        'Quality Control Technician'
    ],
    'ITI in Automotive Technology': [
        'Automotive Technician',
        'Automotive Mechanic',
        'Auto Repair Technician',
        'Automobile Service Technician',
        'Automotive Electrician'
    ],
    'ITI in Welding and Fabrication': [
        'Welder',
        'Fabricator',
        'Welding Technician',
        'Structural Welder',
        'Metal Worker'
    ],
    'ITI in Fitter and Turner': [
        'Fitter',
        'Turner',
        'Assembly Technician',
        'Machinist',
        'Machine Operator'
    ],
    'ITI in Machinist': [
        'Machinist',
        'CNC Machinist',
        'Tool and Die Maker',
        'Machining Technician',
        'Lathe Operator'
    ],
    'ITI in Foundry and Pattern Making': [
        'Foundry Technician',
        'Pattern Maker',
        'Metal Casting Technician',
        'Foundry Worker',
        'Molder'
    ],
    'ITI in CNC Operator': [
        'CNC Machine Operator',
        'CNC Programmer',
        'Machine Shop Operator',
        'CNC Technician',
        'CNC Machinist'
    ],
    'ITI in Electronics and Communication': [
        'Electronics Technician',
        'Communication Technician',
        'Electronics Assembler',
        'PCB Designer',
        'Electronics Repair Technician'
    ],
    'ITI in Instrumentation and Control': [
        'Instrumentation Technician',
        'Control Systems Technician',
        'Instrumentation and Control Engineer',
        'Calibration Technician',
        'Process Control Technician'
    ],
    'ITI in Plumbing and Pipefitting': [
        'Plumber',
        'Pipefitter',
        'Plumbing Technician',
        'Pipe Welder',
        'Gas Fitter'
    ],
    'ITI in Carpentry and Woodworking': [
        'Carpenter',
        'Woodworker',
        'Cabinet Maker',
        'Furniture Designer',
        'Joinery Technician'
    ],
    'ITI in Beauty and Wellness': [
        'Beautician',
        'Hair Stylist',
        'Makeup Artist',
        'Spa Therapist',
        'Skin Care Specialist'
    ]
}
Diploma = {
    'Diploma in Computer Science': [
        'Software Developer',
        'Network Administrator',
        'Database Administrator',
        'Web Developer',
        'Systems Analyst',
        'IT Support Specialist',
        'Cybersecurity Analyst'
    ],
    'Diploma in Digital Marketing': [
        'Digital Marketing Specialist',
        'Social Media Manager',
        'SEO Specialist',
        'Content Marketing Manager',
        'Email Marketing Specialist',
        'PPC Specialist'
    ],
    'Diploma in Mobile App Development': [
        'Mobile App Developer',
        'App Tester',
        'App Designer',
        'UI/UX Designer',
        'Mobile App Support Technician'
    ],
    'Diploma in Cybersecurity': [
        'Cybersecurity Analyst',
        'Security Consultant',
        'Incident Responder',
        'Security Engineer',
        'Penetration Tester'
    ],
    'Diploma in Web Development': [
        'Web Developer',
        'Front-End Developer',
        'Back-End Developer',
        'UI/UX Designer',
        'Web Content Manager'
    ],
    'Diploma in Mechanical Engineering': [
        'Mechanical Engineer',
        'Maintenance Technician',
        'CAD Technician',
        'Quality Control Technician',
        'Production Supervisor'
    ],
    'Diploma in Civil Engineering': [
        'Civil Engineer',
        'Construction Supervisor',
        'Surveyor',
        'CAD Technician',
        'Site Engineer'
    ],
    'Diploma in Electrical Engineering': [
        'Electrical Engineer',
        'Electrician',
        'Electrical Technician',
        'Control Panel Designer',
        'Power Plant Technician'
    ],
    'Diploma in Automobile Engineering': [
        'Automotive Engineer',
        'Automotive Technician',
        'Service Advisor',
        'Quality Control Engineer',
        'Automotive Designer'
    ],
    'Diploma in Chemical Engineering': [
        'Chemical Engineer',
        'Process Technician',
        'Quality Control Technician',
        'Laboratory Technician',
        'Production Supervisor'
    ],
    'Diploma in Electronics and Communication': [
        'Electronics Technician',
        'Telecommunication Technician',
        'Electronic Equipment Assembler',
        'Broadcast Technician',
        'Electronics Engineer'
    ],
    'Diploma in Architecture': [
        'Architectural Drafter',
        'Architectural Assistant',
        'Building Inspector',
        'CAD Technician',
        'Construction Supervisor'
    ],
    'Diploma in Interior Design': [
        'Interior Designer',
        'Interior Decorator',
        'Furniture Designer',
        'Retail Store Designer',
        'Set Designer'
    ],
    'Diploma in Hotel Management': [
        'Hotel Manager',
        'Front Office Executive',
        'Food and Beverage Manager',
        'Restaurant Manager',
        'Guest Relations Manager'
    ],
    'Diploma in Event Management': [
        'Event Planner',
        'Event Coordinator',
        'Wedding Planner',
        'Conference Manager',
        'Exhibition Organizer'
    ],
    'Diploma in Aviation and Hospitality Management': [
        'Airport Ground Staff',
        'Cabin Crew',
        'Airport Operations Manager',
        'Airline Customer Service Agent',
        'Hotel Front Desk Officer'
    ],
    'Diploma in Biotechnology': [
        'Laboratory Technician',
        'Biotechnician',
        'Research Assistant',
        'Quality Control Analyst',
        'Bioprocess Operator'
    ],
    'Diploma in Environmental Science': [
        'Environmental Technician',
        'Environmental Consultant',
        'Sustainability Specialist',
        'Water Quality Analyst',
        'Ecosystem Manager'
    ],
    'Diploma in Veterinary Science': [
        'Veterinary Assistant',
        'Animal Health Technician',
        'Veterinary Technician',
        'Pet Groomer',
        'Wildlife Rehabilitator'
    ],
    'Diploma in Animation and Multimedia': [
        'Animator',
        'Graphic Designer',
        'Video Editor',
        'Multimedia Artist',
        'Motion Graphics Designer'
    ],
    'Diploma in Film Making and Direction': [
        'Film Director',
        'Screenwriter',
        'Film Producer',
        'Cinematographer',
        'Film Editor'
    ],
    'Diploma in Photography': [
        'Photographer',
        'Photojournalist',
        'Photo Editor',
        'Studio Manager',
        'Photography Instructor'
    ],
    'Diploma in Early Childhood Education': [
        'Preschool Teacher',
        'Childcare Worker',
        'Early Childhood Educator',
        'Curriculum Developer',
        'Child Development Specialist'
    ],
    'Diploma in Yoga and Wellness': [
        'Yoga Instructor',
        'Wellness Coach',
        'Holistic Health Practitioner',
        'Fitness Trainer',
        'Meditation Instructor'
    ],
    'Diploma in Financial Accounting': [
        'Accounts Assistant',
        'Junior Accountant',
        'Bookkeeper',
        'Tax Assistant',
        'Audit Assistant'
    ]
}
Vocational = {
    'Vocational Training in Data Entry and Office Automation': [
        'Data Entry Operator',
        'Office Assistant',
        'Administrative Assistant'
    ],
    'Vocational Training in Computer Programming': [
        'Junior Programmer',
        'Software Developer',
        'Web Developer',
        'Application Developer'
    ],
    'Vocational Training in Mobile App Development': [
        'Mobile App Developer',
        'App Tester',
        'App Designer',
        'UI/UX Designer',
        'Mobile App Support Technician'
    ],
    'Vocational Training in Web Development': [
        'Web Developer',
        'Front-End Developer',
        'Back-End Developer',
        'UI/UX Designer',
        'Web Content Manager'
    ],
    'Vocational Training in Computer Hardware and Networking': [
        'IT Support Technician',
        'Network Technician',
        'Hardware Technician',
        'System Administrator',
        'Network Administrator'
    ],
    'Vocational Training in Mobile Phone Repair Technician': [
        'Mobile Phone Technician',
        'Cellphone Repair Technician',
        'Mobile Service Technician',
        'Mobile Hardware Specialist'
    ],
    'Vocational Training in Welding Technician': [
        'Welder',
        'Fabricator',
        'Welding Technician'
    ],
    'Vocational Training in Automotive Technician': [
        'Automotive Technician',
        'Automotive Mechanic',
        'Auto Repair Technician',
        'Automobile Service Technician',
        'Automotive Electrician'
    ],
    'Vocational Training in Electrician': [
        'Electrician',
        'Electrical Technician',
        'Control Panel Designer',
        'Power Plant Technician'
    ],
    'Vocational Training in AutoCAD and Drafting Certification': [
        'CAD Technician',
        'Draftsman',
        'Design Engineer'
    ],
    'Vocational Training in Robotics and Automation Workshop': [
        'Robotics Technician',
        'Automation Technician',
        'Robotics Programmer'
    ],
    'Vocational Training in Machinist and CNC Operator': [
        'Machinist',
        'CNC Machine Operator',
        'Machine Shop Operator'
    ],
    'Vocational Training in HVAC Technician': [
        'HVAC Technician',
        'Heating and Cooling Technician'
    ],
    'Vocational Training in Plumbing and Pipefitting': [
        'Plumber',
        'Pipefitter',
        'Pipe Welder',
        'Gas Fitter'
    ],
    'Vocational Training in Carpentry and Woodworking': [
        'Carpenter',
        'Woodworker',
        'Cabinet Maker',
        'Furniture Designer'
    ],
    'Vocational Training in Hospitality and Customer Service': [
        'Hotel Front Desk Officer',
        'Guest Service Agent',
        'Customer Service Representative'
    ],
    'Vocational Training in Healthcare Assistant Training': [
        'Healthcare Assistant',
        'Nursing Assistant'
    ],
    'Vocational Training in Basic First Aid and Safety Training': [
        'First Aid Responder',
        'Safety Officer'
    ],
    'Vocational Training in Retail Sales and Customer Service': [
        'Retail Sales Associate',
        'Customer Service Representative'
    ],
    'Vocational Training in Graphic Design Essentials': [
        'Graphic Designer',
        'Visual Designer'
    ],
    'Vocational Training in Digital Marketing Certification': [
        'Digital Marketing Specialist',
        'Social Media Manager',
        'SEO Specialist'
    ],
    'Vocational Training in Photography and Videography Course': [
        'Photographer',
        'Videographer',
        'Photo Editor'
    ],
    'Vocational Training in Fashion Design and Tailoring': [
        'Fashion Designer',
        'Tailor',
        'Clothing Designer'
    ],
    'Vocational Training in Language Proficiency Course': [
        'Translator',
        'Language Instructor'
    ],
    'Vocational Training in Beauty and Makeup Artistry': [
        'Makeup Artist',
        'Beauty Consultant'
    ],
    'Vocational Training in Entrepreneurship and Business Skills': [
        'Entrepreneur',
        'Small Business Owner',
        'Business Consultant'
    ],
    'Vocational Training in Culinary Arts and Cooking': [
        'Cook',
        'Chef',
        'Sous Chef'
    ],
    'Vocational Training in Baking and Pastry Arts': [
        'Baker',
        'Pastry Chef'
    ],
    'Vocational Training in Food Safety and Hygiene Certification': [
        'Food Safety Inspector',
        'Food Safety Coordinator'
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
        for i in Diploma['Diploma in Computer Science']:
            print(i)
    elif recommend == "Mechanical and Electrical":
        for i in diploma['Mechanical and Electrical']:
            print(i)
        for i in Diploma['Diploma in Mechanical']:
            print(i)
        for i in Diploma['Diploma in Electrical']:
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
        for i in iti['Computer Science and Information Technology']:
            print(i)
    elif recommend == "Mechanical and Electrical":
        for i in iti['Mechanical and Electrical']:
            print(i)
    elif recommend == "Electronics and Communication":
        for i in iti['Electronics and Communication']:
            print(i)
    elif recommend == "Construction and Design":
        for i in iti['Construction and Design']:
            print(i)
    elif recommend == "Physical Education and Wellness":
        for i in iti['Physical Education and Wellness']:
            print(i)

else:
    if recommend == "Computer Science and Information Technology":
        for i in vocational['Computer Science and Information Technology']:
            print(i)
    elif recommend == "Mechanical and Electrical":
        for i in vocational['Mechanical and Electrical']:
            print(i)
    elif recommend == "Construction and Design":
        for i in vocational['Construction and Design']:
            print(i)
    elif recommend == "Hospitality and Event Management":
        for i in vocational['Hospitality and Event Management']:
            print(i)
    elif recommend == "Arts and Media":
        for i in vocational['Arts and Media']:
            print(i)
    elif recommend == "Physical Education and Wellness":
        for i in vocational['Physical Education and Wellness']:
            print(i)
    elif recommend == "Finance, Business and Marketing":
        for i in vocational['Finance, Business and Marketing']:
            print(i)
    elif recommend == "Culinary Studies and Cooking":
        for i in vocational['Culinary Studies and Cooking']:
            print(i)
           


select = "Vocational Training in Plumbing and Pipefitting"

if branch == 0:
    for j in Diploma.keys():
        if j == select:
            print(Diploma[j])
elif branch == 1:
    for j in ITI.keys():
        if j == select:
            print(ITI[j])
elif branch == 2:
    for j in Vocational.keys():
        if j == select:
            print(Vocational[j])
    
