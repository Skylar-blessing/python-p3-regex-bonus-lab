import re

my_pattern = r"It's such a lovely day today."
my_regex = re.compile(my_pattern)

def test_my_regex():
    assert my_regex.match("It's such a lovely day today.")

    # Add the following test case
    assert my_regex.fullmatch("Some weather we're having today, huh?")

if __name__ == "__main__":
    test_my_regex()
