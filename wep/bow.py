
conf = {}
conf.update( {
        "x_type"         : "ranged" ,

        "x1_dmg"         : 0.29*3   ,
        "x1_sp"          : 184      ,
        "x1_startup"     : 23/60.0  ,
        "x1_recovery"    : 35/60.0  ,

        "x2_dmg"         : 0.37*2   ,
        "x2_sp"          : 92       ,
        "x2_startup"     : 0        ,
        "x2_recovery"    : 33/60.0  ,

        "x3_dmg"         : 0.42*3   ,
        "x3_sp"          : 276      ,
        "x3_startup"     : 0        ,
        "x3_recovery"    : 51/60.0  ,

        "x4_dmg"         : 0.63*2   ,
        "x4_sp"          : 414      ,
        "x4_startup"     : 0        ,
        "x4_recovery"    : 66/60.0  ,

        "x5_dmg"         : 0.35*5   ,
        "x5_sp"          : 529      ,
        "x5_startup"     : 0        ,
        "x5_recovery"    : 24/60.0  ,

        "fs_dmg"         : 0.31*8   ,
        "fs_sp"          : 460      ,
        "fs_startup"     : 63/60.0  , 
        "fs_recovery"    : 37/60.0  , 

        "dodge_recovery" : 43/60.0  ,

        "missile_iv"  : {
            "fs" : 0.3/2 ,
            "x1" : 0.3   ,
            "x2" : 0.3   ,
            "x3" : 0.3   ,
            "x4" : 0.3   ,
            "x5" : 0.3   ,
            }, 

        "mod_wep" : ('crit','chance',0.02),

        })

import bow5b1
import bow5b2
import bow5b3

flame  = bow5b1
water  = bow5b1
wind   = bow5b1

light  = bow5b2

shadow = bow5b3
