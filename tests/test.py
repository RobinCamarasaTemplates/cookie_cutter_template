"""
**Author** : Robin Camarasa

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-08-06

**Project** : Slide latex template ErasmusMC

**Test project generation of Erasmus MC Slides**

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
    "remote_url": "https://github.com/test/test",

    "author_name": "John Doe",
    "author_institution": "Lambda company",
    "author_position": "Intern",
    "author_mail": "john.doe@lambda.com",
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
    files = [
        'cookiecutter.json', 'LICENSE', 'README.md',
        'requirements.txt', 'Makefile'
    ]
    for file_ in files:
        assert (TESTS_ROOT / project_name/ file_).exists()

    assert (
        TESTS_ROOT / project_name / 'tests' / 'test.py'
    ).exists()

    process = subprocess.Popen(
        ['pytest', 'test.py'],
        cwd=(TESTS_ROOT / project_name / 'tests').resolve()
    )
    process.wait()
    assert process.returncode == 0

