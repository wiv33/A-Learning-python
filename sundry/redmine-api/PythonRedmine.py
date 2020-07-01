from redminelib import Redmine

redmine = Redmine('http://10.50.23.144/redmine/', username='wiv1253', password='psmaker3')
project = redmine.project

print(project.id)
