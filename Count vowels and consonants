% Helper rule to define vowels
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Rule to count vowels in a list of characters
count_vowels([], 0). % Base case: empty list has 0 vowels
count_vowels([H|T], Count) :- 
    vowel(H), 
    count_vowels(T, RestCount), 
    Count is RestCount + 1. % Increment count if the head is a vowel

count_vowels([H|T], Count) :- 
    \+ vowel(H), 
    count_vowels(T, Count). % Skip non-vowel characters

% Rule to process a string
vowels_in_string(String, Count) :- 
    string_chars(String, CharList),  % Convert string to character list
    count_vowels(CharList, Count).  % Count vowels in the character list

% Example Query:
% vowels_in_string("This is my first Degree in Saveetha School of Engineering.", Count).
% Output: Count = 18
