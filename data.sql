-- MySQL dump 10.13 Distrib 8.0.32, for Win64 (x86_64)

--

-- Host: localhost Database: searchtable

-- ------------------------------------------------------

-- Server version 8.0.32

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

-- Table structure for table `buy`

--

DROP TABLE IF EXISTS `buy`;

/*!40101 SET @saved_cs_client = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE `buy` (

`Books` varchar(50) DEFAULT NULL,

`Book_Number` int unsigned DEFAULT NULL,

`Price` double DEFAULT NULL,

`Book_Quantity` int unsigned DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--

-- Dumping data for table `buy`

--

LOCK TABLES `buy` WRITE;

/*!40000 ALTER TABLE `buy` DISABLE KEYS */;

INSERT INTO `buy` VALUES ('More Peak District',101,12.99,0),('Lincoinshire Worlds',102,10.99,32),('Value Of York',103,11.99,1),('Peak District',104,12.99,3),('Snowdonia',105,13.99,0),('Malvern and Warwickshire',106,10.99,35),('Cheshire',107,12.99,1);

/*!40000 ALTER TABLE `buy` ENABLE KEYS */;

UNLOCK TABLES;

--

-- Table structure for table `search`

--

DROP TABLE IF EXISTS `search`;

/*!40101 SET @saved_cs_client = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE `search` (

`Id` int NOT NULL AUTO_INCREMENT,

`Area` varchar(50) DEFAULT NULL,

`Book` varchar(100) DEFAULT NULL,

`WalkName` varchar(100) DEFAULT NULL,

`Distance` double DEFAULT NULL,

`Difficult` varchar(50) DEFAULT NULL,

`Page` int unsigned DEFAULT NULL,

PRIMARY KEY (`Id`)

) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--

-- Dumping data for table `search`

--

LOCK TABLES `search` WRITE;

/*!40000 ALTER TABLE `search` DISABLE KEYS */;

INSERT INTO `search` VALUES (1,'peakdistrict','More Peak District','Hathasage',7,'Easy',67),(2,'peakdistrict','More Peak District','Hope and Win Hill',4.5,'Medium',18),(3,'lincoinshire','Lincolnshire Worlds','Thornton Abbey',3.5,'Easy',20),(4,'lincoinshire','Lincolnshire Worlds','Tennyson County',5,'Hard',28),(5,'york','Value of York','Cowlam and Cotham',8,'Hard',64),(6,'york','Value of York','Friedaythorpe',7,'Easy',42),(7,'peakdistrict','Peak District','Magpie Mine',4.5,'Medium',20),(8,'peakdistrict','Peak District','Loard\'s Seat',5.5,'Easy',28),(9,'northwales','Snowdonia','Around Aber',4,'hard',24),(10,'northwales','Snowdonia','Yr Eifl',3.5,'Medium',42),(11,'warwickshire','Malvern and Warwickshire','Bidford-Upon-Avon',8.5,'Medium',78),(12,'cheshire','Cheshire','Dane Valley',5,'Easy',20),(13,'cheshire','Cheshire','Malpas',8.5,'Medium',80),(14,'cheshire','Cheshire','Farndon',6,'Hard',48),(15,'cheshire','Cheshire','Delamere Forest',5.5,'Easy',30);

/*!40000 ALTER TABLE `search` ENABLE KEYS */;

UNLOCK TABLES;

--

-- Table structure for table `users`

--

DROP TABLE IF EXISTS `users`;

/*!40101 SET @saved_cs_client = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE `users` (

`UserName` varchar(50) DEFAULT NULL,

`portofuser` int unsigned DEFAULT NULL,

`books_buy` int unsigned DEFAULT NULL,

`Total_Cost` int unsigned DEFAULT NULL,

`Back_order` int unsigned DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--

-- Dumping data for table `users`

--

LOCK TABLES `users` WRITE;

/*!40000 ALTER TABLE `users` DISABLE KEYS */;

INSERT INTO `users` VALUES ('P',62043,5,0,0),('ja',49305,11,112,0),('P',62043,5,0,0),('joao',60257,8,91,0),('manu',60297,9,91,0),('john',60337,9,0,0),('jon',60338,9,0,0),('kyle',60351,5,70,3),('artur',60393,6,69,0),('qq',60406,2,25,0),('ber',60418,7,89,0),('llll',60434,2,24,0),('luna',60444,7,77,0),('bart ',60463,2,22,0),('uuuu',60479,2,22,0),('ooaoao',60498,2,22,0),('madeli',60499,2,22,0),('jn',60500,7,77,0),('jo',59547,2,22,0),('pppp',59609,2,22,0),('rrrr',59655,2,22,0),('xzx',59692,2,22,0),('za',59695,23,55,0),('y',59698,8,88,0);

/*!40000 ALTER TABLE `users` ENABLE KEYS */;

UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;

/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;

/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */