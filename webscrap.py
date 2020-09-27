#Using Python Crash Course
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(r.status_code)
#convert to python dictionary and store in variable
response_dict = r.json()

#process results
print(response_dict.keys())

print("Total Repositories:", response_dict["total_count"])

#Explore the information about the repositories
repo_dicts = response_dict["items"]
print(len(repo_dicts))

## Run a loop to run through all each of the repository
for repo_dict in repo_dicts:
    print('\nName:', repo_dict["name"])
    print('Owner:', repo_dict["owner"]["login"])
    print('Star:', repo_dict["stargazers_count"])
    print('Repository:', repo_dict["html_url"])
    print('Description:', repo_dict["description"])
# #first item that was pulled from key value - 'items'
# repo_dict = repo_dicts[0]
# print(repo_dict)

# print("\nKeys: ",len(repo_dict))

# for key in sorted(repo_dict.keys()):
#     print(key)

# ## examples of printing each items out
# print('Stars:', repo_dict['stargazers_count'])
# print('repository:', repo_dict['html_url'])

##Start to Visualize Repository
#For Loop to pull name and stargazers into a list
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict["name"])
#     stars.append(repo_dict["stargazers_count"])

# answer to solve the null value in description
#https://stackoverflow.com/questions/44004609/attributeerror-nonetype-object-has-no-attribute-decode
names, stars_labels = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    if repo_dict['description']:
        stars_labels.append({'value': repo_dict['stargazers_count'],
                             'label': repo_dict['description'],
                             'xlink': repo_dict['html_url']})
    else:
        stars_labels.append({'value': repo_dict['stargazers_count'],
                             'label': 'asdf',
                             'xlink': repo_dict['html_url']})

my_style = LS('#333366', base_style=LCS)
###Making Customizations to the bar
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)

# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title  = 'Most Starred Python projects on Github'
chart.x_labels = names

chart.add('', stars_labels)
chart.render_to_file('python3.svg')
