create database local_event_finder;
USE local_event_finder;


CREATE TABLE IF NOT EXISTS users (
  user_id int(11) NOT NULL auto_increment,
  user_name varchar(255) NOT NULL,
  mobile varchar(20) NOT NULL,
  email varchar(255) NOT NULL,
  password varchar(255) NOT NULL,
  Address varchar(50) default NULL,
  created_at timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (user_id),
  UNIQUE KEY email (email)
) ;


CREATE TABLE service_city (
  service_city_id INT AUTO_INCREMENT PRIMARY KEY,
  city_pincode VARCHAR(10) UNIQUE NOT NULL,
  city_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE services_category (
  category_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  category_name VARCHAR(255) NOT NULL UNIQUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE servicers_details (
  servicers_user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  servicers_name VARCHAR(255) NOT NULL,
  servicers_mobile VARCHAR(20) NOT NULL UNIQUE,
  servicers_email VARCHAR(255) NOT NULL UNIQUE,
  servicers_address VARCHAR(255) DEFAULT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE servicers (
  servicers_id INT AUTO_INCREMENT PRIMARY KEY,
  servicers_user_id INT NOT NULL,
  category_id INT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (servicers_user_id) REFERENCES servicers_details(servicers_user_id) ON DELETE CASCADE,
  FOREIGN KEY (category_id) REFERENCES services_category(category_id) ON DELETE CASCADE
);



  CREATE TABLE service (
  service_id INT AUTO_INCREMENT PRIMARY KEY,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT NOT NULL,
  service_price DECIMAL(10,2) NOT NULL CHECK (service_price >= 0),
  service_image TEXT NOT NULL,
  city_pincode VARCHAR(10) NOT NULL,
  service_address VARCHAR(255) NOT NULL,
  category_id INT NOT NULL,
  servicers_user_id INT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (servicers_user_id) REFERENCES servicers_details(servicers_user_id) ON DELETE CASCADE,
  FOREIGN KEY (city_pincode) REFERENCES service_city(city_pincode) ON DELETE CASCADE
);


CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT NOT NULL,
    user_id INT NOT NULL,
    booker_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mobile VARCHAR(15) NOT NULL,
    address TEXT NOT NULL,
    category_name varchar(255) NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    guests INT DEFAULT NULL,
    dj_name VARCHAR(100) DEFAULT NULL,
    theme VARCHAR(255) DEFAULT NULL,
    birthday_age INT DEFAULT NULL,
    
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE booking_status (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    status VARCHAR(255) DEFAULT "PENDING",
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);



CREATE TABLE reviews (
  id INT AUTO_INCREMENT PRIMARY KEY,
  service_id INT NOT NULL,
  user_id INT NOT NULL,
  rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
  review TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE,
  foreign key (user_id) REFERENCES users{user_id}
  
);


DELIMITER //

CREATE TRIGGER tr_service_details_insert 
AFTER INSERT ON service 
FOR EACH ROW
BEGIN
  INSERT INTO servicers (servicers_user_id, category_id) 
  VALUES (NEW.servicers_user_id, NEW.category_id);
END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER booking_status_insert 
AFTER INSERT ON bookings 
FOR EACH ROW
BEGIN
    INSERT INTO booking_status (booking_id) VALUES (NEW.booking_id);
END //

DELIMITER ;
