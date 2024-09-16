-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: programacoes_de_filmes
-- ------------------------------------------------------
-- Server version	8.0.39

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

--
-- Table structure for table `canal`
--

DROP TABLE IF EXISTS `canal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `canal` (
  `num_canal` int NOT NULL,
  `nome` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `sigla` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`num_canal`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canal`
--

LOCK TABLES `canal` WRITE;
/*!40000 ALTER TABLE `canal` DISABLE KEYS */;
INSERT INTO `canal` VALUES (1,'HBO','HBO'),(2,'Cinemax','CMX'),(3,'Telecine','TC'),(4,'TNT','TNT'),(5,'FOX','FOX'),(6,'Netflix','NFLX'),(7,'Amazon Prime','AMZN'),(8,'Disney+','DIS+'),(9,'AMC','AMC'),(10,'Syfy','SYF'),(11,'FX','FX'),(12,'Star Channel','STAR'),(13,'Sony','SONY'),(14,'HBO Max','HBOM'),(15,'Paramount+','PAR+'),(16,'Apple TV+','APL+');
/*!40000 ALTER TABLE `canal` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `canal_before_insert` BEFORE INSERT ON `canal` FOR EACH ROW BEGIN
    IF NEW.nome = 'Proibido' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Inserção bloqueada: Nome do canal não permitido.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `exibicao`
--

DROP TABLE IF EXISTS `exibicao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exibicao` (
  `num_filme` int NOT NULL,
  `num_canal` int NOT NULL,
  `data_exibicao` datetime NOT NULL,
  PRIMARY KEY (`num_filme`,`num_canal`,`data_exibicao`),
  KEY `num_canal` (`num_canal`),
  CONSTRAINT `exibicao_ibfk_1` FOREIGN KEY (`num_canal`) REFERENCES `canal` (`num_canal`) ON UPDATE CASCADE,
  CONSTRAINT `exibicao_ibfk_2` FOREIGN KEY (`num_filme`) REFERENCES `filme` (`num_filme`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exibicao`
--

LOCK TABLES `exibicao` WRITE;
/*!40000 ALTER TABLE `exibicao` DISABLE KEYS */;
INSERT INTO `exibicao` VALUES (1,1,'2024-09-01 20:00:00'),(5,1,'2024-09-09 20:00:00'),(2,2,'2024-09-03 21:00:00'),(5,2,'2024-09-10 21:00:00'),(1,3,'2024-09-02 22:00:00'),(6,3,'2024-09-11 22:00:00'),(2,4,'2024-09-04 19:00:00'),(6,4,'2024-09-12 19:30:00'),(3,5,'2024-09-05 20:30:00'),(7,5,'2024-09-13 20:30:00'),(3,6,'2024-09-06 23:00:00'),(7,6,'2024-09-14 21:00:00'),(4,7,'2024-09-07 18:00:00'),(8,7,'2024-09-15 18:00:00'),(4,8,'2024-09-08 17:30:00'),(8,8,'2024-09-16 17:00:00'),(9,9,'2024-09-17 20:00:00'),(10,10,'2024-09-18 21:00:00'),(11,11,'2024-09-19 22:00:00'),(12,12,'2024-09-20 19:00:00'),(13,13,'2024-09-21 20:30:00'),(14,14,'2024-09-22 21:30:00'),(15,15,'2024-09-23 18:00:00'),(16,16,'2024-09-24 17:00:00');
/*!40000 ALTER TABLE `exibicao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filme`
--

DROP TABLE IF EXISTS `filme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `filme` (
  `num_filme` int NOT NULL,
  `titulo_original` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `titulo_brasil` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ano_lancamento` year NOT NULL,
  `pais_origem` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `categoria` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `duracao` int NOT NULL,
  PRIMARY KEY (`num_filme`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filme`
--

LOCK TABLES `filme` WRITE;
/*!40000 ALTER TABLE `filme` DISABLE KEYS */;
INSERT INTO `filme` VALUES (1,'The Godfather','O Poderoso Chefão',1972,'USA','Crime',175),(2,'The Dark Knight','O Cavaleiro das Trevas',2008,'USA','Action',152),(3,'Inception','A Origem',2010,'USA','Sci-Fi',148),(4,'Parasite','Parasita',2019,'South Korea','Thriller',132),(5,'Interstellar','Interestelar',2014,'USA','Sci-Fi',169),(6,'Joker','Coringa',2019,'USA','Drama',122),(7,'Avatar','Avatar',2009,'USA','Adventure',162),(8,'Titanic','Titanic',1997,'USA','Romance',195),(9,'Fight Club','Clube da Luta',1999,'USA','Drama',139),(10,'Pulp Fiction','Pulp Fiction',1994,'USA','Crime',154),(11,'The Matrix','Matrix',1999,'USA','Sci-Fi',136),(12,'Forrest Gump','Forrest Gump: O Contador de Histórias',1994,'USA','Drama',142),(13,'Gladiator','Gladiador',2000,'USA','Action',155),(14,'The Shawshank Redemption','Um Sonho de Liberdade',1994,'USA','Drama',142),(15,'Inglourious Basterds','Bastardos Inglórios',2009,'USA','War',153),(16,'The Avengers','Os Vingadores',2012,'USA','Action',143);
/*!40000 ALTER TABLE `filme` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-14 17:05:03
