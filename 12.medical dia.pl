% Medical Diagnosis Database
symptom(fever, flu).
symptom(cough, flu).
symptom(fatigue, flu).
symptom(headache, cold).
symptom(sneezing, cold).
symptom(runny_nose, cold).

diagnosis(Symptoms, Disease) :-
    findall(Disease, (member(Symptom, Symptoms), symptom(Symptom, Disease)), Diseases),
    list_to_set(Diseases, PossibleDiseases),
    length(PossibleDiseases, 1),
    Disease = PossibleDiseases.

% Query example:
% ?- diagnosis([fever, cough, fatigue], Disease).
% ?- diagnosis([sneezing, runny_nose], Disease).
