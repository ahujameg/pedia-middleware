.. PEDIA-Middleware documentation master file, created by
   sphinx-quickstart on Fri Feb 23 15:53:48 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PEDIA-Middleware's documentation!
============================================

This is a middleware application for handling integration of variant analysis tools like VarFish with PEDIA (Prioritization of Exome data by image analysis). It can be independently embeded as an iFrame in the Variant Analysis tool. It displays a view that takes the patient image as input and submits it to the GestaltMatcher service. It then retrieves the gene list with the gestalt scores from the GestaltMatcher service and posts it back to the parent window (i.e. the tool embedding this application)


.. raw:: latex

    \part{Overview}

.. toctree::
    :maxdepth: 1
    :caption: Overview
    :name: overview
    :hidden:
    :titlesonly:

    pre_requisites




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
