#TR######################################################################
#	CNCN Metin2 Mainline QC MakeFile							#
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
MAKE = clang++-devel

BIN_DIR = ../../../server/dosyalar/locale/turkey/quest
BIN_TITLE = qc
BIN = $(BIN_DIR)/$(BIN_TITLE)

CFLAGS += -g
CFLAGS += -ggdb
CFLAGS += -DNDEBUG
CFLAGS += -w

INC_DIR += -I../liblua/include
INC_DIR += -I../liblua/src
LIB_DIR += -L../../harici/bsd_libs

LIBS += -llua
LIBS += -llualib

default:
	@clear
	@echo -e "\033[31m QC BU SEKILDE DERLENEMEZ !!!\033[0m"
	@echo -e ""

cncn: clean qc.cc qc.o crc32.o
	@echo -e "\033[32mBIRLESTIRILIYOR \033[0m" $(BIN_TITLE)
	@$(MAKE) -g -o $(BIN) $(INC_DIR) $(LIB_DIR) qc.o crc32.o $(LIBS)

%.o: %.cc
	@echo -e "\033[36mDERLENIYOR \033[0m" $<
	@$(MAKE) $(CFLAGS) -c $< $(INC_DIR) $(LIB_DIR)

clean:
	@rm -f qc.o crc32.o $(BIN)
