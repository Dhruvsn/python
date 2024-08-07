# import numpy as np
# import pandas as pd

# #series - Data 1D Array
# #Data frame - 2D Array

# dic = {
#     "name": ['Ram','Shyam','Sameer','Kajal','Irfan','Rohit'],
#     "Roll no": [1,2,3,4,5,6],
#     "Grades": ['A','B','C','C','B','A'],
#     "Email": ['abc@xyz.com','def@xyz.com','ghi@ers.com','dfd@gix.com','tyu@opk.com','ops@cvb.com']
# }

# df = pd.DataFrame(dic)
# # print(df)
# # df.head(2) 
# # df.tail(2)
# # df.describe()
# cus = pd.read_csv('customer.csv')
# cus
#--------------------------------------------------------------------------------------

# import numpy as np
# import pandas as pd
# cus = pd.read_csv('customer.csv')
# # cus.loc[(48,78),('Company Name','Costumer Name')]
# # cus.loc[np.arange(48,78),:]
# data = cus.loc[:,'Company Name']
# company_data = np.array(data)
# cd = pd.Dataframe(company_data)
# cd

#-----------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd


employees = {
    1: {"company": "Tech Innovators", "employee": "Alice Johnson", "position": "Software Engineer"},
    2: {"company": "Tech Innovators", "employee": "Bob Smith", "position": "Project Manager"},
    3: {"company": "Creative Solutions", "employee": "Cathy Brown", "position": "Designer"},
    4: {"company": "Creative Solutions", "employee": "David Wilson", "position": "UX Researcher"},
    5: {"company": "Health First", "employee": "Eva Davis", "position": "Data Analyst"},
    6: {"company": "Health First", "employee": "Frank Clark", "position": "Healthcare Consultant"},
    7: {"company": "Eco World", "employee": "Grace Lewis", "position": "Environmental Scientist"},
    8: {"company": "Eco World", "employee": "Hank Miller", "position": "Ecologist"},
    9: {"company": "Finance Corp", "employee": "Ivy Martinez", "position": "Accountant"},
    10: {"company": "Finance Corp", "employee": "Jack Anderson", "position": "Financial Analyst"},
    11: {"company": "Market Masters", "employee": "Karen Lee", "position": "Marketing Specialist"},
    12: {"company": "Market Masters", "employee": "Leo Harris", "position": "Content Creator"},
    13: {"company": "Tech Innovators", "employee": "Mia Clark", "position": "DevOps Engineer"},
    14: {"company": "Tech Innovators", "employee": "Nathan Scott", "position": "QA Engineer"},
    15: {"company": "Creative Solutions", "employee": "Olivia Green", "position": "Graphic Designer"},
    16: {"company": "Creative Solutions", "employee": "Peter Adams", "position": "Product Manager"},
    17: {"company": "Health First", "employee": "Quinn Parker", "position": "Nurse"},
    18: {"company": "Health First", "employee": "Rachel Baker", "position": "Doctor"},
    19: {"company": "Eco World", "employee": "Sam Edwards", "position": "Wildlife Biologist"},
    20: {"company": "Eco World", "employee": "Tina Martinez", "position": "Conservationist"},
    21: {"company": "Finance Corp", "employee": "Uma Brooks", "position": "Auditor"},
    22: {"company": "Finance Corp", "employee": "Victor Rivera", "position": "Investment Banker"},
    23: {"company": "Market Masters", "employee": "Wendy Foster", "position": "SEO Specialist"},
    24: {"company": "Market Masters", "employee": "Xander Hughes", "position": "Social Media Manager"},
    25: {"company": "Tech Innovators", "employee": "Yvonne Carter", "position": "Data Scientist"},
    26: {"company": "Tech Innovators", "employee": "Zack Taylor", "position": "Network Engineer"},
    27: {"company": "Creative Solutions", "employee": "Amy Hall", "position": "Animator"},
    28: {"company": "Creative Solutions", "employee": "Brian Young", "position": "Video Editor"},
    29: {"company": "Health First", "employee": "Cindy King", "position": "Physical Therapist"},
    30: {"company": "Health First", "employee": "Derek Turner", "position": "Pharmacist"},
    31: {"company": "Eco World", "employee": "Elena Scott", "position": "Marine Biologist"},
    32: {"company": "Eco World", "employee": "Fred Harris", "position": "Botanist"},
    33: {"company": "Finance Corp", "employee": "Gina White", "position": "Credit Analyst"},
    34: {"company": "Finance Corp", "employee": "Henry Perez", "position": "Loan Officer"},
    35: {"company": "Market Masters", "employee": "Irene Morris", "position": "Brand Strategist"},
    36: {"company": "Market Masters", "employee": "John Ross", "position": "Market Research Analyst"},
    37: {"company": "Tech Innovators", "employee": "Kelly Evans", "position": "System Administrator"},
    38: {"company": "Tech Innovators", "employee": "Liam Collins", "position": "Product Designer"},
    39: {"company": "Creative Solutions", "employee": "Megan Kelly", "position": "Copywriter"},
    40: {"company": "Creative Solutions", "employee": "Nick Ward", "position": "Art Director"},
    41: {"company": "Health First", "employee": "Olga Reed", "position": "Radiologist"},
    42: {"company": "Health First", "employee": "Pauline Scott", "position": "Surgeon"},
    43: {"company": "Eco World", "employee": "Quincy Green", "position": "Geologist"},
    44: {"company": "Eco World", "employee": "Rita Campbell", "position": "Meteorologist"},
    45: {"company": "Finance Corp", "employee": "Steve Adams", "position": "Risk Manager"},
    46: {"company": "Finance Corp", "employee": "Tara Brown", "position": "Financial Planner"},
    47: {"company": "Market Masters", "employee": "Ulysses Davis", "position": "PR Specialist"},
    48: {"company": "Market Masters", "employee": "Vicky Johnson", "position": "Event Coordinator"},
    49: {"company": "Tech Innovators", "employee": "Will Graham", "position": "Mobile Developer"},
    50: {"company": "Tech Innovators", "employee": "Xena Holmes", "position": "Tech Support Specialist"}
}

cd = pd.DataFrame(employees)

# cd.drop_duplicates(subset='company',keep=False)
#---------------------------------------------------------------------------------------




# cd = pd.DataFrame(employees)
# cd=cd.T
# cd.drop_duplicates(subset='company',keep='last')
# cd.to_csv('company_data.csv',index=False)
# # xlrd and openpyxl 
# com_data = pd.read_csv('company_data.csv')
# com_data.drop((i for i in [42,23,3]),axis=0,inplace=True)
# com_data.reset_index(drop=True,inplace=True) # to reset the index
# com_data.to_csv('company_data.csv')
# com_data.to_excel('company_data.xlsx',index=False)
# com_data