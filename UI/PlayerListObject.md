[Back To Index](../index.md)

# PlayerListObject

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[hideLocationIfNotSet](#parameter-hideLocationIfNotSet)<br>
[location](#parameter-location)<br>
[notReadyImage](#parameter-notReadyImage)<br>
[ownerText](#parameter-ownerText)<br>
[playerImage](#parameter-playerImage)<br>
[playerNameText](#parameter-playerNameText)<br>
[readyImage](#parameter-readyImage)<br>
[readyText](#parameter-readyText)<br>
[sceneName](#parameter-sceneName)<br>
[showIfOwner](#parameter-showIfOwner)<br>
[userId](#parameter-userId)<br>

------------------
 ### hideLocationIfNotSet<a name="parameter-hideLocationIfNotSet"></a>
> Will hide the Text component that is responsible for displaying " <br>the player's location if that location currently is not set.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
 ### location<a name="parameter-location"></a>
> The Text component that is responsible for displaying the Unity scene the player is currently in.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text|null

[Back To Top](#)

------------------
 ### notReadyImage<a name="parameter-notReadyImage"></a>
> The GameObject to SetActive if the player is marked as not ready.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
 ### ownerText<a name="parameter-ownerText"></a>
> The Text component that is responsible for displaying if this player is the MasterClient or not.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text|null

[Back To Top](#)

------------------
 ### playerImage<a name="parameter-playerImage"></a>
> The Image component that is specific to this player.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Image|null

[Back To Top](#)

------------------
 ### playerNameText<a name="parameter-playerNameText"></a>
> The Text component that is responsible for displaying the player's name.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text|null

[Back To Top](#)

------------------
 ### readyImage<a name="parameter-readyImage"></a>
> The GameObject to SetActive if the player is marked as ready.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
 ### readyText<a name="parameter-readyText"></a>
> The Text component that is responsible for displaying if the player is marked as ready or not.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text|null

[Back To Top](#)

------------------
 ### sceneName<a name="parameter-sceneName"></a>
> Hidden variable. The scene name this player is currently in.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|"Unknown"

[Back To Top](#)

------------------
 ### showIfOwner<a name="parameter-showIfOwner"></a>
> The Image component to display if this player is the MasterClient.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Image|null

[Back To Top](#)

------------------
 ### userId<a name="parameter-userId"></a>
> Hidden variable. The user id of this player.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|null

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[GetReadyState](#GetReadyState)<br>
[OnDestroy](#OnDestroy)<br>
[RecievedPhotonEvent](#RecievedPhotonEvent)<br>
[SetContents](#SetContents)<br>
[SetPlayerContents](#SetPlayerContents)<br>
[SetPlayerImage](#SetPlayerImage)<br>
[SetReadyState](#SetReadyState)<br>
[Start](#Start)<br>

------------------
 ### public virtual bool GetReadyState()<a name="GetReadyState"></a>
>   Returns if this player is ready or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| True or False, player is ready|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void OnDestroy()<a name="OnDestroy"></a>
>   Removes the `RecievedPhotonEvent` function from Photon's `EventReceived` delegate. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void RecievedPhotonEvent(EventData obj)<a name="RecievedPhotonEvent"></a>
>   Callback method. Called whenever a PhotonEvent is Received. If the event code matches `CB_EVENT_READYUP` it sets the ready stat of this player if the userId that is received matches this one. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|obj|EventData type, the object holding the received event data|

[Back To Top](#)

------------------
 ### public virtual void SetContents(PlayerListInfo info)<a name="SetContents"></a>
>   Sets all the Text and Image values based on the input `info` 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|info|PlayerListInfo type, all the data about this player|

[Back To Top](#)

------------------
 ### public virtual void SetPlayerContents(Photon.Realtime.Player player, string isOwnerText = "ROOM OWNER", string nonOwnerText = "")<a name="SetPlayerContents"></a>
>   Sets the Text and Images based on the input values. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|player|Photon.Realtime.Player type, the |
|isOwnerText|string type, the string value to display if this is a MasterClient|
|nonOwnerText|string type, the string value to display if this is NOT a MasterClient|

[Back To Top](#)

------------------
 ### public virtual void SetPlayerImage(Sprite image)<a name="SetPlayerImage"></a>
>   The Image to set as the player image based on the input `image`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|image|Sprite type, the image to set for the player.|

[Back To Top](#)

------------------
 ### public virtual void SetReadyState(bool inputIsReady)<a name="SetReadyState"></a>
>   Make this player be marked as ready. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|inputIsReady|bool type, this player is ready?|

[Back To Top](#)

------------------
 ### protected virtual void Start()<a name="Start"></a>
>   Sets this component values with the `InstantiationData` for this component. Also adds the `RecievedPhotonEvent` function to the Photon's `EventReceived` delegate so it will be called anytime a PhotonEvent is received. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

