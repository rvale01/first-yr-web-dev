

DROP TABLE IF EXISTS users; 

CREATE TABLE users (
  `email` varchar(40) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `surname` varchar(30) DEFAULT NULL,
  `password` varchar(130) DEFAULT NULL,
  `usersType` varchar(40) NOT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

INSERT INTO users VALUES 
  ('admin@admin.com', 'admin', 'admin', '$5$rounds=535000$UFAWyvFJR9RKQEu0$mgAWHvwnejNNVb8lfAF1IRWfueSNqGAw9K.HvL6gS.2', 'dashboard'),
  ('admin@gmail.com', 'rvale09@gmail.com', 'vale', 'vale', '$5$rounds=535000$pn3yoKIaZeFJaRfT$FJYVntlcyY1RTfoGGD/6hhLcOXFUjBm2PtlRTTmIvwA', 'dashboard'),
  ('rvale09@gmail.com', 'rvale09@gmail.com', 'vale', "valentina", '$5$rounds=535000$wPvHledAyG82tj.r$CUC/TdewZICSmnhQNczWURH3EyUKdp3aydaZAGJZf93', 'standard'),
  ('test@gmail.com', 'rvale09@gmail.com', 'Tester', "test", '$5$rounds=535000$082o5T0j4L449C.V$3scHhfN.eaWH69IKw4jquNb.gGY723de5keVzNdd9p5', 'standard');





DROP TABLE IF EXISTS Timetable; 
CREATE TABLE Timetable (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Leaving` varchar(255) DEFAULT NULL,
  `L_Time` time DEFAULT NULL,
  `Arriving` varchar(255) DEFAULT NULL,
  `A_Time` time DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=1027 DEFAULT CHARSET=latin1 COMMENT='Update autoInc'

INSERT INTO Timetable VALUES 
  (1000, 'Newcastle', '16:45:00', 'Bristol', '18:00:00', 140),
  (1001, 'Bristol', '08:00:00', 'Newcastle', '09:15:00', 140),
  (1002, 'Cardiff', '06:00:00', 'Edinburgh', '07:30:00', 120),
  (1003, 'Bristol', '11:30:00', 'Manchester', '12:30:00', 100),
  (1004, 'Manchester', '12:20:00', 'Bristol', '13:20:00', 100),
  (1005, 'Bristol', '07:40:00', 'London', '08:20:00', 100),
  (1006, 'London', '11:00:00', 'Manchester', '12:20:00', 130),
  (1007, 'Manchester', '12:20:00', 'Glasgow', '13:30:00', 130),
  (1008, 'Bristol', '07:40:00', 'Glasgow', '08:45:00', 160),
  (1009, 'Glasgow', '14:30:00', 'Newcastle', '15:45:00', 130),
  (1010, 'Newcastle', '16:15:00', 'Manchester', '17:05:00', 130),
  (1011, 'Manchester', '18:25:00', 'Bristol', '19:30:00', 100),
  (1012, 'Bristol', '06:20:00', 'Manchester', '07:20:00', 100),
  (1013, 'Portsmouth', '12:00:00', 'Dundee', '14:00:00', 180),
  (1014, 'Dundee', '10:00:00', 'Portsmouth', '12:00:00', 180),
  (1025, 'Bristol', '04:41:00', 'Cardiff', '06:40:00', 100),
  (1026, 'Bristol', '17:00:00', 'Bath', '17:30:00', 40);


DROP TABLE IF EXISTS routes_schedule; 
CREATE TABLE routes_schedule (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `id_timetable` int(11) DEFAULT NULL,
  `seats` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_timetable` (`id_timetable`),
  CONSTRAINT `routes_schedule_ibfk_1` FOREIGN KEY (`id_timetable`) REFERENCES `Timetable` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3007 DEFAULT CHARSET=latin1

INSERT INTO routes_schedule VALUES 
  (3001, '2021-05-20', 1000, 200),
  (3002, '2021-05-12', 1000, 138),
  (3003, '2021-05-16', 1001, 134),
  (3004, '2021-05-20', 1003, 201),
  (3005, '2021-05-22', 1004, 180),
  (3006, '2021-05-27', 1026, 200);




DROP TABLE IF EXISTS bookings; 
CREATE TABLE bookings (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_email` varchar(40) DEFAULT NULL,
  `outId` int(11) DEFAULT NULL,
  `inId` int(11) DEFAULT NULL,
  `children` int(11) DEFAULT NULL,
  `adults` int(11) DEFAULT NULL,
  `status` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `client_email` (`client_email`),
  KEY `bookings_ibfk_2` (`outId`),
  KEY `bookings_ibfk_3` (`inId`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`client_email`) REFERENCES `users` (`email`),
  CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`outId`) REFERENCES `routes_schedule` (`id`),
  CONSTRAINT `bookings_ibfk_3` FOREIGN KEY (`inId`) REFERENCES `routes_schedule` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=latin1

INSERT INTO bookings VALUES 
  (2, 'rvale09@gmail.com', 3002, 3003, 2, 1, 'confirmed'),
  (10, 'rvale09@gmail.com', 3002, 3003, 2, 2, 'confirmed'),
  (15, 'rvale09@gmail.com', 3001, "", 0, 2, 'cancelled'),
  (18, 'rvale09@gmail.com', 3001, "", 0, 1, 'confirmed'),
  (19, 'rvale09@gmail.com', 3003, "", 0, 1, 'confirmed'),
  (22, 'rvale09@gmail.com', 3003, "", 0, 1, 'confirmed'),
  (2, 'rvale09@gmail.com', 3003, "", 0, 1, 'confirmed'),
  (2, 'test@gmail.com', 3001, "", 0, 1, 'cancelled'),
  (2, 'test@gmail.com', 3004, 3005, 0, 1, 'cancelled'),
  (2, 'test@gmail.com', 3004, 3005, 1, 1, 'confirmed'),
  (2, 'test@gmail.com', 3003, "", 1, 2, 'confirmed');


DROP TABLE IF EXISTS reports; 
CREATE TABLE reports (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_booking` int(11) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_booking` (`id_booking`),
  CONSTRAINT `reports_ibfk_1` FOREIGN KEY (`id_booking`) REFERENCES `bookings` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1

INSERT INTO reports VALUES 
  (1, 2, 75),
  (2, 10, 15),
  (3, 15, 60),
  (7, 18, 30),
  (8, 19, 30),
  (20, 30, 210),
  (53, 34, 200),
  (54, 36, 400),
  (55, 37, 350);


Commit;