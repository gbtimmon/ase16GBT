import utest
__name__ = "Peng Wang"

def is_equal(x, y):
	return x == y

@utest.ok
def _okwho():
	"""test case is from wang.py"""
	assert is_equal("Peng Wang", __name__), "test failed in wang.py"
