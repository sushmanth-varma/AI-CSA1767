% Database
student_teacher_sub('Alice', 'Dr. Smith', 'Math101').
student_teacher_sub('Bob', 'Dr. Johnson', 'CS102').
student_teacher_sub('Charlie', 'Dr. Smith', 'Math101').
student_teacher_sub('Diana', 'Dr. Carter', 'Hist201').

% Query examples:
% To find the teacher of a specific subject:
% ?- student_teacher_sub(_, Teacher, 'Math101').
%
% To find students taught by a specific teacher:
% ?- student_teacher_sub(Student, 'Dr. Smith', _).
