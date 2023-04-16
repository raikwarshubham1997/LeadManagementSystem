-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2022 at 07:59 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `my_lms`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
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
  `is_manager` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `is_manager`) VALUES
(1, 'pbkdf2_sha256$390000$wrMFpd9Bzqxh1k5ncupYVK$xKG3to9tu2gjiWmw7ezmJVpmEjdF++DQk8djgYq8eek=', '2022-12-01 10:17:08.088985', 1, 'mr@shubham123', 'shubham', 'Raikwar', 'raikwarshubham288@gmail.com', 1, 1, '2022-11-17 14:25:16.329387', 0),
(2, 'pbkdf2_sha256$390000$sZw8i2Za4MsmCMvzYUSVpD$fQb6RpVEEMMWpd13Z4me48kl0PK4iX7CtHx3+F2Px80=', '2022-11-30 13:14:31.164815', 0, 'rolf@123', 'Rolf', 'Smith', 'techpanda.sr@gmail.com', 1, 1, '2022-11-17 14:27:26.275662', 0),
(3, 'pbkdf2_sha256$390000$O9GllnMpgjpf0cdjOJI5kW$2VwdkJmX5W+DnRFh7RcqXMkj6G+TCyiHExjUU+dcnzU=', NULL, 0, 'rohit@321', 'Rohit', 'Lowansi', 'rohit@gmail.com', 1, 1, '2022-11-17 14:28:27.634001', 0),
(4, 'pbkdf2_sha256$390000$nURV91RlrjQbUvipw9motR$DvnuLS0/KRaWdojhC9jPgGyqPsCjakaBLr4/oA7j5jw=', '2022-11-30 17:20:28.835650', 0, 'Deepak@123', 'Deepak', 'Lowansi', 'techpanda@gmail.com', 0, 1, '2022-11-17 15:21:33.543657', 1),
(5, 'pbkdf2_sha256$390000$yeg710iHy9OcoOidJMOujb$lWR1qAeDN3pM/GXQftxl1Z0tyLyL8upJZIFVM3+wbBM=', NULL, 0, 'jerry@321', 'Jerry', 'jobs', 'mrglowroad@gmail.com', 0, 1, '2022-11-21 13:16:35.828208', 1),
(6, 'pbkdf2_sha256$390000$7scwJ8kipFHsWzqLq2scOU$fCVyJ3L7BmdNQYSTdRyOVuXm5rKVFWZdiNCByGRcLm0=', NULL, 0, 'shivani@1', 'Shivani', 'Sharma', 'shivani@gmail.com', 0, 1, '2022-11-29 15:52:14.974151', 1),
(7, 'pbkdf2_sha256$390000$56PqJBSVopuxFDBtcqsyvc$Ln5F53qL2yNW7XhB7Y1jRERTFQCC0KH503DlNbwyT1U=', NULL, 0, 'devesh@22', 'Devesh', 'Sarathe', 'dev@gmail.com', 1, 1, '2022-11-29 15:56:01.482714', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
