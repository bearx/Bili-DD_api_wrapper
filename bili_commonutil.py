from essential import *
#api reference for dd-center apis
'''
Uniform return format(URF) by bearx
tuple(bool,content)
bool:whether it is ok
content:The original content should be return
if the return is json, the wrapper will automatically decode it.
The api will not try to raise Exception with correct input, network reason will only 
cause False return value.
'''
'''
Method name defination rules:
Convert{x}_{y} is conversion function, will convert {x}->{y}(Now only support roomid/Vuid)
List{x} or Get{x}_{y} or Chk{x}_{y}
List{x} will show all the info
Get{x}_{y} will pass into some limitation (in str format) listed in y, and show corresponding info
Check{x}_{y} will pass into some limitation (in str format) listed in y, and will check whether is {x} is satifsfied
limitation vocabularys:(Will strictly obey rules of suppercase and lowercase)
uid: user(both vups or dds)'s uid
Vuid: vup's uid
roomid: live room's id
'''
def ConvertVuid_roomid(uid):
    t,rid=GetInfo_Vuid(uid)
    if t:
        rid=str(rid['roomid'])
        return (t,rid)
    return (t,"Failed")
def Convertroomid_Vuid(roomid):
    t,rid=GetRoominfo_roomid(roomid)
    if t:
        rid=str(rid['uid'])
        return (t,rid)
    return (t,"Failed")
def GetSpace_uid(uid):
    return (True,f"https://space.bilibili.com/{uid}")
def GetRoom_roomid(roomid):
    return (True,f"https://live.bilibili.com/{roomid}")
def GetRoom_Vuid(uid):
    roomid=ConvertVuid_roomid(uid)
    return (True,f"https://live.bilibili.com/{roomid[-1]}")
#keys in dict is shown in https://github.com/dd-center/vtbs.moe/blob/master/api.md
def ListVtb():
    '''
    list[dict{}]\n
    :return: list of vups, https://api.vtbs.moe/v1/vtbs
    '''
    r=requests.get("https://api.vtbs.moe/v1/vtbs")
    return (r.ok,r.json())
def ListAllinfo():
    '''
    list[dict{}]\n
    :return: All info of vups, https://api.vtbs.moe/v1/info
    '''
    r=requests.get("https://api.vtbs.moe/v1/info")
    return (r.ok,r.json())
def ListCoreinfo():
    '''
    list[dict{}]\n
    :return: core info of vups, https://api.vtbs.moe/v1/short
    '''
    r=requests.get("https://api.vtbs.moe/v1/short")
    return (r.ok,r.json())
def ListAllinfowithvdb():
    '''
    list[dict{}]\n
    :return: all info of vups, and automatically try to solve if he/she is also a vtuber, https://api.vtbs.moe/v1/fullInfo
    '''
    r=requests.get("https://api.vtbs.moe/v1/fullInfo")
    return (r.ok,r.json())
def GetInfo_Vuid(uid):
    '''
    list[dict{}]\n
    :param uid:Vup's uid
    :return: return info of a vup by his/her uid.https://api.vtbs.moe/v1/detail/:mid
    '''
    r=requests.get(f"https://api.vtbs.moe/v1/detail/{uid}")
    return (r.ok,r.json())
def ListAllguard():
    '''
    dict{dict{}}\n
    :return: return list of all the guards in the database,https://api.vtbs.moe/v1/guard/all
    '''
    r=requests.get("https://api.vtbs.moe/v1/guard/all")
    return (r.ok,r.json())
def ListHQguard():
    '''
    dict{dict{}}\n
    :return: some high-quality guards(2nd class guard or DDs),https://api.vtbs.moe/v1/guard/some
    '''
    r=requests.get("https://api.vtbs.moe/v1/guard/some")
    return (r.ok,r.json())
def GetGuard_Vuid(uid):
    '''
    list[dict{}]
    :param uid:Vup's uid
    :return: Guards of certain vup,https://api.vtbs.moe/v1/guard/:mid
    '''
    r=requests.get(f"https://api.vtbs.moe/v1/guard/{uid}")
    return (r.ok,r.json())
def ListBroadcasting():
    '''
    list[]
    :return: All the room which is on broadcasting,
    '''
    r=requests.get("https://api.vtbs.moe/v1/living")
    return (r.ok,r.json())
def GetRoominfo_roomid(roomid):
    '''
    dict{}
    :param roomid: room's id
    :return: Get room's info by roomid,https://api.vtbs.moe/v1/room/:roomid
    '''
    r=requests.get(f"https://api.vtbs.moe/v1/room/{roomid}")
    return (r.ok,r.json())
def ListHFdanmu():
    '''
    dict{list[dict{}]} (the outside dict only contain keys:"day" and "h"}
    :return: High-frequency danmu is pass one day/hour, https://api.vtbs.moe/v1/hawk
    '''
    r=requests.get("https://api.vtbs.moe/v1/hawk")
    return (r.ok,r.json())
def CheckAlive_roomid(roomid):
    '''
    Boolean value
    :param roomid: room's id
    :return: Boolean value represent if the room is broadcasting
    '''
    succ,dr=ListBroadcasting()
    if succ:
        drs={str(t) for t in dr}
        return (succ,roomid in drs)
    return (succ,"Failed")
def Getfollow_uid(uid):
    '''
    dict{int and list[]}
    Get 250 follows of a user with corresponding uid.Not applicable for those who hide their follows in settings.\n
    follows->关注 in Chinese
    :param uid:User's uid(VUP or DD is both ok)
    :return: Follows count and a follows' list contain all uid(atmost 250)
    '''
    burl="https://api.bilibili.com/x/relation/followings?vmid={}&pn={}&ps=50&order={}&jsonp=jsonp".format(uid,"{}","{}")
    ans=set()
    tot=0
    succ=True
    for pn in range(1,6):
        for seq in {"asc"}:
            turl=burl.format(pn,seq)
            resp=requests.get(turl)
            succ=succ and resp.ok
            resp=resp.json()["data"]
            tot=int(resp["total"])
            resp=resp["list"]
            duplicate=0
            for x in resp:
                if str(x["mid"]) in ans:
                    duplicate+=1
                ans.add(str(x["mid"]))
    return (succ,{"count":tot,"list":list(ans)})

if __name__=="__main__":
    #testcases1:Paryi(Vuid:1576121)
    a_vuid=str(1576121)
    #test ListVtb
    la=ListVtb()
    fnd=False
    for x in la[-1]:
        if str(x["mid"])==a_vuid:
            fnd=True
            break
    assert fnd,"Failed"
    #test Convert{x}_{y}
    a_roomid=str(ConvertVuid_roomid(a_vuid)[-1])
    assert str(Convertroomid_Vuid(a_roomid)[-1])==a_vuid,"Failed"
    #test URL concatenate
    print(GetSpace_uid(a_vuid))
    print(GetRoom_roomid(a_roomid))
    print(GetRoom_Vuid(a_vuid))
    #test listallinfo
    _,allifo=ListAllinfo()
    for x in allifo:
        if str(x["mid"])==a_vuid:
            assert str(x["roomid"])==a_roomid,"Failed"
            break
    _,cainfo=ListCoreinfo()
    for x in cainfo:
        if str(x["mid"])==a_vuid:
            assert str(x["roomid"])==a_roomid,"Failed"
            break
    _,allifo=ListAllinfowithvdb()
    for x in allifo:
        if str(x["mid"])==a_vuid:
            assert str(x["roomid"])==a_roomid,"Failed"
            break
    _,csinfo=GetInfo_Vuid(a_vuid)
    assert str(csinfo["roomid"])==a_roomid,"Failed"
    #test guards functional
    _,allg=ListAllguard()
    tx=list(allg.keys())[random.randint(0,len(allg)-1)]
    print(allg[tx])
    print(GetSpace_uid(str(allg[tx]["mid"])))
    _,allg=ListHQguard()
    tx=list(allg.keys())[random.randint(0,len(allg)-1)]
    print(allg[tx])
    print(GetSpace_uid(str(allg[tx]["mid"])))
    _,ctg=GetGuard_Vuid(a_vuid)
    tx=random.randint(0,len(ctg)-1)
    print(ctg[tx])
    print(GetSpace_uid(str(ctg[tx]["mid"])))
    #test list live broadcasting & room info
    _,lbr=ListBroadcasting()
    tx=random.randint(0,len(lbr)-1)
    print(GetRoom_roomid(str(lbr[tx])))
    print(GetRoominfo_roomid(str(lbr[tx]))[-1])
    print(CheckAlive_roomid(str(lbr[tx]))[-1])
    #test danmu
    _,tdm=ListHFdanmu()
    print(tdm["day"])
    dday=dict()
    for x in tdm["day"]:
        dday[x["word"]]=x["weight"]
    print(tdm["h"])
    dh=dict()
    for x in tdm["h"]:
        dh[x["word"]]=x["weight"]
    w=wordcloud.WordCloud(font_path="msyh.ttc")
    w.generate_from_frequencies(dday)
    w.to_file("day.png")
    plt.imshow(plt.imread("day.png"))
    plt.show()
    w.generate_from_frequencies(dh)
    w.to_file("hour.png")
    plt.imshow(plt.imread("hour.png"))
    plt.show()
    #test follow fetch
    test_uid=#Test uid
    _,fuid=Getfollow_uid(str(test_uid))
    print(f"count:{fuid['count']}")
    fuid=fuid["list"]
    n_sample=5
    id_sample=[]
    for x in range(n_sample):
        id_sample.append(random.randint(0,len(fuid)))
    select_uid=[fuid[fx] for fx in id_sample]
    print(f"Selected uid:{select_uid}")
    for suid in select_uid:
        print(GetSpace_uid(suid))
