import os

import github3
import requests
from bs4 import BeautifulSoup

if os.path.exists('/Users/thinkingserious/Workspace/sendgrid-open-source-library-external-data/.env'):
    for line in open('/Users/thinkingserious/Workspace/sendgrid-open-source-library-external-data/.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

if (os.environ.get('ENV') != 'prod'):
    github_token = os.environ.get('GITHUB_TOKEN')
else:
    github_token = os.environ['GITHUB_TOKEN']

github = github3.login(token=github_token)

sendgrid_python = github.repository("sendgrid", "sendgrid-python")

num_pull_requests = sum(1 for i in sendgrid_python.iter_pulls())
num_issues = sum(1 for i in sendgrid_python.iter_issues())
num_commits = sum(1 for i in sendgrid_python.iter_commits())
num_branches = sum(1 for i in sendgrid_python.iter_branches())
num_releases = sum(1 for i in sendgrid_python.iter_releases())
num_contributors = sum(1 for i in sendgrid_python.iter_contributors())
num_watchers = sendgrid_python.watchers
num_stargazers = sendgrid_python.stargazers
num_forks = sendgrid_python.forks_count

url = "https://www.nuget.org/packages/SendGrid"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
mydivs = soup.findAll("p", { "class" : "stat-number" })
nodes = []
for node in mydivs:
   nodes.append(''.join(node.findAll(text=True)))
num_total_csharp_downloads = nodes[0]
num_total_csharp_v_downloads = nodes[1]

mydivs = soup.findAll("p", { "class" : "stat-label" })
nodes = []
for node in mydivs:
   nodes.append(''.join(node.findAll(text=True)))
num_v_downloads_label = nodes[1]

print "Pull Requests, " + \
      "Open Issues, " + \
      "Number of Commits, " + \
      "Number of Branches, " + \
      "Number of Releases, " + \
      "Number of Contributors, " + \
      "Number of Watchers, " + \
      "Number of Stargazers, " + \
      "Number of Forks, " + \
      "Total C# Downloads - Nuget, " + \
      num_v_downloads_label[13:] + " Downloads - Nuget"
print      str(num_pull_requests) + \
    ", " + str(num_issues) + \
    ", " + str(num_commits) + \
    ", " + str(num_branches) + \
    ", " + str(num_releases) + \
    ", " + str(num_contributors) + \
    ", " + str(num_watchers) + \
    ", " + str(num_stargazers) + \
    ", " + str(num_forks) + \
    ", " + str(num_total_csharp_downloads) + \
    ", " + str(num_total_csharp_v_downloads)