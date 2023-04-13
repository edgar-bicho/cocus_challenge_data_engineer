import pytest, sys, glob, os, fnmatch
from challenge1 import is_valid_arguments, search_files


def test_is_valid_arguments_valid_input():
    sys.argv = ['challenge1.py', '*.log', '/var/tmp']
    assert is_valid_arguments() == True

def test_is_valid_arguments_invalid_input():
    sys.argv = ['challenge1.py', '*.log']
    assert is_valid_arguments() == False

def test_is_valid_arguments_path_does_not_exist():
    sys.argv = ['challenge1.py', '*.log', '/invalid/path']
    assert is_valid_arguments() == False

def test_search_files():
    files = search_files('/var/tmp', '*.log')
    assert isinstance(files, list) == True
    assert len(files) > 0
    for file in files:
        assert os.path.isfile(file) == True
        assert fnmatch.fnmatch(file, '*.log') == True

# integration Test: Test the integration between is_valid_arguments() and search_files() by calling "*.log /var/tmp" and verifying the output.
def test_integration():
    sys.argv = ['challenge1.py', '*.log', '/var/tmp']

    if not is_valid_arguments():
        quit()
    files = search_files(sys.argv[2], sys.argv[1])
    for file in files:
        print(file)

    assert len(files) > 0
    for file in files:
        assert os.path.isfile(file) == True
        assert fnmatch.fnmatch(file, '*.log') == True