-- MySQL dump 10.13  Distrib 8.0.22, for FreeBSD12.1 (i386)
--
-- Host: localhost    Database: log
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup
--

-- SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '1791eeec-36f8-11eb-b12a-080027a62507:1-20997';

--
-- Table structure for table `bootlog`
--

DROP TABLE IF EXISTS `bootlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bootlog` (
  `time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `hostname` char(128) NOT NULL DEFAULT 'UNKNOWN',
  `channel` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bootlog`
--

LOCK TABLES `bootlog` WRITE;
/*!40000 ALTER TABLE `bootlog` DISABLE KEYS */;
INSERT INTO `bootlog` VALUES ('2020-12-11 02:31:43','auth',1),('2020-12-11 02:31:52','channel1',1),('2020-12-11 02:57:08','auth',1),('2020-12-11 02:57:10','channel1',1),('2020-12-11 03:06:31','auth',1),('2020-12-11 03:06:39','channel1',1);
/*!40000 ALTER TABLE `bootlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `change_name`
--

DROP TABLE IF EXISTS `change_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `change_name` (
  `pid` int unsigned DEFAULT NULL,
  `old_name` varchar(12) NOT NULL DEFAULT 'NONAME',
  `new_name` varchar(12) NOT NULL DEFAULT 'NONAME',
  `time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `ip` varchar(16) DEFAULT '0.0.0.0'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `change_name`
--

LOCK TABLES `change_name` WRITE;
/*!40000 ALTER TABLE `change_name` DISABLE KEYS */;
/*!40000 ALTER TABLE `change_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `command_log`
--

DROP TABLE IF EXISTS `command_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `command_log` (
  `userid` int DEFAULT NULL,
  `server` int DEFAULT NULL,
  `ip` text,
  `port` int DEFAULT NULL,
  `username` varchar(12) CHARACTER SET big5 COLLATE big5_chinese_ci NOT NULL DEFAULT 'NONAME',
  `command` varchar(20) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `command_log`
--

LOCK TABLES `command_log` WRITE;
/*!40000 ALTER TABLE `command_log` DISABLE KEYS */;
INSERT INTO `command_log` VALUES (10002,999,'192.168.0.11',1,'cinicin','i 19','2020-12-11 02:58:26'),(10002,999,'192.168.0.11',1,'cinicin','m 109','2020-12-11 02:58:37'),(10002,999,'192.168.0.11',1,'cinicin','m 109 100','2020-12-11 02:58:47'),(10002,999,'192.168.0.11',1,'cinicin','m 101 11','2020-12-11 02:59:19'),(10002,999,'192.168.0.11',1,'cinicin','m 101 111','2020-12-11 02:59:30'),(10002,999,'192.168.0.11',1,'cinicin','m 101 111','2020-12-11 02:59:48'),(10002,999,'192.168.0.11',1,'cinicin','m 101 111','2020-12-11 02:59:51'),(10002,999,'192.168.0.11',1,'cinicin','m 101 111','2020-12-11 02:59:51'),(10002,999,'192.168.0.11',1,'cinicin','m 101 111','2020-12-11 02:59:51'),(10002,999,'192.168.0.11',1,'cinicin','m 101 111','2020-12-11 02:59:51'),(10002,999,'192.168.0.11',1,'cinicin','m 101 111','2020-12-11 03:00:36'),(10002,999,'192.168.0.11',1,'cinicin','m 101 111','2020-12-11 03:00:36'),(10002,999,'192.168.0.11',1,'cinicin','m 101 111','2020-12-11 03:00:37'),(10002,999,'192.168.0.11',1,'cinicin','m 109 100','2020-12-11 03:02:07'),(10002,999,'192.168.0.11',1,'cinicin','purge','2020-12-11 03:02:21'),(10002,999,'192.168.0.11',1,'cinicin','level 90','2020-12-11 03:09:30');
/*!40000 ALTER TABLE `command_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cube`
--

DROP TABLE IF EXISTS `cube`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cube` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `pid` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `x` int unsigned NOT NULL DEFAULT '0',
  `y` int unsigned NOT NULL DEFAULT '0',
  `item_vnum` int unsigned NOT NULL DEFAULT '0',
  `item_uid` int unsigned NOT NULL DEFAULT '0',
  `item_count` int unsigned NOT NULL DEFAULT '0',
  `success` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `pid` (`pid`),
  KEY `item_vnum` (`item_vnum`),
  KEY `item_uid` (`item_uid`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cube`
--

LOCK TABLES `cube` WRITE;
/*!40000 ALTER TABLE `cube` DISABLE KEYS */;
/*!40000 ALTER TABLE `cube` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dragon_slay_log`
--

DROP TABLE IF EXISTS `dragon_slay_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dragon_slay_log` (
  `1` varchar(255) NOT NULL,
  `2` varchar(255) NOT NULL,
  `3` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `4` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dragon_slay_log`
--

LOCK TABLES `dragon_slay_log` WRITE;
/*!40000 ALTER TABLE `dragon_slay_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `dragon_slay_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exo_bank_log`
--

DROP TABLE IF EXISTS `exo_bank_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exo_bank_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(30) NOT NULL,
  `money` int NOT NULL,
  `art` varchar(10) NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=272 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exo_bank_log`
--

LOCK TABLES `exo_bank_log` WRITE;
/*!40000 ALTER TABLE `exo_bank_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `exo_bank_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fish_log`
--

DROP TABLE IF EXISTS `fish_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fish_log` (
  `1` int DEFAULT NULL,
  `2` int DEFAULT NULL,
  `3` int DEFAULT NULL,
  `4` int DEFAULT NULL,
  `5` int DEFAULT NULL,
  `6` int DEFAULT NULL,
  `7` int DEFAULT NULL,
  `8` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=big5 COLLATE=big5_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fish_log`
--

LOCK TABLES `fish_log` WRITE;
/*!40000 ALTER TABLE `fish_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `fish_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gmhost`
--

DROP TABLE IF EXISTS `gmhost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gmhost` (
  `mIP` varchar(16) NOT NULL DEFAULT '',
  PRIMARY KEY (`mIP`)
) ENGINE=MyISAM DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gmhost`
--

LOCK TABLES `gmhost` WRITE;
/*!40000 ALTER TABLE `gmhost` DISABLE KEYS */;
/*!40000 ALTER TABLE `gmhost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gmlist`
--

DROP TABLE IF EXISTS `gmlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gmlist` (
  `mID` int unsigned NOT NULL AUTO_INCREMENT,
  `mAccount` varchar(16) NOT NULL DEFAULT '',
  `mName` varchar(16) NOT NULL DEFAULT '',
  `mContactIP` varchar(16) NOT NULL DEFAULT '',
  `mServerIP` varchar(16) NOT NULL DEFAULT 'ALL',
  `mAuthority` enum('IMPLEMENTOR','HIGH_WIZARD','GOD','LOW_WIZARD','PLAYER') DEFAULT 'PLAYER',
  PRIMARY KEY (`mID`)
) ENGINE=MyISAM AUTO_INCREMENT=69019002 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gmlist`
--

LOCK TABLES `gmlist` WRITE;
/*!40000 ALTER TABLE `gmlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `gmlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goldlog`
--

DROP TABLE IF EXISTS `goldlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goldlog` (
  `date` varchar(10) NOT NULL DEFAULT '0000-00-00',
  `time` varchar(8) NOT NULL DEFAULT '00:00:00',
  `pid` int unsigned NOT NULL DEFAULT '0',
  `what` int NOT NULL DEFAULT '0',
  `how` set('BUY','SELL','SHOP_SELL','SHOP_BUY','EXCHANGE_TAKE','EXCHANGE_GIVE','QUEST') DEFAULT NULL,
  `hint` varchar(50) DEFAULT NULL,
  KEY `date_idx` (`date`),
  KEY `pid_idx` (`pid`),
  KEY `what_idx` (`what`),
  KEY `how_idx` (`how`)
) ENGINE=MyISAM DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goldlog`
--

LOCK TABLES `goldlog` WRITE;
/*!40000 ALTER TABLE `goldlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `goldlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hack_crc_log`
--

DROP TABLE IF EXISTS `hack_crc_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hack_crc_log` (
  `time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `login` char(16) NOT NULL DEFAULT '',
  `name` char(24) NOT NULL DEFAULT '',
  `ip` char(15) NOT NULL DEFAULT '',
  `server` char(100) NOT NULL DEFAULT '',
  `why` char(255) NOT NULL DEFAULT '',
  `crc` int NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hack_crc_log`
--

LOCK TABLES `hack_crc_log` WRITE;
/*!40000 ALTER TABLE `hack_crc_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `hack_crc_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hack_log`
--

DROP TABLE IF EXISTS `hack_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hack_log` (
  `time` time DEFAULT NULL,
  `login` longtext CHARACTER SET big5 COLLATE big5_bin,
  `name` varchar(11) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `ip` text CHARACTER SET latin1 COLLATE latin1_swedish_ci,
  `server` varchar(11) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `why` varchar(22) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=big5 COLLATE=big5_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hack_log`
--

LOCK TABLES `hack_log` WRITE;
/*!40000 ALTER TABLE `hack_log` DISABLE KEYS */;
INSERT INTO `hack_log` VALUES ('02:52:28','cncn','cinicin','192.168.0.11','channel1','SHOP_BUY_GOLD_OVERFLOW');
/*!40000 ALTER TABLE `hack_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hackshield_log`
--

DROP TABLE IF EXISTS `hackshield_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hackshield_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time` datetime DEFAULT NULL,
  `account_id` int DEFAULT NULL,
  `login` varchar(20) DEFAULT NULL,
  `pid` int DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `reason` varchar(20) DEFAULT NULL,
  `ip` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hackshield_log`
--

LOCK TABLES `hackshield_log` WRITE;
/*!40000 ALTER TABLE `hackshield_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `hackshield_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingame_ban_log`
--

DROP TABLE IF EXISTS `ingame_ban_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingame_ban_log` (
  `ban_time` datetime DEFAULT NULL,
  `who` varchar(255) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `GM` varchar(255) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `cause` varchar(255) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `until` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=big5 COLLATE=big5_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingame_ban_log`
--

LOCK TABLES `ingame_ban_log` WRITE;
/*!40000 ALTER TABLE `ingame_ban_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `ingame_ban_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `levellog`
--

DROP TABLE IF EXISTS `levellog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `levellog` (
  `name` varchar(50) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `level` int DEFAULT NULL,
  `time` time DEFAULT NULL,
  `playtime` int DEFAULT NULL,
  `account_id` varchar(50) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `pid` varchar(50) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=big5 COLLATE=big5_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `levellog`
--

LOCK TABLES `levellog` WRITE;
/*!40000 ALTER TABLE `levellog` DISABLE KEYS */;
INSERT INTO `levellog` VALUES ('cinicin',2,'02:59:38',4,'10000','10002'),('cinicin',3,'02:59:59',5,'10000','10002'),('cinicin',4,'03:01:36',6,'10000','10002'),('cinicin',5,'03:02:16',7,'10000','10002'),('cinicin',90,'03:09:30',8,'10000','10002');
/*!40000 ALTER TABLE `levellog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locale`
--

DROP TABLE IF EXISTS `locale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locale` (
  `mKey` varchar(255) NOT NULL DEFAULT '',
  `mValue` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`mKey`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locale`
--

LOCK TABLES `locale` WRITE;
/*!40000 ALTER TABLE `locale` DISABLE KEYS */;
/*!40000 ALTER TABLE `locale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locale_bug`
--

DROP TABLE IF EXISTS `locale_bug`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locale_bug` (
  `mKey` varchar(255) NOT NULL DEFAULT '',
  `mValue` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`mKey`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locale_bug`
--

LOCK TABLES `locale_bug` WRITE;
/*!40000 ALTER TABLE `locale_bug` DISABLE KEYS */;
/*!40000 ALTER TABLE `locale_bug` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `type` varchar(20) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `time` time DEFAULT NULL,
  `who` int DEFAULT NULL,
  `x` int DEFAULT NULL,
  `y` int DEFAULT NULL,
  `what` int DEFAULT NULL,
  `how` varchar(20) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `hint` varchar(20) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `ip` text CHARACTER SET latin1 COLLATE latin1_swedish_ci,
  `vnum` int DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=big5 COLLATE=big5_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES ('CHARACTER','08:31:19',10000,321628,807521,5,'GM_LOGIN','','88.226.133.232',0),('CHARACTER','08:31:19',10000,321628,807521,0,'LOGIN','88.226.133.232 90805','88.226.133.232',0),('ITEM','08:31:41',10000,321628,807521,10000116,'GM','Azrail\'in Sand???','88.226.133.232',50186),('ITEM','08:31:42',10000,321628,807521,10000117,'GM','??rak Sand??? I','88.226.133.232',50187),('ITEM','08:31:43',10000,321628,807521,10000118,'GM','??rak Sand??? I I','88.226.133.232',50188),('ITEM','08:31:45',10000,321628,807521,10000119,'SYSTEM','??rak Sand??? I I','88.226.133.232',50188),('ITEM','08:31:45',0,1,0,10000120,'SET_SOCKET','','',19),('ITEM','08:31:45',10000,321628,807521,10000120,'SYSTEM','K?l??+9','88.226.133.232',19),('ITEM','08:31:45',10000,321628,807521,10000121,'SYSTEM','K?rm?z? iksir (K)','88.226.133.232',27051),('ITEM','08:31:45',10000,321628,807521,10000122,'SYSTEM','Mavi ?ksir (K)','88.226.133.232',27052),('ITEM','08:31:45',10000,321628,807521,10000123,'SYSTEM','Ye?il ?ksir (K)','88.226.133.232',27053),('ITEM','08:31:45',10000,321628,807521,10000124,'SYSTEM','Mor ?ksir (K)','88.226.133.232',27054),('ITEM','08:31:45',10000,321628,807521,10000125,'SYSTEM','H?z ?ksiri','88.226.133.232',76012),('ITEM','08:31:45',10000,321628,807521,10000126,'SYSTEM','Sald?r? ?ksiri +10','88.226.133.232',76017),('ITEM','08:31:45',2,100000,0,10000127,'SET_SOCKET','','',76021),('ITEM','08:31:45',10000,321628,807521,10000127,'SYSTEM','G?ne? ?z?t? (K)','88.226.133.232',76021),('ITEM','08:31:45',10000,321628,807521,10000128,'SYSTEM','Ejderha Madalyas?','88.226.133.232',76008),('ITEM','08:31:45',10000,321628,807521,10000129,'SYSTEM','??rak Sand??? III','88.226.133.232',50189),('ITEM','08:31:46',2,100000,0,10000130,'SET_SOCKET','','',76021),('ITEM','08:31:46',10000,321628,807521,10000130,'SYSTEM','G?ne? ?z?t? (K)','88.226.133.232',76021),('ITEM','08:31:46',10000,321628,807521,10000131,'SYSTEM','??rak Sand??? III','88.226.133.232',50189),('CHARACTER','08:43:27',10000,321628,807521,0,'LOGOUT','88.226.133.232 90805','88.226.133.232',0),('CHARACTER','02:32:42',10001,0,0,0,'CREATE PLAYER','','192.168.0.11',0),('CHARACTER','02:34:20',10002,0,0,0,'CREATE PLAYER','','192.168.0.11',0),('CHARACTER','02:34:25',10002,459778,953775,0,'LOGIN','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:35:10',10002,459778,953775,0,'LOGOUT','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:35:58',10002,459778,953775,0,'LOGIN','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:36:03',10002,459778,953775,0,'LOGOUT','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:36:50',10000,321628,807521,5,'GM_LOGIN','','192.168.0.11',0),('CHARACTER','02:37:54',10002,459778,953775,0,'LOGIN','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:37:59',10002,459778,953775,0,'LOGOUT','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:39:32',10002,459778,953775,0,'LOGIN','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:39:37',10002,459778,953775,0,'LOGOUT','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:40:11',10002,459778,953775,0,'LOGIN','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:40:16',10002,459778,953775,0,'LOGOUT','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:49:02',10002,459778,953775,0,'LOGIN','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:52:47',10002,475141,951312,0,'LOGOUT','192.168.0.11 0 1 1 0','192.168.0.11',0),('CHARACTER','02:57:45',10002,475141,951312,5,'GM_LOGIN','','192.168.0.11',0),('CHARACTER','02:57:45',10002,475141,951312,0,'LOGIN','192.168.0.11 0 1 1 0','192.168.0.11',0),('ITEM','02:58:26',0,1,0,10000132,'SET_SOCKET','','',19),('ITEM','03:00:56',0,1,0,10000137,'SET_SOCKET','','',1010),('CHARACTER','03:08:32',10002,472194,952990,5,'GM_LOGIN','','192.168.0.11',0),('ITEM','03:08:47',0,1,0,10000136,'SET_SOCKET','','',19),('CHARACTER','03:09:30',10002,467315,953604,0,'RESET_POINT','','192.168.0.11',0);
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loginlog`
--

DROP TABLE IF EXISTS `loginlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loginlog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` text,
  `time` datetime DEFAULT NULL,
  `channel` int DEFAULT NULL,
  `account_id` int DEFAULT NULL,
  `pid` int DEFAULT NULL,
  `level` int DEFAULT NULL,
  `job` int DEFAULT NULL,
  `playtime` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loginlog`
--

LOCK TABLES `loginlog` WRITE;
/*!40000 ALTER TABLE `loginlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `loginlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loginlog2`
--

DROP TABLE IF EXISTS `loginlog2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loginlog2` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` text,
  `is_gm` int DEFAULT NULL,
  `login_time` datetime DEFAULT NULL,
  `channel` int DEFAULT NULL,
  `account_id` int DEFAULT NULL,
  `pid` int DEFAULT NULL,
  `client_version` text,
  `ip` text,
  `logout_time` datetime DEFAULT NULL,
  `playtime` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=292755 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loginlog2`
--

LOCK TABLES `loginlog2` WRITE;
/*!40000 ALTER TABLE `loginlog2` DISABLE KEYS */;
INSERT INTO `loginlog2` VALUES (292754,'INVALID',0,'2014-10-01 08:31:19',1,1,10000,'','1491240424',NULL,0);
/*!40000 ALTER TABLE `loginlog2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `money_log`
--

DROP TABLE IF EXISTS `money_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `money_log` (
  `VALUES` varchar(100) DEFAULT NULL,
  `DELAYED` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `vnum` varchar(100) DEFAULT NULL,
  `pid` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `money_log`
--

LOCK TABLES `money_log` WRITE;
/*!40000 ALTER TABLE `money_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `money_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pcbang_loginlog`
--

DROP TABLE IF EXISTS `pcbang_loginlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pcbang_loginlog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time` datetime DEFAULT NULL,
  `pcbang_id` int NOT NULL DEFAULT '0',
  `ip` varchar(15) NOT NULL DEFAULT '000.000.000.000',
  `pid` int unsigned DEFAULT NULL,
  `play_time` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pid` (`pid`),
  KEY `pcbang_id` (`pcbang_id`)
) ENGINE=MyISAM DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pcbang_loginlog`
--

LOCK TABLES `pcbang_loginlog` WRITE;
/*!40000 ALTER TABLE `pcbang_loginlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `pcbang_loginlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quest_reward_log`
--

DROP TABLE IF EXISTS `quest_reward_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quest_reward_log` (
  `1` varchar(50) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `2` int DEFAULT NULL,
  `3` int DEFAULT NULL,
  `4` int DEFAULT NULL,
  `5` int DEFAULT NULL,
  `6` int DEFAULT NULL,
  `7` time DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=big5 COLLATE=big5_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quest_reward_log`
--

LOCK TABLES `quest_reward_log` WRITE;
/*!40000 ALTER TABLE `quest_reward_log` DISABLE KEYS */;
INSERT INTO `quest_reward_log` VALUES ('give_basic_weapon',10002,5,2,50187,1,'03:08:38');
/*!40000 ALTER TABLE `quest_reward_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `refinelog`
--

DROP TABLE IF EXISTS `refinelog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `refinelog` (
  `Id` int DEFAULT NULL,
  `pid` int DEFAULT NULL,
  `item_name` varchar(50) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL,
  `item_id` int DEFAULT NULL,
  `step` int DEFAULT NULL,
  `time` time DEFAULT NULL,
  `is_success` int DEFAULT NULL,
  `setType` varchar(50) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=big5 COLLATE=big5_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `refinelog`
--

LOCK TABLES `refinelog` WRITE;
/*!40000 ALTER TABLE `refinelog` DISABLE KEYS */;
/*!40000 ALTER TABLE `refinelog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shout_log`
--

DROP TABLE IF EXISTS `shout_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shout_log` (
  `1` time DEFAULT NULL,
  `2` int DEFAULT NULL,
  `3` int DEFAULT NULL,
  `4` varchar(50) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=big5 COLLATE=big5_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shout_log`
--

LOCK TABLES `shout_log` WRITE;
/*!40000 ALTER TABLE `shout_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `shout_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `speed_hack`
--

DROP TABLE IF EXISTS `speed_hack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `speed_hack` (
  `pid` int DEFAULT NULL,
  `time` time DEFAULT NULL,
  `x` int DEFAULT NULL,
  `y` int DEFAULT NULL,
  `hack_count` varchar(20) CHARACTER SET big5 COLLATE big5_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=big5 COLLATE=big5_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `speed_hack`
--

LOCK TABLES `speed_hack` WRITE;
/*!40000 ALTER TABLE `speed_hack` DISABLE KEYS */;
/*!40000 ALTER TABLE `speed_hack` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-11  3:35:42
