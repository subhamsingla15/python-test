from git import Repo
import os
try: 
    path = os.environ['test']
    # if os.environ['test']:
    #     path = os.environ['test']
except KeyError:
    os.environ['test'] = 'C:/Users/singl/Desktop/test1/abcd'
    path = os.environ['test']

#path ='C:\\Users\\singl\\Desktop\\test\\min'
branchname = 'main'
#branchname = 'release-1'

if os.path.isdir(path):
    repo = Repo(path)
    repo.git.checkout(branchname)
    origin = repo.remote(name='origin')
    origin.pull()
else:
    Repo.clone_from('https://github.com/subhamsingla15/python-test.git',path ,branch=branchname)

    # def del_rw(action, name, exc):
    #     os.chmod(name, stat.S_IWRITE)
    #     os.remove(name)
    # shutil.rmtree(path, onerror=del_rw)


#Repo.clone_from('https://github.com/subhamsingla15/python-test.git',path ,branch=branchname)

#print(os.listdir(path))
# isdir = os.path.isdir(path) 
# print(isdir) 
# if os.listdir(path) !=0:
#     print('removing all files from directory')
#     #path = os.path.join('C:\\Users\\singl\\Desktop\\test', 'min')
#     shutil.rmtree(path,ignore_errors=False)
#     #os.rmdir(path)
# all_files = os.listdir()
# if all_files != 0:

#     for f in all_files:
#         print(f)

# print(os.listdir())
#Repo.clone_from('https://github.com/subhamsingla15/python-test.git',path ,branch='main')
