import adv_test
from adv import *

def module():
    return Luther

class Luther(Adv):
    conf = {
        "mod_a"   : ('crit', 'chance', 0.10) ,
        "mod_d"   :[('att'  , 'passive' , 0.45)  ,
                    ('crit' , 'chance'  , 0.20)] ,
        'condition':'15hits'
        } 

    def s2_proc(this, e):
        Buff('s2_ab',-0.015,10,'def').on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    #lower dps
    #conf['acl'] = """
    #    `s1
    #    `s2
    #    `s3
    #    `fs, seq=4
    #    """

    adv_test.test(module(), conf, verbose=0, mass=0)

