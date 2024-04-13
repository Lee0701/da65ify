CC=gcc
CFLAGS := -Wall -O2

all: gen da65ify

da65ify: da65ify.o
	$(CC) $< -o $@ $(LDFLAGS)

gen: gen/patch_segment_py.c

gen/patch_segment_py.c: patch_segment.py | gen_dir
	xxd -i $< > $@

%.o: src/%.c | gen_dir
	$(CC) $(CFLAGS) -c $< -o $@

gen_dir:
	@mkdir -p gen
