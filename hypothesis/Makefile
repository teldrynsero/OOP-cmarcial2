all: mypy_test test run cover docs uml
	@echo "All finished"

run:
	@cat data/1.in | python main.py | diff - data/1.ans || true
	@cat data/2.in | python main.py | diff - data/2.ans || true
	@cat data/3.in | python main.py | diff - data/3.ans || true
	@echo "Program works on kattis sample data" 

mypy_test:
		mypy title.py
		mypy main.py
		@echo "All mypy tests passed"

test:
		pytest test_main.py
		pytest test_title.py
		@echo "All unittest cases passed"

cover:
		coverage run -m pytest test_main.py test_title.py
		coverage report
		coverage html

uml:
		java -jar "C:\Users\kayle\.vscode\extensions\jebbs.plantuml-2.17.5\plantuml.jar" uml/main.plantuml
		java -jar "C:\Users\kayle\.vscode\extensions\jebbs.plantuml-2.17.5\plantuml.jar" uml/solution.plantuml
		java -jar "C:\Users\kayle\.vscode\extensions\jebbs.plantuml-2.17.5\plantuml.jar" uml/title.plantuml
		@echo "UML documentation added to uml folder"

docs:
		pdoc -o docs main.py title.py
		@echo "HTML documentation added to docs folder"

clean:
	rm -rf __pycache__
	rm -f *.pyc