[Back To Index](../index.md)

# RoomButton

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[_password](#parameter-_password)<br>
[database](#parameter-database)<br>
[indexToLoad](#parameter-indexToLoad)<br>
[isOpen](#parameter-isOpen)<br>
[maxNumOfPlayers](#parameter-maxNumOfPlayers)<br>
[numberOfPlayers](#parameter-numberOfPlayers)<br>
[roomName](#parameter-roomName)<br>

------------------
 ### _password<a name="parameter-_password"></a>
> The password required for this room. Do not set here unless used for testing.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|""

[Back To Top](#)

------------------
 ### database<a name="parameter-database"></a>
> The database that holds all the information about all given scenes.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |SceneDatabase|None

[Back To Top](#)

------------------
 ### indexToLoad<a name="parameter-indexToLoad"></a>
> The scene index to load when this room button is clicked.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |int|0

[Back To Top](#)

------------------
 ### isOpen<a name="parameter-isOpen"></a>
> The text that will display if a player is in a lobby or not

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Text|null

[Back To Top](#)

------------------
 ### maxNumOfPlayers<a name="parameter-maxNumOfPlayers"></a>
> The text that will display the max number of players in this room

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Text|null

[Back To Top](#)

------------------
 ### numberOfPlayers<a name="parameter-numberOfPlayers"></a>
> The text that will display the current number of players in this room

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Text|null

[Back To Top](#)

------------------
 ### roomName<a name="parameter-roomName"></a>
> The text that will display what the name of this room is.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Text|null

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[AddAvailableScene](#AddAvailableScene)<br>
[JoinLobby](#JoinLobby)<br>
[JoinRoom](#JoinRoom)<br>
[SetRoomName](#SetRoomName)<br>
[SetRoomValues](#SetRoomValues)<br>
[SetTotalPlayerCount](#SetTotalPlayerCount)<br>
[SetValues](#SetValues)<br>

------------------
 ### public virtual void AddAvailableScene(LobbyItem sceneItem)<a name="AddAvailableScene"></a>
>   Sets the values of this component based on this input. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|sceneItem|LobbyItem type, Extracts the photon room name from this|

[Back To Top](#)

------------------
 ### public virtual void JoinLobby()<a name="JoinLobby"></a>
>   Calls `UICoreLogic`'s `JoinRoom` function with this set room name. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void JoinRoom()<a name="JoinRoom"></a>
>   Calls the `NetworkManager`'s `JoinRoom` function with the saved room name. If the current scene index also doesn't match it calls the `NetworkLoadLevel` function from the `NetworkManager` as well. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SetRoomName(string inputRoomName)<a name="SetRoomName"></a>
>   Set the name of the photon room to join when clicking this room button based on the `inputRoomName` 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|inputRoomName|string type, the photon room name to join.|

[Back To Top](#)

------------------
 ### public virtual void SetRoomValues(RoomInfo room, string openText = "OPEN", string closedText = "CLOSED")<a name="SetRoomValues"></a>
>   Set the display values based on the input values. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|room|RoomInfo type, extracts room info to display based on this|
|openText|string type, the string to display if the room is open|
|closedText|string type, the string to display if the room is closed|

[Back To Top](#)

------------------
 ### public virtual void SetTotalPlayerCount()<a name="SetTotalPlayerCount"></a>
>   Sets the `numberOfPlayers` string value to be the total number of players currently in this photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SetValues(string inputRoomName, int numOfPlayers, bool inputIsOpen, string roomDisplayName = null)<a name="SetValues"></a>
>   Sets the display values based on the input values. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|inputRoomName|string type, the name of the room to join|
|numOfPlayers|int type, the number of players currently in this room.|
|inputIsOpen|bool type, is this room currently joinable?|
|roomDisplayName|string type, the name of the room to display|

[Back To Top](#)

