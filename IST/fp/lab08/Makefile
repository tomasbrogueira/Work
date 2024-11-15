all::
	for i in ex*.py; do pyreverse $$i -o puml -p `basename $$i`; done
png::
	for i in ex*.py; do pyreverse $$i -o png -p `basename $$i`; done
clean::
	rm -f classes_*.puml classes_*.png
