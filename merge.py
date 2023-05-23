from subprocess import run
def rrun(cmd):
    res = run(cmd.split(" "), capture_output=True, text=True)
    if res.returncode != 0:
        err = f"failed to run {cmd} because {res.stderr if res.stderr else res.stdout}"
        print(err)
        raise Exception()
    return res.stdout
def getBranches():
    raw_branches=rrun("git branch -r --format=%(refname:short)")
    return [x.split("/")[1] for x in raw_branches.split("\n") if x]
print(rrun("git --version"))
rrun("git config pull.rebase false")
for branch in getBranches():
    # TODO: Also for the latest version branch (like 5.2.2, 5.4.0, etc.) 
    if branch == "brain" or branch == "HEAD": # or not branch.startsWith("CURA-"):
        continue
    #try:
    #    ticket_no = int(branch.split("-")[1])
    #except:
    #    continue
    #if ticket_no < 10000:
    #    continue
    
    print(f"branch: {branch}")
    hash_pre=""
    try:
        rrun(f"git checkout {branch}")
        rrun("git pull")
        hash_pre = rrun("git rev-parse HEAD")
    except:
        rrun("git reset --hard")
        continue
    try:
        rrun("git merge main")
    except:
        rrun("git merge --abort")
        rrun("git reset --hard")
        continue
    try:
        hash_post = rrun("git rev-parse HEAD")
        if hash_pre != hash_post:
            print("merge successful")
            rrun("git push")
        else:
            print("no merge needed")
    except:
        continue
