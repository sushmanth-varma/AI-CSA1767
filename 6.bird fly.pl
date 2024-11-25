% Database
bird('sparrow').
bird('penguin').
bird('ostrich').

can_fly('sparrow').
cannot_fly('penguin').
cannot_fly('ostrich').

% Rules
can_bird_fly(Bird) :- can_fly(Bird), write(Bird), write(' can fly.').
can_bird_fly(Bird) :- cannot_fly(Bird), write(Bird), write(' cannot fly.').

% Query example:
% ?- can_bird_fly('sparrow').
% ?- can_bird_fly('penguin').
