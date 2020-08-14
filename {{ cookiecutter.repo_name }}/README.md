# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Requirements
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


## To start a new project, run
``` bash
$ cookiecutter {{ cookiecutter.remote_url }}
```

## To contribute
- Clone repository
```bash
$ git clone {{ cookiecutter.remote_url }}
```
- Install the requirement
```bash
$ pip install -r requirements.txt
```
- Make sure that your modification works
```bash
$ make
```

## Authors
The following authors contributed :
- [{{ cookiecutter.author_name }}]({{ cookiecutter.author_github }})
