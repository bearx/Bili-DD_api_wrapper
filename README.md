# Bili-DD_api_wrapper
Wrapper library for bilibili-apis and DD-center-apis. Not fully complete.

## Contain Two files:
<b>essential.py</b> Contain some common function and import   
<b>bili_commonutil.py</b> Contain wrapper functions.

## Exchange format:
Uniform return format(URF) by bearx  
tuple(bool,content)  
<b>bool</b>:whether it is ok  
<b>content</b>:The original content should be return  
if the return is json, the wrapper will automatically decode it.
The api will not try to raise Exception with correct input, network reason will only cause False return value.

## Function name rules:
Method name defination rules:  
Convert{x}\_{y} is conversion function, will convert {x}->{y}(Now only support roomid/Vuid)  
List{x} or Get{x}\_{y} or Chk{x}\_{y}  
List{x} will show all the info  
Get{x}\_{y} will pass into some limitation (in str format) listed in y, and show corresponding info  
Check{x}\_{y} will pass into some limitation (in str format) listed in y, and will check whether is {x} is satifsfied  
limitation vocabularys:(Will strictly obey rules of suppercase and lowercase)  
uid: user(both vups or dds)'s uid  
Vuid: vup's uid  
roomid: live room's id  

## Hints:
<b>bili_commonutil.py</b> contain testing code, which also indicate how to use these functions.

## UPD(Sept 20,2021):
<b>essential.py</b> Add some new import  
### New function: emotional estimation(Danmu_emotion.py)
  
two new datastructures: wdlist and wdlistem   
wdlist: the same is the result of ListHFdanmu()  
wdlistem: wdlist with emotional tag, use AddEmotionaltag_wdlist().  
  
New function prototype:Add{x}_{y} Add additional tag{x} to {y}.

