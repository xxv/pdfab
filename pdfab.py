#!/usr/bin/env python

from pdfab import PDFab
import sys

import json
from pathlib import Path


svg_path = Path(sys.argv[1])
p = PDFab(svg_path.parent.as_posix(), svg_path.name)

param_list = json.load(open(sys.argv[2]))

for i, params in enumerate(param_list):
    pdf_name="{0}-{1:04d}.pdf".format(svg_path.stem, i)
    p.make_pdf(params, pdf_name)

