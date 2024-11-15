#! /bin/sh
fib() {
	local a b n
#	echo "FIB($1)"
	n=$1
	a=0
	b=1
	while [ $n -gt 1 ]; do
		c=`expr $a + $b`
		a=$b
		b=$c
		n=`expr $n - 1`
		#echo $c
	done
	return $c
}

n=2
if [ $# -eq 1 ]; then n=$1; fi
fib $n
echo "fib($n)=$?"
