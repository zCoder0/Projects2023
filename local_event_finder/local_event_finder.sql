-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.0.27-community-nt - MySQL Community Edition (GPL)
-- Server OS:                    Win32
-- HeidiSQL Version:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for local_event_finder
CREATE DATABASE IF NOT EXISTS `local_event_finder` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `local_event_finder`;

-- Dumping structure for table local_event_finder.bookings
CREATE TABLE IF NOT EXISTS `bookings` (
  `booking_id` int(11) NOT NULL auto_increment,
  `service_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `booker_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `address` text NOT NULL,
  `category_name` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `guests` int(11) default NULL,
  `dj_name` varchar(100) default NULL,
  `theme` varchar(255) default NULL,
  `birthday_age` int(11) default NULL,
  PRIMARY KEY  (`booking_id`),
  KEY `service_id` (`service_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`service_id`) REFERENCES `service` (`service_id`) ON DELETE CASCADE,
  CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table local_event_finder.booking_status
CREATE TABLE IF NOT EXISTS `booking_status` (
  `status_id` int(11) NOT NULL auto_increment,
  `booking_id` int(11) NOT NULL,
  `status` varchar(255) default 'PENDING',
  `created_at` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`status_id`),
  KEY `booking_id` (`booking_id`),
  CONSTRAINT `booking_status_ibfk_1` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`booking_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table local_event_finder.reviews
CREATE TABLE IF NOT EXISTS `reviews` (
  `id` int(11) NOT NULL auto_increment,
  `service_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `review` text NOT NULL,
  `created_at` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`id`),
  KEY `service_id` (`service_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`service_id`) REFERENCES `service` (`service_id`) ON DELETE CASCADE,
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table local_event_finder.service
CREATE TABLE IF NOT EXISTS `service` (
  `service_id` int(11) NOT NULL auto_increment,
  `service_name` varchar(255) NOT NULL,
  `service_description` text NOT NULL,
  `service_price` decimal(10,2) NOT NULL,
  `service_image` text NOT NULL,
  `city_pincode` varchar(10) NOT NULL,
  `service_address` text NOT NULL,
  `category_id` int(11) default NULL,
  `servicers_user_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`service_id`),
  KEY `servicers_user_id` (`servicers_user_id`),
  KEY `city_pincode` (`city_pincode`),
  CONSTRAINT `service_ibfk_1` FOREIGN KEY (`servicers_user_id`) REFERENCES `servicers_details` (`servicers_user_id`) ON DELETE CASCADE,
  CONSTRAINT `service_ibfk_2` FOREIGN KEY (`city_pincode`) REFERENCES `service_city` (`city_pincode`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table local_event_finder.servicers_details
CREATE TABLE IF NOT EXISTS `servicers_details` (
  `servicers_user_id` int(11) NOT NULL auto_increment,
  `servicers_name` varchar(255) NOT NULL,
  `servicers_mobile` varchar(20) NOT NULL,
  `servicers_email` varchar(255) NOT NULL,
  `servicers_password` varchar(50) default NULL,
  `servicers_address` varchar(255) default NULL,
  `created_at` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`servicers_user_id`),
  UNIQUE KEY `servicers_mobile` (`servicers_mobile`),
  UNIQUE KEY `servicers_email` (`servicers_email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table local_event_finder.services_category
CREATE TABLE IF NOT EXISTS `services_category` (
  `category_id` int(11) NOT NULL auto_increment,
  `category_name` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`category_id`),
  UNIQUE KEY `category_name` (`category_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table local_event_finder.service_city
CREATE TABLE IF NOT EXISTS `service_city` (
  `service_city_id` int(11) NOT NULL auto_increment,
  `city_pincode` varchar(10) NOT NULL,
  `city_name` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`service_city_id`),
  UNIQUE KEY `city_pincode` (`city_pincode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table local_event_finder.service_details
CREATE TABLE IF NOT EXISTS `service_details` (
  `servicers_id` int(11) NOT NULL auto_increment,
  `servicers_user_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`servicers_id`),
  KEY `servicers_user_id` (`servicers_user_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `service_details_ibfk_1` FOREIGN KEY (`servicers_user_id`) REFERENCES `servicers_details` (`servicers_user_id`) ON DELETE CASCADE,
  CONSTRAINT `service_details_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `services_category` (`category_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table local_event_finder.users
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(11) NOT NULL auto_increment,
  `user_name` varchar(25) NOT NULL,
  `user_email` varchar(25) NOT NULL,
  `user_password` varchar(25) NOT NULL,
  `user_mobile` varchar(50) NOT NULL,
  `reg_date` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`user_id`),
  UNIQUE KEY `user_email` (`user_email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for trigger local_event_finder.booking_status_insert
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
