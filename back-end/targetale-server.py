#!/usr/bin/env python

import os
import sys
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

	databaseConnection = MySQLdb.connect('localhost','root','querocafe','targetale')
	databaseCursor = databaseConnection.cursor()

	databaseCursor.execute("SELECT * FROM projects WHERE status = 'ESPERA'")

	for project in databaseCursor.fetchall():

		inputPath = project[5]
		inputFormat = project[6]
		promoterome = project[7]
		projectDir = "%s/%s"%(targetaleServerDir, project[0])

		targetalePipeline.setup(input=inputPath)

		

		