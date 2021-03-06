import os
import tempfile
import filecmp
import difflib

os.chdir('../output')

def teardown_function(function):
    if os.path.exists('output.txt'):
        os.remove('output.txt')

def change_dir():
    os.chdir('../output')

def test_file_output():
    open('output.txt', 'w').write("Hello World!")  # the code being tested
    assert os.path.exists('output.txt')

def test_file_output_with_tempfile():
    with tempfile.TemporaryFile('w') as f:
        f.write("Hello World!")  # the code being tested

def test_file_output_with_tempdir(tmpdir):
    tempf = tmpdir.join('output.txt')
    tempf.write("Hello World!")  # the code being tested
    content = tempf.read()
    assert content == "Hello World!"
    # assert False  # uncomment to see fixture path

def test_compare_files():
    open('output.txt', 'w').write("***Hello World***")  # the code being tested
    lines_result = open('output.txt').readlines()
    lines_expected = open('../program_tests/expected.txt').readlines()
    print('\n'.join(difflib.ndiff(lines_result, lines_expected)))
    assert filecmp.cmp('output.txt', '../program_tests/expected.txt')
