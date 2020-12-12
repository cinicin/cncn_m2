LUA = ../..

include $(LUA)/config

EXTRA_DEFS = $(POPEN) $(TMPNAM) $(DEGREES) $(LOADLIB)

OBJS = \
	lauxlib.o\
	lbaselib.o\
	ldblib.o\
	liolib.o\
	lmathlib.o\
	ltablib.o\
	lstrlib.o\
	loadlib.o\

SRCS = \
	lauxlib.c\
	lbaselib.c\
	ldblib.c\
	liolib.c\
	lmathlib.c\
	ltablib.c\
	lstrlib.c\
	loadlib.c\

BIN_DIR = ../../../../harici/bsd_libs

BIN_TITLE = liblualib.a
BIN = $(BIN_DIR)/$(BIN_TITLE)

cncn: clean_bin $(BIN)

cncn_c: clean $(BIN)


%.o: %.c
	@echo -e "\033[36mDERLENIYOR \033[0m" $<
	@$(CC) $(CFLAGS) $(INCDIR) -c $<





$(BIN): $(OBJS)
	@echo -e "\033[32mBIRLESTIRILIYOR\033[0m" $(BIN_TITLE)
	@$(AR) $@ $(OBJS)
	@$(RANLIB) $@

clean_bin:
	@rm -f $(BIN)

clean:
	@rm -f $(OBJS) $(BIN)

co:
	@co -q -f -M $(SRCS)

klean:	clean
	@rm -f $(SRCS)
