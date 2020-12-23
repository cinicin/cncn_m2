#################################################
# CNCN M2 Server Shell Script					#
# Son Düzenleme: 19.12.2020						#
#################################################
#!/bin/sh
# IF YOU WANT TO ADD ANOTHER LANGUAGE SUPPORT EDIT THIS FILE FOR YOUR LANGUAGE.
# You can send pull request to me for adding your contrubition to master branch.
# LANGUAGE CHEAT SHEET
# BN stands for base name
# FN stands for folder name
# DIR stands for directory
# PID stands for process identifier
# BIN stands for binary
if [ ${LANGUAGE} == "en" ]; then
	CHANNEL_BN="channel"
	CORE_BN="c"
	CONFIG_BN="config"
	SERVER_FN="server"
	SRCS_FN="srcs"
	EXTERN_FN="harici"
	SETTINGS_FN="settings"
	DATAS_FN="datas"
	CHANNELS_FN="channels"
	LOGS_FN="logs"
	SERVER_SRC_FN="server_src"
	MSG_1="FOLDER ALREADY EXIST !!!"
	MSG_2="FOLDER CREATED."
	MSG_3="SYMBOLIC LINK CREATED."
	MSG_4="YOU ENTERED INVALID COMMANDS !!!"
	MSG_5="SCRIPT TERMINATED !!!"
	MSG_6="COMMAND NOT FOUND !!!"
	MSG_7="COMMAND"
	MSG_8="SOURCE CLEANED."
	MSG_9="COMPILE STARTED"
	MSG_10="CLOSED."
	MSG_11="ALREADY CLOSED"
	MSG_12="STARTED"
	MSG_13="ALREADY STARTED"
	MSG_14="CHANNEL STARTED"
	MSG_15="CLEANED"
	MSG_16="FOLDER STRUCTURE INSTALLING PLEASE WAIT..."
elif [ ${LANGUAGE} == "tr" ]; then
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
	MSG_1="KLASOR ZATEN VAR !!!"
	MSG_2="KLASOR OLUSTURULDU."
	MSG_3="SEMBOLIK BAGLANTISI OLUSTURULDU."
	MSG_4="GECERSIZ GIRIS YAPTINIZ !!!"
	MSG_5="SCRIPT SONLANDIRILDI !!!"
	MSG_6="KOMUT BULUNAMADI !!!"
	MSG_7="KOMUT"
	MSG_8="KAYNAKLARI TEMIZLENDI."
	MSG_9="DERLEME BASLADI."
	MSG_10="KAPATILDI."
	MSG_11="ZATEN KAPALI."
	MSG_12="ACILDI."
	MSG_13="ZATEN ACIK."
	MSG_14="KANAL ACIK."
	MSG_15="TEMIZLENDI."
	MSG_16="KLASOR YAPISI OLUSTURULUYOR LUTFEN BEKLEYIN..."
else
	clear
	echo "LANGUAGE CONFIGURE FAIL !!!"
	echo "DIL AYARLAMASI BASARISIZ !!!"
fi
