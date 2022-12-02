from jinja2 import Environment, FileSystemLoader
import json


environment = Environment(
    loader=FileSystemLoader("templates/")
)
with open("resume.json") as json_file:
    resume_data = json.load(json_file)

template = environment.get_template("default.html")

print(template.render(resume_data))