# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5

# prefix 'test' as file's name, so pytest can collect test automatically.
# name method with prefix 'test_' or affix '_test', it can be identificated as a test method.
