-- MySQL dump 10.13  Distrib 8.0.22, for FreeBSD12.1 (i386)
--
-- Host: localhost    Database: account
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


--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login` varchar(30) NOT NULL DEFAULT '',
  `password` varchar(45) NOT NULL DEFAULT '',
  `real_name` varchar(16) NOT NULL DEFAULT '',
  `social_id` varchar(7) DEFAULT '',
  `email` varchar(64) NOT NULL DEFAULT '',
  `phone1` varchar(16) DEFAULT NULL,
  `phone2` varchar(16) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `zipcode` varchar(7) NOT NULL DEFAULT '',
  `create_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `question1` varchar(48) DEFAULT NULL,
  `answer1` varchar(48) DEFAULT NULL,
  `question2` varchar(48) DEFAULT NULL,
  `answer2` varchar(48) DEFAULT NULL,
  `is_testor` tinyint(1) NOT NULL DEFAULT '0',
  `status` varchar(8) NOT NULL DEFAULT 'OK',
  `securitycode` varchar(192) NOT NULL DEFAULT '',
  `newsletter` tinyint(1) NOT NULL DEFAULT '0',
  `empire` tinyint NOT NULL DEFAULT '0',
  `name_checked` tinyint(1) NOT NULL DEFAULT '0',
  `availDt` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `mileage` int NOT NULL DEFAULT '0',
  `cash` int NOT NULL DEFAULT '0',
  `gold_expire` datetime NOT NULL DEFAULT '2020-01-24 23:59:59',
  `silver_expire` datetime NOT NULL DEFAULT '2020-01-24 23:59:59',
  `safebox_expire` datetime NOT NULL DEFAULT '2020-01-24 23:59:59',
  `autoloot_expire` datetime NOT NULL DEFAULT '2020-01-24 23:59:59',
  `fish_mind_expire` datetime NOT NULL DEFAULT '2020-01-24 23:59:59',
  `marriage_fast_expire` datetime NOT NULL DEFAULT '2020-01-24 23:59:59',
  `money_drop_rate_expire` datetime NOT NULL DEFAULT '2020-01-24 23:59:59',
  `ttl_cash` int NOT NULL DEFAULT '0',
  `ttl_mileage` int NOT NULL DEFAULT '0',
  `channel_company` varchar(30) NOT NULL DEFAULT '',
  `ban_sure` varchar(30) NOT NULL,
  `ban_neden` varchar(30) NOT NULL,
  `ban_time` datetime NOT NULL,
  `ticket_id` varchar(30) NOT NULL,
  `kim_banlamis` varchar(30) NOT NULL,
  `coins` int NOT NULL DEFAULT '0',
  `web_admin` int NOT NULL DEFAULT '0',
  `web_ip` varchar(15) NOT NULL,
  `web_aktiviert` varchar(32) NOT NULL,
  `server` int NOT NULL DEFAULT '4',
  `bilgi` int NOT NULL DEFAULT '1',
  `email_onay` int NOT NULL DEFAULT '0',
  `last_play` datetime DEFAULT NULL,
  `banacilis` varchar(25) NOT NULL,
  `dost` varchar(30) NOT NULL,
  `gecici` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `login` (`login`),
  KEY `social_id` (`social_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10001 DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (10000,'cncn','*955BE0FC1081F6E6BE5092FB65BCBE87EE96CB8B','','','',NULL,NULL,NULL,'','0000-00-00 00:00:00',NULL,NULL,NULL,NULL,0,'OK','',0,0,0,'0000-00-00 00:00:00',0,0,'2020-01-24 23:59:59','2020-01-24 23:59:59','2020-01-24 23:59:59','2020-01-24 23:59:59','2020-01-24 23:59:59','2020-01-24 23:59:59','2020-01-24 23:59:59',0,0,'',' ',' ','2020-12-08 02:33:31',' ',' ',0,0,' ',' ',4,1,0,'2020-12-11 03:08:25',' ',' ',0);
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` int NOT NULL DEFAULT '0',
  `admin` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `block_exception`
--

DROP TABLE IF EXISTS `block_exception`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `block_exception` (
  `login` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `block_exception`
--

LOCK TABLES `block_exception` WRITE;
/*!40000 ALTER TABLE `block_exception` DISABLE KEYS */;
INSERT INTO `block_exception` VALUES (100);
/*!40000 ALTER TABLE `block_exception` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gametime`
--

DROP TABLE IF EXISTS `gametime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gametime` (
  `UserID` varchar(50) NOT NULL DEFAULT '',
  `paymenttype` tinyint NOT NULL DEFAULT '1',
  `LimitTime` int DEFAULT '0',
  `LimitDt` datetime DEFAULT '1990-01-01 00:00:00',
  `Scores` int DEFAULT '0',
  PRIMARY KEY (`UserID`)
) ENGINE=MyISAM DEFAULT CHARSET=euckr;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gametime`
--

LOCK TABLES `gametime` WRITE;
/*!40000 ALTER TABLE `gametime` DISABLE KEYS */;
/*!40000 ALTER TABLE `gametime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gametimeip`
--

DROP TABLE IF EXISTS `gametimeip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gametimeip` (
  `ipid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `ip` varchar(11) NOT NULL DEFAULT '000.000.000',
  `startIP` int NOT NULL DEFAULT '0',
  `endIP` int NOT NULL DEFAULT '255',
  `paymenttype` tinyint NOT NULL DEFAULT '1',
  `LimitTime` int NOT NULL DEFAULT '0',
  `LimitDt` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `readme` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`ipid`),
  UNIQUE KEY `ip_uniq` (`ip`,`startIP`,`endIP`),
  KEY `ip_idx` (`ip`)
) ENGINE=MyISAM DEFAULT CHARSET=euckr;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gametimeip`
--

LOCK TABLES `gametimeip` WRITE;
/*!40000 ALTER TABLE `gametimeip` DISABLE KEYS */;
/*!40000 ALTER TABLE `gametimeip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gametimelog`
--

DROP TABLE IF EXISTS `gametimelog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gametimelog` (
  `login` varchar(16) DEFAULT NULL,
  `type` enum('IP_FREE','FREE','IP_TIME','IP_DAY','TIME','DAY') DEFAULT NULL,
  `logon_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `logout_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `use_time` int DEFAULT NULL,
  `ip` varchar(15) NOT NULL DEFAULT '000.000.000.000',
  `server` varchar(32) NOT NULL DEFAULT '',
  KEY `login_key` (`login`)
) ENGINE=MyISAM DEFAULT CHARSET=gb2312;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gametimelog`
--

LOCK TABLES `gametimelog` WRITE;
/*!40000 ALTER TABLE `gametimelog` DISABLE KEYS */;
/*!40000 ALTER TABLE `gametimelog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iptocountry`
--

DROP TABLE IF EXISTS `iptocountry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `iptocountry` (
  `IP_FROM` varchar(16) DEFAULT NULL,
  `IP_TO` varchar(16) DEFAULT NULL,
  `COUNTRY_NAME` varchar(16) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iptocountry`
--

LOCK TABLES `iptocountry` WRITE;
/*!40000 ALTER TABLE `iptocountry` DISABLE KEYS */;
/*!40000 ALTER TABLE `iptocountry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `is_items`
--

DROP TABLE IF EXISTS `is_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `is_items` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `vnum` int unsigned NOT NULL,
  `kategorie_id` int unsigned NOT NULL,
  `bild` varchar(50) NOT NULL,
  `beschreibung` varchar(200) NOT NULL,
  `preis` int unsigned NOT NULL,
  `anzeigen` varchar(1) NOT NULL,
  `attrtype0` tinyint NOT NULL DEFAULT '0',
  `attrvalue0` smallint NOT NULL DEFAULT '0',
  `attrtype1` tinyint NOT NULL DEFAULT '0',
  `attrvalue1` smallint NOT NULL DEFAULT '0',
  `attrtype2` tinyint NOT NULL DEFAULT '0',
  `attrvalue2` smallint NOT NULL DEFAULT '0',
  `attrtype3` tinyint NOT NULL DEFAULT '0',
  `attrvalue3` smallint NOT NULL DEFAULT '0',
  `attrtype4` tinyint NOT NULL DEFAULT '0',
  `attrvalue4` smallint NOT NULL DEFAULT '0',
  `attrtype5` tinyint NOT NULL DEFAULT '0',
  `attrvalue5` smallint NOT NULL DEFAULT '0',
  `attrtype6` tinyint NOT NULL DEFAULT '0',
  `attrvalue6` smallint NOT NULL DEFAULT '0',
  `socket0` int unsigned NOT NULL DEFAULT '0',
  `socket1` int unsigned NOT NULL DEFAULT '0',
  `socket2` int unsigned NOT NULL DEFAULT '0',
  `socket3` int unsigned NOT NULL DEFAULT '0',
  `socket4` int unsigned NOT NULL DEFAULT '0',
  `socket5` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `is_items`
--

LOCK TABLES `is_items` WRITE;
/*!40000 ALTER TABLE `is_items` DISABLE KEYS */;
/*!40000 ALTER TABLE `is_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `is_kategorien`
--

DROP TABLE IF EXISTS `is_kategorien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `is_kategorien` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `titel` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `is_kategorien`
--

LOCK TABLES `is_kategorien` WRITE;
/*!40000 ALTER TABLE `is_kategorien` DISABLE KEYS */;
/*!40000 ALTER TABLE `is_kategorien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `is_log`
--

DROP TABLE IF EXISTS `is_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `is_log` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `account_id` int unsigned NOT NULL,
  `vnum` int unsigned NOT NULL,
  `preis` int unsigned NOT NULL,
  `zeitpunkt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `is_log`
--

LOCK TABLES `is_log` WRITE;
/*!40000 ALTER TABLE `is_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `is_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monarch`
--

DROP TABLE IF EXISTS `monarch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `monarch` (
  `empire` int unsigned NOT NULL DEFAULT '0',
  `pid` int unsigned DEFAULT '0',
  `name` varchar(16) DEFAULT NULL,
  `windate` datetime DEFAULT '0000-00-00 00:00:00',
  `money` bigint unsigned DEFAULT '0',
  PRIMARY KEY (`empire`)
) ENGINE=MyISAM DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monarch`
--

LOCK TABLES `monarch` WRITE;
/*!40000 ALTER TABLE `monarch` DISABLE KEYS */;
/*!40000 ALTER TABLE `monarch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `titel` varchar(200) NOT NULL,
  `inhalt` text NOT NULL,
  `datum` int unsigned NOT NULL,
  `hot` tinyint(1) NOT NULL,
  `kategorie` int unsigned NOT NULL,
  `author` int unsigned NOT NULL,
  `anzeigen` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `psc_log`
--

DROP TABLE IF EXISTS `psc_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `psc_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `account_id` int NOT NULL,
  `admin_id` int DEFAULT NULL,
  `card_type` varchar(20) NOT NULL,
  `waehrung` varchar(10) NOT NULL,
  `psc_code` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `psc_betrag` decimal(5,2) NOT NULL,
  `psc_pass` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `status` int NOT NULL,
  `kommentar` varchar(200) NOT NULL,
  `datum` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `psc_log`
--

LOCK TABLES `psc_log` WRITE;
/*!40000 ALTER TABLE `psc_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `psc_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `send_notice`
--

DROP TABLE IF EXISTS `send_notice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `send_notice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` tinyint NOT NULL DEFAULT '0',
  `server` varchar(3) NOT NULL DEFAULT '',
  `show_check` tinyint NOT NULL DEFAULT '0',
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `send_notice`
--

LOCK TABLES `send_notice` WRITE;
/*!40000 ALTER TABLE `send_notice` DISABLE KEYS */;
/*!40000 ALTER TABLE `send_notice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server_settings`
--

DROP TABLE IF EXISTS `server_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `server_settings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `variable` varchar(20) NOT NULL,
  `beschreibung` varchar(100) NOT NULL,
  `typ` enum('CHA','BOO','INT','DEC') NOT NULL,
  `value` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `variable` (`variable`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server_settings`
--

LOCK TABLES `server_settings` WRITE;
/*!40000 ALTER TABLE `server_settings` DISABLE KEYS */;
/*!40000 ALTER TABLE `server_settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tele_block`
--

DROP TABLE IF EXISTS `tele_block`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tele_block` (
  `account_id` int NOT NULL DEFAULT '0',
  `lastlogin` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `tele_block` varchar(30) NOT NULL DEFAULT '',
  PRIMARY KEY (`account_id`)
) ENGINE=MyISAM DEFAULT CHARSET=big5;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tele_block`
--

LOCK TABLES `tele_block` WRITE;
/*!40000 ALTER TABLE `tele_block` DISABLE KEYS */;
/*!40000 ALTER TABLE `tele_block` ENABLE KEYS */;
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

-- Dump completed on 2020-12-11  3:34:16
