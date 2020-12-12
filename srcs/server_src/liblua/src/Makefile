LUA = ..

include $(LUA)/config

OBJS = \
	lapi.o\
	lcode.o\
	ldebug.o\
	ldo.o\
	ldump.o\
	lfunc.o\
	lgc.o\
	llex.o\
	lmem.o\
	lobject.o\
	lopcodes.o\
	lparser.o\
	lstate.o\
	lstring.o\
	ltable.o\
	ltests.o\
	ltm.o\
	lundump.o\
	lvm.o\
	lzio.o\

SRCS = \
	lapi.c\
	lcode.c\
	ldebug.c\
	ldo.c\
	ldump.c\
	lfunc.c\
	lgc.c\
	llex.c\
	lmem.c\
	lobject.c\
	lopcodes.c\
	lparser.c\
	lstate.c\
	lstring.c\
	ltable.c\
	ltests.c\
	ltm.c\
	lundump.c\
	lvm.c\
	lzio.c\
	lapi.h\
	lcode.h\
	ldebug.h\
	ldo.h\
	lfunc.h\
	lgc.h\
	llex.h\
	llimits.h\
	lmem.h\
	lobject.h\
	lopcodes.h\
	lparser.h\
	lstate.h\
	lstring.h\
	ltable.h\
	ltm.h\
	lundump.h\
	lvm.h\
	lzio.h\

BIN_DIR = ../../../harici/bsd_libs

BIN_TITLE = liblua.a
BIN = $(BIN_DIR)/$(BIN_TITLE)

cncn: clean_bin $(BIN)

cncn_c: clean $(BIN)


%.o: %.c
	@echo -e "\033[32mDERLENIYOR \033[0m" $<
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
