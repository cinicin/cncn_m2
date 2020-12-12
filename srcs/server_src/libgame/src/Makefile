#TR######################################################################
#	CNCN Metin2 Mainline LibGame MakeFile								#
#	Son Düzenleme: 28.11.2020											#
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

BIN_DIR = ../../../harici/bsd_libs
BIN_TITLE = libgame.a
BIN = $(BIN_DIR)/$(BIN_TITLE)

$(shell if [ ! -e Depend ]; then touch Depend; fi)

INC_DIR = -I../include

CFLAGS += -w
CFLAGS += -Wall
CFLAGS += -O2
CFLAGS += -pipe
CFLAGS += -fno-exceptions
CFLAGS += -m32
CFLAGS += -mtune=i686
CFLAGS += -fstack-protector
CFLAGS += -std=c++2a

OBJFILES = \
	grid.o\
	attribute.o\
	targa.o\

default:
	@clear
	@echo -e "\033[31mLIBGAME BU SEKILDE DERLENEMEZ !!!\033[0m"
	@echo -e ""

cncn: depend $(BIN)

$(BIN): $(OBJFILES)
	@echo -e "\033[32mBIRLESTIRILIYOR \033[0m" $(BIN_TITLE)
	@ar cru $(BIN) $(OBJFILES) $(LIBS)
	@ranlib $(BIN)
	@chmod 700 $(BIN)

clean:
	@rm -f *.o $(BIN)

depend:
	@$(CC) $(CFLAGS) $(INC_DIR) -MM *.cc > Depend

$(OBJFILES):
	@echo -e "\033[32mDERLENIYOR \033[0m" $<
	@$(CC) $(CFLAGS) $(INC_DIR) -c $<

include Depend
