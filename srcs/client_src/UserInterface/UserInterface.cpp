#include "StdAfx.h"
#include "PythonApplication.h"
#include "ProcessScanner.h"
#include "PythonExceptionSender.h"
#include "resource.h"
#include "Version.h"

#ifdef _DEBUG
#include <crtdbg.h>
#endif

#include "../eterPack/EterPackManager.h"
#include "../eterLib/Util.h"
#include "../CWebBrowser/CWebBrowser.h"
#include "../eterBase/CPostIt.h"

#include "CheckLatestFiles.h"

#include "Hackshield.h"
#include "NProtectGameGuard.h"
#include "WiseLogicXTrap.h"

extern "C" {  
extern int _fltused;  
volatile int _AVOID_FLOATING_POINT_LIBRARY_BUG = _fltused;  
};  
extern "C" { FILE __iob_func[3] = { *stdin,*stdout,*stderr }; }

#pragma comment(linker, "/NODEFAULTLIB:libci.lib")

#pragma comment( lib, "version.lib" )
#pragma comment( lib, "python27.lib" )
#pragma comment( lib, "imagehlp.lib" )
#pragma comment( lib, "devil.lib" )
#pragma comment( lib, "granny2.lib" )
#pragma comment( lib, "mss32.lib" )
#pragma comment( lib, "winmm.lib" )
#pragma comment( lib, "imm32.lib" )
#pragma comment( lib, "oldnames.lib" )
#pragma comment( lib, "SpeedTreeRT.lib" )
#pragma comment( lib, "dinput8.lib" )
#pragma comment( lib, "dxguid.lib" )
#pragma comment( lib, "ws2_32.lib" )
#pragma comment( lib, "strmiids.lib" )
#pragma comment( lib, "ddraw.lib" )
#pragma comment( lib, "dmoguids.lib" )
//#pragma comment( lib, "wsock32.lib" )
#include <stdlib.h>
#include <cryptopp/cryptoppLibLink.h>
bool __IS_TEST_SERVER_MODE__=false;

extern bool SetDefaultCodePage(DWORD codePage);

#ifdef USE_OPENID
extern int openid_test;
#endif

static const char * sc_apszPythonLibraryFilenames[] =
{
	"UserDict.pyc",
	"__future__.pyc",
	"copy_reg.pyc",
	"linecache.pyc",
	"ntpath.pyc",
	"os.pyc",
	"site.pyc",
	"stat.pyc",
	"string.pyc",
	"traceback.pyc",
	"types.pyc",
	"\n",
};

char gs_szErrorString[512] = "";

void ApplicationSetErrorString(const char* szErrorString)
{
	strcpy(gs_szErrorString, szErrorString);
}

bool CheckPythonLibraryFilenames()
{
	for (int i = 0; *sc_apszPythonLibraryFilenames[i] != '\n'; ++i)
	{
		std::string stFilename = "lib\\";
		stFilename += sc_apszPythonLibraryFilenames[i];

		if (_access(stFilename.c_str(), 0) != 0)
		{
			return false;
		}

		MoveFile(stFilename.c_str(), stFilename.c_str());
	}

	return true;
}

struct ApplicationStringTable 
{
	HINSTANCE m_hInstance;
	std::map<DWORD, std::string> m_kMap_dwID_stLocale;
} gs_kAppStrTable;

void ApplicationStringTable_Initialize(HINSTANCE hInstance)
{
	gs_kAppStrTable.m_hInstance=hInstance;
}

const std::string& ApplicationStringTable_GetString(DWORD dwID, LPCSTR szKey)
{
	char szBuffer[512];
	char szIniFileName[256];
	char szLocale[256];

	::GetCurrentDirectory(sizeof(szIniFileName), szIniFileName);
	if(szIniFileName[lstrlen(szIniFileName)-1] != '\\')
		strcat(szIniFileName, "\\");
	strcat(szIniFileName, "metin2client.dat");

	strcpy(szLocale, LocaleService_GetLocalePath());
	if(strnicmp(szLocale, "locale/", strlen("locale/")) == 0)
		strcpy(szLocale, LocaleService_GetLocalePath() + strlen("locale/"));
	::GetPrivateProfileString(szLocale, szKey, NULL, szBuffer, sizeof(szBuffer)-1, szIniFileName);
	if(szBuffer[0] == '\0')
		LoadString(gs_kAppStrTable.m_hInstance, dwID, szBuffer, sizeof(szBuffer)-1);
	if(szBuffer[0] == '\0')
		::GetPrivateProfileString("en", szKey, NULL, szBuffer, sizeof(szBuffer)-1, szIniFileName);
	if(szBuffer[0] == '\0')
		strcpy(szBuffer, szKey);

	std::string& rstLocale=gs_kAppStrTable.m_kMap_dwID_stLocale[dwID];
	rstLocale=szBuffer;

	return rstLocale;
}

const std::string& ApplicationStringTable_GetString(DWORD dwID)
{
	char szBuffer[512];

	LoadString(gs_kAppStrTable.m_hInstance, dwID, szBuffer, sizeof(szBuffer)-1);
	std::string& rstLocale=gs_kAppStrTable.m_kMap_dwID_stLocale[dwID];
	rstLocale=szBuffer;

	return rstLocale;
}

const char* ApplicationStringTable_GetStringz(DWORD dwID, LPCSTR szKey)
{
	return ApplicationStringTable_GetString(dwID, szKey).c_str();
}

const char* ApplicationStringTable_GetStringz(DWORD dwID)
{
	return ApplicationStringTable_GetString(dwID).c_str();
}

////////////////////////////////////////////

int Setup(LPSTR lpCmdLine); // Internal function forward

bool PackInitialize(const char * c_pszFolder)
{
	NANOBEGIN
	if (_access(c_pszFolder, 0) != 0)
		return true;

	std::string stFolder(c_pszFolder);
	stFolder += "/";

	std::string stFileName(stFolder);
	stFileName += "Index";

	CMappedFile file;
	LPCVOID pvData;

	if (!file.Create(stFileName.c_str(), &pvData, 0, 0))
	{
		LogBoxf("FATAL ERROR! File not exist: %s", stFileName.c_str());
		TraceError("FATAL ERROR! File not exist: %s", stFileName.c_str());
		return true;
	}

	CMemoryTextFileLoader TextLoader;
	TextLoader.Bind(file.Size(), pvData);

	bool bPackFirst = TRUE;

	const std::string& strPackType = TextLoader.GetLineString(0);

	if (strPackType.compare("FILE") && strPackType.compare("PACK"))
	{
		TraceError("Pack/Index has invalid syntax. First line must be 'PACK' or 'FILE'");
		return false;
	}

#ifdef _DISTRIBUTE
	Tracef("¾Ë¸²: ÆÑ ¸ğµåÀÔ´Ï´Ù.\n");
	
	//if (0 == strPackType.compare("FILE"))
	//{
	//	bPackFirst = FALSE;
	//	Tracef("¾Ë¸²: ÆÄÀÏ ¸ğµåÀÔ´Ï´Ù.\n");
	//}
	//else
	//{
	//	Tracef("¾Ë¸²: ÆÑ ¸ğµåÀÔ´Ï´Ù.\n");
	//}
#else
	bPackFirst = FALSE;
	Tracef("¾Ë¸²: ÆÄÀÏ ¸ğµåÀÔ´Ï´Ù.\n");
#endif

	CTextFileLoader::SetCacheMode();
#if defined(USE_RELATIVE_PATH)
	CEterPackManager::Instance().SetRelativePathMode();
#endif
	CEterPackManager::Instance().SetCacheMode();
	CEterPackManager::Instance().SetSearchMode(bPackFirst);

	CSoundData::SetPackMode(); // Miles ÆÄÀÏ Äİ¹éÀ» ¼ÂÆÃ

	std::string strPackName, strTexCachePackName;
	for (DWORD i = 1; i < TextLoader.GetLineCount() - 1; i += 2)
	{
		const std::string & c_rstFolder = TextLoader.GetLineString(i);
		const std::string & c_rstName = TextLoader.GetLineString(i + 1);

		strPackName = stFolder + c_rstName;
		strTexCachePackName = strPackName + "_texcache";

		CEterPackManager::Instance().RegisterPack(strPackName.c_str(), c_rstFolder.c_str());
		CEterPackManager::Instance().RegisterPack(strTexCachePackName.c_str(), c_rstFolder.c_str());
	}

	CEterPackManager::Instance().RegisterRootPack((stFolder + std::string("root")).c_str());
	NANOEND
	return true;
}

bool RunMainScript(CPythonLauncher& pyLauncher, const char* lpCmdLine)
{
	initpack();
	initdbg();
	initime();
	initgrp();
	initgrpImage();
	initgrpText();
	initwndMgr();
	/////////////////////////////////////////////
	initudp();
	initapp();
	initsystem();
	initchr();
	initchrmgr();
	initPlayer();
	initItem();
	initNonPlayer();
	initTrade();
	initChat();
	initTextTail();
	initnet();
	initMiniMap();
	initProfiler();
	initEvent();
	initeffect();
	initfly();
	initsnd();
	initeventmgr();
	initshop();
	initskill();
	initquest();
	initBackground();
	initMessenger();
	initsafebox();
	initguild();
	initServerStateChecker();

	NANOBEGIN

	// RegisterDebugFlag
	{
		std::string stRegisterDebugFlag;

#ifdef _DISTRIBUTE 
		stRegisterDebugFlag ="__DEBUG__ = 0";
#else
		stRegisterDebugFlag ="__DEBUG__ = 1"; 
#endif

		if (!pyLauncher.RunLine(stRegisterDebugFlag.c_str()))
		{
			TraceError("RegisterDebugFlag Error");
			return false;
		}
	}

	// RegisterCommandLine
	{
		std::string stRegisterCmdLine;

		const char * loginMark = "-cs";
		const char * loginMark_NonEncode = "-ncs";
		const char * seperator = " ";

		std::string stCmdLine;
		const int CmdSize = 3;
		vector<std::string> stVec;
		SplitLine(lpCmdLine,seperator,&stVec);
		if (CmdSize == stVec.size() && stVec[0]==loginMark)
		{
			char buf[MAX_PATH];	//TODO ¾Æ·¡ ÇÔ¼ö string ÇüÅÂ·Î ¼öÁ¤
			base64_decode(stVec[2].c_str(),buf);
			stVec[2] = buf;
			string_join(seperator,stVec,&stCmdLine);
		}
		else if (CmdSize <= stVec.size() && stVec[0]==loginMark_NonEncode)
		{
			stVec[0] = loginMark;
			string_join(" ",stVec,&stCmdLine);
		}
		else
			stCmdLine = lpCmdLine;

		stRegisterCmdLine ="__COMMAND_LINE__ = ";
		stRegisterCmdLine+='"';
		stRegisterCmdLine+=stCmdLine;
		stRegisterCmdLine+='"';

		const CHAR* c_szRegisterCmdLine=stRegisterCmdLine.c_str();
		if (!pyLauncher.RunLine(c_szRegisterCmdLine))
		{
			TraceError("RegisterCommandLine Error");
			return false;
		}
	}
	{
		vector<std::string> stVec;
		SplitLine(lpCmdLine," " ,&stVec);

		if (stVec.size() != 0 && "--pause-before-create-window" == stVec[0])
		{
#ifdef XTRAP_CLIENT_ENABLE
			if (!XTrap_CheckInit())
				return false;
#endif
			system("pause");
		}
		if (!pyLauncher.RunFile("system.py"))
		{
			TraceError("RunMain Error");
			return false;
		}
	}

	NANOEND
	return true;
}

bool Main(HINSTANCE hInstance, LPSTR lpCmdLine)
{
#ifdef LOCALE_SERVICE_YMIR
	extern bool g_isScreenShotKey;
	g_isScreenShotKey = true;
#endif

	DWORD dwRandSeed=time(NULL)+DWORD(GetCurrentProcess());
	srandom(dwRandSeed);
	srand(random());

	SetLogLevel(1);

#ifdef LOCALE_SERVICE_VIETNAM_MILD
	extern BOOL USE_VIETNAM_CONVERT_WEAPON_VNUM;
	USE_VIETNAM_CONVERT_WEAPON_VNUM = true;
#endif

	if (_access("perf_game_update.txt", 0)==0)
	{
		DeleteFile("perf_game_update.txt");
	}

	if (_access("newpatch.exe", 0)==0)
	{		
		system("patchupdater.exe");
		return false;
	}
#ifndef __VTUNE__
	ilInit();
#endif
	if (!Setup(lpCmdLine))
		return false;

#ifdef _DEBUG
	OpenConsoleWindow();
	OpenLogFile(true); // true == uses syserr.txt and log.txt
#else
	OpenLogFile(false); // false == uses syserr.txt only
#endif

	static CLZO				lzo;
	static CEterPackManager	EterPackManager;

	if (!PackInitialize("pack"))
	{
		LogBox("Pack Initialization failed. Check log.txt file..");
		return false;
	}

	if(LocaleService_LoadGlobal(hInstance))
		SetDefaultCodePage(LocaleService_GetCodePage());

	CPythonApplication * app = new CPythonApplication;

	app->Initialize(hInstance);

	bool ret=false;
	{
		CPythonLauncher pyLauncher;
		CPythonExceptionSender pyExceptionSender;
		SetExceptionSender(&pyExceptionSender);

		if (pyLauncher.Create())
		{
			ret=RunMainScript(pyLauncher, lpCmdLine);	//°ÔÀÓ ½ÇÇàÁß¿£ ÇÔ¼ö°¡ ³¡³ªÁö ¾Ê´Â´Ù.
		}

		//ProcessScanner_ReleaseQuitEvent();
		
		//°ÔÀÓ Á¾·á½Ã.
		app->Clear();

		timeEndPeriod(1);
		pyLauncher.Clear();
	}

	app->Destroy();
	delete app;
	
	return ret;
}

HANDLE CreateMetin2GameMutex()
{
	SECURITY_ATTRIBUTES sa;
	ZeroMemory(&sa, sizeof(SECURITY_ATTRIBUTES));
	sa.nLength				= sizeof(sa);
	sa.lpSecurityDescriptor	= NULL;
	sa.bInheritHandle		= FALSE;

	return CreateMutex(&sa, FALSE, "Metin2GameMutex");
}

void DestroyMetin2GameMutex(HANDLE hMutex)
{
	if (hMutex)
	{
		ReleaseMutex(hMutex);
		hMutex = NULL;
	}
}

void __ErrorPythonLibraryIsNotExist()
{
	LogBoxf("FATAL ERROR!! Python Library file not exist!");
}

bool __IsTimeStampOption(LPSTR lpCmdLine)
{
	const char* TIMESTAMP = "/timestamp";
	return (strncmp(lpCmdLine, TIMESTAMP, strlen(TIMESTAMP))==0);
}

void __PrintTimeStamp()
{
#ifdef	_DEBUG
	if (__IS_TEST_SERVER_MODE__)
		LogBoxf("METIN2 BINARY TEST DEBUG VERSION %s  ( MS C++ %d Compiled )", __TIMESTAMP__, _MSC_VER);
	else
		LogBoxf("METIN2 BINARY DEBUG VERSION %s ( MS C++ %d Compiled )", __TIMESTAMP__, _MSC_VER);
	
#else
	if (__IS_TEST_SERVER_MODE__)
		LogBoxf("METIN2 BINARY TEST VERSION %s  ( MS C++ %d Compiled )", __TIMESTAMP__, _MSC_VER);
	else
		LogBoxf("METIN2 BINARY DISTRIBUTE VERSION %s ( MS C++ %d Compiled )", __TIMESTAMP__, _MSC_VER);			
#endif			
}

bool __IsLocaleOption(LPSTR lpCmdLine)
{
	return (strcmp(lpCmdLine, "--locale") == 0);
}

bool __IsLocaleVersion(LPSTR lpCmdLine)
{
	return (strcmp(lpCmdLine, "--perforce-revision") == 0);
}

#ifdef USE_OPENID
//2012.07.16 ±è¿ë¿í
//ÀÏº» OpenID Áö¿ø. ÀÎÁõÅ° ÀÎÀÚ Ãß°¡
bool __IsOpenIDAuthKeyOption(LPSTR lpCmdLine)
{
	return (strcmp(lpCmdLine, "--openid-authkey") == 0);
}

bool __IsOpenIDTestOption(LPSTR lpCmdLine) //Å¬¶óÀÌ¾ğÆ®¿¡¼­ ·Î±×ÀÎÀÌ °¡´ÉÇÏ´Ù.
{
	return (strcmp(lpCmdLine, "--openid-test") == 0);
}
#endif /* USE_OPENID */

int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	if (strstr(lpCmdLine, "--hackshield") != 0)
		return 0;

#ifdef _DEBUG
	_CrtSetDbgFlag( _CRTDBG_ALLOC_MEM_DF | _CRTDBG_CHECK_CRT_DF | _CRTDBG_LEAK_CHECK_DF );
	//_CrtSetBreakAlloc( 110247 ); 
#endif

	ApplicationStringTable_Initialize(hInstance);

	LocaleService_LoadConfig("locale.cfg");
	SetDefaultCodePage(LocaleService_GetCodePage());	

#ifdef XTRAP_CLIENT_ENABLE
	if (!XTrap_Init())
		return 0;
#endif

#ifdef USE_AHNLAB_HACKSHIELD
	if (!HackShield_Init())
		return 0;
#endif

#ifdef USE_NPROTECT_GAMEGUARD
	if (!GameGuard_Init())
		return 0;
#endif

#if defined(CHECK_LATEST_DATA_FILES)
	if (!CheckLatestFiles())
		return 0;
#endif

	bool bQuit = false;
	bool bAuthKeyChecked = false;	//OpenID ¹öÀü¿¡¼­ ÀÎÁõÅ°°¡ µé¾î¿Ô´ÂÁö ¾Ë±â À§ÇÑ ÀÎÀÚ.
	int nArgc = 0;
	PCHAR* szArgv = CommandLineToArgv( lpCmdLine, &nArgc );

	for( int i=0; i < nArgc; i++ ) {
		if(szArgv[i] == 0)
			continue;
		if (__IsLocaleVersion(szArgv[i])) // #0000829: [M2EU] ¹öÀü ÆÄÀÏÀÌ Ç×»ó »ı±âÁö ¾Êµµ·Ï ¼öÁ¤ 
		{
			char szModuleName[MAX_PATH];
			char szVersionPath[MAX_PATH];
			GetModuleFileName(NULL, szModuleName, sizeof(szModuleName));
			sprintf(szVersionPath, "%s.version", szModuleName);
			FILE* fp = fopen(szVersionPath, "wt");
			if (fp)
			{
				extern int METIN2_GET_VERSION();
				fprintf(fp, "r%d\n", METIN2_GET_VERSION());
				fclose(fp);
			}
			bQuit = true;
		} else if (__IsLocaleOption(szArgv[i]))
		{
			FILE* fp=fopen("locale.txt", "wt");
			fprintf(fp, "service[%s] code_page[%d]", 
				LocaleService_GetName(), LocaleService_GetCodePage());
			fclose(fp);
			bQuit = true;
		} else if (__IsTimeStampOption(szArgv[i]))
		{
			__PrintTimeStamp();
			bQuit = true;
		} else if ((strcmp(szArgv[i], "--force-set-locale") == 0))
		{
			// locale ¼³Á¤¿£ ÀÎÀÚ°¡ µÎ °³ ´õ ÇÊ¿äÇÔ (·ÎÄÉÀÏ ¸íÄª, µ¥ÀÌÅÍ °æ·Î)
			if (nArgc <= i + 2)
			{
				MessageBox(NULL, "Invalid arguments", ApplicationStringTable_GetStringz(IDS_APP_NAME, "APP_NAME"), MB_ICONSTOP);
				goto Clean;
			}

			const char* localeName = szArgv[++i];
			const char* localePath = szArgv[++i];

			LocaleService_ForceSetLocale(localeName, localePath);
		}
#ifdef USE_OPENID
		else if (__IsOpenIDAuthKeyOption(szArgv[i]))	//2012.07.16 OpenID : ±è¿ë¿í
		{
			// ÀÎÁõÅ° ¼³Á¤¿£ ÀÎÀÚ°¡ ÇÑ °³ ´õ ÇÊ¿äÇÔ (ÀÎÁõÅ°)
			if (nArgc <= i + 1)
			{
				MessageBox(NULL, "Invalid arguments", ApplicationStringTable_GetStringz(IDS_APP_NAME, "APP_NAME"), MB_ICONSTOP);
				goto Clean;
			}

			const char* authKey = szArgv[++i];

			//ongoing (2012.07.16)
			//ÀÎÁõÅ° ÀúÀåÇÏ´Â ºÎºĞ
			LocaleService_SetOpenIDAuthKey(authKey);

			bAuthKeyChecked = true;
		}
		else if (__IsOpenIDTestOption(szArgv[i]))
		{
			openid_test = 1;

		}
#endif /* USE_OPENID */
	}

#ifdef USE_OPENID
	//OpenID
	//OpenID Å¬¶óÀÌ¾ğÆ®ÀÇ °æ¿ìÀÎÁõÅ°¸¦ ¹Ş¾Æ¿ÀÁö ¾ÊÀ» °æ¿ì (À¥À» Á¦¿ÜÇÏ°í ½ÇÇà ½Ã) Å¬¶óÀÌ¾ğÆ® Á¾·á.
	
	if (false == bAuthKeyChecked && !openid_test)
	{
		MessageBox(NULL, "Invalid execution", ApplicationStringTable_GetStringz(IDS_APP_NAME, "APP_NAME"), MB_ICONSTOP);
		goto Clean;
	}
#endif /* USE_OPENID */


	if(bQuit)
		goto Clean;

#if defined(NEEDED_COMMAND_ARGUMENT)
	// ¿É¼ÇÀÌ ¾øÀ¸¸é ºñÁ¤»ó ½ÇÇàÀ¸·Î °£ÁÖ, ÇÁ·Î±×·¥ Á¾·á
	if (strstr(lpCmdLine, NEEDED_COMMAND_ARGUMENT) == 0) {
		MessageBox(NULL, ApplicationStringTable_GetStringz(IDS_ERR_MUST_LAUNCH_FROM_PATCHER, "ERR_MUST_LAUNCH_FROM_PATCHER"), ApplicationStringTable_GetStringz(IDS_APP_NAME, "APP_NAME"), MB_ICONSTOP);
			goto Clean;
	}
#endif

#if defined(NEEDED_COMMAND_CLIPBOARD)
	{
		CHAR szSecKey[256];
		CPostIt cPostIt( "VOLUME1" );

		if( cPostIt.Get( "SEC_KEY", szSecKey, sizeof(szSecKey) ) == FALSE ) {
			MessageBox(NULL, ApplicationStringTable_GetStringz(IDS_ERR_MUST_LAUNCH_FROM_PATCHER, "ERR_MUST_LAUNCH_FROM_PATCHER"), ApplicationStringTable_GetStringz(IDS_APP_NAME, "APP_NAME"), MB_ICONSTOP);
			goto Clean;
		}
		if( strstr(szSecKey, NEEDED_COMMAND_CLIPBOARD) == 0 ) {
			MessageBox(NULL, ApplicationStringTable_GetStringz(IDS_ERR_MUST_LAUNCH_FROM_PATCHER, "ERR_MUST_LAUNCH_FROM_PATCHER"), ApplicationStringTable_GetStringz(IDS_APP_NAME, "APP_NAME"), MB_ICONSTOP);
			goto Clean;
		}
		cPostIt.Empty();
	}
#endif

	WebBrowser_Startup(hInstance);

	if (!CheckPythonLibraryFilenames())
	{
		__ErrorPythonLibraryIsNotExist();
		goto Clean;
	}

	Main(hInstance, lpCmdLine);

#ifdef USE_NPROTECT_GAMEGUARD
	GameGuard_NoticeMessage();
#endif

	WebBrowser_Cleanup();

	::CoUninitialize();

	if(gs_szErrorString[0])
		MessageBox(NULL, gs_szErrorString, ApplicationStringTable_GetStringz(IDS_APP_NAME, "APP_NAME"), MB_ICONSTOP);

Clean:
#ifdef USE_AHNLAB_HACKSHIELD
	HackShield_Shutdown();
#endif
	SAFE_FREE_GLOBAL(szArgv);

	return 0;
}

//granny_log_message_origin Origin,
//	char const* File,
//	granny_int32x Line,
//	char const* Message,
//	void* UserData)
//{
//	TraceError("GRANNY: %s", Message);
//}

int Setup(LPSTR lpCmdLine)
{
	/* 
	 *	Å¸ÀÌ¸Ó Á¤¹Ğµµ¸¦ ¿Ã¸°´Ù.
	 */
	TIMECAPS tc; 
	UINT wTimerRes; 

	if (timeGetDevCaps(&tc, sizeof(TIMECAPS)) != TIMERR_NOERROR) 
		return 0;

	wTimerRes = MINMAX(tc.wPeriodMin, 1, tc.wPeriodMax); 
	timeBeginPeriod(wTimerRes); 

	/*
	 *	±×·¡´Ï ¿¡·¯ ÇÚµé¸µ
	 */

	//granny_log_callback Callback;
 //   Callback.Function = GrannyError;
 //   Callback.UserData = 0;
 //   GrannySetLogCallback(&Callback);
	return 1;
}
