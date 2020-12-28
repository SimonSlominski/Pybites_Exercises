from collections import namedtuple
import os

from github import Github

gh = Github()

user = gh.get_user('simonslominski')

Repo = namedtuple('Repo', 'name stars forks')

def get_repo_stats(user, n=5):
    repos = []
    for repo in user.get_repos():
        if repo.fork:
            continue

        repos.append(Repo(name=repo.name,
                          stars=repo.stargazers_count,
                          forks=repo.forks_count))

    return sorted(repos, key=lambda x: x.stars, reverse=True)[:n]

mystats = get_repo_stats(user)
print(mystats)
