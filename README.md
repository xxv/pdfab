PDFab
=====

A tool for generating many PDFs from an SVG image template and a bunch of data.
For example: this can be used to generate a bunch of name badges for a
conference (including supporting things like toggling special flair for
sponsors).

This is somewhat similar to Word's mail merge feature.

Ingredients
-----------

* Inkscape
* Python 3.4
* Jinja2

Instructions
------------

Create your SVG document and prepare it so it renders properly in Inkscape. In
place of any text you wish to have replaced, use the standard Jinja2 template
strings (e.g. `{{ name }}`).

Because the SVG document is run through Jinja2, you can actually switch layers,
disable/enable elements, etc. using conditionals and other Jinja2 structures.
This can be carefully written to avoid being eaten by Inkscape by using comments:

    <!-- {% if show_layer %} -->
    <g […] />
    <!-- {% endif %} -->

Example
-------

To run the example, simply do:

    ./pdfab.py namecard.svg test.json

This will read `namecard.svg` and generate a PDF for every item in the
`test.json` file.

License
-------

PDFab — churn out hundreds of beautiful templated PDFs  
Copyright (C) 2015-2016  Steve Pomeroy <steve@staticfree.info>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
