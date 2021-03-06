#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
complexity
----------

Main package for Complexity.
"""

import os

from .generate import generate_context, copy_assets, generate_html


__version__ = '0.4.2'


def complexity(project_dir, output_dir):
    """
    API equivalent to using complexity at the command line.
    
    .. note:: You must delete `output_dir` before calling this. This also does
       not start the Complexity development server; you can do that from your
       code if desired.
    """

    # Generate the context data
    json_dir = os.path.join(project_dir, 'json/')

    context = None
    if os.path.exists(json_dir):
        context = generate_context(json_dir)

    # Generate and serve the HTML site
    generate_html(project_dir, output_dir, context)
    copy_assets(project_dir, output_dir)