person('John', '1990-01-15').
person('Alice', '1985-06-23').
person('Bob', '1992-12-05').

find_person(Name, DOB) :- person(Name, DOB).
