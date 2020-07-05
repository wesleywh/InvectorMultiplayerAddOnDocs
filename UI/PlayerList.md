[Back To Index](../index.md)

# PlayerList

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[anim](#parameter-anim)<br>
[autoCloseWithChatBox](#parameter-autoCloseWithChatBox)<br>
[closeAnimation](#parameter-closeAnimation)<br>
[closeSound](#parameter-closeSound)<br>
[content](#parameter-content)<br>
[debugging](#parameter-debugging)<br>
[delayDisable](#parameter-delayDisable)<br>
[openAnimation](#parameter-openAnimation)<br>
[openSound](#parameter-openSound)<br>
[openWindow](#parameter-openWindow)<br>
[playerJoinObject](#parameter-playerJoinObject)<br>
[rootObj](#parameter-rootObj)<br>
[soundSource](#parameter-soundSource)<br>

------------------
### anim<a name="parameter-anim"></a>

> If supplied will trigger the open/close animations on this component.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Animation|null

[Back To Top](#)

------------------
### autoCloseWithChatBox<a name="parameter-autoCloseWithChatBox"></a>

> Automatically close the playerlist window when the chatbox is open.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

------------------
### closeAnimation<a name="parameter-closeAnimation"></a>

> The close animation name to play on the anim component.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|"CloseList"

[Back To Top](#)

------------------
### closeSound<a name="parameter-closeSound"></a>

> The sound that will play when closing the player list window.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioClip|null

[Back To Top](#)

------------------
### content<a name="parameter-content"></a>

> The gameobject that will hold the content of your scroll view.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
### debugging<a name="parameter-debugging"></a>

> If you want to see everything this is doing in runtime. Turn on debugging to log to the console.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### delayDisable<a name="parameter-delayDisable"></a>

> How long to wait after a button press to disable/enable the chat window. " <br>This is helpful if you are playing an animation.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|2.0f

[Back To Top](#)

------------------
### openAnimation<a name="parameter-openAnimation"></a>

> The open animation name to play on the anim component.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|"OpenList"

[Back To Top](#)

------------------
### openSound<a name="parameter-openSound"></a>

> The sound that will play when opening the player list window.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioClip|null

[Back To Top](#)

------------------
### openWindow<a name="parameter-openWindow"></a>

> OnHold = Display the player window when you're holding the selected key.\n\n" <br>OnPress = Display the player window and close the player window with the key press.\n\n" <br>Invoke = Have another script open the window. No key press will open this window.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |PressType|PressType.OnPress

[Back To Top](#)

------------------
### playerJoinObject<a name="parameter-playerJoinObject"></a>

> The object that will hold the visual item that will be " <br>instantiated as a child of the content gameobject. This object " <br>must have the \"PlayerListObject\" component attached to it's root.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
### rootObj<a name="parameter-rootObj"></a>

> When enabling/disable this playerList it will enable/disable this object.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
### soundSource<a name="parameter-soundSource"></a>

> The AudioSource that the open/close sounds will play from.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioSource|null

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[AddPlayer](#AddPlayer)<br>
[AddPlayer](#AddPlayer)<br>
[AddPlayers](#AddPlayers)<br>
[Awake](#Awake)<br>
[ClearPlayerList](#ClearPlayerList)<br>
[ClearPlayerList](#ClearPlayerList)<br>
[DoEnable](#DoEnable)<br>
[EnablePlayerListWindow](#EnablePlayerListWindow)<br>
[PlaySound](#PlaySound)<br>
[RemovePlayer](#RemovePlayer)<br>
[RemovePlayer](#RemovePlayer)<br>
[SetPlayerList](#SetPlayerList)<br>
[Update](#Update)<br>
[UpdateLocationToCurrentScene](#UpdateLocationToCurrentScene)<br>
[UpdateLocationToGoingToScene](#UpdateLocationToGoingToScene)<br>
[UpdatePlayer](#UpdatePlayer)<br>

------------------
### public virtual void AddPlayer(string chatUserId)<a name="AddPlayer"></a>

>   Calls the `AddPlayer` with a new `PlayerListInfo` object based on the input `chatUserId`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|chatUserId|***No found decription**|

[Back To Top](#)

------------------
### public virtual void AddPlayer(PlayerListInfo player)<a name="AddPlayer"></a>

>   Creates a child gameobject with all the settings found in the input `PlayerListInfo` object. Also makes sure the scale and positioning is correct. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|player|PlayerListInfo type, the information for this player to display|

[Back To Top](#)

------------------
### public virtual void AddPlayers(List<PlayerListInfo> players)<a name="AddPlayers"></a>

>   Calls `AddPlayer` function for each player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|players|***No found decription**|

[Back To Top](#)

------------------
### protected virtual void Awake()<a name="Awake"></a>

>   Makes sure the `rootObj` is inactive 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void ClearPlayerList(string temp)<a name="ClearPlayerList"></a>

>   Calls `ClearPlayerList` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|temp|***No found decription**|

[Back To Top](#)

------------------
### public virtual void ClearPlayerList()<a name="ClearPlayerList"></a>

>   Destroys every child gameobject. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual IEnumerator DoEnable(bool isEnabled)<a name="DoEnable"></a>

>   Enables the `rootObject`, plays the animation, and plays the open or close sound via the `PlaySound` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, show or hide the player list window|

[Back To Top](#)

------------------
### public virtual void EnablePlayerListWindow(bool isEnabled)<a name="EnablePlayerListWindow"></a>

>   Calls the `DoEnable` IEnumerator. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|***No found decription**|

[Back To Top](#)

------------------
### protected virtual void PlaySound(AudioClip soundClip = null, float volumeLevel = 0.5f)<a name="PlaySound"></a>

>   Play the input `soundClip` at the specified `volumeLevel` on the `soundSource` AudioSource. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|soundClip|AudioClip type, the AudioClip to play.|
|volumeLevel|float type, the volume to set the `soundSource` to.|

[Back To Top](#)

------------------
### public virtual void RemovePlayer(string chatUserId)<a name="RemovePlayer"></a>

>   Calls the `RemovePlayer` function with a new `PlayerListInfo` based on the input `chatUserId` 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|chatUserId|strign type, the chat user id|

[Back To Top](#)

------------------
### public virtual void RemovePlayer(PlayerListInfo player)<a name="RemovePlayer"></a>

>   Find the child object that matches the User Id of the input player and destroys it. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|player|PlayerListInfo type, extracts user id from this|

[Back To Top](#)

------------------
### public virtual void SetPlayerList()<a name="SetPlayerList"></a>

>   Returns a list of all subscribers in the chatbox's data channel.   Calls `GetDataSubScribers` function and loops through those calling the `AddPlayer` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| List<string> of data channel subscribers|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   Will watch for when the users presses the `keyToPress` doing it like the specified `openWindow` type. If those criteria match it will open or close this window. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void UpdateLocationToCurrentScene()<a name="UpdateLocationToCurrentScene"></a>

>   Broadcasts data via the data channel on the chatbox to set the UserId to be in a new Unity scene. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void UpdateLocationToGoingToScene()<a name="UpdateLocationToGoingToScene"></a>

>   Broadcasts data via the data channel on the chatbox to set this UserId to be in a transition state. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void UpdatePlayer(PlayerListInfo info)<a name="UpdatePlayer"></a>

>   Find the child object that matches the input `info` and calls the `SetContents` function with the input `info` on it. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|info|PlayerListInfo type, the information for a given player|

[Back To Top](#)

