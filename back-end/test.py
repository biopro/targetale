#!/usr/bin/env python

from targeTALE import *

annotale = wrappers.annotale()
annotale.setup(file="test/datasets/sequence.fasta",outdir="test/results/fasta/annotale",mode="fasta")
annotale.run()

talgetter = wrappers.talgetter()

gene2uniprot = wrappers.gene2uniprot()

for rvd in annotale.rvds:

    print rvd[0],':', rvd[1]
    print '----------------------------------------------------------'

    talgetter.setup(rvd=rvd[1], promoterome='db/promoteromes/Prom_250_bp.txt', outfile='test/results/fasta/talgetter/%s.txt'%rvd[0])
    talgetter.run()
    print 'Targets found:', len(talgetter.targets)
    print gene2uniprot.map(talgetter.targets)
