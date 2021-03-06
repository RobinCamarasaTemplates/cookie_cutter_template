"""
**Author** : {{ cookiecutter.author_name }}

**Institution** : {{ cookiecutter.author_institution }}

**Position** : {{ cookiecutter.author_position }}

**Contact** : {{ cookiecutter.author_mail }}

**Date** : {% now 'utc', '%Y-%m-%d' %}

**Project** : {{ cookiecutter.repo_name }}

**Test {{ cookiecutter.repo_name }} project **

"""
import sys
import os
from datetime import datetime
import pytest
import shutil
from pathlib import Path
from cookiecutter import main
import subprocess


ROOT = Path(__file__).parents[1]
TESTS_ROOT = ROOT / 'test_output'
EXTRA_CONTEXT = {
    "project_name": "Awesome test",
    "description": "Description",
    "remote_url": "github.com",

    "author_name": "John Doe",
    "author_institution": "john.doe@lambda.com",
    "author_position": "Intern",
    "author_github": "https://github.com/JohnDoe"
}


def test_generate_project() -> None:
    """
    Test project generation

    :return: None
    """
    # Clean
    if TESTS_ROOT.exists():
        shutil.rmtree(TESTS_ROOT)
    TESTS_ROOT.mkdir()

    # Get path
    output_dir = TESTS_ROOT.resolve()

    # Launch project generation
    main.cookiecutter(
        str(ROOT),
        no_input=True,
        extra_context=EXTRA_CONTEXT,
        output_dir=output_dir
    )

    # Test project generation
    project_name = 'awesome-test'
    assert (TESTS_ROOT / project_name).exists()
