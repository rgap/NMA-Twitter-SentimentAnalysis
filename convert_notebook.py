import nbformat
from nbconvert import ScriptExporter

# Load the notebook
with open("sentiment_analysis.ipynb") as f:
    notebook = nbformat.read(f, as_version=4)

# Create a script exporter
script_exporter = ScriptExporter()

# Convert the notebook to a script
(script, resources) = script_exporter.from_notebook_node(notebook)

# Save the script
with open("sentiment_analysis.py", "w") as f:
    f.write(script)
