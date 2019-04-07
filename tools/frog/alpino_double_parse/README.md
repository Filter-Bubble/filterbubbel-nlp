
run frog normally to get the full parse
frog -n <input> > <output>

run frog wiht --skip=mt to get the bare parse:
 * no multiword units
 * no (re-)tokenization

frog --skip=mt -n <input> > <output>
