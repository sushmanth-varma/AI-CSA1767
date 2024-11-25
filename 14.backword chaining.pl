% Rules and Facts
fact(a).
fact(b).
rule(c) :- fact(a), fact(b).
rule(d) :- rule(c).

backward_chain(Goal) :-
    fact(Goal);
    rule(Goal).

% Query example:
% ?- backward_chain(d).
% ?- backward_chain(c).
