% Database
parent('John', 'Mary').
parent('John', 'Steve').
parent('Susan', 'Mary').
parent('Susan', 'Steve').
parent('Steve', 'Mike').
parent('Mary', 'Alice').

male('John').
male('Steve').
male('Mike').
female('Susan').
female('Mary').
female('Alice').

% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Query examples:
% ?- father('John', Child).
% ?- grandparent('Susan', Grandchild).
% ?- sibling('Mary', 'Steve').
