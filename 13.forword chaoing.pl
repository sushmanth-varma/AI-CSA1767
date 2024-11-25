% Rules and Facts
fact(a).
fact(b).
rule(c) :- fact(a), fact(b).
rule(d) :- fact(c).

forward_chain(Goal) :-
    fact(Goal);
    (rule(Goal), assert(fact(Goal))).

% Query example:
% ?- forward_chain(d).
