#################################################
# CNCN M2 Server Shell Script					#
# Son Düzenleme: 19.12.2020						#
#################################################
#!/bin/sh
#################################################################################
# SCRIPT SETTINGS
LANGUAGE="tr" # `tr` or `en` also you can edit config.sh for adding your language.
PROCESSOR=2
#################################################################################
. config.sh
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
CRYPTOPP_SRC_DIR=${SRCS_DIR}/${EXTERN_FN}/cryptopp_8_30/cryptopp
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
		print 1 39 0 "${1}" && print 1 32 7 "	${2}	" && print 8 33 4 "${MSG_1}"
	else
		print 1 39 0 "${1}" && print 1 32 7 "	${2}	" && print 8 33 7 "${MSG_2}"
		cd ${1} && mkdir ${2}
	fi
	sleep 0.08
}
create_symlink()
{
	cd ${1} && rm -rf ${3}
	cd ${1} && ln -s ${2} ${3}
	print 1 39 0 "${1}" && print 1 32 7 "	${3}	" && print 8 33 7 "${MSG_3}"
	sleep 0.08
}
rename_it()
{
	cd ${1} && mv ${2} ${3}
	sleep 0.1
}
compile_source()
{
	if [ ${1} -eq 1 ];then
		print 1 33 4 "LIBGAME		" && print 8 32 7 "${MSG_9}"
		cd ${LIBGAME_SRC_DIR} && gmake depend
		cd ${LIBGAME_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 2 ];then
		print 1 33 4 "LIBLUA		" && print 8 32 7 "${MSG_9}"
		cd ${LIBLUA_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 3 ];then
		print 1 33 4 "LIBPOLY		" && print 8 32 7 "${MSG_9}"
		cd ${LIBPOLY_SRC_DIR} && gmake depend
		cd ${LIBPOLY_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 4 ];then
		print 1 33 4 "LIBSQL		" && print 8 32 7 "${MSG_9}"
		cd ${LIBSQL_SRC_DIR} && gmake depend
		cd ${LIBSQL_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 5 ];then
		print 1 33 4 "LIBTHECORE	" && print 8 32 7 "${MSG_9}"
		cd ${LIBTHECORE_SRC_DIR} && gmake depend
		cd ${LIBTHECORE_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 6 ];then
		print 1 33 4 "QC		" && print 8 32 7 "${MSG_9}"
		cd ${QC_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 7 ];then
		print 1 33 4 "DB		" && print 8 32 7 "${MSG_9}"
		cd ${DB_SRC_DIR} && gmake depend
		cd ${DB_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 8 ];then
		print 1 33 4 "GAME		" && print 8 32 7 "${MSG_9}"
		cd ${GAME_SRC_DIR} && gmake depend
		cd ${GAME_SRC_DIR} && gmake cncn -j${PROCESSOR}
	elif [ ${1} -eq 88 ];then
		print 1 33 4 "CRYPTOPP	" && print 8 32 7 "${MSG_9}"
		cd ${CRYPTOPP_SRC_DIR} && gmake depend
		cd ${CRYPTOPP_SRC_DIR} && gmake cncn -j${PROCESSOR}
	fi
}
clear_source()
{
	if [ ${1} -eq 1 ];then
		cd ${LIBGAME_SRC_DIR} && gmake clean
		print 1 33 4 "LIBGAME		" && print 8 32 7 "${MSG_8}"
	elif [ ${1} -eq 2 ];then
		cd ${LIBLUA_SRC_DIR} && gmake clean
		print 1 33 4 "LIBLUA		" && print 8 32 7 "${MSG_8}"
	elif [ ${1} -eq 3 ];then
		cd ${LIBPOLY_SRC_DIR} && gmake clean
		print 1 33 4 "LIBPOLY		" && print 8 32 7 "${MSG_8}"
	elif [ ${1} -eq 4 ];then
		cd ${LIBSQL_SRC_DIR} && gmake clean
		print 1 33 4 "LIBSQL		" && print 8 32 7 "${MSG_8}"
	elif [ ${1} -eq 5 ];then
		cd ${LIBTHECORE_SRC_DIR} && gmake clean
		print 1 33 4 "LIBTHECORE	" && print 8 32 7 "${MSG_8}"
	elif [ ${1} -eq 6 ];then
		cd ${QC_SRC_DIR} && gmake clean
		print 1 33 4 "QC		" && print 8 32 7 "${MSG_8}"
	elif [ ${1} -eq 7 ];then
		cd ${DB_SRC_DIR} && gmake clean
		print 1 33 4 "DB		" && print 8 32 7 "${MSG_8}"
	elif [ ${1} -eq 8 ];then
		cd ${GAME_SRC_DIR} && gmake clean
		print 1 33 4 "GAME		" && print 8 32 7 "${MSG_8}"
	elif [ ${1} -eq 88 ];then
		cd ${CRYPTOPP_SRC_DIR} && gmake clean
		print 1 33 4 "CRYPTOPP	" && print 8 32 7 "${MSG_8}"
	fi
}
setup_folder_structure()
{
	clear
	print 8 33 7 "${MSG_16}"
	rename_it ${SERVER_DIR} "dosyalar" ${DATAS_FN} 2>/dev/null
	rename_it ${SERVER_DIR} "ayarlar" ${SETTINGS_FN} 2>/dev/null
	rename_it ${SERVER_DIR} "datas" ${DATAS_FN} 2>/dev/null
	rename_it ${SERVER_DIR} "settings" ${SETTINGS_FN} 2>/dev/null
	cd ${SERVER_DIR} && rm -rf loglar 2>/dev/null
	cd ${SERVER_DIR} && rm -rf kanallar 2>/dev/null
	cd ${SERVER_DIR} && rm -rf logs 2>/dev/null
	cd ${SERVER_DIR} && rm -rf channels 2>/dev/null
	sleep 2
	create_folder ${YER} ${SERVER_FN}
	create_folder ${SERVER_DIR} ${CHANNELS_FN}
	create_folder ${SERVER_DIR} ${DATAS_FN}
	create_folder ${DATAS_DIR} package
	create_folder ${SERVER_DIR} ${SETTINGS_FN}
	create_folder ${SERVER_DIR} ${LOGS_FN}
	create_folder ${CHANNELS_DIR} ${CHANNEL_BN}_test
	create_folder ${CHANNELS_DIR} ${CHANNEL_BN}_auth
	create_folder ${CHANNELS_DIR} ${CHANNEL_BN}_db
	create_folder ${CHANNELS_DIR} ${CHANNEL_BN}_99
	for v in 1 2 3 4; do
	create_folder ${CHANNELS_DIR} ${CHANNEL_BN}_${v}
	done
	for v in 1 2 3 4; do
	create_folder ${CHANNELS_DIR}/${CHANNEL_BN}_${v} ${CORE_BN}_1
	create_folder ${CHANNELS_DIR}/${CHANNEL_BN}_${v} ${CORE_BN}_2
	create_folder ${CHANNELS_DIR}/${CHANNEL_BN}_${v} ${CORE_BN}_3
	create_folder ${CHANNELS_DIR}/${CHANNEL_BN}_${v} ${CORE_BN}_4
	create_folder ${CHANNELS_DIR}/${CHANNEL_BN}_${v} ${CORE_BN}_5
	done
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_test
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_db
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_auth
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_99
	for v in 1 2 3 4; do
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_${v}_${CORE_BN}_1
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_${v}_${CORE_BN}_2
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_${v}_${CORE_BN}_3
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_${v}_${CORE_BN}_4
	create_folder ${LOGS_DIR} ${CHANNEL_BN}_${v}_${CORE_BN}_5
	done
	for v in 1 2 3 4; do
		for z in 1 2 3 4 5; do
			create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}/${CORE_BN}_${z}" "../../../${SETTINGS_FN}/${CONFIG_BN}_${CHANNEL_BN}_${v}_${CORE_BN}_${z}" "CONFIG"
			create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}/${CORE_BN}_${z}" "../../../${SETTINGS_FN}/game" "game_${CHANNEL_BN}_${v}_${CORE_BN}_${z}"
			create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}/${CORE_BN}_${z}" "../../../${DATAS_FN}/locale" "locale"
			create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}/${CORE_BN}_${z}" "../../../${DATAS_FN}/data" "data"
			create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}/${CORE_BN}_${z}" "../../../${DATAS_FN}/mark" "mark"
			create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}/${CORE_BN}_${z}" "../../../${DATAS_FN}/package" "package"
			create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}/${CORE_BN}_${z}" "../../../${LOGS_FN}/${CHANNEL_BN}_${v}_${CORE_BN}_${z}" "log"
		done
	done
	for v in test 99 auth; do
		create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}" "../../${LOGS_FN}/${CHANNEL_BN}_${v}" "log"
		create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}" "../../${SETTINGS_FN}/${CONFIG_BN}_${CHANNEL_BN}_${v}" "CONFIG"
		create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}" "../../${DATAS_FN}/package" "package"
		create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}" "../../${DATAS_FN}/data" "data"
		create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}" "../../${DATAS_FN}/locale" "locale"
		create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}" "../../${DATAS_FN}/mark" "mark"
		create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_${v}" "../../${SETTINGS_FN}/game" "game_${CHANNEL_BN}_${v}"
	done
	create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_db" "../../${SETTINGS_FN}/db" "db"
	create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_db" "../../${SETTINGS_FN}/${CONFIG_BN}_${CHANNEL_BN}_db" "CONFIG"
	create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_db" "../../${LOGS_FN}/${CHANNEL_BN}_db" "log"
	create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_db" "../../${SETTINGS_FN}/item_proto_${LANGUAGE}.txt" "item_proto.txt"
	create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_db" "../../${SETTINGS_FN}/item_names_${LANGUAGE}.txt" "item_names.txt"
	create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_db" "../../${SETTINGS_FN}/mob_proto_${LANGUAGE}.txt" "mob_proto.txt"
	create_symlink "${CHANNELS_DIR}/${CHANNEL_BN}_db" "../../${SETTINGS_FN}/mob_names_${LANGUAGE}.txt" "mob_names.txt"
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
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 33 "${MSG_10}"
					kill -9 ${PID_VALUE} > /dev/null 2> /dev/null & sleep 0.5
				else
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 39 0 "${MSG_11}"
				fi
			else
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 39 0 "${MSG_11}"
			fi
		else
			for t in 1 2 3 4 5
			do
				PID="${PID_DIR}/${CORE_BN}_${t}/pid"
				if [ -e ${PID} ]; then
					PID_VALUE=`cat ${PID}`
					if ps -p ${PID_VALUE} > /dev/null
					then
						print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${t}	" && print 8 33 33 "${MSG_10}"
						kill -9 ${PID_VALUE} > /dev/null 2> /dev/null & sleep 0.5
					else
						print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${t}	" && print 8 39 0 "${MSG_11}"
					fi
				else
					print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${t}	" && print 8 39 0 "${MSG_11}"
				fi
			done

		fi
	else
		PID="${PID_DIR}/pid"
		if [ -e ${PID} ]; then
			PID_VALUE=`cat ${PID}`
			if ps -p ${PID_VALUE} > /dev/null
			then
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 33 "${MSG_10}"
				kill -9 ${PID_VALUE} > /dev/null 2> /dev/null & sleep 0.5
			else
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 39 0 "${MSG_11}"
			fi
		else
			print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 39 0 "${MSG_11}"
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
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 32 4 "${MSG_13}"
				else
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "${MSG_12}"
					cd ${PID_DIR} && ./game_${CHANNEL_BN}_${1} &
					sleep 2
				fi
			else
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "${MSG_12}"
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
						print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${y}	" && print 8 32 4 "${MSG_13}"
					else
						print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${y}	" && print 8 33 4 "${MSG_12}"
						cd ${PID_DIR}/${CORE_BN}_${y} && ./game_${CHANNEL_BN}_${1}_${CORE_BN}_${y} &
						sleep 2
					fi
				else
					print 1 33 7 "${CHANNEL_BN} ${1} ${CORE_BN} ${y}	" && print 8 33 4 "${MSG_12}"
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
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 32 4 "${MSG_13}"
				else
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "${MSG_12}"
					cd ${PID_DIR} && ./db &
					sleep 8
				fi
			else
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "${MSG_12}"
				cd ${PID_DIR} && ./db &
				sleep 8
			fi
		else
			PID="${PID_DIR}/pid"
			if [ -e ${PID} ]; then
				PID_VALUE=`cat ${PID}`
				if ps -p ${PID_VALUE} > /dev/null
				then
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 32 4 "${MSG_13}"
				else
					print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "${MSG_12}"
					cd ${PID_DIR} && ./game_${CHANNEL_BN}_${1} &
					sleep 2
				fi
			else
				print 1 33 7 "${CHANNEL_BN} ${1}	" && print 8 33 4 "${MSG_12}"
				cd ${PID_DIR} && ./game_${CHANNEL_BN}_${1} &
				sleep 2
			fi
		fi
	fi
}
clear_all_logs()
{
	for u in syserr syslog PTS stdout p2p_packet_info.txt packet_info.txt
	do
		if [ -e ${1}/${u} ]; then
			cd ${1} && rm -rf ${u}
		else
			sleep 0.02
		fi
	done
}
clear_channel()
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
					print 1 33 4 "${CHANNEL_BN} ${1}	" && print 8 33 7 "${MSG_14}"
				else
					clear_all_logs ${PID_DIR}
					print 1 33 4 "${CHANNEL_BN}_99	" print 8 32 7 "${MSG_15}"
				fi
			else
				clear_all_logs ${PID_DIR}
				print 1 33 4 "${CHANNEL_BN}_99	" print 8 32 7 "${MSG_15}"
			fi
		else
			for y in 1 2 3 4 5
			do
				PID="${PID_DIR}/${CORE_BN}_${y}/pid"
				NEW_PID_DIR="${PID_DIR}/${CORE_BN}_${y}"
				if [ -e ${PID} ]; then
					PID_VALUE=`cat ${PID}`
					if ps -p ${PID_VALUE} > /dev/null
					then
						print 1 0 33 "${CHANNEL_BN} ${1} ${CORE_BN} ${y}	" && print 8 33 4 "${MSG_14}"
					else
						print 1 0 33 "${CHANNEL_BN} ${1} ${CORE_BN} ${y}	" && print 8 32 4 "${MSG_15}"
						clear_all_logs ${NEW_PID_DIR}
					fi
				else
					print 1 0 33 "${CHANNEL_BN} ${1} ${CORE_BN} ${y}	" && print 8 32 4 "${MSG_15}"
					clear_all_logs ${NEW_PID_DIR}
				fi
			done
		fi
	else
			PID="${PID_DIR}/pid"
			if [ -e ${PID} ]; then
				PID_VALUE=`cat ${PID}`
				if ps -p ${PID_VALUE} > /dev/null
				then
					print 1 33 4 "${CHANNEL_BN} ${1}	" && print 8 33 7 "${MSG_14}"
				else
					print 1 33 4 "${CHANNEL_BN} ${1}	" && print 8 32 7 "${MSG_15}"
					clear_all_logs ${PID_DIR}
				fi
			else
					print 1 33 4 "${CHANNEL_BN} ${1}	" && print 8 32 7 "${MSG_15}"
					clear_all_logs ${PID_DIR}
			fi
	fi
}
command_parser()
{
	parser_num=0
	for i in ${1}
	do
		parser_num=$((parser_num+1))
	done
	if [ ${parser_num} -gt 9 ]; then
		print 8 31 31 "${MSG_4}"
		print 8 31 31 "${MSG_5}"
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
		elif [ ${i} = "compile" ]; then rtfi="${rtfi} 1"
		elif [ ${i} = "d" ]; then rtfi="${rtfi} 1"
		elif [ ${i} = "baslat" ]; then rtfi="${rtfi} 2"
		elif [ ${i} = "start" ]; then rtfi="${rtfi} 2"
		elif [ ${i} = "b" ]; then rtfi="${rtfi} 2"
		elif [ ${i} = "ac" ]; then rtfi="${rtfi} 2"
		elif [ ${i} = "kapat" ]; then rtfi="${rtfi} 3"
		elif [ ${i} = "kill" ]; then rtfi="${rtfi} 3"
		elif [ ${i} = "close" ]; then rtfi="${rtfi} 3"
		elif [ ${i} = "k" ]; then rtfi="${rtfi} 3"
		elif [ ${i} = "kurulum" ]; then rtfi="${rtfi} 4"
		elif [ ${i} = "setup" ]; then rtfi="${rtfi} 4"
		elif [ ${i} = "clear" ]; then rtfi="${rtfi} 5"
		elif [ ${i} = "temizle" ]; then rtfi="${rtfi} 5"
		elif [ ${i} = "clean" ]; then rtfi="${rtfi} 6"
		elif [ ${i} = "temiz" ]; then rtfi="${rtfi} 6"
		elif [ ${i} = "libgame" ]; then rtfi_s="${rtfi_s} 1"
		elif [ ${i} = "liblua" ]; then rtfi_s="${rtfi_s} 2"
		elif [ ${i} = "libpoly" ]; then rtfi_s="${rtfi_s} 3"
		elif [ ${i} = "libsql" ]; then rtfi_s="${rtfi_s} 4"
		elif [ ${i} = "libthecore" ]; then rtfi_s="${rtfi_s} 5"
		elif [ ${i} = "qc" ]; then rtfi_s="${rtfi_s} 6"
		elif [ ${i} = "db" ]; then rtfi_s="${rtfi_s} 7" && rtfi_c="${rtfi_c} db"
		elif [ ${i} = "game" ]; then rtfi_s="${rtfi_s} 8"
		elif [ ${i} = "all" ]; then rtfi_s="88 1 2 3 4 5 6 7 8" && rtfi_c="db auth 1 2 3 4 99"
		elif [ ${i} = "hepsini" ]; then rtfi_s="88 1 2 3 4 5 6 7 8" && rtfi_c="db auth 1 2 3 4 99"
		elif [ ${i} = "ymir" ]; then rtfi_s=" 1 2 3 4 5"
		elif [ ${i} = "lib" ]; then rtfi_s=" 88 1 2 3 4 5"
		elif [ ${i} = "cryptopp" ]; then rtfi_s=" 88"
		elif [ ${i} = "1" ]; then rtfi_c="${rtfi_c} 1"
		elif [ ${i} = "2" ]; then rtfi_c="${rtfi_c} 2"
		elif [ ${i} = "3" ]; then rtfi_c="${rtfi_c} 3"
		elif [ ${i} = "4" ]; then rtfi_c="${rtfi_c} 4"
		elif [ ${i} = "auth" ]; then rtfi_c="${rtfi_c} auth"
		elif [ ${i} = "99" ]; then rtfi_c="${rtfi_c} 99"
		elif [ ${i} = "test" ]; then rtfi_c="${rtfi_c} test"
		else
			print 1 31 7 "${i}" && print 8 0 31 "	${MSG_6}"
		fi
	done
	execute
}
execute()
{
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
		elif [ ${a} -eq 5 ]; then
			for b in ${rtfi_c}
			do
				if [ ${b} = "cncn_null" ]; then sleep 0.1
				else
					clear_channel ${b}
				fi
			done
		elif [ ${a} -eq 6 ]; then
			for b in ${rtfi_s}
			do
				if [ ${b} = "cncn_null" ]; then sleep 0.1
				else
					clear_source ${b}
				fi
			done
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
print 1 32 7 "${MSG_7}" && print 1 39 0 " = "
read command
clear
command_parser "${command}"

