#!/usr/bin/env python

import os
import sys
import csv
import shutil
import subprocess
import bioservices

class annotale:

    def __init__(self):

        self.APPLICATION_PATH = os.path.abspath(sys.argv[0])
        self.APPLICATION_DIR  = os.path.dirname(self.APPLICATION_PATH)
        self.JAVA_PATH = "/usr/bin/java"
        self.ANNOTALE_PATH = "%s/bin/annotale/annotale.jar"%(self.APPLICATION_DIR)
        self.file = None
        self.outdir = None
        self.mode = None
        self.log_dir = None
        self.rvds = []
    
    def setup(self, file, outdir, mode):

        self.file = file
        self.outdir = os.path.abspath(outdir)
        self.mode = mode

        if not os.path.isdir(outdir):

            try:

                os.mkdir(outdir)
            
            except:

                print "Unable to create directory '%s'"%outdir
                return False
        
        self.log_dir = '%s/../logs'%self.outdir

        if not os.path.isdir(self.log_dir):

            os.mkdir(self.log_dir)
        
        if mode == 'fasta':
            
            shutil.copy(file, "%s/genome.fasta"%outdir)
            self.file = "%s/genome.fasta"%outdir
        
        elif mode == 'genbank':

            shutil.copy(file, "%s/genome.gbk"%outdir)
            self.file = "%s/genome.gbk"%outdir

        else:

            print "Unsuported file mode '%s' (must be 'fasta' or 'genbank')"%self.mode
            return False 
        
        return True

    def run(self):

        # rodar preditor

        annotale_predict_stdout = "%s/../logs/annotale_predict.stdout.log"%(self.log_dir)
        annotale_predict_stderr = "%s/../logs/annotale_predict.stderr.log"%(self.log_dir)
        annotale_predict_cmd = "%s -jar %s predict g=%s outdir=%s"%(self.JAVA_PATH, 
                                                                self.ANNOTALE_PATH, 
                                                                self.file, 
                                                                self.outdir)
        
        subprocess.call(annotale_predict_cmd, shell=True, stdout=open(annotale_predict_stdout, 'w'), 
                                                          stderr=open(annotale_predict_stderr, 'w'))
        
        tale_file = "%s/TALE_DNA_sequences.fasta"%(self.outdir)

        if not os.path.isfile(tale_file):

            print "File '%s' was not found"%tale_file
            return False       

        # rodar analizador

        annotale_analyze_stdout = "%s/../logs/annotale_analyze.stdout.log"%(self.log_dir)
        annotale_analyze_stderr = "%s/../logs/annotale_analyze.stderr.log"%(self.log_dir)
        annotale_analyze_cmd = "%s -jar %s analyze t=%s outdir=%s"%(self.JAVA_PATH, 
                                                               self.ANNOTALE_PATH, 
                                                               tale_file, 
                                                               self.outdir)

 
        subprocess.call(annotale_analyze_cmd, shell=True, stdout=open(annotale_analyze_stdout, 'w'), 
                                                          stderr=open(annotale_analyze_stderr, 'w'))


        # rodar construtor

        annotale_build_stdout = "%s/../logs/annotale_build.stdout.log"%(self.log_dir)
        annotale_build_stderr = "%s/../logs/annotale_build.stderr.log"%(self.log_dir)
        annotale_build_cmd = "%s -jar %s build t=%s outdir=%s"%(self.JAVA_PATH, 
                                                               self.ANNOTALE_PATH, 
                                                               tale_file, 
                                                               self.outdir)
        
        subprocess.call(annotale_build_cmd, shell=True, stdout=open(annotale_build_stdout, 'w'), 
                                                        stderr=open(annotale_build_stderr, 'w'))

        # rodar atribuidor

        currentDir = os.getcwd()
        os.chdir(self.outdir)

        if not os.path.isfile('TALE_DNA_parts.fasta'):

            print "File 'TALE_DNA_parts.fasta' was not found"
            return False               

        annotale_build_stdout = "%s/../logs/annotale_assign.stdout.log"%(self.log_dir)
        annotale_build_stderr = "%s/../logs/annotale_assign.stderr.log"%(self.log_dir)
        annotale_build_cmd = "%s -jar %s assign t=TALE_DNA_parts.fasta c=Class_builder.xml outdir=%s"%(self.JAVA_PATH, 
                                                               self.ANNOTALE_PATH, 
                                                               os.getcwd())
        
        subprocess.call(annotale_build_cmd, shell=True, stdout=open(annotale_build_stdout, 'w'), 
                                                        stderr=open(annotale_build_stderr, 'w'))

        os.chdir(currentDir)

        # ler dados das classes

        for class_dir in os.listdir("%s"%self.outdir):

            class_dir = os.path.abspath("%s/%s"%(self.outdir,class_dir))

            #print class_dir
            
            if os.path.isdir(class_dir):

                for file in os.listdir(class_dir):

                    if not os.path.splitext(file)[1] == '.txt':

                        continue
                    
                    if not 'Class_report_for_' in file:

                        continue
                    
                    class_name = file.split('Class_report_for_')[1]
                    
                    fileContent = open("%s/%s"%(class_dir, file)).read().split('\n')
                    rvd = fileContent[4].split('\t')[0].strip(' ').replace(' ', '-')
                    self.rvds.append([class_name.split('.')[0], rvd])               


class talgetter:

    def __init__(self):

        self.APPLICATION_PATH = os.path.abspath(sys.argv[0])
        self.APPLICATION_DIR  = os.path.dirname(self.APPLICATION_PATH)
        self.JAVA_PATH = "/usr/bin/java"
        self.TALGETTER_PATH = "%s/bin/talgetter/talgetter.jar"%(self.APPLICATION_DIR)
        self.promoterome = None
        self.outfile = None
        self.outdir = None
        self.targets = []

    def setup(self, rvd, promoterome, outfile=os.getcwd(), evalue=1e-10, pvalue=0.01, top=10000):

        outdir = os.path.dirname(outfile)
        self.outdir = outdir

        if not os.path.isdir(outdir):

            try:

                os.mkdir(outdir)
            
            except:

                print "Unable to create directory '%s'"%outdir
                return False

        self.rvd = rvd
        self.promoterome = promoterome
        self.outfile = outfile
        self.evalue = evalue
        self.pvalue = pvalue
        self.top = top  

        return True

    def run(self):

        talgatter_log_stderr = open("%s/../logs/talgetter_stderr.log"%(self.outdir),'w')
        talgatter_cmd = "%s -jar %s input=%s rvd='%s' top=%s pthresh=%s "%(self.JAVA_PATH, 
                                                                             self.TALGETTER_PATH,
                                                                             self.promoterome,
                                                                             self.rvd,
                                                                             self.top,
                                                                             self.pvalue)
        subprocess.call(talgatter_cmd, stdout=open(self.outfile,'w'), stderr=talgatter_log_stderr, shell=True)

        if os.path.isfile(self.outfile):

            outputHandle = open(self.outfile)
            outputParser = csv.reader(outputHandle, delimiter='\t')

            for rowIndex, row in enumerate(outputParser):

                if rowIndex == 0 or len(row) < 8:

                    continue
        
                if float(row[7]) <= self.evalue and float(row[8]) <= self.pvalue:

                     self.targets.append(row[0])

class gene2uniprot:

    def __init__(self):

        self.uniprot = bioservices.uniprot.UniProt()

    def map(self, genes):

        resultados = []

        for gene in genes:

            raw_resultlist = self.uniprot.search('gene:%s taxonomy:"oryza sativa"'%gene)
            resultlist = raw_resultlist.strip('\n').split('\n')

            if resultlist:

                uniprotId = resultlist[0]

            else:

                uniprotId = None

            resultados.append((gene, uniprotId))
        
        return resultados



class quickgo:

    def __init__():

        self.JAVA_PATH = "/usr/bin/java"