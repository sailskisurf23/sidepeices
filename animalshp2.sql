DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS pets;

CREATE TABLE animals
  (
  species VARCHAR(55) PRIMARY KEY,
  vertebrate_class VARCHAR(55),
  appearance VARCHAR(55),
  num_legs INTEGER
  );

CREATE TABLE pets
  (
  name VARCHAR(55) PRIMARY KEY,
  species VARCHAR(55) REFERENCES animals(species),
  owner VARCHAR(55),
  gender VARCHAR(55),
  color VARCHAR(55)
  );

INSERT INTO animals VALUES
  ('cat','mammal','fur',4),
  ('rat','mammal','fur',4),
  ('owl','bird','feathers',2),
  ('snake','reptile','dryscales',0),
  ('toad','amphibian','smoothskin',4),
  ('alligator','reptile','dry scales',4);

INSERT INTO pets VALUES
  ('Nagini','snake','Lord Voldemort','female','green'),
  ('Hedwig','owl','Harry Potter','female','snow white'),
  ('Scabbers','rat','Ron Weasley','male','unspecified'),
  ('Pigwidgeon','owl','Ron Weasley','male','grey'),
  ('Crookshanks','cat','Herminone Granger','male','ginger'),
  ('Mrs Norris','cat','Argus Filch','female','dust-coloured'),
  ('Trevor','toad','Neville Longbottom','male','brown');


select appearance from animals where species = 'rat';

/* Use IN to show the species for animals with vertebrate_class 'mammal' and 'amphibian'. */

select species from animals where vertebrate_class in ('mammal', 'amphibian');

/* Use BETWEEN xxx AND xxx to show species
that have at least 1 leg, but no more than than 3 legs. */

select species from animals where num_legs BETWEEN 1 and 3;

/* Use LIKE 'X' to show species that have an appearance that starts with 'f'. */

select species from animals
where appearance like 'f%';

/* Use CASE to show pet names and a column to indicate whether the pet's name is long or short
(a long name is strictly more than 6 characters long). Filter to select only female pets */

SELECT a,
       CASE WHEN a=1 THEN 'one'
            WHEN a=2 THEN 'two'
            ELSE 'other'
       END
    FROM test;

SELECT name,
  CASE
    WHEN length(name) < 7 THEN 'short'
    WHEN length(name) > 6 THEN 'long'
  END
  FROM pets WHERE gender = 'female'
  ;


/* Use DISTINCT to list the species that can be pets - each species should appear only once. */

select DISTINCT species from pets ;

/* Use COUNT to see how many pets Ron Weasley owns. */

select count(*) from pets where owner = 'Ron Weasley' ;

/*Use string concatenation to output the string:
'Ron Weasley has X pets', where 'X' is the number of pets he has. */

SELECT
'Ron Weasley has ' || count(*) || ' pets'
FROM pets WHERE owner = 'Ron Weasley' ;

/*
Use GROUP BY to count how many pets each owner has.
Give the output as 'NAME has X pets',
with names alphabetically ordered (use ORDER BY).
*/

SELECT owner || ' has ' || count(*) || ' pets'
FROM pets
GROUP BY owner ;

/* Use HAVING to select all owners who have exactly one pet. */

SELECT owner
FROM pets
GROUP BY owner
HAVING count(*) = 1;

/* Use JOIN to display the names of the pets and their vertebrate class. */

SELECT pets.name, animals.vertebrate_class
FROM pets INNER JOIN animals ON animals.species = pets.species ;


/* Now let's find out what our pets look like: list all the pets' names,
their appearance and their color. */

SELECT pets.name, animals.appearance, pets.color
FROM pets INNER JOIN animals ON animals.species = pets.species ;

/* Use WHERE to display the owners of male pets,
the name of the pets and their vertebrate class. */

SELECT pets.owner , pets.name, animals.vertebrate_class
FROM pets INNER JOIN animals ON animals.species = pets.species
WHERE pets.gender = 'male';

/* Use HAVING to select owners who have pets of more than one vertebrate class. */
SELECT pets.owner
FROM pets INNER JOIN animals ON animals.species = pets.species
GROUP BY pets.owner
HAVING COUNT(animals.vertebrate_class) > 1 ;

/* Use HAVING to select owners who have exactly one pet. */

SELECT pets.owner
FROM pets INNER JOIN animals ON animals.species = pets.species
GROUP BY pets.owner
HAVING COUNT(pets.name) = 1 ;

Select owner from pets group by owner having count(name) = 1 ;
