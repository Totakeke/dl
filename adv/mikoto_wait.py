import adv_test
import adv
import adv.mikoto
import wep.blade
from core.timeline import *
from core.log import *

def module():
    return Mikoto_wait

class Mikoto_wait(adv.mikoto.Mikoto):
    def init(this):
        this.atspd = 1.0
        this.stance = 0
        this.s1 = Mikoto_s1_wait("s1", this.conf["s1_sp"])
        this.s1event = Event("s1buff", this.s1_end)
        this.s2event = Event("s2buff", this.s2_end)


class Mikoto_s1_wait(adv.Skill):
    def check(this):
        if this.hold :
            return 0
        if this.charged >= this.sp:
            return 1
        else:
            return 0


    def rs(this, e):
        this.hold = 1


    def ns(this, e):
        this.hold = 0


    def init(this):
        this.hold = 0
        add_event_listener("ruin_stance", this.rs)
        add_event_listener("no_stance", this.ns)




if __name__ == '__main__':
    conf = {}

    al = {
        #'sp': ["s1","s2"],
        'x5': ["s1"],
        'x4': ["s1"],
        'x3': ["s1"],
        'x2': ["s1"],
        'x1': ["s1"],
        's': ["s1","s3","s2"],
        } 

    conf['al'] = al

    adv_test.test(module(), conf, verbose=0)

