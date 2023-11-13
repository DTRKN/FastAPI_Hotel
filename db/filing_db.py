filing_hotels = """ INSERT INTO hotels (id, name, location, services, rooms_quantity, image_id)
VALUES
    (1, 'Hotel 1', 'New York', '{"tv": true, "ac": true, "wi-fi": true}', 100, 1),
    (2, 'Hotel 2', 'Los Angeles', '{"tv": true, "ac": true, "wi-fi": true}', 200, 2),
    (3, 'Hotel 3', 'Chicago', '{"tv": true, "ac": true, "wi-fi": true}', 300, 3),
    (4, 'Hotel 4', 'Houston', '{"tv": true, "ac": true, "wi-fi": true}', 400, 4),
    (5, 'Hotel 5', 'San Francisco', '{"tv": true, "ac": true, "wi-fi": true}', 500, 5); """

filing_bookings = """ INSERT INTO bookings (room_id, user_id, date_from, date_to, price)
VALUES
  (1, 1, '2022-01-01', '2022-02-03', 100),
  (5, 2, '2022-01-10', '2022-03-12', 150),
  (1, 3, '2022-02-01', '2022-03-05', 200),
  (5, 4, '2022-03-01', '2022-04-03', 100),
  (3, 4, '2022-04-01', '2022-05-05', 150),
  (6, 2, '2022-05-01', '2022-06-03', 200),
  (2, 4, '2022-06-01', '2022-07-05', 100),
  (4, 4, '2022-07-01', '2022-08-03', 150),
  (9, 3, '2022-08-01', '2022-09-05', 200),
  (8, 1, '2022-09-01', '2022-10-03', 100); """

filing_user = """ INSERT INTO user (id, email, hash_password)
VALUES
    (1, 'user1@example.com', '123456'),
    (2, 'user2@example.com', '234567'),
    (3, 'user3@example.com', '345678'),
    (4, 'user4@example.com', '456789'),
    (5, 'user5@example.com', '567890'); """

filing_rooms = """ INSERT INTO rooms (id, hotel_id, name, description, price, services, quantity, image_id)
VALUES
    (1, 1, 'Single Room', 'A small room with a single bed', 100, '{"tv": true, "ac": true, "wi-fi": true}', 5, 1),
    (2, 1, 'Double Room', 'A larger room with a double bed', 200, '{"tv": true, "ac": true, "wi-fi": true}', 9, 2),
    (3, 2, 'Suite', 'A luxurious suite with a living room and a double bed', 300, '{"tv": true, "ac": true, "wi-fi": true, "minibar": true}', 2, 3),
    (4, 2, 'Family Room', 'A spacious room with a double bed and a sofa bed', 400, '{"tv": true, "ac": true, "wi-fi": true, "minibar": true}', 6, 4),
    (5, 3, 'Deluxe Room', 'A stylish room with a king-size bed and a sitting area', 500, '{"tv": true, "ac": true, "wi-fi": true, "minibar": true}', 3, 5),
    (6, 3, ' Junior Suite', 'A cozy suite with a double bed and a sitting area', 600, '{"tv": true, "ac": true, "wi-fi": true, "minibar": true}', 5, 6),
    (7, 5, 'Executive Room', 'A luxurious room with a king-size bed and a working area', 700, '{"tv": true, "ac": true, "wi-fi": true, "minibar": true}', 2, 7),
    (8, 4, 'Apartment', 'A spacious apartment with a living room, a kitchen, and a double bed', 800, '{"tv": true, "ac": true, "wi-fi": true, "minibar": true}', 12, 8),
    (9, 4, ' Penthouse', 'A luxurious penthouse with a terrace and a double bed', 900, '{"tv": true, "ac": true, "wi-fi": true, "minibar": true}', 5, 9),
    (10, 5, 'Presidential Suite', 'A luxurious suite with a living room, a dining area, and a double bed', 1000, '{"tv": true, "ac": true, "wi-fi": true, "minibar": true}', 13, 10); """

