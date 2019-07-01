#!/usr/bin/python
# Author : Vishal Bhardwaj
# Currently PhysRevD, PhysRevLett, PTEP, JHEP, EPJC
# Just provide the location of the .bibtex files location of the files in a file bbtex.tex'
# Once can modify the script to create the list as per his/her vvish.
# You can also make .latex tables or itemize.
# It seems to work fine.  It counts the total Authors, arrange the papers year wise.
# Script can be made much better using functions and better control.
# However, I don't have much time or patience. It solved my purpose and I am happy with it. Sharing with the community in order to make their life useful.
# Enjoy and if you think it help you then share with others also.
# Code is somewhat quick and dirty one.
# Help in preparing automatic latex file for you form .bibtex in the type of format you want
# Helps in creating that stupid and fucking job application :D
# Currently, it itemize for latex. I can also make Tables from it.

import os
import re
import fnmatch
import sys

cwd=os.getcwd()


#Your family name if you want to find in the first authors or so.
myName='Bhardwaj'

# Store first 9 names in the authorList
storeName=['a','b','c','d','e','f','g','h','i']

iNameFinder=9
iNF=0

#year in which you find the authorlist
Years=[2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007]

#sys.exit()

for iY in Years:
    iFile=open('bbtext.tex', 'r')

    for line in iFile:
        if not line.strip():
            break
   
        nline=line.strip('\n')
        if fnmatch.fnmatch(nline,'*JHEP*'):
            APrint=0
            iNF=0
            iAuth=0
            iTitle='Still to Search'
            iVol=999999
            iYear=9999
            iPage=9999
            iJournal='PRL'
            rFile=open(nline, 'r')
            for rlFile in rFile:
                if re.match('year=', rlFile):
                    year0=rlFile.strip('year="')
                    year1=year0.strip('",\n')
                    iYear=year1
                        
                if re.match('journal=', rlFile):
                    journal0=rlFile.strip('journal="')
                    journal1=journal0.strip('",\n')
                    iJournal=journal1
                    
                if re.match('title=', rlFile):
                    title0=rlFile.strip('title="')
                    title1=title0.strip('",\n')
                    iTitle=title1
                if re.match('volume=', rlFile):
                    volume0=rlFile.strip('volume="')
                    volume1=volume0.strip('",\n')
                    iVol=volume1
                if re.match('pages=', rlFile):
                    page0=rlFile.strip('pages="')
                    page1=page0.strip('",\n')
                    iPage=page1


                if re.match('and ', rlFile):
                    rlFile1=rlFile.strip('and ')
                    rlFile2=rlFile1.strip('\n')
                    rlFile3=rlFile2.strip('"')
                    iAuth=iAuth+1
                    iAuthor=os.path.basename(rlFile3).split(", ")
                    if (iNF < 5 ) :
                        if iAuthor[0] == 'Bhardwaj':
                            APrint=iNF+1
                        storeName[iNF]=iAuthor[1]+ ' ' + iAuthor[0]
                        iNF=iNF+1
                    
            if str(iY) == str(iYear):
                if APrint > 0:
                    print "\item{"
                    for iAF in range(APrint):
                        print storeName[APrint] +", "
                    print "{\it et al.} (Belle Collaboration), (" + str(iAuth)+ " Authors), " + iTitle + "," + iJournal + " {\\bf{"+ iVol + "}}, "+ iPage +" (" +  iYear + ").}"
                            
                else:
                    print "\item{"+ storeName[0]+ " {\it et al.} (Belle Collaboration), (" + str(iAuth)+ " Authors), "  + iTitle + ", " + iJournal + " {\\bf{"+ iVol + "}}, "+ iPage +" (" +  iYear + ").}"


        if fnmatch.fnmatch(nline,'*epjc*'):
            iNF=0
            iAuth=0
            iTitle='Still to Search'
            iVol=999999
            iYear=9999
            iPage=9999
            iJournal='PRL'
            rFile=open(nline, 'r')
            for rlFile in rFile:

                if re.match('journal=', rlFile):
                    journal0=rlFile.strip('journal="')
                    journal1=journal0.strip('",\n')
                    iJournal=journal1
                    
                if re.match('title=', rlFile):
                    title0=rlFile.strip('title="')
                    title1=title0.strip('",\n')
                    iTitle=title1
                if re.match('volume=', rlFile):
                    volume0=rlFile.strip('volume="')
                    volume1=volume0.strip('",\n')
                    iVol=volume1
                if re.match('year=', rlFile):
                    year0=rlFile.strip('year="')
                    year1=year0.strip('",\n')
                    iYear=year1

                if re.match('pages=', rlFile):
                    page0=rlFile.strip('pages="')
                    page1=page0.strip('",\n')
                    iPage=page1

                if re.match('and ', rlFile):
                    rlFile1=rlFile.strip('and ')
                    rlFile2=rlFile1.strip('\n')
                    rlFile3=rlFile2.strip('"')
                    iAuth=iAuth+1
                    iAuthor=os.path.basename(rlFile3).split(", ")
                    if (iNF < 5 ) :
                        if iAuthor[0] == 'Bhardwaj':
                            APrint=iNF+1
                        storeName[iNF]=iAuthor[1]+ ' ' + iAuthor[0]
                        iNF=iNF+1

            if str(iY) ==  str(iYear) :
                if APrint > 0:
                    print "\item{"
                    for iAF in range(APrint):
                        print storeName[APrint] +", "
                    print "{\it et al.} (Belle Collaboration), (" + str(iAuth)+ " Authors), " + iTitle + "," + iJournal + " {\\bf{"+ iVol + "}}, "+ iPage +" (" +  iYear + ").}"
                            
                else:
                    print "\item{"+ storeName[0]+ " {\it et al.} (Belle Collaboration), (" + str(iAuth)+ " Authors), "  + iTitle + ", " + iJournal + " {\\bf{"+ iVol + "}}, "+ iPage +" (" +  iYear + ").}"
        

        if fnmatch.fnmatch(nline,'citations-*'):
            iNF=0
            iAuth=0
            iTitle='Still to Search'
            iVol=999999
            iYear=9999
            iPage=9999
            iMonth=9999
            iJournal='PRL'
            rFile=open(nline, 'r')
            for rlFile in rFile:
                if re.match('    journal = {', rlFile):
                    journal0=rlFile.strip('    journal = {')
                    journal1=journal0.strip('},\r')
                    iJournal=journal0.split('}',1)[0]
                if re.match('    title = "{', rlFile):
                    title0=rlFile.strip('    title = "{')
                    title1=title0.strip('"},\r')
                    iTitle=title0.split('}',1)[0]
                if re.match('    volume = {', rlFile):
                    volume0=rlFile.strip('    volume = {')
                    iVol=volume0.split('},',1)[0]
                if re.match('    year = {', rlFile):
                    year0=rlFile.strip('    year = {')
                    iYear=year0.split('},',1)[0]
                if re.match('    month = {', rlFile):
                    mon0=rlFile.strip('    month = {')
                    iMonth=mon0.split('}',1)[0]
                if re.match('    eprint = {', rlFile):
                    rTexT='    eprint = {http://oup.prod.sis.lan/ptep/article-pdf/'+str(iYear)#+str(iMonth)+'/'
                    rTexT='    eprint = {http://oup.prod.sis.lan/ptep/article-pdf'
                    page0=rlFile.strip(rTexT)
                    iPage=page0.split('/',3)[2]
                    page1=page0.strip('",\r')

                if re.match("    author = ", rlFile):
                    rlFile1=rlFile.strip('},\n')
                    rlFile2=rlFile1.strip('  author = {')
                    rlFile3=rlFile2.strip('and Belle Collaboration},\r')
                    rlFile3=rlFile2.strip(' and (The Belle Collaboration)},\r')
                    TrlFile=os.path.basename(rlFile3).split(" and ")
                    for iL in TrlFile:
                        iAuthor=os.path.basename(iL).split(", ")
                        
                        
                        if (iNF < 5 ) :
                            storeName[iNF]=iAuthor[1]+ ' ' + iAuthor[0]
                            
                            if iAuthor[0] == 'Bhardwaj':
                                APrint=iNF+1
                            iNF=iNF+1
            if str(iY) == str(iYear):
                if APrint > 0:
                    print "\item{"

                    for iAF in range(APrint):
                        print storeName[iAF]+", "
                    print "{\it et al.} (Belle Collaboration), (" + str(len(TrlFile))+ " Authors), " + iTitle + "," + iJournal + "{ \\bf{"+ str(iVol) + "}}, "+ str(iPage) +" (" +  str(iYear) + ").}"
                        
                else:
                    print  "\item{"+ storeName[0]+ " {\it et al.} (Belle Collaboration), (" + str(len(TrlFile))+ " Authors), "  + iTitle + ", " + iJournal + "{\\bf{"+ str(iVol) + "}}, "+ str(iPage) +" (" +  str(iYear) + ").}"



    
        if fnmatch.fnmatch(nline,'PhysRev*'):
            APrint=0
            iNF=0
            iAuth=0
            iTitle='Still to Search'
            iVol=999999
            iYear=9999
            iPage=9999
            iJournal='PRL'
            rFile=open(nline, 'r')
            rFile=open(nline, 'r')
            for rlFile in rFile:
                if re.match('  journal =', rlFile):
                    journal0=rlFile.strip('  journal = {')
                    journal1=journal0.strip('},\n')
                    iJournal=journal1
                if re.match('  title = ', rlFile):
                    title0=rlFile.strip('  title = {')
                    title1=title0.strip('},\n')
                    iTitle=title1
                if re.match('  volume = ', rlFile):
                    volume0=rlFile.strip('  volume = {')
                    volume1=volume0.strip('},\n')
                    iVol=volume1
                if re.match('  year =', rlFile):
                    year0=rlFile.strip('  year = {')
                    year1=year0.strip('},\n')
                    iYear=year1
                if re.match('  pages =', rlFile):
                    page0=rlFile.strip('  pages = {')
                    page1=page0.strip('},\n')
                    iPage=page1


                
                if re.match("author ", rlFile):
                    rlFile1=rlFile.strip('",\n')
                    rlFile2=rlFile1.strip('author = "')
                    TrlFile=os.path.basename(rlFile2).split(" and ")
                    for iL in TrlFile:
                        print iL

                if re.match("  author =", rlFile):
                    rlFile1=rlFile.strip('},\n')
                    rlFile2=rlFile1.strip('  author = {')
                    #  print rlFile
                    TrlFile=os.path.basename(rlFile2).split(" and ")
                    # print TrlFile
                    for iL in TrlFile:
                        iAuthor=os.path.basename(iL).split(", ")
                        if (iNF < 5 ) :
                            storeName[iNF]=iAuthor[1]+ ' '+iAuthor[0]
                            if iAuthor[0] == 'Bhardwaj':
                                APrint=iNF+1
                            iNF=iNF+1

            if str(iY) == str(iYear):
           
                if APrint > 0:
                    print "\item{"

                    for iAF in range(APrint):
                        print storeName[iAF]+", "
                    print "{\it et al.} (Belle Collaboration), (" + str(len(TrlFile))+ " Authors), " + iTitle + "," + iJournal + "{ \\bf{"+ str(iVol) + "}}, "+ str(iPage) +" (" +  str(iYear) + ").}"
                            
                else:
                    print "\item{"+ storeName[0]+ " {\it et al.} (Belle Collaboration), (" + str(len(TrlFile))+ " Authors), "  + iTitle + ", " + iJournal + "{ \\bf{"+ str(iVol) + "}}, "+ str(iPage) +" (" +  str(iYear) + ").}"

 

    

        if fnmatch.fnmatch(nline,'S0*.bib'):
            APrint=0
            iNF=0
            iAuth=0
            iTitle='Still to Search'
            iVol=999999
            iYear=9999
            iPage=9999
            iJournal='PRL'
            rFile=open(nline, 'r')
            for rlFile in rFile:
                if re.match('journal = ', rlFile):
                    journal0=rlFile.strip('journal = "')
                    journal1=journal0.strip('",\n')
                    iJournal=journal1
                if re.match('title = ', rlFile):
                    title0=rlFile.strip('title = "')
                    title1=title0.strip('",\n')
                    iTitle=title1
                if re.match('volume = ', rlFile):
                    volume0=rlFile.strip('volume = "')
                    volume1=volume0.strip('",\n')
                    iVol=volume1
                if re.match('year = ', rlFile):
                    year0=rlFile.strip('year = "')
                    year1=year0.strip('",\n')
                    iYear=year1
                if re.match('pages = ', rlFile):
                    page0=rlFile.strip('pages = "')
                    page1=page0.strip('",\n')
                    iPage=page1


                if re.match("author ", rlFile):
                    rlFile1=rlFile.strip('",\n')
                    rlFile2=rlFile1.strip('author = "')
                    TrlFile=os.path.basename(rlFile2).split(" and ")
                    for iL in TrlFile:
                        if (iNF < 5 ) :
                            storeName[iNF]=iL
                            
                            if iL == 'V. Bhardwaj':
                                APrint=iNF+1
                            iNF=iNF+1

            if str(iY) == str(iYear):
           
                if APrint > 0:
                    print "\item{"

                    for iAF in range(APrint):
                        print storeName[iAF]+", "
                    print "{\it et al.} (Belle Collaboration), (" + str(len(TrlFile))+ " Authors), " + iTitle + "," + iJournal + "{ \\bf{"+ str(iVol) + "}}, "+ str(iPage) +" (" +  str(iYear) + ").}"
                            
                else:
                    print  "\item{"+storeName[0]+ " {\it et al.} (Belle Collaboration), (" + str(len(TrlFile))+ " Authors), "  + iTitle + ", " + iJournal + "{ \\bf{"+ str(iVol) + "}}, "+ str(iPage) +" (" +  str(iYear) + ").}"

 
print 'Auto created for \LaTeX from .bibtex - {\it script by {\tt V. Bhardwaj}}'        
