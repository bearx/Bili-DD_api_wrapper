import snownlp

from essential import *
from bili_commonutil import *
#URF format
def AddEmotiontag_wdlist(wdlist):
    assert isinstance(wdlist,list),"Should be list[dict{}]"
    assert isinstance(wdlist[0],dict),"Should be list[dict{}]"
    assert "word" in wdlist[0].keys(),"Each dict should contain key->'word'"
    for sid in range(len(wdlist)):
        sw=wdlist[sid]["word"]
        wdlist[sid]["emotion"]=snownlp.SnowNLP(sw).sentiments
    return (True,len(wdlist))
def GetWordcloud_wfdict(wfdict):
    #wfdict:{"word":weight}
    w=wordcloud.WordCloud(font_path="msyh.ttc")
    w.generate_from_frequencies(wfdict)
    return (True,w)
def GetWordcloud_wdlist(wdlist):
    wfdict={}
    for x in wdlist:
        wfdict[x["word"]]=x["weight"]
    return GetWordcloud_wfdict(wfdict)
def SplitEmotion_wdlistem(wdlistem,thresh=0.45):
    pos,neg=[],[]
    for x in wdlistem:
        if x["emotion"]>=thresh:
            pos.append(x)
        else:
            neg.append(x)
    return (True,{"positive":pos,"negative":neg})
def GetEmscore_wdlistem(wdlistem,thresh=0.45):
    sumpos,sumneg=0,0
    for x in wdlistem:
        if x["emotion"]<thresh:
            sumneg+=x['emotion']*x["weight"]
        else:
            sumpos+=x['emotion']*x["weight"]
    return (True,{"positive":sumpos,"negative":sumneg})
if __name__=="__main__":
    _,dm=ListHFdanmu()
    print("--------Daily Danmu classification--------")
    AddEmotiontag_wdlist(dm["day"])
    _,sprd=SplitEmotion_wdlistem(dm["day"])
    _,day_wcpos=GetWordcloud_wdlist(sprd["positive"])
    day_wcpos.to_file("day_pos.png")
    plt.imshow(plt.imread("day_pos.png"))
    plt.show()
    _,day_wcneg=GetWordcloud_wdlist(sprd["negative"])
    day_wcneg.to_file("day_neg.png")
    plt.imshow(plt.imread("day_neg.png"))
    plt.show()
    print(f"Total(day): pos:{len(sprd['positive'])};neg:{len(sprd['negative'])}")
    _,res=GetEmscore_wdlistem(dm['day'])
    day_sumpos,day_sumneg=res["positive"],res["negative"]
    print(f"Emotion Score: pos:{day_sumpos};neg:{day_sumneg};diff:{day_sumpos-day_sumneg}")
    print("--------Hourly Danmu classification--------")
    AddEmotiontag_wdlist(dm["h"])
    _,sprd=SplitEmotion_wdlistem(dm["h"])
    _,h_wcpos=GetWordcloud_wdlist(sprd["positive"])
    h_wcpos.to_file("hour_pos.png")
    plt.imshow(plt.imread("hour_pos.png"))
    plt.show()
    _,h_wcneg=GetWordcloud_wdlist(sprd["negative"])
    h_wcneg.to_file("hour_neg.png")
    plt.imshow(plt.imread("hour_neg.png"))
    plt.show()
    _,res=GetEmscore_wdlistem(dm['h'])
    h_sumpos,h_sumneg=res["positive"],res["negative"]
    print(f"Total(day): pos:{len(sprd['positive'])};neg:{len(sprd['negative'])}")
    print(f"Emotion Score: pos:{h_sumpos};neg:{h_sumneg};diff:{h_sumpos-h_sumneg}")

