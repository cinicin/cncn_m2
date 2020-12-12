#################################################
# CNCN M2 Server Shell Script					#
# Son Düzenleme: 12.12.2020						#
#################################################
#!/bin/sh
PROCESSOR=2
LOCALE="turkey"
#################################################################################
# BN short for BASE NAME
# FN short for FOLDER NAME
CHANNEL_BN="kanal"
CORE_BN="c"
CONFIG_BN="ayar"
SERVER_FN="server"
SRCS_FN="srcs"
EXTERN_FN="harici"
SETTINGS_FN="ayarlar"
DATAS_FN="dosyalar"
CHANNELS_FN="kanallar"
LOGS_FN="loglar"
SERVER_SRC_FN="server_src"
CONFIG_BN="ayar"
#################################################################################
#	ASSIGNMENTS DONT TOUCH
# DIR short for DIRECTORY
YER=${PWD}
SERVER_DIR="${YER}/${SERVER_FN}"
SRCS_DIR="${YER}/${SRCS_FN}"
SETTINGS_DIR="${SERVER_DIR}/${SETTINGS_FN}"
DATAS_DIR="${SERVER_DIR}/${DATAS_FN}"
CHANNELS_DIR="${SERVER_DIR}/${CHANNELS_FN}"
LOGS_DIR="${SERVER_DIR}/${LOGS_FN}"
DATA_DIR="${DATAS_DIR}/data"
LOCALE_DIR="${DATAS_DIR}/locale"
MARK_DIR="${DATAS_DIR}/mark"
PACKAGE_DIR="${DATAS_DIR}/package"
SERVER_SRC_DIR=${SRCS_DIR}/${SERVER_SRC_FN}
LIBGAME_SRC_DIR=${SERVER_SRC_DIR}/libgame/src
LIBLUA_SRC_DIR=${SERVER_SRC_DIR}/liblua
LIBPOLY_SRC_DIR=${SERVER_SRC_DIR}/libpoly
LIBSQL_SRC_DIR=${SERVER_SRC_DIR}/libsql
LIBTHECORE_SRC_DIR=${SERVER_SRC_DIR}/libthecore/src
QC_SRC_DIR=${SERVER_SRC_DIR}/quest
GAME_SRC_DIR=${SERVER_SRC_DIR}/game/src
DB_SRC_DIR=${SERVER_SRC_DIR}/db/src
CRYPTOPP_SRC_DIR=${SRCS_DIR}/${EXTERN_FN}/cryptopp_8_20/cryptopp
#################################################################################
#	FUNCTIONS
print()#CNCN ECHO FUNCTION v0.1
{
	if [ ${1} -eq 8 ]; then
		echo -e "\e[${2}m\e[${3}m${4}\e[0m"
	else
		echo -e "\e[${2}m\e[${3}m${4}\c\e[0m"
		sleep 0.1
	fi
}
create_folder()
{
	if [ -d ${1}/${2} ]
	then
		print 1 33 7 "${2}" && print 1 39 0 "	KLASORU ZATEN	" && print 1 33 4 "${1}" && print 8 39 0 "	LOKASYONUNDA VAR !!!"
		CNCN=2
	else
		print 1 33 7 "${2}" && print 1 39 0 "	KLASORU	" && print 1 33 4 "${1}" && print 8 39 0 "	LOKASYONUNDA OLUSTURULDU..."
		cd ${1} && mkdir ${2}
		CNCN=8
	fi
	sleep 0.08
}
compile_source()
{
	if [ ${1} -eq 1 ];then
		cd ${LIBGAME_SRC_DIR} && gmake clean
		cd ${LIBGAME_SRC_DIR} && gmake depend
		cd ${LIBGAME_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 2 ];then
		cd ${LIBLUA_SRC_DIR} && gmake clean
		cd ${LIBLUA_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 3 ];then
		cd ${LIBPOLY_SRC_DIR} && gmake clean
		cd ${LIBPOLY_SRC_DIR} && gmake depend
		cd ${LIBPOLY_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 4 ];then
		cd ${LIBSQL_SRC_DIR} && gmake clean
		cd ${LIBSQL_SRC_DIR} && gmake depend
		cd ${LIBSQL_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 5 ];then
		cd ${LIBTHECORE_SRC_DIR} && gmake clean
		cd ${LIBTHECORE_SRC_DIR} && gmake depend
		cd ${LIBTHECORE_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 6 ];then
		cd ${QC_SRC_DIR} && gmake clean
		cd ${QC_SRC_DIR} && gmake depend
		cd ${QC_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 7 ];then
		cd ${DB_SRC_DIR} && gmake clean
		cd ${DB_SRC_DIR} && gmake depend
		cd ${DB_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 8 ];then
		cd ${GAME_SRC_DIR} && gmake clean
		cd ${GAME_SRC_DIR} && gmake depend
		cd ${GAME_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 88 ];then
		cd ${CRYPTOPP_SRC_DIR} && gmake clean
		cd ${CRYPTOPP_SRC_DIR} && gmake depend
		cd ${CRYPTOPP_SRC_DIR} && gmake cncn -j${PROCESSOR}

	fi
}
setup_folder_structure()
{
	clear
	create_folder ${YER} ${SERVER_FN}
	create_folder ${SERVER_DIR} ${CHANNELS_FN}
	create_folder ${SERVER_DIR} ${DATAS_FN}
	create_folder ${DATAS_DIR} package
	create_folder ${SERVER_DIR} ${SETTINGS_FN}
	create_folder ${SERVER_DIR} ${LOGS_FN}
	create_folder ${CHANNELS_DIR} ${CHANNEL_BN}_test
	create_folder ${CHANNELS_DIR} ${CHANNEL_BN}_auth
	create_folder ${CHANNELS_DIR} ${CHANNEL_BN}_db
	for i in 1 2 3 4; do
		create_folder ${CHANNELS_DIR} ${CHANNEL_BN}_${i}
	done
	create_folder ${CHANNELS_DIR} ${CHANNEL_BN}_99
	for i in 1 2 3 4; do
		create_folder ${CHANNELS_DIR}/${CHANNEL_BN}_${i} ${CORE_BN}_1
		create_folder ${CHANNELS_DIR}/${CHANNEL_BN}_${i} ${CORE_BN}_2
		create_folder ${CHANNELS_DIR}/${CHANNEL_BN}_${i} ${CORE_BN}_3
		create_folder ${CHANNELS_DIR}/${CHANNEL_BN}_${i} ${CORE_BN}_4
		create_folder ${CHANNELS_DIR}/${CHANNEL_BN}_${i} ${CORE_BN}_5
	done
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_test
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_db
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_auth
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_99
	for i in 1 2 3 4; do
		create_folder ${LOGS_DIR} ${CHANNEL_BN}_${i}_${CORE_BN}_1
		create_folder ${LOGS_DIR} ${CHANNEL_BN}_${i}_${CORE_BN}_2
		create_folder ${LOGS_DIR} ${CHANNEL_BN}_${i}_${CORE_BN}_3
		create_folder ${LOGS_DIR} ${CHANNEL_BN}_${i}_${CORE_BN}_4
		create_folder ${LOGS_DIR} ${CHANNEL_BN}_${i}_${CORE_BN}_5
	done
	for a in 1 2 3 4; do
		for i in 1 2 3 4 5; do
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && rm -rf CONFIG
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && ln -s ../../../${SETTINGS_FN}/${CONFIG_BN}_${CHANNEL_BN}_${a}_${CORE_BN}_${i} CONFIG
			print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}-${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "CONFIG	" && print 8 39 0 "SEMBOLIK BAGLANTISI OLUSTURULDU..."
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && rm -rf game_${CHANNEL_BN}_${a}_${CORE_BN}_${i}
			cd  ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && ln -s ../../../${SETTINGS_FN}/game game_${CHANNEL_BN}_${a}_${CORE_BN}_${i}
			print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}-${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "game	" && print 8 39 0 "SEMBOLIK BAGLANTISI OLUSTURULDU..."
		done
	done
	for a in 1 2 3 4; do
		for i in 1 2 3 4 5; do
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && rm -rf locale
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && ln -s ../../../${DATAS_FN}/locale locale
			print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "locale	" && print 8 39 0 "SEMBOLIK BAGLANTISI OLUSTURULDU..."
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && rm -rf data
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && ln -s ../../../${DATAS_FN}/data data
			print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "data	" && print 8 39 0 "SEMBOLIK BAGLANTISI OLUSTURULDU..."
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && rm -rf mark
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && ln -s ../../../${DATAS_FN}/mark mark
			print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "mark	" && print 8 39 0 "SEMBOLIK BAGLANTISI OLUSTURULDU..."
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && rm -rf package
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && ln -s ../../../${DATAS_FN}/package package
			print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "package	" && print 8 39 0 "SEMBOLIK BAGLANTISI OLUSTURULDU..."
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && rm -rf log
			cd ${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i} && ln -s ../../../${LOGS_FN}/${CHANNEL_BN}_${a}_${CORE_BN}_${i} log
			print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${a}/${CORE_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "log	" && print 8 39 0 "SEMBOLIK BAGLANTISI OLUSTURULDU..."
		done
	done
	for i in test 99 auth; do
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && rm -rf log
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && ln -s ../../${LOGS_FN}/${CHANNEL_BN}_${i} log
		print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "log	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && rm -rf CONFIG
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && ln -s ../../${SETTINGS_FN}/${CONFIG_BN}_${CHANNEL_BN}_${i} CONFIG
		print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "CONFIG	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && rm -rf package
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && ln -s ../../${DATAS_FN}/package package
		print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "package	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && rm -rf data
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && ln -s ../../${DATAS_FN}/data data
		print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "data	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && rm -rf locale
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && ln -s ../../${DATAS_FN}/locale locale
		print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "locale	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && rm -rf mark
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && ln -s ../../${DATAS_FN}/mark mark
		print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "mark	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && rm -rf game_${CHANNEL_BN}_${i}
		cd ${CHANNELS_DIR}/${CHANNEL_BN}_${i} && ln -s ../../${SETTINGS_FN}/game game_${CHANNEL_BN}_${i}
		print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_${i}" && print 1 39 0 "	ICINDE	" && print 1 32 4 "game	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
	done
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && rm -rf db
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && ln -s ../../${SETTINGS_FN}/db db
	print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_db" && print 1 39 0 "	ICINDE	" && print 1 32 4 "db	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && rm -rf CONFIG
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && ln -s ../../${SETTINGS_FN}/${CONFIG_BN}_${CHANNEL_BN}_db CONFIG
	print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_db" && print 1 39 0 "	ICINDE	" && print 1 32 4 "CONFIG	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && rm -rf log
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && ln -s ../../${LOGS_FN}/${CHANNEL_BN}_db log
	print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_db" && print 1 39 0 "	ICINDE	" && print 1 32 4 "log	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && rm -rf item_proto.txt
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && ln -s ../../${SETTINGS_FN}/item_proto.txt item_proto.txt
	print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_db" && print 1 39 0 "	ICINDE	" && print 1 32 4 "item_proto.txt	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && rm -rf item_names.txt
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && ln -s ../../${SETTINGS_FN}/item_names.txt item_names.txt
	print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_db" && print 1 39 0 "	ICINDE	" && print 1 32 4 "item_names.txt	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && rm -rf mob_proto.txt
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && ln -s ../../${SETTINGS_FN}/mob_proto.txt mob_proto.txt
	print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_db" && print 1 39 0 "	ICINDE	" && print 1 32 4 "mob_proto.txt	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && rm -rf mob_names.txt
	cd ${CHANNELS_DIR}/${CHANNEL_BN}_db && ln -s ../../${SETTINGS_FN}/mob_names.txt mob_names.txt
	print 1 33 7 "${CHANNELS_DIR}/${CHANNEL_BN}_db" && print 1 39 0 "	ICINDE	" && print 1 32 4 "mob_names.txt	" && print 8 39 0  "SEMBOLIK BAGLANTISI OLUSTURULDU..."
}
command_parser()
{
	parser_num=0
	for i in ${1}
	do
		parser_num=$((parser_num+1))
	done
	sleep 0.01
	if [ ${parser_num} -gt 9 ]; then
		print 8 31 31 "GECERSIZ KOMUT GIRISI YAPTINIZ !!!"
		print 8 31 31 "SCRIPT SONLANDIRILDI !!!"
	exit
	fi
	COMMANDS=${1}

	while [ ${parser_num} -le 8 ]; do
		COMMANDS="${COMMANDS} cncn_null"
		parser_num=$((parser_num+1))
	done
	rtfi="cncn_null"
	rtfi_s="cncn_null"
	rtfi_c="cncn_null"
	for i in ${COMMANDS}
	do
		if [ ${i} = "cncn_null" ]; then sleep 0.01
		elif [ ${i} = "derle" ]; then rtfi="${rtfi} 1"
		elif [ ${i} = "Derle" ]; then rtfi="${rtfi} 1"
		elif [ ${i} = "compile" ]; then rtfi="${rtfi} 1"
		elif [ ${i} = "d" ]; then rtfi="${rtfi} 1"
		elif [ ${i} = "gmake" ]; then rtfi="${rtfi} 1"
		elif [ ${i} = "make" ]; then rtfi="${rtfi} 1"
		elif [ ${i} = "kurulum" ]; then rtfi="${rtfi} 4"
		elif [ ${i} = "setup" ]; then rtfi="${rtfi} 4"
#BASLAT
		elif [ ${i} = "baslat" ]; then rtfi="${rtfi} 2"
		elif [ ${i} = "start" ]; then rtfi="${rtfi} 2"
		elif [ ${i} = "b" ]; then rtfi="${rtfi} 2"
		elif [ ${i} = "Baslat" ]; then rtfi="${rtfi} 2"
		elif [ ${i} = "Start" ]; then rtfi="${rtfi} 2"
		elif [ ${i} = "ac" ]; then rtfi="${rtfi} 2"
		elif [ ${i} = "Ac" ]; then rtfi="${rtfi} 2"
#KAPAT
		elif [ ${i} = "kapat" ]; then rtfi="${rtfi} 3"
		elif [ ${i} = "kill" ]; then rtfi="${rtfi} 3"
		elif [ ${i} = "close" ]; then rtfi="${rtfi} 3"
		elif [ ${i} = "k" ]; then rtfi="${rtfi} 3"
		elif [ ${i} = "Close" ]; then rtfi="${rtfi} 3"
		elif [ ${i} = "Kapat" ]; then rtfi="${rtfi} 3"
#SRCS
		elif [ ${i} = "libgame" ]; then rtfi_s="${rtfi_s} 1"
		elif [ ${i} = "liblua" ]; then rtfi_s="${rtfi_s} 2"
		elif [ ${i} = "libpoly" ]; then rtfi_s="${rtfi_s} 3"
		elif [ ${i} = "libsql" ]; then rtfi_s="${rtfi_s} 4"
		elif [ ${i} = "libthecore" ]; then rtfi_s="${rtfi_s} 5"
		elif [ ${i} = "qc" ]; then rtfi_s="${rtfi_s} 6"
		elif [ ${i} = "db" ]; then rtfi_s="${rtfi_s} 7" && rtfi_c="${rtfi_c} db"
		elif [ ${i} = "game" ]; then rtfi_s="${rtfi_s} 8"
		elif [ ${i} = "all" ]; then rtfi_s="1 2 3 4 5 6 7 8" && rtfi_c="db auth 1 2 3 4 99"
		elif [ ${i} = "hepsi" ]; then rtfi_s="1 2 3 4 5 6 7 8" && rtfi_c="db auth 1 2 3 4 99"
		elif [ ${i} = "ymir" ]; then rtfi_s=" 1 2 3 4 5"
		elif [ ${i} = "lib" ]; then rtfi_s=" 1 2 3 4 5 88"
		elif [ ${i} = "cryptopp" ]; then rtfi_s=" 88"
# CHANNELS
		elif [ ${i} = "1" ]; then rtfi_c="${rtfi_c} 1"
		elif [ ${i} = "2" ]; then rtfi_c="${rtfi_c} 2"
		elif [ ${i} = "3" ]; then rtfi_c="${rtfi_c} 3"
		elif [ ${i} = "4" ]; then rtfi_c="${rtfi_c} 4"
		elif [ ${i} = "auth" ]; then rtfi_c="${rtfi_c} auth"
		elif [ ${i} = "99" ]; then rtfi_c="${rtfi_c} 99"
		elif [ ${i} = "test" ]; then rtfi_c="${rtfi_c} test"
		else
			print 8 33 33 "${i} KOMUTU BULUNAMADI !!!"
		fi
	done
	execute
}
kill_pid()
{
	PID_DIR="${CHANNELS_DIR}/${CHANNEL_BN}_${1}"
	if [ ${1} -eq ${1} ] 2>/dev/null
	then
		if [ ${1} -eq 99 ]; then
			PID="${PID_DIR}/pid"
			if [ -e ${PID} ]; then
				PID_VALUE=`cat ${PID}`
				if ps -p ${PID_VALUE} > /dev/null
				then
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 33 "KAPATILDI !!!"
					kill -9 ${PID_VALUE} > /dev/null 2> /dev/null & sleep 0.5
				else
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 39 0 "ZATEN KAPALI..."
				fi
			else
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 39 0 "ZATEN KAPALI..."
			fi
		else
			for t in 1 2 3 4 5
			do
				PID="${PID_DIR}/${CORE_BN}_${t}/pid"
				if [ -e ${PID} ]; then
					PID_VALUE=`cat ${PID}`
					if ps -p ${PID_VALUE} > /dev/null
					then
						print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${t}	" && print 8 33 33 "KAPATILDI !!!"
						kill -9 ${PID_VALUE} > /dev/null 2> /dev/null & sleep 0.5
					else
						print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${t}	" && print 8 39 0 "ZATEN KAPALI..."
					fi
				else
					print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${t}	" && print 8 39 0 "ZATEN KAPALI..."
				fi
			done

		fi
	else
		PID="${PID_DIR}/pid"
		if [ -e ${PID} ]; then
			PID_VALUE=`cat ${PID}`
			if ps -p ${PID_VALUE} > /dev/null
			then
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 33 "KAPATILDI !!!"
				kill -9 ${PID_VALUE} > /dev/null 2> /dev/null & sleep 0.5
			else
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 39 0 "ZATEN KAPALI..."
			fi
		else
			print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 39 0 "ZATEN KAPALI..."
		fi
	fi
}
start_pid()
{
	PID_DIR="${CHANNELS_DIR}/${CHANNEL_BN}_${1}"
	if [ ${1} -eq ${1} ] 2>/dev/null
	then
		if [ ${1} -eq 99 ]
		then
			PID="${PID_DIR}/pid"
			if [ -e ${PID} ]; then
				PID_VALUE=`cat ${PID}`
				if ps -p ${PID_VALUE} > /dev/null
				then
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 32 4 "ZATEN ACIK"
				else
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "BASLATILDI"
					cd ${PID_DIR} && ./game_${CHANNEL_BN}_${1} &
					sleep 2
				fi
			else
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "BASLATILDI"
				cd ${PID_DIR} && ./game_${CHANNEL_BN}_${1} &
				sleep 2
			fi
		else
			for y in 1 2 3 4 5
			do
				PID="${PID_DIR}/${CORE_BN}_${y}/pid"
				if [ -e ${PID} ]; then
					PID_VALUE=`cat ${PID}`
					if ps -p ${PID_VALUE} > /dev/null
					then
						print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${y}	" && print 8 32 4 "ZATEN ACIK"
					else
						print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${y}	" && print 8 33 4 "BASLATILDI"
						cd ${PID_DIR}/${CORE_BN}_${y} && ./game_${CHANNEL_BN}_${1}_${CORE_BN}_${y} &
						sleep 2
					fi
				else
					print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${y}	" && print 8 33 4 "BASLATILDI"
					cd ${PID_DIR}/${CORE_BN}_${y} && ./game_${CHANNEL_BN}_${1}_${CORE_BN}_${y} &
					sleep 2
				fi
			done
		fi
	else
		if [ ${1} = "db" ]; then
			PID="${PID_DIR}/pid"
			if [ -e ${PID} ]; then
				PID_VALUE=`cat ${PID}`
				if ps -p ${PID_VALUE} > /dev/null
				then
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 32 4 "ZATEN ACIK"
				else
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "BASLATILDI"
					cd ${PID_DIR} && ./db &
					sleep 8
				fi
			else
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "BASLATILDI"
				cd ${PID_DIR} && ./db &
				sleep 8
			fi
		else
			PID="${PID_DIR}/pid"
			if [ -e ${PID} ]; then
				PID_VALUE=`cat ${PID}`
				if ps -p ${PID_VALUE} > /dev/null
				then
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 32 4 "ZATEN ACIK"
				else
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "BASLATILDI"
					cd ${PID_DIR} && ./game_${CHANNEL_BN}_${1} &
					sleep 2
				fi
			else
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "BASLATILDI"
				cd ${PID_DIR} && ./game_${CHANNEL_BN}_${1} &
				sleep 2
			fi
		fi
	fi
}
execute()
{
	# echo " rtfi = ${rtfi}"
	# echo " rtfi_s = ${rtfi_s}"
	# echo " rtfi_c = ${rtfi_c}"
	for a in ${rtfi}
	do
		if [ ${a} = "cncn_null" ]; then sleep 0.1
		elif [ ${a} -eq 1 ]; then
			for b in ${rtfi_s}
			do
				if [ ${b} = "cncn_null" ]; then sleep 0.1
				else
					compile_source ${b}
				fi
			done
		elif [ ${a} -eq 2 ]; then
			for b in ${rtfi_c}
			do
				if [ ${b} = "cncn_null" ]; then sleep 0.1
				else
					start_pid ${b}
				fi
			done
		elif [ ${a} -eq 3 ]; then
			for b in ${rtfi_c}
			do
				if [ ${b} = "cncn_null" ]; then sleep 0.1
				else
					kill_pid ${b}
				fi
			done
		elif [ ${a} -eq 4 ]; then
			setup_folder_structure
		fi
	done
}
#################################################################################
clear
echo -e "\e[32m                      -//:'            \e[0m"
echo -e "\e[32m                     -hhhhhh+           \e[0m"
echo -e "\e[32m                     shhhhhhh'          \e[0m"
echo -e "\e[32m                  .:ohddhhhy:           \e[0m"
echo -e "\e[32m               .oyhddddddd.             \e[0m"
echo -e "\e[32m              'yhhdddmmmddo             \e[0m"
echo -e "\e[32m              shhhh-mmmmddhyo:'         \e[0m"
echo -e "\e[32m             .hhhh:ommmdhdhhhhh/        \e[0m"
echo -e "\e[32m              .::..dmmmo '-/sso.    VERSIYON = 1.0.0    \e[0m"
echo -e "\e[32m                  +dddd.                \e[0m"
echo -e "\e[32m                 :hdddh/'               \e[0m"
echo -e "\e[32m               'shhddddhho.             \e[0m"
echo -e "\e[32m              :hhhhy:+hhhhhs:           \e[0m"
echo -e "\e[32m            .ohhhh+'  ':shhhho          \e[0m"
echo -e "\e[32m         -+yhhhhy-      .hhhh/          \e[0m"
echo -e "\e[32m      -+hhhhhho:'       +hhhy'          \e[0m"
echo -e "\e[32m    .hhhhhho-           hhhho           \e[0m"
echo -e "\e[32m    :hhhh-             -hhhhs'          \e[0m"
echo -e "\e[32m     -+/.              -yhhhy.          \e[0m"
echo -e "\e[32m                         '..            \e[0m"
echo -e "\e[32m KOMUT = \c[0m" && echo -e "\e[39m\c[0m"
read command
clear
command_parser "${command}"
