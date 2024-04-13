CC=gcc
CFLAGS := -Wall -O2

da65ify: da65ify.o src/patch_segment_py.c
	$(CC) $< -o $@ $(LDFLAGS)

src/patch_segment_py.c: patch_segment.py
	xxd -i $< > $@

%.o: src/%.c
	$(CC) $(CFLAGS) -c $< -o $@
