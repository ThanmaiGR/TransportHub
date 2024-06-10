-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: transporthub
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add cab companies',1,'add_cabcompanies'),(2,'Can change cab companies',1,'change_cabcompanies'),(3,'Can delete cab companies',1,'delete_cabcompanies'),(4,'Can view cab companies',1,'view_cabcompanies'),(5,'Can add locations',2,'add_locations'),(6,'Can change locations',2,'change_locations'),(7,'Can delete locations',2,'delete_locations'),(8,'Can view locations',2,'view_locations'),(9,'Can add routes',3,'add_routes'),(10,'Can change routes',3,'change_routes'),(11,'Can delete routes',3,'delete_routes'),(12,'Can view routes',3,'view_routes'),(13,'Can add cab fare structure',4,'add_cabfarestructure'),(14,'Can change cab fare structure',4,'change_cabfarestructure'),(15,'Can delete cab fare structure',4,'delete_cabfarestructure'),(16,'Can view cab fare structure',4,'view_cabfarestructure'),(17,'Can add connections',5,'add_connections'),(18,'Can change connections',5,'change_connections'),(19,'Can delete connections',5,'delete_connections'),(20,'Can view connections',5,'view_connections'),(21,'Can add stops',6,'add_stops'),(22,'Can change stops',6,'change_stops'),(23,'Can delete stops',6,'delete_stops'),(24,'Can view stops',6,'view_stops'),(25,'Can add route details',7,'add_routedetails'),(26,'Can change route details',7,'change_routedetails'),(27,'Can delete route details',7,'delete_routedetails'),(28,'Can view route details',7,'view_routedetails'),(29,'Can add log entry',8,'add_logentry'),(30,'Can change log entry',8,'change_logentry'),(31,'Can delete log entry',8,'delete_logentry'),(32,'Can view log entry',8,'view_logentry'),(33,'Can add permission',9,'add_permission'),(34,'Can change permission',9,'change_permission'),(35,'Can delete permission',9,'delete_permission'),(36,'Can view permission',9,'view_permission'),(37,'Can add group',10,'add_group'),(38,'Can change group',10,'change_group'),(39,'Can delete group',10,'delete_group'),(40,'Can view group',10,'view_group'),(41,'Can add user',11,'add_user'),(42,'Can change user',11,'change_user'),(43,'Can delete user',11,'delete_user'),(44,'Can view user',11,'view_user'),(45,'Can add content type',12,'add_contenttype'),(46,'Can change content type',12,'change_contenttype'),(47,'Can delete content type',12,'delete_contenttype'),(48,'Can view content type',12,'view_contenttype'),(49,'Can add session',13,'add_session'),(50,'Can change session',13,'change_session'),(51,'Can delete session',13,'delete_session'),(52,'Can view session',13,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$SsP1iAbiMbmFgoBCGHdXbj$tGbalhy5+CC0Ha0d7jvIqGV20ts2QDlwUkuL4HPTEAY=','2024-06-07 11:56:53.984567',0,'user1','user','1','user@user.com',0,1,'2024-05-24 09:57:18.215990'),(2,'pbkdf2_sha256$720000$Bqu6ppJDdeLftmNA7Y1YOn$NlupXJdK3mL51hYd/1FoZ2QOiTQQvEvX0pooplnPHY0=','2024-05-24 09:59:59.423565',1,'admin','','','',1,1,'2024-05-24 09:59:43.700407');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `FirstNameNotBlankBeforeUpdate` BEFORE UPDATE ON `auth_user` FOR EACH ROW BEGIN
    IF NEW.last_name IS NOT NULL AND NEW.first_name = '' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'First name cannot be blank with Last Name';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_cabcompanies`
--

DROP TABLE IF EXISTS `core_cabcompanies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_cabcompanies` (
  `CompanyID` int NOT NULL AUTO_INCREMENT,
  `CompanyName` varchar(255) NOT NULL,
  PRIMARY KEY (`CompanyID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_cabcompanies`
--

LOCK TABLES `core_cabcompanies` WRITE;
/*!40000 ALTER TABLE `core_cabcompanies` DISABLE KEYS */;
INSERT INTO `core_cabcompanies` VALUES (1,'SwiftRide'),(2,'MetroCabs'),(3,'CityWheels');
/*!40000 ALTER TABLE `core_cabcompanies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_cabfarestructure`
--

DROP TABLE IF EXISTS `core_cabfarestructure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_cabfarestructure` (
  `CompanyID` int NOT NULL,
  `BasePrice` decimal(10,2) NOT NULL,
  `PricePerKM` decimal(5,2) NOT NULL,
  `BaseKM` decimal(4,2) NOT NULL,
  PRIMARY KEY (`CompanyID`),
  CONSTRAINT `core_cabfarestructur_CompanyID_9409b236_fk_core_cabc` FOREIGN KEY (`CompanyID`) REFERENCES `core_cabcompanies` (`CompanyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_cabfarestructure`
--

LOCK TABLES `core_cabfarestructure` WRITE;
/*!40000 ALTER TABLE `core_cabfarestructure` DISABLE KEYS */;
INSERT INTO `core_cabfarestructure` VALUES (1,18.00,5.50,1.50),(2,20.00,7.50,2.00),(3,14.00,4.80,1.00);
/*!40000 ALTER TABLE `core_cabfarestructure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_connections`
--

DROP TABLE IF EXISTS `core_connections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_connections` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Distance` decimal(3,1) NOT NULL,
  `DestinationID` int NOT NULL,
  `SourceID` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_connections_DestinationID_3d0f6644_fk_core_loca` (`DestinationID`),
  KEY `core_connections_SourceID_3a01cd4e_fk_core_locations_LocationID` (`SourceID`),
  CONSTRAINT `core_connections_DestinationID_3d0f6644_fk_core_loca` FOREIGN KEY (`DestinationID`) REFERENCES `core_locations` (`LocationID`),
  CONSTRAINT `core_connections_SourceID_3a01cd4e_fk_core_locations_LocationID` FOREIGN KEY (`SourceID`) REFERENCES `core_locations` (`LocationID`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_connections`
--

LOCK TABLES `core_connections` WRITE;
/*!40000 ALTER TABLE `core_connections` DISABLE KEYS */;
INSERT INTO `core_connections` VALUES (1,7.0,2,1),(2,2.0,5,1),(3,7.0,1,2),(4,5.0,3,2),(5,3.0,4,2),(6,5.0,2,3),(7,5.0,6,3),(8,2.0,7,3),(9,3.0,2,4),(10,4.0,5,4),(11,4.0,7,4),(12,10.0,8,4),(13,2.0,1,5),(14,4.0,4,5),(15,2.0,6,5),(16,8.0,10,5),(17,2.0,5,6),(18,5.0,3,6),(19,5.0,7,6),(20,4.0,9,6),(21,2.0,3,7),(22,4.0,4,7),(23,5.0,6,7),(24,3.0,8,7),(25,3.0,7,8),(26,7.0,10,8),(27,10.0,4,8),(28,2.0,9,8),(29,4.0,6,9),(30,2.0,8,9),(31,4.0,10,9),(32,8.0,5,10),(33,7.0,8,10),(34,4.0,9,10);
/*!40000 ALTER TABLE `core_connections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_locations`
--

DROP TABLE IF EXISTS `core_locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_locations` (
  `LocationID` int NOT NULL AUTO_INCREMENT,
  `LocationName` varchar(255) NOT NULL,
  `Latitude` decimal(10,8) NOT NULL,
  `Longitude` decimal(11,8) NOT NULL,
  PRIMARY KEY (`LocationID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_locations`
--

LOCK TABLES `core_locations` WRITE;
/*!40000 ALTER TABLE `core_locations` DISABLE KEYS */;
INSERT INTO `core_locations` VALUES (1,'Riverside District',40.71280000,-74.00600000),(2,'Downtown Square',40.71230000,-74.00780000),(3,'Harborview Heights',40.71650000,-74.01540000),(4,'Millside Quarter',40.71950000,-74.00590000),(5,'Central Plaza',40.71520000,-74.00860000),(6,'University Junction',40.72010000,-74.00290000),(7,'Warehouse District',40.71690000,-74.01340000),(8,'Artist\'s Alley',40.72130000,-74.00370000),(9,'Financial District',40.70740000,-74.01190000),(10,'Industrial Zone',40.71430000,-74.00850000);
/*!40000 ALTER TABLE `core_locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_routedetails`
--

DROP TABLE IF EXISTS `core_routedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_routedetails` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `StopSequence` int NOT NULL,
  `RouteID` int NOT NULL,
  `StopID` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_routedetails_RouteID_id_StopSequence_3ea8e458_uniq` (`RouteID`,`StopSequence`),
  KEY `core_routedetails_StopID_19e210c6_fk_core_stops_StopID` (`StopID`),
  CONSTRAINT `core_routedetails_RouteID_ee0d54b5_fk_core_routes_RouteID` FOREIGN KEY (`RouteID`) REFERENCES `core_routes` (`RouteID`),
  CONSTRAINT `core_routedetails_StopID_19e210c6_fk_core_stops_StopID` FOREIGN KEY (`StopID`) REFERENCES `core_stops` (`StopID`)
) ENGINE=InnoDB AUTO_INCREMENT=157 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_routedetails`
--

LOCK TABLES `core_routedetails` WRITE;
/*!40000 ALTER TABLE `core_routedetails` DISABLE KEYS */;
INSERT INTO `core_routedetails` VALUES (79,1,1,1),(80,2,1,2),(81,3,1,4),(82,4,1,5),(83,5,1,1),(84,1,2,4),(85,2,2,8),(86,3,2,9),(87,4,2,6),(88,5,2,5),(89,6,2,4),(90,1,3,1),(91,2,3,2),(92,3,3,4),(93,4,3,7),(94,5,3,3),(95,6,3,6),(96,7,3,9),(97,8,3,10),(98,9,3,5),(99,10,3,1),(100,1,4,5),(101,2,4,4),(102,3,4,8),(103,4,4,7),(104,5,4,6),(105,6,4,5),(106,1,5,8),(107,2,5,9),(108,3,5,10),(109,4,5,8),(110,1,6,4),(111,2,6,7),(112,3,6,3),(113,4,6,6),(114,5,6,9),(115,6,6,10),(116,7,6,8),(117,8,6,4),(118,1,7,1),(119,2,7,5),(120,3,7,4),(121,4,7,2),(122,5,7,1),(123,1,8,4),(124,2,8,5),(125,3,8,6),(126,4,8,9),(127,5,8,8),(128,6,8,4),(129,1,9,1),(130,2,9,5),(131,3,9,10),(132,4,9,9),(133,5,9,6),(134,6,9,3),(135,7,9,7),(136,8,9,4),(137,9,9,2),(138,10,9,1),(139,1,10,5),(140,2,10,6),(141,3,10,7),(142,4,10,8),(143,5,10,4),(144,6,10,5),(145,1,11,8),(146,2,11,10),(147,3,11,9),(148,4,11,8),(149,1,12,4),(150,2,12,8),(151,3,12,10),(152,4,12,9),(153,5,12,6),(154,6,12,3),(155,7,12,7),(156,8,12,4);
/*!40000 ALTER TABLE `core_routedetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_routes`
--

DROP TABLE IF EXISTS `core_routes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_routes` (
  `RouteID` int NOT NULL AUTO_INCREMENT,
  `VehicleType` varchar(50) NOT NULL,
  `RouteName` varchar(255) NOT NULL,
  `FarePerKM` decimal(5,2) NOT NULL,
  PRIMARY KEY (`RouteID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_routes`
--

LOCK TABLES `core_routes` WRITE;
/*!40000 ALTER TABLE `core_routes` DISABLE KEYS */;
INSERT INTO `core_routes` VALUES (1,'Bus','451A',3.00),(2,'Bus','557A',3.50),(3,'Metro','10A',4.50),(4,'Bus','781A',2.70),(5,'Bus','335A',2.80),(6,'Metro','24A',3.50),(7,'Bus','451C',3.00),(8,'Bus','557C',3.50),(9,'Metro','10C',4.50),(10,'Bus','781C',2.70),(11,'Bus','335C',2.80),(12,'Metro','24C',3.50);
/*!40000 ALTER TABLE `core_routes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_stops`
--

DROP TABLE IF EXISTS `core_stops`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_stops` (
  `StopID` int NOT NULL,
  `StopName` varchar(250) NOT NULL,
  `Location` int NOT NULL,
  PRIMARY KEY (`StopID`),
  KEY `core_stops_Location_a77c4a5f_fk_core_locations_LocationID` (`Location`),
  CONSTRAINT `core_stops_Location_a77c4a5f_fk_core_locations_LocationID` FOREIGN KEY (`Location`) REFERENCES `core_locations` (`LocationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_stops`
--

LOCK TABLES `core_stops` WRITE;
/*!40000 ALTER TABLE `core_stops` DISABLE KEYS */;
INSERT INTO `core_stops` VALUES (1,'Riverside Station',1),(2,'Downtown Hub',2),(3,'Harborview Terminal',3),(4,'Millside Junction',4),(5,'Central Square',5),(6,'University Stop',6),(7,'Warehouse Depot',7),(8,'Artist\'s Alley Station',8),(9,'Financial Center Stop',9),(10,'Industrial Hub',10);
/*!40000 ALTER TABLE `core_stops` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (8,'admin','logentry'),(10,'auth','group'),(9,'auth','permission'),(11,'auth','user'),(12,'contenttypes','contenttype'),(1,'core','cabcompanies'),(4,'core','cabfarestructure'),(5,'core','connections'),(2,'core','locations'),(7,'core','routedetails'),(3,'core','routes'),(6,'core','stops'),(13,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-05-24 09:54:37.510737'),(2,'auth','0001_initial','2024-05-24 09:54:39.138718'),(3,'admin','0001_initial','2024-05-24 09:54:39.493109'),(4,'admin','0002_logentry_remove_auto_add','2024-05-24 09:54:39.510111'),(5,'admin','0003_logentry_add_action_flag_choices','2024-05-24 09:54:39.523108'),(6,'contenttypes','0002_remove_content_type_name','2024-05-24 09:54:39.683007'),(7,'auth','0002_alter_permission_name_max_length','2024-05-24 09:54:39.856915'),(8,'auth','0003_alter_user_email_max_length','2024-05-24 09:54:39.879010'),(9,'auth','0004_alter_user_username_opts','2024-05-24 09:54:39.886713'),(10,'auth','0005_alter_user_last_login_null','2024-05-24 09:54:40.020445'),(11,'auth','0006_require_contenttypes_0002','2024-05-24 09:54:40.027369'),(12,'auth','0007_alter_validators_add_error_messages','2024-05-24 09:54:40.039375'),(13,'auth','0008_alter_user_username_max_length','2024-05-24 09:54:40.210583'),(14,'auth','0009_alter_user_last_name_max_length','2024-05-24 09:54:40.353647'),(15,'auth','0010_alter_group_name_max_length','2024-05-24 09:54:40.381556'),(16,'auth','0011_update_proxy_permissions','2024-05-24 09:54:40.390634'),(17,'auth','0012_alter_user_first_name_max_length','2024-05-24 09:54:40.538359'),(18,'core','0001_initial','2024-05-24 09:54:41.636575'),(19,'core','0002_alter_connections_destinationid_and_more','2024-05-24 09:54:42.938593'),(20,'core','0003_alter_cabfarestructure_companyid','2024-05-24 09:54:43.054736'),(21,'core','0004_rename_location_stops_locationid','2024-05-24 09:54:43.063814'),(22,'core','0005_alter_locations_options','2024-05-24 09:54:43.078814'),(23,'core','0006_remove_routedetails_arrivaltime_delete_schedules','2024-05-24 09:54:43.128820'),(24,'core','0007_cabfarestructure_basekm','2024-05-24 09:54:43.180173'),(25,'core','0008_alter_cabcompanies_options_and_more','2024-05-24 09:54:43.193167'),(26,'sessions','0001_initial','2024-05-24 09:54:43.261181');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('o998jfnbp4ceqlxqwfavodi05w3xuidx','eyJ0aW1lIjoiMjAyNC0wNi0yMSAxMToxMTowMCIsImNob2ljZSI6IkJvdGgifQ:1sFYFK:ASCMpjZ_4nAcKRZUlSKOzfnYYDsYVkJEHCQjCEXcFl0','2024-06-21 11:59:02.805274'),('zwt30f0apunaoi5l8l1482qhz4gpsfp2','.eJxVjDkOwjAQRa-CXBNrZpwhS0lBxxkij-3gsMRSlgpxdxwpBbT_vf_eqrPrErt1DlM3eNUqVMffTax7hHED_m7HW9Iujcs0iN4UvdNZX5MPz_Pu_gWinWN-CxOdLBgXyAesDaOhuoHKeMYGsZcmgLBUKNiXvvRMvWANJySqBDzl6DK8Qi4RUFkAFwYPwC1zC5Chi2lwG77YKajPF1NpQhA:1sASAa:TqawfJHkqZxI_417iNMA8XtIzyj8j4Arz3V22FuRmn8','2024-06-07 10:29:04.489894');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'transporthub'
--

--
-- Dumping routines for database 'transporthub'
--
/*!50003 DROP PROCEDURE IF EXISTS `GetLocationNames` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetLocationNames`(
    IN start_id INT,
    IN stop_id INT
)
BEGIN
    SELECT 
        (SELECT LocationName FROM core_locations WHERE LocationID = start_id) AS start_name,
        (SELECT LocationName FROM core_locations WHERE LocationID = stop_id) AS stop_name;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetRouteName` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetRouteName`(
    IN route_id INT
)
BEGIN
    SELECT RouteName
    FROM core_routes
    WHERE RouteID = route_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-10 19:44:43
