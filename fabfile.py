from fabric.api import local, env


def prod():
    env.ENV = 'prod'
    env.branch = 'main'
    env.repo = 'https://git.heroku.com/aasimkhan-in.git'


def deploy(branch=False):
    local('git push heroku main')


def config():
    local('heroku config')
