from fabric.api import local

def build():
    local("cd bslint && pylint bslint -r n")
    local("cd tests && pylint tests -r n")