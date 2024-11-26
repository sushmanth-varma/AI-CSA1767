% Facts and Rules
happy(X) :- pass(X, history), win(X, lottery). % Anyone passing history and winning the lottery is happy.
pass(X, exams) :- study(X); lucky(X).         % Anyone who studies or is lucky passes all exams.
lucky(john).                                  % John is lucky.
pass(john, history) :- lucky(john).           % Derived: John can pass history since he is lucky.
win(X, lottery) :- lucky(X).                  % Anyone who is lucky wins the lottery.

% Query to prove that John is happy:
% happy(john).  % Output: true
