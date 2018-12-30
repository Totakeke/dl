import adv_test
import adv
import wep.blade as weapon
from core.timeline import *
from core.log import *



def module():
    return Musashi

class Musashi(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 4.32*2   ,
        "s1_sp"       : 2567   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.9    ,

        "s2_dmg"      : 0   ,
        "s2_sp"       : 4430   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.1    ,

        #"s3_dmg"      : 3.54*3 ,
        #"s3_sp"       : 8030   ,
        #"s3_startup"  : 0.1    ,
        #"s3_recovery" : 2.7    ,

        "mod_a"   : ('att'  , 'buff', 0.03) ,
        "mod_a"   : ('att'  , 'punisher', 0.08/2) ,
        "mod_d"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'chance' , 0.06) ,
        } )
    conf.update(weapon.conf)

    def init(this):
        this.dmg_make("s1_poison",2.65)
        this.dmg_make("s1_poison",2.65)
        this.dmg_make("s1_poison",2.65)
        this.s2buff = adv.Buff("s2",0.3,5,'att')

    def s2_proc(this, e):
        this.s2buff.on()

    



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5 
        `s3, s
        """
    adv_test.test(module(), conf, verbose=0)

