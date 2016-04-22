#include <string>
#include <iostream>
 
#include <ros/ros.h>
#include <json_prolog/prolog.h>
#include <stdio.h>

#include <yarp/os/all.h>
#include <yarp/os/Network.h>
#include <yarp/os/Port.h>
#include <yarp/os/Bottle.h>
#include <yarp/os/Time.h>
 
using namespace std;
using namespace json_prolog;
using namespace yarp::os;

int main(int argc, char *argv[])
{
  ros::init(argc, argv, "test_json_prolog");
 
  Prolog pl;
 
  //////////////////////////////////////////////////////////////////////////////////////////////////
  // TEST to setup KB correctly...
  // Cup
  PrologQueryProxy bdgs1 =pl.query("rdf_assert(niklas:'Cup', niklas:'hasObjectMaterialType', niklas:'Ceramic').");
  PrologQueryProxy bdgs2 =pl.query("rdf_assert(niklas:'Cup', niklas:'hasObjectShapeType', niklas:'Round').");
  PrologQueryProxy bdgs3 =pl.query("rdf_assert(niklas:'Cup', niklas:'hasObjectUsedFor', niklas:'DrinkingEvent').");

  // DishwashingSoap
  PrologQueryProxy bdgs4 =pl.query("rdf_assert(niklas:'DishwashingSoap', niklas:'hasObjectMaterialType', niklas:'Plastic').");
  PrologQueryProxy bdgs5 =pl.query("rdf_assert(niklas:'DishwashingSoap', niklas:'hasObjectShapeType', niklas:'Long').");
  PrologQueryProxy bdgs6 =pl.query("rdf_assert(niklas:'DishwashingSoap', niklas:'hasObjectUsedFor', niklas:'CleaningEvent').");

  // LaundryDetergent
  PrologQueryProxy bdgs7 =pl.query("rdf_assert(niklas:'LaundryDetergent', niklas:'hasObjectMaterialType', niklas:'Plastic').");
  PrologQueryProxy bdgs8 =pl.query("rdf_assert(niklas:'LaundryDetergent', niklas:'hasObjectShapeType', niklas:'Long').");
  PrologQueryProxy bdgs9 =pl.query("rdf_assert(niklas:'LaundryDetergent', niklas:'hasObjectUsedFor', niklas:'CleaningEvent').");

  // Plate
  PrologQueryProxy bdgs10 =pl.query("rdf_assert(niklas:'Plate', niklas:'hasObjectMaterialType', niklas:'Ceramic').");
  PrologQueryProxy bdgs11 =pl.query("rdf_assert(niklas:'Plate', niklas:'hasObjectShapeType', niklas:'Round').");
  PrologQueryProxy bdgs12 =pl.query("rdf_assert(niklas:'Plate', niklas:'hasObjectUsedFor', niklas:'EatingEvent').");

  // Soap
  PrologQueryProxy bdgs13 =pl.query("rdf_assert(niklas:'Soap', niklas:'hasObjectMaterialType', niklas:'Clear').");
  PrologQueryProxy bdgs14 =pl.query("rdf_assert(niklas:'Soap', niklas:'hasObjectShapeType', niklas:'Rectangular').");
  PrologQueryProxy bdgs15 =pl.query("rdf_assert(niklas:'Soap', niklas:'hasObjectUsedFor', niklas:'CleaningEvent').");

  // Sponge
  PrologQueryProxy bdgs16 =pl.query("rdf_assert(niklas:'Sponge', niklas:'hasObjectMaterialType', niklas:'Wet').");
  PrologQueryProxy bdgs17 =pl.query("rdf_assert(niklas:'Sponge', niklas:'hasObjectShapeType', niklas:'Rectangular').");
  PrologQueryProxy bdgs18 =pl.query("rdf_assert(niklas:'Sponge', niklas:'hasObjectUsedFor', niklas:'CleaningEvent').");

  // Sprayer
  PrologQueryProxy bdgs19 =pl.query("rdf_assert(niklas:'Sprayer', niklas:'hasObjectMaterialType', niklas:'Plastic').");
  PrologQueryProxy bdgs20 =pl.query("rdf_assert(niklas:'Sprayer', niklas:'hasObjectShapeType', niklas:'Long').");
  PrologQueryProxy bdgs21 =pl.query("rdf_assert(niklas:'Sprayer', niklas:'hasObjectUsedFor', niklas:'CleaningEvent').");
  ////////////////////////////////////////////////////////////////////////////////////////////////


  Network yarp;
  Network::init();

  BufferedPort<Bottle> port1, port2, port3, port4;
  port1.close(); port2.close(); port3.close(); port4.close();
  
  port1.open("/Prolog_object");  // Object
  port2.open("/Prolog_material");  // Material
  port3.open("/Prolog_shape");  // Shape
  port4.open("/Prolog_affordance");  // Affordance

  int check1=0, check2=0, check3=0, check4=0;

  // INIT: Regardless which values in the beginning	
  string Material_ = "";
  string Shape_ = ""; 
  string Affordance_ = "";


  // Start WHILE-SCHLEIFE
  while(true){
  	
	//if(yarp.isConnected("/GURLS_material_out", "/Prolog_material")==false){//yarp.connect("/Caffe_object_out", "/Prolog_object");}  	
	if(yarp.isConnected("/GURLS_material_out", "/Prolog_material")==false){yarp.connect("/GURLS_material_out", "/Prolog_material");}
  	if(yarp.isConnected("/GURLS_shape_out", "/Prolog_shape")==false){yarp.connect("/GURLS_shape_out", "/Prolog_shape");}
  	if(yarp.isConnected("/GURLS_affordance_out", "/Prolog_affordance")==false){yarp.connect("/GURLS_affordance_out", "/Prolog_affordance");}

	//Bottle *input1 = port1.read();
	Bottle *input2 = port2.read();
	Bottle *input3 = port3.read();
	Bottle *input4 = port4.read();

	//if(input1 !=NULL) {string Object_ = input1->toString(); check1=1;}      
	if(input2 !=NULL) {Material_ = input2->toString(); check2=1;}    
	if(input3 !=NULL) {Shape_ = input3->toString(); check3=1;}       
	if(input4 !=NULL) {Affordance_ = input4->toString(); check4=1;}  

	if(check1+check2+check3+check4 > 0) {cout << "Check1: "<< check1<< ", Check2: "<< check2<< ", Check3: "<< check3<< ", Check4: "<< check4 << endl;}

	if((check2 == 1) && (check3 == 1) && (check4 == 1) )  {        
		
		// Retreiving the right object.... 
		string query_m;
		// Currently not working:
		// query_m = "rdf_assert(A, niklas:hasObjectMaterialType, niklas:'"+ Material_ +"'), rdf_assert(A, niklas:hasObjectShapeType, niklas:'"+ Shape_ +"'), rdf_assert(A, niklas:hasObjectUsedFor, niklas:'" + Affordance_ + "').";
		query_m = "owl_has(A, niklas:'hasObjectMaterialType', niklas:'"+ Material_ +"'), owl_has(A, niklas:'hasObjectShapeType', niklas:'"+ Shape_ +"'), owl_has(A, niklas:'hasObjectUsedFor', niklas:'" + Affordance_ + "').";
            
		cout << "Inputs received. Starting Prolog query." << endl;

		PrologQueryProxy bdgs = pl.query(query_m);
		//cout <<"Object is: " + Object_ << endl;
		cout <<"Material is: " + Material_ << endl;
		cout <<"Shape is: " + Shape_ << endl;
		cout <<"Affordance is: " + Affordance_ << endl;

		int found_sol=0;
		
		for(PrologQueryProxy::iterator it=bdgs.begin(); it != bdgs.end(); it++)
  		{
    			PrologBindings bdg = *it;
    			cout << "Found solution: " << (bool)(it == bdgs.end()) << endl;
		    	cout << "A = " << bdg["A"] << endl;
    			//cout << "B = " << bdg["B"] << endl;
    			//cout << "C = " << bdg["C"] << endl;
			found_sol=1;
		}

		if(found_sol==0){
			
			string bool_learn_object, Object_, bool_material, bool_shape, bool_affordance;
			cout << "No solution found. Do you want to learn the new object? (yes/no)" << endl;
			getline(cin, bool_learn_object);
			
			if(bool_learn_object == "yes") {
				cout << "Please write the correct name of the object:" << endl;
				getline(cin, Object_);
							
				cout << "Is Material:"+Material_+" correct? (yes/no)"<< endl;
				getline(cin, bool_material);
				if(bool_material=="no"){
					cout << "Please enter the correct material:"<< endl;
					getline(cin, Material_);
				}
			
				cout << "Is Shape:"+Shape_+" correct? (yes/no)" << endl;
				getline(cin, bool_shape);
				if(bool_shape=="no"){
					cout << "Please enter the correct shape:"<< endl;
					getline(cin, Shape_);
				}
				
				cout << "Is Affordance:"+Affordance_+" correct? (yes/no)" << endl;
				getline(cin, bool_affordance);
				if(bool_affordance=="no"){
					cout << "Please enter the correct affordance:"<< endl;
					getline(cin, Affordance_);
				}			

              		 	// If new object: manual data entry!		
				query_m = "rdf_assert(niklas:'"+ Object_ +"', niklas:'hasObjectMaterialType', niklas:'"+ Material_ +"')";
				PrologQueryProxy bdgs__assert_1 = pl.query(query_m);
				query_m = "rdf_assert(niklas:'"+ Object_ +"', niklas:'hasObjectShapeType', niklas:'"+ Shape_ +"')";
				PrologQueryProxy bdgs__assert_2 = pl.query(query_m);
				query_m = "rdf_assert(niklas:'"+ Object_ +"', niklas:'hasObjectUsedFor', niklas:'" + Affordance_ + "').";
				PrologQueryProxy bdgs__assert_3 = pl.query(query_m);

            
				cout << Object_ +" is being learnt... Starting Prolog query." << endl;
				// Currently not working:
				//query_m = "rdf_assert(A, niklas:'hasObjectMaterialType', niklas:'"+ Material_ +"'), rdf_assert(A, niklas:'hasObjectShapeType', niklas:'"+ Shape_ +"'), rdf_assert(A, niklas:'hasObjectUsedFor', niklas:'" + Affordance_ + "').";
				query_m = "owl_has(A, niklas:'hasObjectMaterialType', niklas:'"+ Material_ +"'), owl_has(A, niklas:'hasObjectShapeType', niklas:'"+ Shape_ +"'), owl_has(A, niklas:'hasObjectUsedFor', niklas:'" + Affordance_ + "').";

				PrologQueryProxy bdgs__assert_answer = pl.query(query_m);

				for(PrologQueryProxy::iterator it=bdgs__assert_answer.begin(); it != bdgs__assert_answer.end(); it++)
  				{
    					PrologBindings bdg = *it;
    					cout << "Found solution: " << (bool)(it == bdgs__assert_answer.end()) << endl;
				    	cout << "A = " << bdg["A"] << endl;
    				}

				cout << "Exporting object class into OWL-file..." << endl;
				PrologQueryProxy bdgs__export_class = pl.query("export_object_class(niklas:'"+Object_+"', '/home/niklas/catkin_ws/src/niklas_package/owl/Learned_Objects/"+Object_+"_Class.owl').");
			}
		}
        } 
 
  }

  return 0;
}
