/** CONSTRUCT DATABASE **/

DROP DATABASE IF EXISTS targetale;
CREATE DATABASE targetale;
USE targetale;

/** DEFINE TABLES **/


CREATE TABLE projects (

    id int primary key auto_increment,
    userEmail text not null,
    submissionDate date  not null,
    finishedDate date,
    status text  not null,
    inputFilePath text not null,
    inputFileFormat text not null,
    promoterome text not null

);


