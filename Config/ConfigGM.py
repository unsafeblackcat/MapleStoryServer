from Config.ConfigBase import *

class ConfigGM(ConfigBase):
    def __init__(self, config_path) -> None:
        super().__init__(config_path)
        
        self.m_help = self.get_item('help')
        self.m_commands = self.get_item('commands')
        self.m_droplimit = self.get_item('droplimit')
        self.m_time = self.get_item('time')
        self.m_buyback = self.get_item('buyback')
        self.m_gacha = self.get_item('gacha')
        self.m_dispose = self.get_item('dispose')
        self.m_equiplv = self.get_item('equiplv')
        self.m_rates = self.get_item('rates')
        self.m_online = self.get_item('online')
        self.m_bug = self.get_item('bug')
        self.m_points = self.get_item('points')
        self.m_event = self.get_item('event')
        self.m_ranks = self.get_item('ranks')
        self.m_autoadd = self.get_item('autoadd')
        self.m_toggleexp = self.get_item('toggleexp')
        self.m_mapowner = self.get_item('mapowner')
        self.m_map = self.get_item('map')
        self.m_buyfame = self.get_item('buyfame')
        self.m_pfp = self.get_item('pfp')
        self.m_bosshp = self.get_item('bosshp')
        self.m_mobhp = self.get_item('mobhp')
        self.m_whatdropsfrom = self.get_item('whatdropsfrom')
        self.m_whodrops = self.get_item('whodrops')
        self.m_buffme = self.get_item('buffme')
        self.m_goto = self.get_item('goto')
        self.m_recharge = self.get_item('recharge')
        self.m_whereami = self.get_item('whereami')
        self.m_hide = self.get_item('hide')
        self.m_unhide = self.get_item('unhide')
        self.m_sp = self.get_item('sp')
        self.m_ap = self.get_item('ap')
        self.m_empowerme = self.get_item('empowerme')
        self.m_buffmap = self.get_item('buffmap')
        self.m_buff = self.get_item('buff')
        self.m_bomb = self.get_item('bomb')
        self.m_dc = self.get_item('dc')
        self.m_cleardrops = self.get_item('cleardrops')
        self.m_clearslot = self.get_item('clearslot')
        self.m_clearsavelocs = self.get_item('clearsavelocs')
        self.m_warp = self.get_item('warp')
        self.m_warphere = self.get_item('warphere')
        self.m_warpto = self.get_item('warpto')
        self.m_summon = self.get_item('summon')
        self.m_reach = self.get_item('reach')
        self.m_follow = self.get_item('follow')
        self.m_gmshop = self.get_item('gmshop')
        self.m_heal = self.get_item('heal')
        self.m_item = self.get_item('item')
        self.m_drop = self.get_item('drop')
        self.m_level = self.get_item('level')
        self.m_levelpro = self.get_item('levelpro')
        self.m_setslot = self.get_item('setslot')
        self.m_setstat = self.get_item('setstat')
        self.m_maxstat = self.get_item('maxstat')
        self.m_maxskill = self.get_item('maxskill')
        self.m_resetskill = self.get_item('resetskill')
        self.m_search = self.get_item('search')
        self.m_jail = self.get_item('jail')
        self.m_unjail = self.get_item('unjail')
        self.m_job = self.get_item('job')
        self.m_unbug = self.get_item('unbug')
        self.m_id = self.get_item('id')
        self.m_gachalist = self.get_item('gachalist')
        self.m_loot = self.get_item('loot')
        self.m_debuff = self.get_item('debuff')
        self.m_fly = self.get_item('fly')
        self.m_spawn = self.get_item('spawn')
        self.m_mutemap = self.get_item('mutemap')
        self.m_checkdmg = self.get_item('checkdmg')
        self.m_inmap = self.get_item('inmap')
        self.m_reloadevents = self.get_item('reloadevents')
        self.m_reloaddrops = self.get_item('reloaddrops')
        self.m_reloadportals = self.get_item('reloadportals')
        self.m_reloadmap = self.get_item('reloadmap')
        self.m_reloadshops = self.get_item('reloadshops')
        self.m_hpmp = self.get_item('hpmp')
        self.m_maxhpmp = self.get_item('maxhpmp')
        self.m_music = self.get_item('music')
        self.m_monitor = self.get_item('monitor')
        self.m_monitors = self.get_item('monitors')
        self.m_ignore = self.get_item('ignore')
        self.m_ignored = self.get_item('ignored')
        self.m_pos = self.get_item('pos')
        self.m_togglecoupon = self.get_item('togglecoupon')
        self.m_togglewhitechat = self.get_item('togglewhitechat')
        self.m_fame = self.get_item('fame')
        self.m_givenx = self.get_item('givenx')
        self.m_givevp = self.get_item('givevp')
        self.m_givems = self.get_item('givems')
        self.m_giverp = self.get_item('giverp')
        self.m_expeds = self.get_item('expeds')
        self.m_kill = self.get_item('kill')
        self.m_seed = self.get_item('seed')
        self.m_maxenergy = self.get_item('maxenergy')
        self.m_killall = self.get_item('killall')
        self.m_notice = self.get_item('notice')
        self.m_rip = self.get_item('rip')
        self.m_openportal = self.get_item('openportal')
        self.m_closeportal = self.get_item('closeportal')
        self.m_pe = self.get_item('pe')
        self.m_startevent = self.get_item('startevent')
        self.m_endevent = self.get_item('endevent')
        self.m_startmapevent = self.get_item('startmapevent')
        self.m_stopmapevent = self.get_item('stopmapevent')
        self.m_online2 = self.get_item('online2')
        self.m_ban = self.get_item('ban')
        self.m_unban = self.get_item('unban')
        self.m_healmap = self.get_item('healmap')
        self.m_healperson = self.get_item('healperson')
        self.m_hurt = self.get_item('hurt')
        self.m_killmap = self.get_item('killmap')
        self.m_night = self.get_item('night')
        self.m_npc = self.get_item('npc')
        self.m_face = self.get_item('face')
        self.m_hair = self.get_item('hair')
        self.m_startquest = self.get_item('startquest')
        self.m_completequest = self.get_item('completequest')
        self.m_resetquest = self.get_item('resetquest')
        self.m_timer = self.get_item('timer')
        self.m_timermap = self.get_item('timermap')
        self.m_timerall = self.get_item('timerall')
        self.m_warpmap = self.get_item('warpmap')
        self.m_warparea = self.get_item('warparea')
        self.m_gotonpc = self.get_item('gotonpc')
        self.m_xiguai = self.get_item('xiguai')
        self.m_servermessage = self.get_item('servermessage')
        self.m_proitem = self.get_item('proitem')
        self.m_seteqstat = self.get_item('seteqstat')
        self.m_exprate = self.get_item('exprate')
        self.m_mesorate = self.get_item('mesorate')
        self.m_droprate = self.get_item('droprate')
        self.m_bossdroprate = self.get_item('bossdroprate')
        self.m_questrate = self.get_item('questrate')
        self.m_travelrate = self.get_item('travelrate')
        self.m_fishrate = self.get_item('fishrate')
        self.m_itemvac = self.get_item('itemvac')
        self.m_forcevac = self.get_item('forcevac')
        self.m_zakum = self.get_item('zakum')
        self.m_horntail = self.get_item('horntail')
        self.m_pinkbean = self.get_item('pinkbean')
        self.m_pap = self.get_item('pap')
        self.m_pianus = self.get_item('pianus')
        self.m_cake = self.get_item('cake')
        self.m_playernpc = self.get_item('playernpc')
        self.m_playernpcremove = self.get_item('playernpcremove')
        self.m_pnpc = self.get_item('pnpc')
        self.m_pnpcremove = self.get_item('pnpcremove')
        self.m_pmob = self.get_item('pmob')
        self.m_pmobremove = self.get_item('pmobremove')
        self.m_debug = self.get_item('debug')
        self.m_set = self.get_item('set')
        self.m_showpackets = self.get_item('showpackets')
        self.m_showmovelife = self.get_item('showmovelife')
        self.m_showsessions = self.get_item('showsessions')
        self.m_iplist = self.get_item('iplist')
        self.m_setgmlevel = self.get_item('setgmlevel')
        self.m_warpworld = self.get_item('warpworld')
        self.m_saveall = self.get_item('saveall')
        self.m_dcall = self.get_item('dcall')
        self.m_mapplayers = self.get_item('mapplayers')
        self.m_getacc = self.get_item('getacc')
        self.m_shutdown = self.get_item('shutdown')
        self.m_clearquestcache = self.get_item('clearquestcache')
        self.m_clearquest = self.get_item('clearquest')
        self.m_supplyratecoupon = self.get_item('supplyratecoupon')
        self.m_spawnallpnpcs = self.get_item('spawnallpnpcs')
        self.m_eraseallpnpcs = self.get_item('eraseallpnpcs')
        self.m_addchannel = self.get_item('addchannel')
        self.m_addworld = self.get_item('addworld')
        self.m_removechannel = self.get_item('removechannel')
        self.m_removeworld = self.get_item('removeworld')
        self.m_shtj = self.get_item('shtj')
        return