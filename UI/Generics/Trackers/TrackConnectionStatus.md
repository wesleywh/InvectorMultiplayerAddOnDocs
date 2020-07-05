[Back To Index](../../../index.md)

# TrackConnectionStatus

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[OnConnectedToLobby](#parameter-OnConnectedToLobby)<br>
[OnConnectedToRoom](#parameter-OnConnectedToRoom)<br>
[texts](#parameter-texts)<br>

------------------
### OnConnectedToLobby<a name="parameter-OnConnectedToLobby"></a>

> UnityEvent. Called when you successfully connect to the Photon Lobby.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |UnityEvent|new UnityEvent()

[Back To Top](#)

------------------
### OnConnectedToRoom<a name="parameter-OnConnectedToRoom"></a>

> UnityEvent. Called when you successfully connect to a photon room.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |UnityEvent|new UnityEvent()

[Back To Top](#)

------------------
### texts<a name="parameter-texts"></a>

> The Text objects to set their string values to be whatever " <br>the current connection status is of the NetworkManager.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text[]|new Text[] { }

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[OnEnable](#OnEnable)<br>
[SetText](#SetText)<br>
[Update](#Update)<br>

------------------
### protected virtual void OnEnable()<a name="OnEnable"></a>

>   Resets the lobby/room unity event fired status' 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void SetText(string inputText)<a name="SetText"></a>

>   Set the string value of all the `texts` according to whatever the input value is. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|inputText|string type, the connection status to set.|

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   Will set the `texts` values to be whatever the NetworkManager connection status is dynamically. Will also only fire the `OnConnectedToLobby` and `OnConnectedToRoom` once based on their fired status'. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

