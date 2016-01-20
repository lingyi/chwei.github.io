# How to Sync Changes or Commits from Upstream in Github

There are four steps to finish syncing changes from upstream:

##step one : specify a upstream repo
Adding upstream repo:
> git remote add upstream <remote_repo>

Additionally, query current branches list in remote repo:
> git remote -v

## step two : fetch changes from upstream
> git fetch upstream

## step three: merge the upstream to local master
> git checkout master ## local master
> git merge upstream/master 

## step four : commit to local and push to remote repo
> git add . ## track all merge-changes
> git commit -s -m "merge from upstream."
> git push



