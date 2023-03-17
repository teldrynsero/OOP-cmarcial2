all: mypy_test test run uml docs cover
		@echo "All finished"

run:
		@cat data/data.in | python main.py | diff - data/data.ans || true
		@echo "Program worked on sample data"

mypy_test:
		mypy main.py
		mypy fraction.py
		@echo "All mypy tests passed"

test:
		pytest test_main.py
		pytest test_fraction.py

		@echo "All unittest cases passed"

uml:
		java -jar "C:\Users\kayle\.vscode\extensions\jebbs.plantuml-2.17.5\plantuml.jar" uml/main.plantuml
		java -jar "C:\Users\kayle\.vscode\extensions\jebbs.plantuml-2.17.5\plantuml.jar" uml/solution.plantuml
		java -jar "C:\Users\kayle\.vscode\extensions\jebbs.plantuml-2.17.5\plantuml.jar" uml/fraction.plantuml
		@echo "UML documentation added to uml folder"

docs:
		pdoc -o docs main.py fraction.py
		@echo "HTML documentation added to docs folder"

cover:
		coverage run -m pytest test_main.py test_fraction.py
		coverage report
		coverage html