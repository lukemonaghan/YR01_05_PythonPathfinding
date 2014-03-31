//---------------------------
//------ Luke Monaghan ------
//---------------------------
#ifndef _PYTHON_H_
#define _PYTHON_H_
//--------------------------- ExportImport
#if defined (_WIN32)
    #ifdef LUKEMONAGHANFW_EXPORTS
        #define LUKEMONAGHANFW __declspec(dllexport)
    #else
        #define LUKEMONAGHANFW __declspec(dllimport)
    #endif  
#endif
#if defined(__APPLE__) || defined(__MACH__)
	#define LUKEMONAGHANFW __attribute__((visibility("default")))
#endif
//--------------------------- Python
#include <Python.h>
//--------------------------- Check we are on windows
#if defined(_WIN32)
	#define __func__ __FUNCTION__
#endif
//--------------------------- Python Functions
LUKEMONAGHANFW bool      LMF_PyInitialise();
LUKEMONAGHANFW bool      LMF_PyInitialise( int argc, char* argv[]);
LUKEMONAGHANFW PyObject* LMF_ImportPythonModule( const char* a_pyModuleName);
LUKEMONAGHANFW void      LMF_ReloadPythonModule( PyObject* a_pModule);
LUKEMONAGHANFW bool      LMF_CallPythonFunction( PyObject* a_pModule, char* cs_FunctionName);
LUKEMONAGHANFW bool		 LMF_CallPythonFunction( PyObject* a_pModule, char* cs_FunctionName,char* VarTypes,...);
//-- TypeDefs
typedef PyObject* PythonModule;
//--------------------------- End of Functions
#endif