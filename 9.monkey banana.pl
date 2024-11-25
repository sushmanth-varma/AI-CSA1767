% Monkey and Banana Problem: Monkey wants a banana from a location in the room.

% Actions
move(state(middle, onbox, middle, hasnot),
     grasp,
     state(middle, onbox, middle, has)).

move(state(L, onfloor, L, H),
     climb,
     state(L, onbox, L, H)).

move(state(L1, onfloor, L1, H),
     push(L1, L2),
     state(L2, onfloor, L2, H)).

move(state(L1, onfloor, B, H),
     walk(L1, L2),
     state(L2, onfloor, B, H)).

% Recursive solution
can_get(state(_, _, _, has)).
can_get(State1) :-
    move(State1, _, State2),
    can_get(State2).

% Query example:
% ?- can_get(state(atdoor, onfloor, atwindow, hasnot)).
