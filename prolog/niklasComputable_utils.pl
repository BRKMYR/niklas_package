:- module(niklasComputables_utils,
    [
	detectObject/4, 	
	comp_onTopTable/2,
	comp_newInstance/2,
	create_instance_from_class/3,
	check_MaterialType/2,
	check_ShapeType/2,
	check_AffordanceType/2
    ]).

:- use_module(library('semweb/rdfs')).
:- use_module(library('semweb/rdf_db')).
:- use_module(library('owl')).
:- use_module(library('owl_parser')).
:- use_module(library('rdfs_computable')).
:- use_module(library('knowrob_objects')).

%:- owl_parser:owl_parse('package://niklas_package/owl/icubworld.owl').
:- rdf_db:rdf_register_ns(icubworld, 'http://www.semanticweb.org/niklas/ontologies/2016/3/icubworld.owl#', [keep(true)]).
:- rdf_db:rdf_register_ns(niklasComputables, 'http://knowrob.org/kb/niklasComputables.owl#', [keep(true)]).


%%%%%%%%%%%%%% Costum computables %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%% Property computables %%%%%%%%%%%%%%%%%%%%%%%%

%% Check which objects have a certain material type (Ceramic, Plastic, Clear), shape and attribute.
%%% detectObject(?Obj, ?Material, ?Shape, ?Attribute) is nondet.
%
% @param Obj     Object instance of interest
% @param Material_str    Material type of the objects
% @param Shape_str       Shape type of the objects
% @param Affordance_str  Affordance type of the objects
% 
%
detectObject(Obj, Material_str, Shape_str, Affordance_str):-
	%rdf_assert(Obj, icubworld:hasObjectMaterialType, icubworld:Material_str), rdf_assert(Obj, icubworld:hasObjectShapeType, icubworld:Shape_str), rdf_assert(Obj, icubworld:hasObjectUsedFor, icubworld:Affordance_str).
	rdf_assert(A, icubworld:hasObjectMaterialType, icubworld:'Ceramic'), rdf_assert(A, icubworld:hasObjectShapeType, icubworld:'Round'), rdf_assert(A, icubworld:hasObjectUsedFor, icubworld:'EatingEvent').

	write('detectObject function successful: '), write(Obj), nl.

%% Check which objects have a certain material type (Ceramic, Plastic, Clear).
%%% check_MaterialType(?Obj, ?ValueNewObj) is nondet.
%
% @param Obj     Object instance of interest
% @param ValueNewObj    Material type of the objects
% 
%
check_MaterialType(Obj, MaterialValue):-
	owl_has(Obj, icubworld:hasObjectMaterialType, X), owl_individual_of(X, icubworld:MaterialValue).

	%write('check_MaterialType function successful: '), write(Obj), nl.

%% Check which objects have a certain shape type (Long, round, rectangular).
%%% check_ShapeType(?Obj, ?ValueNewObj) is nondet.
%
% @param Obj     Object instance of interest
% @param ValueNewObj    Shape type of the objects
% 
%
check_ShapeType(Obj, ShapeValue):-
	owl_has(Obj, icubworld:hasObjectShapeType, X), owl_individual_of(X, icubworld:ShapeValue).

	%write('check_ShapeType function successful: '), write(Obj), nl.

%% Check which objects have a certain material type (Ceramic, Plastic, Clear).
%%% check_MaterialType(?Obj, ?ValueNewObj) is nondet.
%
% @param Obj     Object instance of interest
% @param ValueNewObj    Affordance type of the objects
% 
%
check_AffordanceType(Obj, AffordanceValue):-
	owl_has(Obj, icubworld:hasObjectAffordanceType, X), owl_individual_of(X, icubworld:AffordanceValue).

	%write('check_AffordanceType function successful: '), write(Obj), nl.




%% Compare the Z position of the objects to determine if they are on-top of the table
%%% comp_onTopTable(?Obj, ?ValueNewObj) is nondet.
%
% Find all Objects that are onTop of the table and retreive their Z positions
%
% @param Obj     Object instance of interest
% @param ValueNewObj    Z position of the detected object
% 
%
comp_onTopTable(Obj, ValueNewObj):-
	owl_has(A, knowrob:objectActedOn, Obj), 
	owl_has(A, knowrob:eventOccursAt, Robj),
	owl_has(Robj, knowrob:m23, ValueObj), 
	strip_literal_type(ValueObj, ValueNewObj),
	atom_to_term(ValueNewObj, TermObjZ, _),

 	owl_individual_of(Table,  knowrob:'KitchenTable'),
	owl_has(Atable, knowrob:objectActedOn, Table),
	owl_has(Atable, knowrob:eventOccursAt, Vtable),
	owl_has(Vtable, knowrob:m23, ValueTable), 
	strip_literal_type(ValueTable, ValueNewTable),
	atom_to_term(ValueNewTable, TermTableZ, _),
	
    	TermObjZ>TermTableZ,

	write('Found an object on top of the table: '), write(Obj), nl.


%%%%%%%%%% Class computables %%%%%%%%%%%%%%%%%%%%%%%%
% this computable will create a new instance of the given class
% In this particular example, it will be of the Class 'Cup'
%
% comp_newInstance(?Instance, +Class) is nondet.
% @param Class		represents the name of the class where the instance will be created. 
%			The class has to be given as inout argument. Class could be of two forms: 
%			Class='http://www.semanticweb.org/niklas/ontologies/2016/3/icubworld.owl#Cup' (the desired URL)
%			Class='Cup'  <- if this is chosen then it will be created in Knowrob ontology
% @param Instance	asserted new instance

comp_newInstance(Instance, 'Cup'):-
	% We need to specify the ID of the new instance,
	% in this case it will always be '50'
	ID='50',
	create_instance_from_class('http://www.semanticweb.org/niklas/ontologies/2016/3/icubworld.owl#Cup', ID, Instance).
	

% This function will create an instance of a desired class
% create_instance_from_class(+Class, +Instance_ID, ?Instance)
% The created instance will have the predicate/property rdf:type 
% to correctly inheritate the properties of its super-classes
%
% @param Class		represents the name of the class where the instance will be created. 
%			Class could be of two forms: 
%			Class='http://www.semanticweb.org/niklas/ontologies/2016/3/icubworld.owl#Cup' (the desired URL)
%			Class='Cup'  <- if this is chosen then it will be created in Knowrob ontology
% @param Instance_ID	is the new ID that the instance will have
% @param Instance	asserted new instance

create_instance_from_class(Class, Instance_ID, Instance) :-
	% We need to find out if the Class has URL or not
	((concat_atom(List, '#', Class),length(List,Length),Length>1) ->
	( % Class has already a URI
	   Class_path=Class );
	  % When the class does not have URL, will get the icubworld path
	(atom_concat('http://www.semanticweb.org/niklas/ontologies/2016/3/icubworld.owl#', Class, Class_path),
	write(Class_path), nl
 	)),
	% Create the path of the new instance
	atom_concat(Class_path,  '_', Class2),
	atom_concat(Class2, Instance_ID, Instance),
	
	% assert/create the new instance
	rdf_assert(Instance, rdf:type, Class_path).


