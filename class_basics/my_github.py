#!/usr/bin/env python3

import os
from github import Github

#help(Github)

token=os.environ['GITHUB_TOKEN']

gh = Github(login_or_token=token)
#print(gh.get_user())

repo = gh.get_repo('debruce/family_class')

for b in repo.get_branches():
    print(b)

for commit in repo.get_commits():
    # help(commit)
    print(f"author = {commit.author}")
    print(f"files = {commit.files}")
    print(f"parents = {commit.parents}")
    print(f"sha = {commit.sha}")
    print(f"stats.additions = {commit.stats.additions}")
    print(f"stats.deletions = {commit.stats.deletions}")
    print(f"stats.total = {commit.stats.total}")
    for f in commit.files:
        print(f"    sha={f.sha} name=={f.filename}")
    #help(commit.stats)
    print()

# help(repo)

# for r in g.get_repos():
#     print(r)