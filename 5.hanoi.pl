% Move n disks from Source to Destination using Auxiliary
hanoi(0, _, _, _) :- !.
hanoi(N, Source, Destination, Auxiliary) :-
    N > 0,
    N1 is N - 1,
    hanoi(N1, Source, Auxiliary, Destination),
    write('Move disk from '), write(Source), write(' to '), write(Destination), nl,
    hanoi(N1, Auxiliary, Destination, Source).

% Query example:
% ?- hanoi(3, 'A', 'C', 'B').
