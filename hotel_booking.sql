-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 17, 2024 at 12:09 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_booking`
--

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `payment_type` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`payment_type`) VALUES
('Cash'),
('Online'),
('Online'),
('Online');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `First_Name` varchar(15) NOT NULL,
  `Last_Name` varchar(15) NOT NULL,
  `Title` varchar(7) NOT NULL,
  `Email` varchar(25) NOT NULL,
  `Phone_Number` varchar(11) NOT NULL,
  `Terms_Accepted` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`First_Name`, `Last_Name`, `Title`, `Email`, `Phone_Number`, `Terms_Accepted`) VALUES
('Izzaty', 'Mat Nazer', 'Ms.', 'izzaty@gmail.com', '01241456798', 'Accepted'),
('Rabiatul', 'Sanusi', 'Ms.', 'rabiatul@gmail.com', '0136169837', 'Accepted'),
('Ahmad', 'Naim', 'Mr.', 'ahmadnaim11@gmail.com', '0128849126', 'Accepted'),
('Amri', 'Amsyar', 'Mr.', 'amriamsyar@gmail.com', '01124141266', 'Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `room_selection`
--

CREATE TABLE `room_selection` (
  `date_booking` date NOT NULL,
  `days` int(11) NOT NULL,
  `room_type` varchar(10) NOT NULL,
  `total_price` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room_selection`
--

INSERT INTO `room_selection` (`date_booking`, `days`, `room_type`, `total_price`) VALUES
('2024-02-05', 1, 'Single Roo', '300'),
('2024-02-20', 3, 'King Room', '2100'),
('2024-02-20', 3, 'Queen Room', '1500'),
('2024-03-01', 2, 'Suite Room', '2400');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
