N=12

all::
	gcc -o fibiter -O3 fibiter.c
	gcc -o fibrec -O3 fibrec.c
	gcc -fPIC -shared -o libfib.so libfib.c
	-javac fibiter.java
	-javac fibrec.java
	# dx --dex --no-strict --output=classes.dex . # android
	# jar fib.jar classes.dex # android
	-jar -cf fib.jar *.class

fib::
	time python3 fibiter.py $N
	time python3 fibrec.py $N
	time python3 cfib.py $N
	-time java -jar fib.jar fibiter $N
	-time java -jar fib.jar fibrec $N
	time ./fibiter $N
	time ./fibrec $N

test:: all
	bash -c "time sh fibrec.sh 12; read x"
	bash -c "time sh fibrec.sh 18; read x"
	bash -c "time python3 fibrec.py 18; read x"
	bash -c "time python3 fibrec.py 35; read x"
	bash -c "time python3 cfib.py 35; read x"
	bash -c "time java fibrec 35; read x"
	bash -c "time java fibrec 42; read x"
	bash -c "time ./fibrec 42; read x"
	bash -c "time ./fibrec 45; read x"
	bash -c "time sh fibiter.sh 45; read x"
	bash -c "time python3 fibiter.py 45; read x"
	bash -c "time java fibiter 45; read x"
	bash -c "time ./fibiter 45"

clean::
	rm -f fibiter fibrec *.class *.jar classes.dex libfib.so
