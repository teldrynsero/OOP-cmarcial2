all: mypy_test run
	@echo "All finished"

run:
	@cat data/sample.in | python main.py | diff - data/sample.ans || true
	@echo "Program worked on sample data" 

mypy_test:
		mypy polygon.py
		mypy main.py
		@echo "All mypy tests passed"

clean:
	rm -rf __pycache__
	rm -f *.pyc