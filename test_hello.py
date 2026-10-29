from hello import greet

def test_greet():
    result = greet()
    print("Test output:", result)
    assert result == "Hello, World!"