//---------------------------
//------ Luke Monaghan ------
//---------------------------
#ifndef LUKEMONAGHANFW_H_
#define LUKEMONAGHANFW_H_
//--------------------------- ExportImport
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
//--------------------------- Framework Controller
LUKEMONAGHANFW bool FrameworkInitialise(char* title, unsigned int width, unsigned int height , bool fullscreen, float fLeftOff = 0.0f, float fRightOff = 1.0f, float fBottomOff = 1.0f, float fTopOff = 0.0f);
LUKEMONAGHANFW bool FrameworkUpdate();
LUKEMONAGHANFW void FrameworkClearScreen();
LUKEMONAGHANFW void FrameworkBGColour(float r,float g,float b,float a);
LUKEMONAGHANFW void FrameworkWindowResize(int width, int height);
LUKEMONAGHANFW void FrameworkFullscreen(bool fullscr);
LUKEMONAGHANFW void FrameworkBlendMode(int i_Begin, int i_Final, int i_Equation);
LUKEMONAGHANFW void FrameworkShutdown();
//--------------------------- Camera
LUKEMONAGHANFW void CameraMove(float xoff, float yoff);
LUKEMONAGHANFW void CameraRotate(float angle);
LUKEMONAGHANFW void CameraZoom(float amount);
//--------------------------- Image
LUKEMONAGHANFW int          SpriteLoad  (char* path, int width = 0, int height = 0,int xoffset = 0, int yoffset = 0);					        
LUKEMONAGHANFW void         SpriteMove  (int SpriteID, float x, float y, float depth = 50.0f);
LUKEMONAGHANFW void         SpriteRotate(int SpriteID, float angle, bool add = true);
LUKEMONAGHANFW void         SpriteScale (int SpriteID, float xscale, float yscale);
LUKEMONAGHANFW void         SpriteResize(int SpriteID, int width, int height);
LUKEMONAGHANFW void         SpriteUVset (int SpriteID, float uMin, float vMin, float uMax, float vMax);
LUKEMONAGHANFW void         SpriteColour(int SpriteID, float f_Red, float f_Green, float f_Blue, float f_Alpha);
LUKEMONAGHANFW void         SpriteDraw  (int SpriteID,bool Camera0_world1 = 0);
LUKEMONAGHANFW void         SpriteUnload(int SpriteID);
//--------------------------- Particle Emitters
LUKEMONAGHANFW unsigned int ParticleEmitterLoad(int SpriteID);
LUKEMONAGHANFW unsigned int ParticleEmitterLoad(int SpriteID, float startx, float starty,float startdepth, float endx, float endy, float enddepth, float lifetimeinsec);
LUKEMONAGHANFW void         ParticleEmitterUnload(unsigned int EmitterID);
LUKEMONAGHANFW void         ParticleEmitterPerStep    (unsigned int EmitterID, float amount);
LUKEMONAGHANFW void         ParticleEmitterSetPosition(unsigned int EmitterID, float x     , float y     , float depth, bool start0_end1);
LUKEMONAGHANFW void         ParticleEmitterSetSize    (unsigned int EmitterID, float Width , float Height             , bool start0_end1);
LUKEMONAGHANFW void         ParticleEmitterSetColour  (unsigned int EmitterID, float f_Red, float f_Green, float f_Blue, float f_Alpha, bool start0_end1);
LUKEMONAGHANFW void         ParticleEmitterSetOffset  (unsigned int EmitterID, int i_XOffset, int i_YOffset);
LUKEMONAGHANFW void		    ParticleEmitterSetRotation(unsigned int EmitterID, float f_AmountPerStep,bool start0_end1);
LUKEMONAGHANFW void         ParticleEmitterDraw(int EmitterID,bool Camera0_world1);
//--------------------------- Model
LUKEMONAGHANFW int  ModelLoad  (char* path);
LUKEMONAGHANFW void ModelMove  (int ModelID, float x, float y, float depth = 0.0f);
LUKEMONAGHANFW void ModelRotate(int ModelID, float angle, bool add = true);
LUKEMONAGHANFW void ModelScale (int ModelID, float xscale, float yscale);
LUKEMONAGHANFW void ModelResize(int ModelID, int width, int height);
LUKEMONAGHANFW void ModelDraw  (int ModelID,bool Camera0_world1);
LUKEMONAGHANFW void ModelUnload(int ModelID);
//--------------------------- Fonts
LUKEMONAGHANFW int  FontLoad(char* path);
LUKEMONAGHANFW void FontUnload(int FontID);
LUKEMONAGHANFW void FontColour(int FontID, float f_Red, float f_Green, float f_Blue, float f_Alpha);
LUKEMONAGHANFW void DrawString(int FontID,char* string,float x, float y,bool Camera0_world1 = 0,float depth = 0.0f,bool center = false);
LUKEMONAGHANFW void DrawInt   (int FontID,int Value   ,float x, float y,bool Camera0_world1 = 0,float depth = 0.0f,bool center = false);
LUKEMONAGHANFW void DrawFloat (int FontID,float Value ,float x, float y,bool Camera0_world1 = 0,float depth = 0.0f,bool center = false);
//--------------------------- Shaders
LUKEMONAGHANFW int  ShaderLoad(char* relativepath);
LUKEMONAGHANFW void ShaderUse (int ShaderID);
LUKEMONAGHANFW void ShaderUnload(int ShaderID);
//--------------------------- ID's
LUKEMONAGHANFW int  GetDefaultShaderID();
LUKEMONAGHANFW int  GetDefaultFontID();
LUKEMONAGHANFW int  GetInstanceCount();
//--------------------------- MISC
LUKEMONAGHANFW void VSyncSet(int mode);
//--------------------------- DeltaTime
LUKEMONAGHANFW void  DeltaTimeSet();
LUKEMONAGHANFW float DeltaTimeGet();
//--------------------------- FPS
LUKEMONAGHANFW float FPSGet();
LUKEMONAGHANFW float FPSAvGet();
//---------------------------
LUKEMONAGHANFW void lineDraw();/////////////////////////////////NO IN YET!!!
//--------------------------- Key Checking
LUKEMONAGHANFW int KeyDown(int key);
LUKEMONAGHANFW int KeyUp(int key);
LUKEMONAGHANFW int KeyPressed(int key);//UNUSED
LUKEMONAGHANFW int KeyReleased(int key);//UNUSED
//--------------------------- Mouse Position Getting
LUKEMONAGHANFW void MousePosGet(int &x, int &y);
LUKEMONAGHANFW void MousePosSet(int  x, int  y);
//--------------------------- Mouse Button Checking
LUKEMONAGHANFW int MouseDown(int MouseButton);
LUKEMONAGHANFW int MouseUp(int MouseButton);
LUKEMONAGHANFW int MousePressed(int MouseButton);//UNUSED
LUKEMONAGHANFW int MouseReleased(int MouseButton);//UNUSED
//--------------------------- Scrollwheel
LUKEMONAGHANFW int  MouseScrollGet();
//--------------------------- Sound
#if defined(_WIN32)
LUKEMONAGHANFW unsigned int SoundLoad(char* path);
LUKEMONAGHANFW void         SoundUnload(unsigned int SoundSourceID);
LUKEMONAGHANFW void			SoundRestart(bool sndmngr = false);
LUKEMONAGHANFW void			SoundShutdown();
//--------------------------- Controls
LUKEMONAGHANFW unsigned int SoundPlay(unsigned int SoundSourceID,bool loop = false,float volume = 1.0f, float speed = 1.0f);
LUKEMONAGHANFW void         SoundPause(unsigned int SoundInstanceID);
LUKEMONAGHANFW void         SoundResume(unsigned int SoundInstanceID);
LUKEMONAGHANFW void         SoundStop(unsigned int SoundInstanceID);
//--------------------------- Volume
LUKEMONAGHANFW void			SoundVolume(unsigned int SoundInstanceID,float value);
LUKEMONAGHANFW void			SoundSpeed (unsigned int SoundInstanceID,float value);
//--------------------------- Advanced features
LUKEMONAGHANFW void			SoundLoop(unsigned int SoundInstanceID);
LUKEMONAGHANFW void			SoundVolumeMain(float value);
LUKEMONAGHANFW void			SoundStopAll();
LUKEMONAGHANFW void			SoundPauseAll(bool paused = true);
//--------------------------- Xbox Input
LUKEMONAGHANFW unsigned int ControllerAdd();
LUKEMONAGHANFW void         ControllerRemove(unsigned int ControllerID);

LUKEMONAGHANFW bool		    ControllerConnected(unsigned int ControllerID);
						    
LUKEMONAGHANFW bool		    ControllerButton     (unsigned int ControllerID,int ButtonID);
LUKEMONAGHANFW bool		    ControllerThumbstick (unsigned int ControllerID,bool L0_R1,bool X0_Y1,float &ReturnVal);
LUKEMONAGHANFW bool		    ControllerTrigger    (unsigned int ControllerID,bool L0_R1,float &ReturnVal);
LUKEMONAGHANFW void		    ControllerVibrate    (unsigned int ControllerID,unsigned short leftamount = 65535,unsigned short rightamount = 65535);
#endif
//--------------------------- INIT VARS
typedef enum {
//--------------------------- Keyboard Special Keys
KEY_UNKNOWN       =  -1,
KEY_SPACE         =  32,
KEY_SPECIAL       =  256,
KEY_ESC           =  KEY_SPECIAL+1,
KEY_F1            =  KEY_SPECIAL+2,
KEY_F2            =  KEY_SPECIAL+3,
KEY_F3            =  KEY_SPECIAL+4,
KEY_F4            =  KEY_SPECIAL+5,
KEY_F5            =  KEY_SPECIAL+6,
KEY_F6            =  KEY_SPECIAL+7,
KEY_F7            =  KEY_SPECIAL+8,
KEY_F8            =  KEY_SPECIAL+9,
KEY_F9            =  KEY_SPECIAL+10,
KEY_F10           =  KEY_SPECIAL+11,
KEY_F11           =  KEY_SPECIAL+12,
KEY_F12           =  KEY_SPECIAL+13,
KEY_F13           =  KEY_SPECIAL+14,
KEY_F14           =  KEY_SPECIAL+15,
KEY_F15           =  KEY_SPECIAL+16,
KEY_F16           =  KEY_SPECIAL+17,
KEY_F17           =  KEY_SPECIAL+18,
KEY_F18           =  KEY_SPECIAL+19,
KEY_F19           =  KEY_SPECIAL+20,
KEY_F20           =  KEY_SPECIAL+21,
KEY_F21           =  KEY_SPECIAL+22,
KEY_F22           =  KEY_SPECIAL+23,
KEY_F23           =  KEY_SPECIAL+24,
KEY_F24           =  KEY_SPECIAL+25,
KEY_F25           =  KEY_SPECIAL+26,
KEY_UP            =  KEY_SPECIAL+27,
KEY_DOWN          =  KEY_SPECIAL+28,
KEY_LEFT          =  KEY_SPECIAL+29,
KEY_RIGHT         =  KEY_SPECIAL+30,
KEY_LSHIFT        =  KEY_SPECIAL+31,
KEY_RSHIFT        =  KEY_SPECIAL+32,
KEY_LCTRL         =  KEY_SPECIAL+33,
KEY_RCTRL         =  KEY_SPECIAL+34,
KEY_LALT          =  KEY_SPECIAL+35,
KEY_RALT          =  KEY_SPECIAL+36,
KEY_TAB           =  KEY_SPECIAL+37,
KEY_ENTER         =  KEY_SPECIAL+38,
KEY_BACKSPACE     =  KEY_SPECIAL+39,
KEY_INSERT        =  KEY_SPECIAL+40,
KEY_DEL           =  KEY_SPECIAL+41,
KEY_PAGEUP        =  KEY_SPECIAL+42,
KEY_PAGEDOWN      =  KEY_SPECIAL+43,
KEY_HOME          =  KEY_SPECIAL+44,
KEY_END           =  KEY_SPECIAL+45,
KEY_KP_0          =  KEY_SPECIAL+46,
KEY_KP_1          =  KEY_SPECIAL+47,
KEY_KP_2          =  KEY_SPECIAL+48,
KEY_KP_3          =  KEY_SPECIAL+49,
KEY_KP_4          =  KEY_SPECIAL+50,
KEY_KP_5          =  KEY_SPECIAL+51,
KEY_KP_6          =  KEY_SPECIAL+52,
KEY_KP_7          =  KEY_SPECIAL+53,
KEY_KP_8          =  KEY_SPECIAL+54,
KEY_KP_9          =  KEY_SPECIAL+55,
KEY_KP_DIVIDE     =  KEY_SPECIAL+56,
KEY_KP_MULTIPLY   =  KEY_SPECIAL+57,
KEY_KP_SUBTRACT   =  KEY_SPECIAL+58,
KEY_KP_ADD        =  KEY_SPECIAL+59,
KEY_KP_DECIMAL    =  KEY_SPECIAL+60,
KEY_KP_EQUAL      =  KEY_SPECIAL+61,
KEY_KP_ENTER      =  KEY_SPECIAL+62,
KEY_KP_NUM_LOCK   =  KEY_SPECIAL+63,
KEY_CAPS_LOCK     =  KEY_SPECIAL+64,
KEY_SCROLL_LOCK   =  KEY_SPECIAL+65,
KEY_PAUSE         =  KEY_SPECIAL+66,
KEY_LSUPER        =  KEY_SPECIAL+67,
KEY_RSUPER        =  KEY_SPECIAL+68,
KEY_MENU          =  KEY_SPECIAL+69,
//--------------------------- Mouse Buttons		  
MOUSE_BUTTON_1     = 0,
MOUSE_BUTTON_LEFT  = 0,

MOUSE_BUTTON_2     = 1,
MOUSE_BUTTON_RIGHT = 1,

MOUSE_BUTTON_3     = 2,
MOUSE_BUTTON_MIDDLE= 2,

MOUSE_BUTTON_4     = 3,
MOUSE_BUTTON_5     = 4,
MOUSE_BUTTON_6     = 5,
MOUSE_BUTTON_7     = 6,
MOUSE_BUTTON_8     = 7,
//--------------------------- VSync Settings
VSYNC_OFF = 0,
VSYNC_ON = 1,
VSYNC_HALF = 2,
//--------------------------- Xbox Controller
X_DPAD_UP = 1,
X_DPAD_DOWN = 2,
X_DPAD_LEFT = 4,
X_DPAD_RIGHT = 8,

X_BUTTON_START = 16,
X_BUTTON_BACK = 32,

X_STICK_LEFT = 64,
X_STICK_RIGHT = 128,

X_BUMPER_LEFT = 256,
X_BUMPER_RIGHT = 512,

X_BUTTON_A = 4096,
X_BUTTON_B = 8192,
X_BUTTON_X = 16384,
X_BUTTON_Y = 32768,
//--------------------------- Blend Modes
BLEND_MODE_ZERO = 0,
BLEND_MODE_ONE  = 1,
BLEND_MODE_SRC_COLOR = 0x0300,
BLEND_MODE_ONE_MINUS_SRC_COLOR = 0x0301,
BLEND_MODE_DST_COLOR = 0x0306,
BLEND_MODE_ONE_MINUS_DST_COLOR = 0x0307,
BLEND_MODE_SRC_ALPHA = 0x0302,
BLEND_MODE_ONE_MINUS_SRC_ALPHA = 0x0303,
BLEND_MODE_DST_ALPHA = 0x0304,
BLEND_MODE_ONE_MINUS_DST_ALPHA = 0x0305,
BLEND_MODE_CONSTANT_COLOR = 0x8001,
BLEND_MODE_ONE_MINUS_CONSTANT_COLOR = 0x8002,
BLEND_MODE_CONSTANT_ALPHA = 0x8003,
BLEND_MODE_ONE_MINUS_CONSTANT_ALPHA = 0x8004,
//--------------------------- Blend Equations
BLEND_EQUATION_FUNC_ADD = 0x8006,
BLEND_EQUATION_FUNC_SUBTRACT = 0x800A,
BLEND_EQUATION_FUNC_REVERSE_SUBTRACT = 0x800B,
BLEND_EQUATION_MIN = 0x8007,
BLEND_EQUATION_MAX = 0x8008,
};
typedef unsigned int ParticleEmitter,Model,Sprite,Font,Sound,Controller;
#endif


/*--------------------------- TODO ---------------------------*\
assignment 5 (should be done...)

SPRITES/FONTS (simples)
    draw fixing
        check inside camera first
        camwidth /2 + sprwidth*spoffx
        camheight/2 + sprwidth*sproff
    
    Multiple Views
        World
            position
            rotation
            projection
        Camera
            projection

Multiplayer(unimportant)
    Connect
    Disconnect
    send data
    recieve data
    check connected
*/