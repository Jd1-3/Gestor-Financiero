-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-07-2024 a las 11:52:04
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestor_financiero`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gastos`
--

CREATE TABLE `gastos` (
  `ID` int(11) NOT NULL,
  `Origen` text NOT NULL,
  `Valor` int(10) NOT NULL,
  `Fecha` date NOT NULL,
  `Categoria` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `gastos`
--

INSERT INTO `gastos` (`ID`, `Origen`, `Valor`, `Fecha`, `Categoria`) VALUES
(1, 'Origen1', 100, '2024-07-01', 'prestamos'),
(2, 'Origen2', 200, '2024-07-02', 'Pasajes'),
(3, 'Origen3', 300, '2024-07-03', 'Compras'),
(4, 'Origen4', 400, '2024-07-04', 'Renta'),
(5, 'Origen5', 500, '2024-07-05', 'Transferencia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingresos`
--

CREATE TABLE `ingresos` (
  `ID` int(11) NOT NULL,
  `Origen` varchar(10) NOT NULL,
  `Valor` int(11) NOT NULL,
  `Fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ingresos`
--

INSERT INTO `ingresos` (`ID`, `Origen`, `Valor`, `Fecha`) VALUES
(1, 'Trabajo', 500, '2024-07-01'),
(2, 'Trabajo', 1000, '2024-07-02'),
(3, 'Freelance', 800, '2024-07-03'),
(4, 'Regalo', 500, '2024-07-04'),
(5, 'Empresa', 500, '2024-07-05');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `overview`
--

CREATE TABLE `overview` (
  `ID` int(11) NOT NULL,
  `Ingresos_Totales` int(11) NOT NULL,
  `Gastos_Totales` int(11) NOT NULL,
  `Dinero_Restante` int(11) NOT NULL,
  `Fecha_inicial` date NOT NULL,
  `Fecha_final` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `gastos`
--
ALTER TABLE `gastos`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `ingresos`
--
ALTER TABLE `ingresos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Cantidad` (`Valor`);

--
-- Indices de la tabla `overview`
--
ALTER TABLE `overview`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ingresos`
--
ALTER TABLE `ingresos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
