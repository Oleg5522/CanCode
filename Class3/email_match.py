import pandas as pd

...
#Task : Locate employees who have not replied to survey
...

#Read in global
gl_email_df = pd.read_csv("nyspi_global.csv") # Read in
email_global_list = gl_email_df["UserPrincipalName"].tolist() # convert to list
email_global_list = [e.lower() for e in email_global_list] # convert emails to lowerca

# global email list info
print(type(email_global_list)) # confirm it is a list
print(len(email_global_list)) # confirm length matches csv 
print(email_global_list) # spot check list

# Read in respondents 
respondents_email = pd.read_csv("respondents.csv") # Read-in
respondents_list = respondents_email["nyspi_email"].tolist( ) # convert to list
respondents_list = [e.lower() for e in respondents_list] # convert emails to lowercase

# respondents list info
print(type(respondents_list))
print(len(respondents_list))
print(respondents_list)

# Check with intersection, 0 output
matches = list(set(respondents_list).intersection(non_matches))
print(matches)

#Generate output
non_respondents_df = pd.DataFrame(non_matches)
non_respondents_df.to_csv("output.csv", index = False)