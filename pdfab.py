#!/usr/bin/env python

from pathlib import Path
from pdfab import PDFab
import json
import sys
from jinja2 import Environment, FileSystemLoader

svg_path = Path(sys.argv[1])
path = svg_path.parent.absolute().as_posix()
print("Attempting to load from {:s}".format(path))
environment = Environment(loader = FileSystemLoader(path))
p = PDFab(environment, svg_path.name)

param_list = json.load(open(sys.argv[2]))

for i, params in enumerate(param_list):
    pdf_name="{0}-{1:04d}.pdf".format(svg_path.stem, i)
    p.make_pdf(params, pdf_name)

