from pyactiveresource.activeresource import ActiveResource


class Issue(ActiveResource):
    _site = 'http://10.50.23.144/redmine'
    _user = 'wiv1253'
    _password = 'psmaker3'


# Get issues
issues = Issue.find()

# Get a specific issue, from its id
issue = Issue.find(3746)

print(issue.attributes.get('subject'))
