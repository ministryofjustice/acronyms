import re
from dataclasses import dataclass
from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
from datetime import datetime

# Small dataclass to hold an Acronym, helps a lot with templating
@dataclass
class Acronym:
    abbreviation: str
    definition: str
    url: str
    info: str 

# Config
readme_path   = 'README.md'
templates_path = 'template'
template_name  = 'acronyms.jinja2'
output_file    = "index.html"

# Open README and store
with open(readme_path, "r", encoding="UTF-8") as f:
    lines = f.read().splitlines()

# Remove everything above the acronyms, split by the README table seperators '|' and store result
# This effectively produces a list of lists, each sub list containing a line with the different columns of the acronym table 
split_lines = [line.split('|') for line in list(filter(lambda l: re.search("(^\|)", l), lines))[2:]]

# Pop every line to cleanse 
for line in split_lines:
    del line[0]

# Create final list of cleansed acronyms
acronyms = []
for line in split_lines:
    acronyms.append(Acronym(line[0].strip(), line[1].strip(), line[2].strip(), line[3].strip()))
    
# Load Jinja2 templates
env = Environment(
    loader=FileSystemLoader(templates_path),
    autoescape=select_autoescape()
)

# Render the template with the acronyms
template = env.get_template(template_name)
rendered_template = template.render(list=acronyms, last_updated=datetime.now().strftime("%Y-%m-%d %H:%M"))

# Write to a file
with open(output_file, "w", encoding="UTF-8") as fh:
    fh.write(rendered_template)
