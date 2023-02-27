all: run mypy_test test
	@echo "All finished"

run:
	@cat data/m0000.in | python main.py | diff - data/m0000.ans || true
	@cat data/m0001.in | python main.py | diff - data/m0001.ans || true
	@cat data/m0002.in | python main.py | diff - data/m0002.ans || true
	@cat data/m0003.in | python main.py | diff - data/m0003.ans || true
	@cat data/m0004.in | python main.py | diff - data/m0004.ans || true
	@cat data/m0005.in | python main.py | diff - data/m0005.ans || true
	@echo "All kattis sample test data test done!"

mypy_test:
		mypy morse.py
		mypy main.py
		@echo "All mypy tests passed!"

test:
	pytest test_solution.py
	pytest test_morse.py
	@echo "All unittest cases passed!"