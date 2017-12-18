#!/usr/bin/env python

import wrappers 

class pipeline:
    """
    this class defines an objects that executes the main analysis pipelines of
    targetale
    """

    def __init__(self):

        """
        constructor
        """

        self.status = "idle"
        self.input = ""
        self.outdir = ""
        self.database = ""
        self.format = ""

        return None

    def setup(self, input, outdir, database, format):

        """
        option setup
        """

        self.input = input
        self.outdir = outdir
        self.database = database
        self.format = format

        return None
    
    def run(self):

        """
        Executes the pipeline
        """

        annotale = wrappers.annotale()
        talgetter = wrappers.talgetter()
        gene2uniprot = wrappers.gene2uniprot()
        quickgo = wrappers.quickgo()

        # run annotale



        return None