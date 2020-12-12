#TR######################################################################
#	CNCN Metin2 Mainline LibPoly MakeFile								#
#	Son Düzenleme: 12.12.2020											#
#																		#
#	İletişim:															#
#		TurkMMO:	https://forum.turkmmo.com/uye/1108698-cinicin/		#
#		Discord:	CNCN#5381											#
#		Githup:		https://github.com/cinicin							#
#EN######################################################################
#	İletişim = Contact													#
#	Son Düzenleme = last revision date									#
#########################################################################
CC = clang++-devel

BIN_DIR = ../../harici/bsd_libs
BIN_TITLE = libpoly.a
BIN = $(BIN_DIR)/$(BIN_TITLE)

$(shell if [ ! -e Depend ]; then touch Depend; fi)

CFLAGS += -w
CFLAGS += -Wall
CFLAGS += -O2
CFLAGS += -pipe
CFLAGS += -fno-exceptions
CFLAGS += -m32
CFLAGS += -mtune=i686
CFLAGS += -fstack-protector
CFLAGS += -D_GLIBCXX_USE_CXX11_ABI=1
CFLAGS += -std=c++2a
CFLAGS += -fno-rtti

OBJFILES = Base.o Poly.o SymTable.o Symbol.o

default:
	@clear
	@echo -e "\033[31m LIBPOLY BU SEKILDE DERLENEMEZ !!!\033[0m"
	@echo -e ""

cncn: depend $(BIN)

cncn_c: clean depend $(BIN)

$(BIN): $(OBJFILES)
	@echo -e "\033[32mBIRLESTIRILIYOR \033[0m" $(BIN_TITLE)
	@ar cru $(BIN) $(OBJFILES) $(LIBS)
	@ranlib $(BIN)
	@chmod 700 $(BIN)

clean:
	@rm -f *.o $(BIN)

depend:
	@touch Depend
	@$(CC) $(CFLAGS) -MM *.cc > Depend

$(OBJFILES):
	@echo -e "\033[36mDERLENIYOR \033[0m" $<
	@$(CC) $(CFLAGS) -c $<

include Depend
