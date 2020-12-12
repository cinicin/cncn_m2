#####################################################
#	CNCN Metin2 Mainline Database Cache MakeFile	#
#		Son Düzenleme: 12.12.2020					#
#####################################################
#	Bilgiler:										#
#		Degisken isimleri olarak lugata yerlesmis	#
#		atamalar yaptım kulak dolgunlugunuz olsun	#
#		DIR = DIRECTORY kısaltmasıdır				#.
#		BIN = BINARY kısaltmasıdır.					#
#		INC = INCLUDE kısaltmasıdır.				#
#		LIB = LIBRARY kısaltmasıdır.				#
#	Diğer önem arz eden bilgiler ilgili satırların.	#
#	yanında yorum olarak yazmakta.					#
#####################################################
CC = clang++-devel
OBJ_DIR = OBJDIR
BIN_DIR = ../../../../server/ayarlar
BIN_TITLE = db
BIN = $(BIN_DIR)/$(BIN_TITLE)

#OBJE KLASORU YOKSA OLUSTURALIM
$(shell if [ ! -d $(OBJ_DIR) ]; then mkdir $(OBJ_DIR); fi)
#DAYANAK DOSYASI OLMAMA IHTIMALINE KONTROL KOYALIM.
$(shell if [ ! -e Depend ]; then touch Depend; fi)

CFLAGS += -g
CFLAGS += -ggdb
CFLAGS += -DNDEBUG
CFLAGS += -w	#warningleri ekrana basmayı engeller.
CFLAGS += -m32
CFLAGS += -mtune=i686
CFLAGS += -fstack-protector
CFLAGS += -Wall
CFLAGS += -O2
CFLAGS += -fno-rtti
CFLAGS += -pipe
CFLAGS += -fno-exceptions
CFLAGS += -D_THREAD_SAFE
CFLAGS += -std=c++2a

INC_DIR += -I../../../harici/boost_1_75_0
INC_DIR += -I../../../harici/mysql_8_22

LIB_DIR += -L../../../harici/bsd_libs
LIB_DIR += -L/usr/local/lib/mysql

LIBS += -lmysqlclient
LIBS += -lthecore
LIBS += -lpoly
LIBS += -lz
LIBS += -lsql
LIBS += -lgame
LIBS += -pthread
LIBS += -lm

SRCS = \
	Config.cpp\
	NetBase.cpp\
	Peer.cpp\
	PeerBase.cpp\
	Main.cpp\
	Lock.cpp\
	DBManager.cpp\
	Cache.cpp\
	LoginData.cpp\
	ClientManager.cpp\
	ClientManagerPlayer.cpp\
	ClientManagerLogin.cpp\
	ClientManagerBoot.cpp\
	ClientManagerParty.cpp\
	ClientManagerGuild.cpp\
	GuildManager.cpp\
	HB.cpp\
	PrivManager.cpp\
	MoneyLog.cpp\
	ItemAwardManager.cpp\
	ClientManagerEventFlag.cpp\
	Marriage.cpp\
	Monarch.cpp\
	BlockCountry.cpp\
	ItemIDRangeManager.cpp\
	ClientManagerHorseName.cpp\
	AuctionManager.cpp\
	ProtoReader.cpp\
	CsvReader.cpp\

OBJS = $(SRCS:%.cpp=$(OBJ_DIR)/%.o)

default:
	@clear
	@echo -e "\033[31m DB BU SEKILDE DERLENEMEZ !!!\033[0m"
	@echo -e ""

cncn: clean_bin depend $(BIN)

cncn_c: clean depend $(BIN)

$(BIN): $(OBJS)
	@echo -e "\033[32mBIRLESTIRILIYOR \033[0m" $(BIN_TITLE)
	@$(CC) $(CFLAGS) $(LIB_DIR) $(OBJS) $(LIBS) -o $(BIN)


$(OBJ_DIR)/%.o: %.cpp
	@echo -e "\033[32mDERLENIYOR\033[0m" $<
	@$(CC) $(CFLAGS) $(INC_DIR) -c $< -o $@

clean_bin:
	@rm -f $(BIN)

clean:
	@rm -f $(OBJS) $(BIN)

depend:
	@touch Depend
	@makedepend -fDepend $(INC_DIR) -I/usr/include/c++/3.3 -I/usr/include/c++/4.2 -p$(OBJ_DIR)/ $(SRCS) 2> /dev/null


sinclude Depend
