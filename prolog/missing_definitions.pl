%% This file asserts new knowledge into the ontology that can not be retrieved from icubworld.owl due to the open and closed world theorems. 
%% The used namespace is "icubworld" and the object properties are %"hasObjectMaterialType", "hasObjectShapeType", and "hasAttributeShapeType". 
%
%%%%%%%%%%%%%%%%%%%%%%% NEW %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 7 objects with their respective attributes and affordances

:- module(definitions,
    [
	defineCleaningDevice/1,
	%defineCleaningImplement/1,
	defineCleaningPersonal/1,
	defineCleaningTool/1,
	defineCleaningSubstance/1,
	%defineContainer/1,
	defineFoodVessel/1,
	defineDrinkingVessel/1,
	defineEatingVessel/1,
	setDefinitions/1
    ]).

%%% CleaningDevice
defineCleaningDevice(A):-
	owl_subclass_of(A, icubworld:'CleaningDevice'), rdf_assert(A, icubworld:'hasObjectUsedFor', icubworld:'CleaningEvent').

%% CleaningImplement
% no ontologies here because new learned objects could have other attributes

% CleaningPersonal (subclass is Soap)
defineCleaningPersonal(A):-
	owl_subclass_of(A, icubworld:'CleaningPersonal'), rdf_assert(A, icubworld:'hasObjectMaterialType', icubworld:'Clear'), rdf_assert(A, icubworld:'hasObjectShapeType', icubworld:'Rectangular').

% CleaningTool (subclass is Sponge)
defineCleaningTool(A):-
	owl_subclass_of(A, icubworld:'CleaningTool'), rdf_assert(A, icubworld:'hasObjectMaterialType', icubworld:'Wet'), rdf_assert(A, icubworld:'hasObjectShapeType', icubworld:'Rectangular').

%% CleaningSubstance (subclasses are DishwashingDetergent, LaundryDetergent and Sprayer)
defineCleaningSubstance(A):-
	owl_subclass_of(A, icubworld:'CleaningSubstance'), rdf_assert(A, icubworld:'hasObjectMaterialType', icubworld:'Plastic'), rdf_assert(A, icubworld:'hasObjectShapeType', icubworld:'Long').

%%% Container
% no ontologies here because new learned objects could have other attributes

%% FoodVessel
defineFoodVessel(A):-
	owl_subclass_of(A, icubworld:'FoodVessel'), rdf_assert(A, icubworld:'hasObjectMaterialType', icubworld:'Ceramic'), rdf_assert(A, icubworld:'hasObjectShapeType', icubworld:'Round').

% DrinkingVessel (subclass is Cup)
defineDrinkingVessel(A):-
	owl_subclass_of(A, icubworld:'DrinkingVessel'), rdf_assert(A, icubworld:'hasObjectUsedFor', icubworld:'DrinkingEvent').

% EatingVessel (subclass is Plate)
defineEatingVessel(A):-
	owl_subclass_of(A, icubworld:'EatingVessel'), rdf_assert(A, icubworld:'hasObjectUsedFor', icubworld:'EatingEvent').

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Calling setDefinitions in the beginning of the program
setDefinitions(A, B, C, D, E, F, G, H, I):-
	defineCleaningDevice(A),
	%defineCleaningImplement(B),
	defineCleaningPersonal(C),
	defineCleaningTool(D),
	defineCleaningSubstance(E),
	%defineContainer(F),
	defineFoodVessel(G),
	defineDrinkingVessel(H),
	defineEatingVessel(I).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

