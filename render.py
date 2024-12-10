from jinja2 import Environment, FileSystemLoader
import json

# Load JSON data
with open('data.json') as f:
    data = json.load(f)

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render template with JSON data
output = template.render(data)

# Write output to HTML file
with open('output.html', 'w') as f:
    f.write(output)

print("HTML file generated: output.html")
