CREATE DATABASE cotonwate;

use cotonwate


CREATE TABLE  vetements (
    id INT auto_increment primary key,
    NUID VARCHAR(30) NOT NULL,
    intitule VARCHAR(100) NOT NULL,
    couleur VARCHAR(100) NOT NULL,
    taille VARCHAR(100) NOT NULL,
    marque VARCHAR(100) NOT NULL,
    prix VARCHAR(100) NOT NULL,
    enStock VARCHAR(100) NOT NULL,
    date_add DATE,
    date_update DATE,
) ENGINE=INNODB;

