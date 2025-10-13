from pathlib import Path
from src.app import handler
from yaml import safe_load

# Prepare CV definitions
# Load each YAML into a nested CV object
cv_definitions = []
cv_definitions_dir = Path(__file__).parent.joinpath('input', 'cv_definitions')
for item in cv_definitions_dir.iterdir():
    if item.is_file() and str(item).endswith('.yaml'):
        cv_string = item.read_text()
        cv_yaml = safe_load(cv_string)
        cv_definitions.append(cv_yaml)

# Prepare stylesheets
stylesheet_strings = []
stylesheet_dir = Path(__file__).parent.joinpath('input', 'css')

for item in stylesheet_dir.iterdir():
    if item.is_file():
        stylesheet_strings.append(item.read_text())

# Prepare HTML template
template_string = None
template_path = Path(__file__).parent.joinpath('input', 'html', 'default.html.jinja')
template_string = template_path.read_text()

event = {
    'template_string': template_string,
    'stylesheet_strings': stylesheet_strings,
    'cv_definitions': cv_definitions
}

handler(event=event, context={})
