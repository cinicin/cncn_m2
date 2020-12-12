#TR######################################################################
#	CNCN Metin2 Mainline LibSQL MakeFile								#
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
BIN_TITLE = libsql.a
BIN = $(BIN_DIR)/$(BIN_TITLE)

$(shell if [ ! -e Depend ]; then touch Depend; fi)

INC_DIR = -I../include

INC_DIR += -I../../harici/mysql_8_22

CFLAGS += -w
CFLAGS += -Wall
CFLAGS += -O2
CFLAGS += -pipe
CFLAGS += -D_GLIBCXX_USE_CXX11_ABI=1
CFLAGS += -fno-exceptions
CFLAGS += -D_THREAD_SAFE
CFLAGS += -m32
CFLAGS += -mtune=i686
CFLAGS += -fstack-protector
CFLAGS += -std=c++2a

OBJFILES = AsyncSQL.o Semaphore.o Tellwait.o Statement.o

default:
	@clear
	@echo -e "\033[31mLIBSQL BU SEKILDE DERLENEMEZ !!! \033[0m"
	@echo -e ""

cncn: depend
	@$(MAKE) -s $(BIN)

$(BIN): $(OBJFILES)
	@echo -e "\033[32mBIRLESTIRILIYOR \033[0m" $(BIN_TITLE)
	@ar cru $(BIN) $(OBJFILES) $(LIBS)
	@ranlib $(BIN)
	@chmod 700 $(BIN)

clean:
	@rm -f *.o $(BIN)

depend:
	@$(CC) $(CFLAGS) $(INC_DIR) -MM *.cpp > Depend

$(OBJFILES):
	@echo -e "\033[32mDERLENIYOR \033[0m" $<
	@$(CC) $(CFLAGS) $(INC_DIR) -c $<

include Depend
