import dataclasses


@dataclasses.dataclass
class Hash:
    str: str


@dataclasses.dataclass
class File:
    name: str


@dataclasses.dataclass
class Commit:
    hash: Hash
    files: list[File] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class CommitLine:
    commits: list[Commit] = dataclasses.field(default_factory=list)
