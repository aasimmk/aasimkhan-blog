from fabric.api import local, env


def prod():
    env.ENV = 'prod'
    env.branch = 'main'
    env.repo = 'aptible-prod git@beta.aptible.com:medconx-prod/medconx-backend-prod.git'


def deploy(branch=False):
    if branch:
        use_branch = branch
    else:
        use_branch = env.branch

    remotes = local('git remote', capture=True).splitlines()

    if ('aptible-%(env)s' % {'env': env.ENV}) in remotes:
        local('git push aptible-%(env)s %(use_branch)s:master' % {
            'use_branch': use_branch,
            'env': env.ENV
        })
    else:
        local('git remote add %(repo)s' % {'repo': env.repo})
        local('git push aptible-%(env)s %(use_branch)s:master' % {
            'use_branch': use_branch,
            'env': env.ENV
        })


def launch():
    if env.ENV == 'dev':
        local('ENV=%(env)s docker-compose -f docker-compose.yml up --build' % {'env': env.ENV})
    else:
        local('ENV=%(env)s docker-compose up --build' % {'env': env.ENV})


def config():
    local('aptible config')
