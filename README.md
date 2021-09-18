# Bili-DD_api_wrapper
Wrapper library for bilibili-apis and DD-center-apis. Not fully complete.

## Contain Two files:
<b>essential.py</b> Contain some common function and import <br>
<b>bili_commonutil.py</b> Contain wrapper functions.

## Exchange format:
Uniform return format(URF) by bearx<br>
tuple(bool,content)<br>
<b>bool</b>:whether it is ok<br>
<b>content</b>:The original content should be return<br>
if the return is json, the wrapper will automatically decode it.
The api will not try to raise Exception with correct input, network reason will only cause False return value.

## Function name rules:
Method name defination rules:<br>
Convert{x}\_{y} is conversion function, will convert {x}->{y}(Now only support roomid/Vuid)<br>
List{x} or Get{x}\_{y} or Chk{x}\_{y}<br>
List{x} will show all the info<br>
Get{x}\_{y} will pass into some limitation (in str format) listed in y, and show corresponding info<br>
Check{x}\_{y} will pass into some limitation (in str format) listed in y, and will check whether is {x} is satifsfied<br>
limitation vocabularys:(Will strictly obey rules of suppercase and lowercase)<br>
uid: user(both vups or dds)'s uid<br>
Vuid: vup's uid<br>
roomid: live room's id<br>

## Hints:
<b>bili_commonutil.py</b> contain testing code, which also indicate how to use these functions.