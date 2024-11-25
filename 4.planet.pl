% Database
planet('Mercury', 57.91, 0.330, 'No').
planet('Venus', 108.2, 4.87, 'No').
planet('Earth', 149.6, 5.97, 'Yes').
planet('Mars', 227.9, 0.642, 'No').
planet('Jupiter', 778.5, 1898, 'No').
planet('Saturn', 1434, 568, 'No').
planet('Uranus', 2871, 86.8, 'No').
planet('Neptune', 4495, 102, 'No').

% Query examples:
% To find planets with life:
% ?- planet(Name, _, _, 'Yes').
%
% To find planets within a certain distance from the Sun:
% ?- planet(Name, Distance, _, _), Distance < 300.
