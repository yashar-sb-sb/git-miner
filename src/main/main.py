# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import git
from git import Repo

from src.main.entities.Commit import *

if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


repo = Repo('/opt/jam')

commits = list(repo.iter_commits(rev='initiall..master'))[::-1]


def crete_commit(commit: git.Commit):
    files = list(map(lambda name: File(name.split('/')[-1]), commit.stats.files.keys()))
    return Commit(Hash(""), files)


line = CommitLine(list(map(
    crete_commit
    ,
    commits
)))

dic = dict()

for index, commit in enumerate(line.commits):
    for file in commit.files:
        if file.name not in dic:
            dic[file.name] = 0
        dic[file.name] += index

for file in sorted(dic.items(), key=lambda item: item[1]):
    print(int(file[1]/len(line.commits)), file[0])
