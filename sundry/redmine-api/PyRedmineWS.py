# Import the Redmine class
from redminelib import Redmine
from dateutil.relativedelta import relativedelta

# API 1129f2a77b13868fc9398a8d4e1c84eedbf1070b

server = Redmine('http://10.50.23.144/redmine/projects/jam_managemeoj', username='wiv1253', password='psmaker3')

project = server.projects['parrot']

# Find Eric in the user data
for u in server.users:
    if u.firstname == 'Eric' and u.lastname == 'Idle':
        user = u
        break
else:
    raise Exception("Didn't find Eric Idle in the user dateabase")

# Extend issues in project assigned to user by two weeks
for issue in project.issues(assigned_to_id=user.id):
    if issue.due_date is not None:
        issue.due_date += relativedelta(weeks=+2)
        issue.save('Giving Eric more time to complete - he was out ill')
