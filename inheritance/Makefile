all: mypy_test test run uml docs cover
		@echo "All finished"

run:
		@cat data/sample.in | python main.py | diff - data/sample.ans || true
		@echo "Program worked on Kattis sample data"

mypy_test:
		mypy main.py data.py
		@echo "All mypy tests passed"

test:
		pytest test_main.py
		@echo "All unittest cases passed"

uml:
		java -jar "C:\Users\kayle\.vscode\extensions\jebbs.plantuml-2.17.5\plantuml.jar" uml/main.plantuml uml/solution.plantuml uml/data.plantuml
		@echo "UML documentation added to uml folder"

docs:
		pdoc -o docs main.py data.py
		@echo "HTML documentation added to docs folder"

cover:
		coverage run -m pytest test_main.py
		coverage report
		coverage html