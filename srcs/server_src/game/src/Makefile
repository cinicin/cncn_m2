#####################################################
#	CNCN Metin2 Mainline Server Binary MakeFile	#
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
BIN_TITLE = game
BIN = $(BIN_DIR)/$(BIN_TITLE)

#OBJE KLASORU YOKSA OLUSTURALIM
$(shell if [ ! -d $(OBJ_DIR) ]; then mkdir $(OBJ_DIR); fi)
#DAYANAK DOSYASI OLMAMA IHTIMALINE KONTROL KOYALIM.
$(shell if [ ! -e Depend ]; then touch Depend; fi)

CFLAGS += -g
CFLAGS += -ggdb
CFLAGS += -DNDEBUG
CFLAGS += -w	#Uyarıları ekrana basmayı engeller geliştirme yaparken kaldırın.
CFLAGS += -Wall
CFLAGS += -m32
CFLAGS += -O2
CFLAGS += -pipe
CFLAGS += -fexceptions
CFLAGS += -D_THREAD_SAFE
CFLAGS += -fstack-protector-all
CFLAGS += -std=c++2a
CFLAGS += -DBOOST_ERROR_CODE_HEADER_ONLY
CFLAGS += -ferror-limit=1


INC_DIR += -I../../../harici/boost_1_75_0
INC_DIR += -I../../../harici/devIL_1_80
INC_DIR += -I../../../harici/mysql_8_22
INC_DIR += -I../../../harici/cryptopp_8_20
INC_DIR += -I../../liblua/include
INC_DIR += -I/usr/local/include

LIB_DIR += -L../../../harici/bsd_libs
LIB_DIR += -L/usr/local/lib/mysql
LIB_DIR += -L/usr/local/lib

LIBS += -pthread
LIBS += -lm
LIBS += -lmd
LIBS += -lIL
LIBS += -lpng
LIBS += -ltiff
LIBS += -lmng
LIBS += -llcms
LIBS += -ljpeg
LIBS += -lmysqlclient
LIBS += -lz
LIBS += -lcryptopp
LIBS += -lthecore
LIBS += -lpoly
LIBS += -llua
LIBS += -llualib
LIBS += -lsql
LIBS += -lgame

C_FILE = \
	minilzo.c\

CPP_FILE = \
			BattleArena.cpp\
			FSM.cpp\
			MarkConvert.cpp\
			MarkImage.cpp\
			MarkManager.cpp\
			OXEvent.cpp\
			TrafficProfiler.cpp\
			ani.cpp\
			arena.cpp\
			banword.cpp\
			battle.cpp\
			blend_item.cpp\
			block_country.cpp\
			buffer_manager.cpp\
			building.cpp\
			castle.cpp\
			char.cpp\
			char_affect.cpp\
			char_battle.cpp\
			char_change_empire.cpp\
			char_horse.cpp\
			char_item.cpp\
			char_manager.cpp\
			char_quickslot.cpp\
			char_resist.cpp\
			char_skill.cpp\
			char_state.cpp\
			PetSystem.cpp\
			cmd.cpp\
			cmd_emotion.cpp\
			cmd_general.cpp\
			cmd_gm.cpp\
			cmd_oxevent.cpp\
			config.cpp\
			constants.cpp\
			crc32.cpp\
			cube.cpp\
			db.cpp\
			desc.cpp\
			desc_client.cpp\
			desc_manager.cpp\
			desc_p2p.cpp\
			dev_log.cpp\
			dungeon.cpp\
			empire_text_convert.cpp\
			entity.cpp\
			entity_view.cpp\
			event.cpp\
			event_queue.cpp\
			exchange.cpp\
			file_loader.cpp\
			fishing.cpp\
			gm.cpp\
			guild.cpp\
			guild_manager.cpp\
			guild_war.cpp\
			horse_rider.cpp\
			horsename_manager.cpp\
			input.cpp\
			input_auth.cpp\
			input_db.cpp\
			input_login.cpp\
			input_main.cpp\
			input_p2p.cpp\
			input_teen.cpp\
			input_udp.cpp\
			ip_ban.cpp\
			item.cpp\
			item_addon.cpp\
			item_attribute.cpp\
			item_manager.cpp\
			item_manager_idrange.cpp\
			locale.cpp\
			locale_service.cpp\
			log.cpp\
			login_data.cpp\
			lzo_manager.cpp\
			marriage.cpp\
			matrix_card.cpp\
			messenger_manager.cpp\
			mining.cpp\
			mob_manager.cpp\
			monarch.cpp\
			motion.cpp\
			over9refine.cpp\
			p2p.cpp\
			packet_info.cpp\
			party.cpp\
			passpod.cpp\
			pcbang.cpp\
			polymorph.cpp\
			priv_manager.cpp\
			pvp.cpp\
			questevent.cpp\
			questlua.cpp\
			questlua_affect.cpp\
			questlua_arena.cpp\
			questlua_ba.cpp\
			questlua_building.cpp\
			questlua_danceevent.cpp\
			questlua_dungeon.cpp\
			questlua_forked.cpp\
			questlua_game.cpp\
			questlua_global.cpp\
			questlua_guild.cpp\
			questlua_horse.cpp\
			questlua_pet.cpp\
			questlua_item.cpp\
			questlua_marriage.cpp\
			questlua_mgmt.cpp\
			questlua_monarch.cpp\
			questlua_npc.cpp\
			questlua_oxevent.cpp\
			questlua_party.cpp\
			questlua_pc.cpp\
			questlua_quest.cpp\
			questlua_target.cpp\
			questmanager.cpp\
			questnpc.cpp\
			questpc.cpp\
			refine.cpp\
			regen.cpp\
			safebox.cpp\
			sectree.cpp\
			sectree_manager.cpp\
			sequence.cpp\
			shop.cpp\
			skill.cpp\
			start_position.cpp\
			target.cpp\
			text_file_loader.cpp\
			trigger.cpp\
			utils.cpp\
			vector.cpp\
			war_map.cpp\
			wedding.cpp\
			xmas_event.cpp\
			panama.cpp\
			threeway_war.cpp\
			map_location.cpp\
			auth_brazil.cpp\
			BlueDragon.cpp\
			BlueDragon_Binder.cpp\
			DragonLair.cpp\
			questlua_dragonlair.cpp\
			skill_power.cpp\
			affect.cpp\
			SpeedServer.cpp\
			questlua_speedserver.cpp\
			auction_manager.cpp\
			FileMonitor_FreeBSD.cpp\
			ClientPackageCryptInfo.cpp\
			cipher.cpp\
			buff_on_attributes.cpp\
			dragon_soul_table.cpp\
			DragonSoul.cpp\
			group_text_parse_tree.cpp\
			char_dragonsoul.cpp\
			questlua_dragonsoul.cpp\
			shop_manager.cpp\
			shopEx.cpp\
			item_manager_read_tables.cpp\

C_OBJS = $(C_FILE:%.c=$(OBJ_DIR)/%.o)
CPP_OBJS = $(CPP_FILE:%.cpp=$(OBJ_DIR)/%.o)

MAIN_OBJ = $(OBJ_DIR)/main.o
MAIN_CPP = main.cpp

default:
	@clear
	@echo -e "\033[0;31m GAME BU SEKILDE DERLENEMEZ !!!\033[0m"
	@echo -e ""

cncn: clean_bin depend $(BIN)

cncn_c: clean depend $(BIN)

$(OBJ_DIR)/minilzo.o: minilzo.c
	@$(CC) $(CFLAGS) $(INC_DIR) -c $< -o $@
	@echo -e "\033[32mDERLENIYOR \033[0m" $<

$(OBJ_DIR)/%.o: %.cpp
	@echo -e "\033[32mDERLENIYOR \033[0m" $<
	@$(CC) $(CFLAGS) $(INC_DIR) -c $< -o $@

$(BIN): $(CPP_OBJS) $(C_OBJS) $(MAIN_OBJ)
	@echo -e "\033[32mBIRLESTIRILIYOR \033[0m" $(BIN_NAME)
	@$(CC) $(CFLAGS) $(LIB_DIR) $(C_OBJS) $(CPP_OBJS) $(MAIN_OBJ) $(LIBS) -o $(BIN) -g

clean_bin:
	@rm -f $(BIN)

clean:
	@rm -f $(C_OBJS) $(CPP_OBJS) $(MAIN_OBJ) $(BIN) Depend

depend:
	@makedepend -f Depend $(INC_DIR) -I/usr/include/c++/3.3 -I/usr/include/c++/4.2 -p$(OBJ_DIR)/ $(CPP_FILE) $(C_FILE) $(MAIN_CPP) 2> /dev/null > Depend

sinclude Depend
