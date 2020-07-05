[Back To Index](../index.md)

# SyncPlayer

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[_positionLerpRate](#parameter-_positionLerpRate)<br>
[_rotationLerpRate](#parameter-_rotationLerpRate)<br>
[_syncAnimations](#parameter-_syncAnimations)<br>
[itemDict](#parameter-itemDict)<br>
[teamName](#parameter-teamName)<br>

------------------
 ### _positionLerpRate<a name="parameter-_positionLerpRate"></a>
> How fast to move to the new position when the networked equivalent of this player receives an update from the server. High values will 'snap' to position, while too low values will feel sluggish or unresponsive. This is something to play with until you get right.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|17.0f

[Back To Top](#)

------------------
 ### _rotationLerpRate<a name="parameter-_rotationLerpRate"></a>
> How fast to move to the new rotation when the networked equivalent of this player receives an update from the server. High values will 'snap' to position, while too low values will feel sluggish or unresponsive. This is something to play with until you get right.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|17.0f

[Back To Top](#)

------------------
 ### _syncAnimations<a name="parameter-_syncAnimations"></a>
> This will sync the bone positions. Makes it so players on the network can see where this player is looking.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

------------------
 ### itemDict<a name="parameter-itemDict"></a>
> Hidden variable. The item dictionary of the player. This is used to save it to the `PlayerData`.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|None|GameObject>|new Dictionary<int, GameObject>()

[Back To Top](#)

------------------
 ### teamName<a name="parameter-teamName"></a>
> The name of the team you're currently on. Set this by calling \"SetTeamName\" function on the " <br>NetworkManager component.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|""

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Awake](#Awake)<br>
[BuildAnimatorParamsDict](#BuildAnimatorParamsDict)<br>
[BuildItemDictionary](#BuildItemDictionary)<br>
[DeadEnableDeathCam](#DeadEnableDeathCam)<br>
[EnableDeathCamera](#EnableDeathCamera)<br>
[EnableSendingAnimations](#EnableSendingAnimations)<br>
[EnableSendingPosRot](#EnableSendingPosRot)<br>
[EnterLadder](#EnterLadder)<br>
[ExitLadder](#ExitLadder)<br>
[GetArrowId](#GetArrowId)<br>
[Jump](#Jump)<br>
[ModifyHitTags](#ModifyHitTags)<br>
[NetworkActiveRagdoll](#NetworkActiveRagdoll)<br>
[NetworkDisableRagdoll](#NetworkDisableRagdoll)<br>
[OnDropItem](#OnDropItem)<br>
[OnReceiveDamage](#OnReceiveDamage)<br>
[Respawn](#Respawn)<br>
[Respawn](#Respawn)<br>
[SetBodyPart](#SetBodyPart)<br>
[SetBodyParts](#SetBodyParts)<br>
[SetLayer](#SetLayer)<br>
[SetTags](#SetTags)<br>
[Start](#Start)<br>
[Update](#Update)<br>

------------------
 ### protected virtual void Awake()<a name="Awake"></a>
>   Sets the `itemData` variable and disables the enable switching on the death camera by calling the `EnableSwitching` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void BuildAnimatorParamsDict()<a name="BuildAnimatorParamsDict"></a>
>   Populates the `animParams` variable which is used to know what animator parameters to watch and send updates over the network for. Calls via `Start` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void BuildItemDictionary()<a name="BuildItemDictionary"></a>
>   Populates the `itemDict` parameter so when an item is equipped/unequipped it will know the GameObject to spawn based on that items Id. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void DeadEnableDeathCam(GameObject temp = null)<a name="DeadEnableDeathCam"></a>
>   Turn on the death camera by calling `EnableDeathCamera` with a true value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|temp|Placed here for UnityEvent activation. Otherwise not used.|

[Back To Top](#)

------------------
 ### public virtual void EnableDeathCamera(bool isEnabled)<a name="EnableDeathCamera"></a>
>   Allows/Disallows switching on the `DeathCamera` component by calling `EnableSwitching` with the specified value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, allow switching the camera or not.|

[Back To Top](#)

------------------
 ### public virtual void EnableSendingAnimations(bool isEnabled)<a name="EnableSendingAnimations"></a>
>   Make it so the owner player can send his animation parameters over the network. The network players will set their animation parameters based on what they recieve from the owner player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, allow the owner player to send their animator parameters|

[Back To Top](#)

------------------
 ### public virtual void EnableSendingPosRot(bool isEnabled)<a name="EnableSendingPosRot"></a>
>   Send the position and rotation of the owner player over the network so the network players will set their position and rotation based on what they receive. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, allow sending the position and rotation over the network?|

[Back To Top](#)

------------------
 ### public virtual void EnterLadder()<a name="EnterLadder"></a>
>   Makes the networked players play the enter ladder animation. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void ExitLadder()<a name="ExitLadder"></a>
>   Makes the networked players play the exit ladder animation 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual int GetArrowId()<a name="GetArrowId"></a>
>   Returns the id that the next arrow should use. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| The arrow id to use|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void Jump()<a name="Jump"></a>
>   Makes the other networked players jump in response to this owners command. Meant to be used with the OnJump UnityEvent in the `vThirdPersonController`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void ModifyHitTags()<a name="ModifyHitTags"></a>
>   Make sure the network versions allowed to hit the `Player` Layer and tag and the owner player is NOT allowed to hit the `Player` Layer and tag. These settings are set in the `vMeleeManager` component. Called via `Start`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void NetworkActiveRagdoll(vDamage damage = null)<a name="NetworkActiveRagdoll"></a>
>   Turns on ragdoll effects for the networked players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|damage|Placed here to be used with UnityEvents, otherwise not used.|

[Back To Top](#)

------------------
 ### protected virtual void NetworkDisableRagdoll()<a name="NetworkDisableRagdoll"></a>
>   Turns off ragdoll effects for the networked players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void OnDropItem(vItem item, int value)<a name="OnDropItem"></a>
>   Makes all network players drop and item with the specified amount. Also Send a drop command to the data channel on the `Chatbox` so when other players enter this unity scene that item is dropped for their version of the game as well. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|item|vItem type, the item to drop|
|value|int type, the amount of this item to drop|

[Back To Top](#)

------------------
 ### public virtual void OnReceiveDamage(vDamage damage)<a name="OnReceiveDamage"></a>
>   Used to set the damage to zero if the sender is on the same team and you disallow team damaging. This function is meant to be called by the OnReceiveDamage unityevent on the `vThirdPersonController`. If damage is received then it is replicated to all networked players 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|damage|***No found decription**|

[Back To Top](#)

------------------
 ### public virtual void Respawn()<a name="Respawn"></a>
>   Calls the `Respawn` function with a null gameobject 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void Respawn(GameObject go)<a name="Respawn"></a>
>   Calls the `SavePlayer` function in the network manager and also calls the `Respawn` function on the `PlayerRespawn` component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|go|Placed here for calling with UnityEvents. Otherwise not used.|

[Back To Top](#)

------------------
 ### protected virtual void SetBodyPart(Transform target = null, bool isTrigger = true)<a name="SetBodyPart"></a>
>   Used by the `SetBodyParts` function. Will set the target transform to enable or disable it's trigger if it has one. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|Transform type, the transform to target|
|isTrigger|bool type, enable or disable the trigger.|

[Back To Top](#)

------------------
 ### protected virtual void SetBodyParts(bool isTrigger)<a name="SetBodyParts"></a>
>   Turns the triggers on/off for the body parts of the player based on the input value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isTrigger|bool type, enable the triggers for all the body parts?|

[Back To Top](#)

------------------
 ### protected virtual void SetLayer()<a name="SetLayer"></a>
>   Set the layers to the none owner layers. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void SetTags(Transform target)<a name="SetTags"></a>
>   Sets the tags to be the none owner tags on all transforms of this object. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void Start()<a name="Start"></a>
>   Builds the item dictionary used to spawn weapons over the network based on the weaponds id. Also disables/enables a series of components on this player if you're a networked player of the owner player. Disables the death camera and builds the animator parameters to sync over the network. Also sets the layers and tags of the player via the `SetLayer` and `SetTags` functions. Finally enables/disables the triggers on the body parts via the `SetBodyParts` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void Update()<a name="Update"></a>
>   Sets the networked players position/rotation based on the received values from the owner player. Also is responsible for playing the "Roll" animation if the owner player enters the roll state. Finally checks if the owner has entered a ragdoll stat, if so enables/disables ragdoll for the networked player based on the setting the owner currently is in. This is also responsible for showing or hiding the cursor if the inventory is open or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

