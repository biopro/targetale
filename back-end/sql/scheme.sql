/** CONSTRUCT DATABASE **/

DROP DATABASE IF EXISTS targetale;
CREATE DATABASE targetale;
USE targetale;

/** DEFINE TABLES **/


CREATE TABLE projects (

    id int primary key auto_increment,
    user text not null,
    submissionDate date  not null,
    status text  not null,
    inputFile BLOB  not null,
    promoterome text  not null

);