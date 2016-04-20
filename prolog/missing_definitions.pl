%% This file asserts new knowledge into the ontology that is not available in objects_affordances_attributes.owl. The used namespace is "niklas" and the object properties are %"hasObjectMaterialType", "hasObjectShapeType", and "hasAttributeShapeType". 
%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% parse OWL files, register name spaces
:- owl_parser:owl_parse('package://niklas_package/owl/niklasComputables.owl').
:- owl_parser:owl_parse('package://niklas_package/owl/objects_affordances_attributes.owl').

:- rdf_db:rdf_register_ns(knowrob, 'http://knowrob.org/kb/knowrob.owl#', [keep(true)]).
:- rdf_db:rdf_register_ns(niklas, 'http://knowrob.org/kb/objects_affordances_attributes.owl#', [keep(true)]).
:- rdf_db:rdf_register_ns(niklasComputables, 'http://knowrob.org/kb/niklasComputables.owl#', [keep(true)]).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% NOT NEEDED:
% create_instance_from_class('http://knowrob.org/kb/objects_affordances_attributes.owl#Cup', 1,X).
% create_instance_from_class('http://knowrob.org/kb/objects_affordances_attributes.owl#DishwashingSoap', 1,X).
% create_instance_from_class('http://knowrob.org/kb/objects_affordances_attributes.owl#LaundryDetergent', 1,X).
% create_instance_from_class('http://knowrob.org/kb/objects_affordances_attributes.owl#Plate', 1,X).
% create_instance_from_class('http://knowrob.org/kb/objects_affordances_attributes.owl#Soap', 1,X).
% create_instance_from_class('http://knowrob.org/kb/objects_affordances_attributes.owl#Sponge', 1,X).
% create_instance_from_class('http://knowrob.org/kb/objects_affordances_attributes.owl#Sprayer', 1,X).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% 7 objects with their respective attributes and affordances

%% Cup
rdf_assert(niklas:'Cup', niklas:'hasObjectMaterialType', niklas:'Ceramic').
rdf_assert(niklas:'Cup', niklas:'hasObjectShapeType', niklas:'Round').
rdf_assert(niklas:'Cup', niklas:'hasObjectUsedFor', niklas:'DrinkingEvent').

%% DishwashingSoap
rdf_assert(niklas:'DishwashingSoap', niklas:'hasObjectMaterialType', niklas:'Plastic').
rdf_assert(niklas:'DishwashingSoap', niklas:'hasObjectShapeType', niklas:'Long').
rdf_assert(niklas:'DishwashingSoap', niklas:'hasObjectUsedFor', niklas:'CleaningEvent').

%% LaundryDetergent
rdf_assert(niklas:'LaundryDetergent', niklas:'hasObjectMaterialType', niklas:'Plastic').
rdf_assert(niklas:'LaundryDetergent', niklas:'hasObjectShapeType', niklas:'Long').
rdf_assert(niklas:'LaundryDetergent', niklas:'hasObjectUsedFor', niklas:'CleaningEvent').

%% Plate
rdf_assert(niklas:'Plate', niklas:'hasObjectMaterialType', niklas:'Ceramic').
rdf_assert(niklas:'Plate', niklas:'hasObjectShapeType', niklas:'Round').
rdf_assert(niklas:'Plate', niklas:'hasObjectUsedFor', niklas:'EatingEvent').

%% Soap
rdf_assert(niklas:'Soap', niklas:'hasObjectMaterialType', niklas:'Clear').
rdf_assert(niklas:'Soap', niklas:'hasObjectShapeType', niklas:'Rectangular').
rdf_assert(niklas:'Soap', niklas:'hasObjectUsedFor', niklas:'CleaningEvent').

%% Sponge
rdf_assert(niklas:'Sponge', niklas:'hasObjectMaterialType', niklas:'Wet').
rdf_assert(niklas:'Sponge', niklas:'hasObjectShapeType', niklas:'Rectangular').
rdf_assert(niklas:'Sponge', niklas:'hasObjectUsedFor', niklas:'CleaningEvent').

%% Sprayer
rdf_assert(niklas:'Sprayer', niklas:'hasObjectMaterialType', niklas:'Plastic').
rdf_assert(niklas:'Sprayer', niklas:'hasObjectShapeType', niklas:'Long').
rdf_assert(niklas:'Sprayer', niklas:'hasObjectUsedFor', niklas:'CleaningEvent').

