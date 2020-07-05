[Back To Index](../index.md)

# CallNetworkEvents

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[holder](#parameter-holder)<br>
[syncCrossScenes](#parameter-syncCrossScenes)<br>

------------------
 ### holder<a name="parameter-holder"></a>
> This is only important if \"syncCrossScenes\" is true. \n\nThe object you want to track " <br>the position of. When trying to sync this item across the scene it uses it's name and this " <br>holder position to try and figure out what object to update.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Transform|null

[Back To Top](#)

------------------
 ### syncCrossScenes<a name="parameter-syncCrossScenes"></a>
> Do you want these actions to persist between scenes for all players or have it " <br>be a call that will only execute for players currently in this scene?

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[CallFloatInvoke1](#CallFloatInvoke1)<br>
[CallGameObjectInvoke1](#CallGameObjectInvoke1)<br>
[CallGameObjectInvoke2](#CallGameObjectInvoke2)<br>
[CallGameObjectInvoke3](#CallGameObjectInvoke3)<br>
[CallGameObjectInvoke4](#CallGameObjectInvoke4)<br>
[CallNetworkInvoke1](#CallNetworkInvoke1)<br>
[CallNetworkInvoke2](#CallNetworkInvoke2)<br>
[CallNetworkInvoke3](#CallNetworkInvoke3)<br>
[CallNetworkInvoke4](#CallNetworkInvoke4)<br>
[CallNetworkInvoke5](#CallNetworkInvoke5)<br>
[InvokeEvent](#InvokeEvent)<br>
[InvokeSingleEvent](#InvokeSingleEvent)<br>
[SceneUpdateFloatInvokeEvent](#SceneUpdateFloatInvokeEvent)<br>
[SceneUpdateGameObjectInvokeEvent](#SceneUpdateGameObjectInvokeEvent)<br>
[SceneUpdateNoInputInvokeEvent](#SceneUpdateNoInputInvokeEvent)<br>

------------------

 ### public virtual void CallFloatInvoke1(float value)<a name="CallFloatInvoke1"></a>
>   Calls `InvokeSingleEvent` function with a value value and number 1 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|value|float type, the value to pass to the UnityEvents|

[Back To Top](#)

------------------
 ### public virtual void CallGameObjectInvoke1(GameObject target)<a name="CallGameObjectInvoke1"></a>
>   Calls `InvokeGameObjectEvent` with the input gameobject and 1 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|GameObject type, What GameObject to invoke these unity events with|

[Back To Top](#)

------------------
 ### public virtual void CallGameObjectInvoke2(GameObject target)<a name="CallGameObjectInvoke2"></a>
>   Calls `InvokeGameObjectEvent` with the input gameobject and 2 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|GameObject type, What GameObject to invoke these unity events with|

[Back To Top](#)

------------------
 ### public virtual void CallGameObjectInvoke3(GameObject target)<a name="CallGameObjectInvoke3"></a>
>   Calls `InvokeGameObjectEvent` with the input gameobject and 3 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|GameObject type, What GameObject to invoke these unity events with|

[Back To Top](#)

------------------
 ### public virtual void CallGameObjectInvoke4(GameObject target)<a name="CallGameObjectInvoke4"></a>
>   Calls `InvokeGameObjectEvent` with the input gameobject and 4 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|GameObject type, What GameObject to invoke these unity events with|

[Back To Top](#)

------------------
 ### public virtual void CallNetworkInvoke1()<a name="CallNetworkInvoke1"></a>
>   This will call the `InvokeEvent` function with 1 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void CallNetworkInvoke2()<a name="CallNetworkInvoke2"></a>
>   This will call the `InvokeEvent` function with 2 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void CallNetworkInvoke3()<a name="CallNetworkInvoke3"></a>
>   This will call the `InvokeEvent` function with 3 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void CallNetworkInvoke4()<a name="CallNetworkInvoke4"></a>
>   This will call the `InvokeEvent` function with 4 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void CallNetworkInvoke5()<a name="CallNetworkInvoke5"></a>
>   This will call the `InvokeEvent` function with 5 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void InvokeEvent(int number = 0)<a name="InvokeEvent"></a>
>   This will invoke one of the no input UnityEvents on every connected players copy. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|number|int type, What no input UnityEvent number to invoke|

[Back To Top](#)

------------------
 ### protected virtual void InvokeSingleEvent(float value, int number = 0)<a name="InvokeSingleEvent"></a>
>   Invokes The float unity events across the network with the specified number and value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|value|float type, the float value to pass to these UnityEvents|
|number|The unityevent number to invoke|

[Back To Top](#)

------------------
 ### public virtual void SceneUpdateFloatInvokeEvent(string[] input)<a name="SceneUpdateFloatInvokeEvent"></a>
>   Designed to invoke the RPC call for the float input type based on your input number 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|input|***No found decription**|

[Back To Top](#)

------------------
 ### public virtual void SceneUpdateGameObjectInvokeEvent(string[] input)<a name="SceneUpdateGameObjectInvokeEvent"></a>
>   Designed to invoke the RPC call for the GameObject input type based on your input number 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|input|***No found decription**|

[Back To Top](#)

------------------
 ### public virtual void SceneUpdateNoInputInvokeEvent(string[] input)<a name="SceneUpdateNoInputInvokeEvent"></a>
>   Designed to invoke the RPC call based on the input number 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|input|***No found decription**|

[Back To Top](#)

