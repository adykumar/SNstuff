import os,sys
import glob
import fnmatch
import operator
import collections

def probeJavaFile(filepath):
    testCount=0
    #print "\n\n\n\n\n\n\n\n\n",filepath
    fin= open(filepath,"r")
    all= fin.readlines()
    for line in all:
        if "@test" in line.lower(): #or "@step" in line.lower():
            if "//" in line: continue
            #print line.rstrip(),"  "
            testCount+=1
    return testCount

def probeDirs():
    projectDict={}
    cwd= os.getcwd()
    dir_list= glob.glob(cwd+"/*/*")
    print dir_list
    for dirbase in dir_list:
        versionName= ""
        vn= 0
        if "fuji" in dirbase:
            versionName= "fuji"
            vn=0
        elif "geneva" in dirbase:
            versionName= "geneva"
            vn=1
        elif "helsinki" in dirbase:
            versionName="helsinki"
            vn=2
        else: pass

        if "dump" in dirbase: continue
        fileCount=0
        testTotalCount=0
        #path = 'C:/Users/sam/Desktop/file1'
        #configfiles = [os.path.join(dirpath, f)
        for dirpath, dirnames, files in os.walk(dirbase):
            for f in files:
                if f.endswith(".java"):
                    #print "**",dirpath+"//"+f
                    parts= dirpath.split("/")
                    #print parts[7]
                    tc=probeJavaFile(dirpath+"//"+f)
                    if parts[7] not in projectDict:
                        projectDict[parts[7]]= {}
                        projectDict[parts[7]]['fuji']=0
                        projectDict[parts[7]]['geneva']=0
                        projectDict[parts[7]]['helsinki']=0
                        #projectDict[parts[7]].append({'fuji':0})
                        #projectDict[parts[7]].append({'geneva':0})
                        #projectDict[parts[7]].append({'helsinki':0})
                    else: projectDict[parts[7]][versionName]+=tc
                    fileCount+=1
                    testTotalCount+=tc
    #sorted_dict = sorted(projectDict.items(), key=operator.itemgetter(1) )
    sorted_dict= collections.OrderedDict(sorted(projectDict.items()))
        #for key in sorted_dict:
        #    print key[0]," : ",key[1]
    for key in sorted_dict:
        print key, sorted_dict[key]
    #print projectDict
    #print "Java Files Scanned:",fileCount,"Total Tests:",testTotalCount


if __name__== "__main__":
        print "Here it begins!\n"
        probeDirs()
