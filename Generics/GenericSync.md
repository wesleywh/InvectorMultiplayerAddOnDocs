[Back To Index](../index.md)

# GenericSync

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[ignoreParams](#parameter-ignoreParams)<br>
[positionLerpRate](#parameter-positionLerpRate)<br>
[rotationLerpRate](#parameter-rotationLerpRate)<br>
[syncAnimations](#parameter-syncAnimations)<br>
[syncAnimatorWeights](#parameter-syncAnimatorWeights)<br>
[syncPosition](#parameter-syncPosition)<br>
[syncRotation](#parameter-syncRotation)<br>
[syncTriggers](#parameter-syncTriggers)<br>

------------------
### ignoreParams<a name="parameter-ignoreParams"></a>

> The animator parameters that you don't want to sync across the network

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |List<string>|new List<string>()

[Back To Top](#)

------------------
### positionLerpRate<a name="parameter-positionLerpRate"></a>

> How fast to move the networked versions position to the desired location.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|17.0f

[Back To Top](#)

------------------
### rotationLerpRate<a name="parameter-rotationLerpRate"></a>

> How fast to move the networked versions rotation to the desired rotation.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|17.0f

[Back To Top](#)

------------------
### syncAnimations<a name="parameter-syncAnimations"></a>

> Sync the animations of the object across the network.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### syncAnimatorWeights<a name="parameter-syncAnimatorWeights"></a>

> Sync the animator layer weights across the network.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### syncPosition<a name="parameter-syncPosition"></a>

> Sync the position of this transform across the network.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### syncRotation<a name="parameter-syncRotation"></a>

> Sync the rotation of this transform across the network.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### syncTriggers<a name="parameter-syncTriggers"></a>

> Attempt to sync triggers (if syncAnimations is true). If triggers are still not synced then you must use an RPC to do so, no other method will work.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[BuildAnimatorParamsDict](#BuildAnimatorParamsDict)<br>
[NewPlayerEnteredOrLeft](#NewPlayerEnteredOrLeft)<br>
[OnDestroy](#OnDestroy)<br>
[Start](#Start)<br>
[SyncTrigger](#SyncTrigger)<br>
[Update](#Update)<br>

------------------
### protected virtual void BuildAnimatorParamsDict()<a name="BuildAnimatorParamsDict"></a>

>   Will find all the animator parameters in the selected animator controller and store those types and names as a key value pair dictionary for later reading and syncing over the network. Also starts trigger watchers if `syncTriggers` is true. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void NewPlayerEnteredOrLeft()<a name="NewPlayerEnteredOrLeft"></a>

>   Will send the position and rotation of this object to all others on the network. The networked versions will receive this information and will snap to the position and rotation received. Sent via RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void OnDestroy()<a name="OnDestroy"></a>

>   This is only used to remove the need to call the `NewPlayerEnteredOrLeft` function from the `OnPlayerNumberingChanged` delegate 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void Start()<a name="Start"></a>

>   Attempts to find the animator, if none is found will disable syncing animations. Also builds the parameter dictionary to sync across the network as they change. Makes use of the `OnPlayerNumberingChanged` delegate provided by Photon to call `NewPlayerEnteredOrLeft` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual IEnumerator SyncTrigger(string triggerName)<a name="SyncTrigger"></a>

>   A simple thread that is dedicated to watching for when a trigger is fired. When fired it will fire and RPC to the other networked versions to update theirs. This is unreliable as it doesn't always catch the trigger. For a more reliable method find where the trigger is being fired and in that function make this RPC call. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True| |

| Parameter Name | Description |
|:---|:---|
|triggerName|The trigger name to watch and update over the network|

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   Used to smoothly rotate and move to the position of the owner. This is only run if this is the networked version. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

