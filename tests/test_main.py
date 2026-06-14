from python_upskilling import greet


def test_greet_returns_expected_message() -> None:
    assert greet("Tester") == "Hello, Tester! Welcome to python-upskilling."
