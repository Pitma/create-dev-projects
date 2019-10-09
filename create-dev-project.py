import os
import sys
import requests

#Credentials

pw = os.environ['GITSECRET']
user = 'pitma'

def create(projectName):
    print ("das neue Projekt heißt", projectName)
    # define the name of the directory to be created
    path = os.getcwd()+'\\' + projectName

    if not os.path.exists(path):
        os.mkdir(path)
        os.chdir(path)
        print("Directory " , path ,  " Created ")
        createReadMe()
        createRepo(projectName)
        initGit(projectName)
    else:    
        print("Directory " , path ,  " already exists")
      

def createReadMe():
    try:
        open("README.md","w+")
    except OSError:
        print ("Creation of the file readme.md failed")
    else:
        print ("Successfully created the file readme.md")
        

def createRepo(projectName):
    data = '{"name":"' + projectName + '"}'
    response = requests.post('https://api.github.com/user/repos', data=data, auth=(user,pw))
    print(response)

def initGit(projectName):
    os.system('git init')
    os.system('git add README.md')
    os.system('git commit -m "First commit!')
    os.system('git remote add origin \"https://'+user+':'+pw+'@github.com/'+user+'/' + projectName + '.git\"')
    os.system('git push -u origin master')
    
if __name__ == "__main__":
    try:
        projectName = sys.argv[1]
        create(projectName)
        os.system('code .')
    except:
        print('Bitte Projektnamen angeben:')