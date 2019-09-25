import os
os.chdir("/home/amir/github/")
repos = os.listdir() # list of all local repositories
for repo in repos:   
    if not repo.startswith("."): # if that repo is not a hidden file <in linux hiddin files names starts with . dot
        os.chdir(repo) # go to that local repo
        git_status = os.popen("git status").read() # read current status
        if '(use "git push" to publish your local commits)' in git_status:
        	os.system("git push origin master")
        elif "Untracked files" in git_status or "Changes not staged for commit" in git_status:
            aa = [i.strip() for i in git_status.splitlines()]
            print(f"**********{repo}**********")
            for i in aa:
	            if i and i.startswith("Untracked files") or i.startswith("Changes not staged for commit"):
	            	os.system("git add . ; git commit -m 'updated'; git push origin master")
            print("\n\n")
        os.chdir("..")