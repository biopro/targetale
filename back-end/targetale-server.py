#!/usr/bin/env python

import os
import sys
import gc
import time
import MySQLdb
import targeTALE

# define constants

startupScreen = """
=======================================================================
Targetale: A web tool to map TALE genes in the genome X. oryzae strains 
and their potential targets in O. sativa
-----------------------------------------------------------------------

Server running

=======================================================================
"""

targetaleServerPath = os.path.abspath(sys.argv[0])
targetaleServerDir = os.path.dirname(targetaleServerPath)

print "Server running dir: ", targetaleServerDir

# targeTale applicaiton

#targetalePipeline = targeTale.pipeline()

# iteration loop

while True:

	# conectar com o banco de dados

	databaseConnection = MySQLdb.connect('localhost','root','querocafe','targetale')
	databaseCursor = databaseConnection.cursor()

	# recuperar projetos em espera

	databaseCursor.execute("SELECT * FROM projects WHERE status = 'queued'")

	# iterar projetos em espera

	project = databaseCursor.fetchone()

	if project == None:

		gc.collect()
		time.sleep(5)
		
		continue

	# recuperar dados do projeto

	project_id = project[0]
	project_userEmail = project[1]
	project_submissionDate = project[2]
	project_finishedDaste = project[3]
	project_status = project[4]
	project_inputFilePath = project[5]
	project_inputFileFormat = project[6]
	project_promoterome = project[7]

	# definir diretorio do projeto

	projectDir = "/etc/targetale/projects/%s"%(project[0])

	if not os.path.isdir(projectDir):

		os.mkdir(projectDir)

	# rodar pipeline

	targetale = targeTALE.pipeline()
	targetale.setup(input="file.fasta",format="fasta",outdir="projectDir",database="")
	targetale.run()

	# checar status

	project_status = targetale.status
	print project_status

	# atualizar database

	databaseCursor.execute("UPDATE projects SET status='%s' finishedDate=CURDATE() WHERE id=%s"%(project_status,project_id))
	databaseConnection.commit()

	# limpeza do garbage collector e espera
	
	del databaseConnection
	del databaseCursor
	
	gc.collect()
	time.sleep(5)

		

		
