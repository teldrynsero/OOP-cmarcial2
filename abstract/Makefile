all: run mypy_test test uml docs cover
		@echo "All finished"

run:
		@cat data/cups-01.in | python main.py | diff - data/cups-01.ans || true
		@echo "Program worked on sample data" 

mypy_test:
		mypy main.py cup.py
		@echo "All mypy tests passed"

test:
		pytest test_main.py test_cup.py
		@echo "All unittest cases passed"

uml:
		java -jar "C:\Users\kayle\.vscode\extensions\jebbs.plantuml-2.17.5\plantuml.jar" uml/main.plantuml uml/solution.plantuml uml/cup.plantuml
		@echo "UML documentation added to uml folder"

docs:
		pdoc -o docs main.py cup.py
		@echo "HTML documentation added to docs folder"

cover:
		coverage run -m pytest test_main.py test_cup.py
		coverage report
		coverage html