import bow

conf = {}
conf.update(bow.conf)

conf.update({
        "s3_buff"     : [0.25, 10, 'crit','chance','self'] ,
        "s3_sp"       : 7316          ,
        "s3_startup"  : 0.10+0.15     ,
        "s3_recovery" : 1.05-0.15     ,
    })

conf['str_w'] = 1.5 * 518
