import sword

conf = {}
conf.update(sword.conf)

conf.update({
        "s3_dmg"      : 5*1.65   ,
        "s3_sp"       : 6847     ,
        "s3_startup"  : 0.1      ,
        "s3_recovery" : 3.1      ,
    })
conf['str_w'] = 556*1.5
