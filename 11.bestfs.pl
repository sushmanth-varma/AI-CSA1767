% Best-First Search

% Example graph with costs
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 2).
edge(c, d, 4).
edge(c, e, 2).
edge(d, goal, 1).
edge(e, goal, 5).

% Heuristic values
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 5).
heuristic(d, 2).
heuristic(e, 6).
heuristic(goal, 0).

% Best-first search
best_first_search(Node, Path, Goal) :-
    best_first([[Node]], Goal, Path).

best_first([[Goal | Path] | _], Goal, [Goal | Path]).
best_first([CurrentPath | OtherPaths], Goal, FinalPath) :-
    extend(CurrentPath, NewPaths),
    append(OtherPaths, NewPaths, AllPaths),
    sort(AllPaths, SortedPaths),
    best_first(SortedPaths, Goal, FinalPath).

extend([Node | Path], NewPaths) :-
    findall([NewNode, Node | Path],
            (edge(Node, NewNode, _), \+ member(NewNode, [Node | Path])),
            NewPaths).

% Query example:
% ?- best_first_search(a, Path, goal).
