from setuptools import setup, find_packages

install_requires = ['Django', 'celery', 'djangorestframework']
tests_require = ['pytest', 'pytest-runner>=2.0,<3dev', 'pytest-flake8']

setup(
    name='{{ cookiecutter.project_slug }}',
    version='0.0.1',
    description="{{ cookiecutter.description }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    url="{{ cookiecutter.project_url }}",
    install_requires=install_requires,
    tests_require=tests_require,
    packages=find_packages(exclude=['tests']),
    extras_require={
        'test': tests_require
    },
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
