from jinja2 import Environment, FileSystemLoader
import json


with open('data.json') as f:
    data = json.load(f)


env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')


output = template.render(data)


with open('output.html', 'w') as f:
    f.write(output)

print("HTML file generated: output.html")
