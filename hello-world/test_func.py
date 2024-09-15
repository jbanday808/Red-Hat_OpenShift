import unittest

func = __import__("func")

class TestFunc(unittest.TestCase):

    def test_func_empty_request(self):
        # Call the main function and capture the response and status code
        resp, code = func.main({})
        print(f"Response: {resp}, Status Code: {code}")  # Add this print statement for debugging
        # Check if the response is "Hello World!"
        self.assertEqual(resp, "Hello World!")
        # Check if the status code is 200
        self.assertEqual(code, 200)

if __name__ == "__main__":
    unittest.main()