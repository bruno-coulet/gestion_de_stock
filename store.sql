DROP DATABASE IF EXISTS store;
CREATE DATABASE store;

USE store;

CREATE TABLE `product` (
  `id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT ,
  `name` varchar(255) ,
  `description` text,
  `price` int,
  `quantity` int,
  `id_category` int
);

CREATE TABLE `category` (
  `id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT ,
  `name` varchar(255)
);