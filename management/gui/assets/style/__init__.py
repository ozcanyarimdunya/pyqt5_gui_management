#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os

__version__ = "1.0.0"
__author__ = "ColinDuquesnoy"


def _logger():
    return logging.getLogger('management')


def load_style():
    # import of the rc file
    import management.gui.assets.style.style_rc
    path = os.path.join(os.path.dirname(__file__), 'style.qss')
    file_text = open(path, 'r').read()
    return file_text
