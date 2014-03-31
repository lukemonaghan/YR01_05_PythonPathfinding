//\=========================== Clean LMF Python framework - Luke Monaghan
#include "LukeMonaghanFrameworkPython.h"
#include "LukeMonaghanFramework.h"
#include <iostream>
//\=========================== Varibles
int iScreenWidth = 1280, iScreenHeight = 720;
bool bPressed = false;
//\=========================== Main
int main(int argc, const char * argv[]){
	PythonModule pMod;
    FrameworkInitialise("Luke Monaghan - Assignment 6 - Python \"Script it up!\" - A* and Dijkstras", iScreenWidth,iScreenHeight, false);
    LMF_PyInitialise();
    pMod = LMF_ImportPythonModule( "Main" );
    LMF_CallPythonFunction(pMod, "Load","ii",iScreenWidth,iScreenHeight);
    while(FrameworkUpdate()){
        FrameworkClearScreen();
        DeltaTimeSet();
		LMF_CallPythonFunction(pMod,"Update");
		if (KeyDown(KEY_F5) && !bPressed){
			bPressed = true;
			LMF_CallPythonFunction(pMod,"Unload");
			LMF_ReloadPythonModule(pMod);
			LMF_CallPythonFunction(pMod,"Load","ii",iScreenWidth,iScreenHeight);
		}if (KeyUp(KEY_F5)){
			bPressed = false;
		}
		if (KeyDown(KEY_ESC)){
			system("cls");
		}
    }
    LMF_CallPythonFunction(pMod, "Unload");
    FrameworkShutdown();
    return 1+1-1-1;
}
//\=========================== EOF