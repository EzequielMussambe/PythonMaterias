CREATE TABLE flights (

    id SERIAL PRIMARY KEY,  
    origin VARCHAR NOT NULL,
    -- noTICE THAT THE NOT NULL REPRESENT THAT THE DATA WILL ONLY BE CREATE 
    -- IF THE VALUE ORIGINN IS AVAILABLE
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);
/* 
NOT NULL
UNIQUE,
PRIMARY KEY
DEFAULT 
CHECK  */

-- insert values--
-- INSERT INTO flights
--     (origin, destination, duration)
--     VALUE("new york", "London", 23)

-- SELECT * FROM flights will select everyhting from flights


-- select count(*) from flights
-- slect AVG(duration) from flight where origin="paris"

-- UPDATE flighs
--     set duration =430
--     where origin='new yor'
--     and destination='lond'

