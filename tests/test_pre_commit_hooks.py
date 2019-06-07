from pre_commit_hooks import __version__


def test_version():
    assert __version__ == '0.1.0'
    print("Hi")