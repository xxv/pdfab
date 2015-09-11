#!/usr/bin/python
# -*- coding: utf-8 -*-

from jinja2 import Environment, PackageLoader
import subprocess
from tempfile import NamedTemporaryFile

#####################################################################

class PDFab:
    def __init__(self, package, svg_file, export_dpi=300):
        print("{} {}".format(package, svg_file))
        self.svg_file = svg_file
        self.env = Environment(loader = PackageLoader(package))
        self.template = self.env.get_template(svg_file)
        self.export_dpi = export_dpi

    def make_pdf(self, params, pdf_name):
        temp = NamedTemporaryFile(mode="w", suffix=".svg")
        temp.write(self.template.render(params))
        temp.flush()

        subprocess.call(["inkscape", "--export-dpi", str(self.export_dpi), "-A", pdf_name, temp.name])
        temp.close()
