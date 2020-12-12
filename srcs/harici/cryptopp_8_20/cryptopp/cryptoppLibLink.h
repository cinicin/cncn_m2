#ifndef _CRYPTOPPLIBLINK_H_
#define _CRYPTOPPLIBLINK_H_

#ifdef _DLL
#ifndef CRYPTOPP_IMPORTS
#define CRYPTOPP_IMPORTS
#endif
#endif

#if defined(CRYPTOPP_IMPORTS)
#include "dll.h"
#else
    #ifdef _WIN32
        #ifndef _DEBUG
            #pragma comment( lib, "cryptlib_release.lib" )
        #else
            #pragma comment( lib, "cryptlib_debug.lib" )
        #endif
    #endif
#endif

#endif /* !_CRYPTOPPLIBLINK_H_ */
