from jira.client import JIRA
import argparse

def agr_parse():
	parser = argparse.ArgumentParser()
	parser.add_argument('-s','--site', help = 'Enter jira site name',
		type = str, default = 'https://jira.rocket-internet.de')
	parser.add_argument('-u','--username', help = 'Enter your jira username',
		type = str, default = 'anshul.sharma')
	parser.add_argument('-p','--password', help = 'Enter your password', type = str,
		required = True)
	args = parser.parse_args()
	return args.site, args.username, args.password

if __name__ == '__main__':
	server, username, password = agr_parse()
	options = { 'server' : server }
	auth_tuple = (username, password)
	jira = JIRA(options = options, basic_auth = auth_tuple)

	my_issues = jira.search_issues('assignee in (currentUser())')

	for issue in my_issues:
		print issue, issue.fields.summary, issue.fields.reporter
