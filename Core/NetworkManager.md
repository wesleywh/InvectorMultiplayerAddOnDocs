[Back To Index](../index.md)

# NetworkManager

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Delegates](#delegate-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[_connectStatus](#parameter-_connectStatus)<br>
[_connecting](#parameter-_connecting)<br>
[_currentLevelIndex](#parameter-_currentLevelIndex)<br>
[allowTeamDamaging](#parameter-allowTeamDamaging)<br>
[autoSpawnPlayer](#parameter-autoSpawnPlayer)<br>
[cachedRoomList](#parameter-cachedRoomList)<br>
[connect_attempts](#parameter-connect_attempts)<br>
[database](#parameter-database)<br>
[debugging](#parameter-debugging)<br>
[defaultSpawnPoint](#parameter-defaultSpawnPoint)<br>
[displayDebugWindow](#parameter-displayDebugWindow)<br>
[gameVersion](#parameter-gameVersion)<br>
[initalTeamSpawnPointNames](#parameter-initalTeamSpawnPointNames)<br>
[lobbyEvents](#parameter-lobbyEvents)<br>
[maxPlayerPerRoom](#parameter-maxPlayerPerRoom)<br>
[otherEvents](#parameter-otherEvents)<br>
[playerEvents](#parameter-playerEvents)<br>
[playerPrefab](#parameter-playerPrefab)<br>
[reconnect](#parameter-reconnect)<br>
[replayScenes](#parameter-replayScenes)<br>
[roomEvents](#parameter-roomEvents)<br>
[spawnAtSaved](#parameter-spawnAtSaved)<br>
[spawnPointsTag](#parameter-spawnPointsTag)<br>
[syncScenes](#parameter-syncScenes)<br>
[teamName](#parameter-teamName)<br>
[voiceRecorder](#parameter-voiceRecorder)<br>

------------------
### _connectStatus<a name="parameter-_connectStatus"></a>

> Shows the current connection process. This is great for UI to reference and use.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|""

[Back To Top](#)

------------------
### _connecting<a name="parameter-_connecting"></a>

> Says if you're currently connecting to the Photon Server, Lobby, or Room. (false after connection is made)

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
### _currentLevelIndex<a name="parameter-_currentLevelIndex"></a>

> The current index of the Unity scene that your currently in. This is used for internal " <br>logic in the NetworkManager and ChatBox.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |int|-1

[Back To Top](#)

------------------
### allowTeamDamaging<a name="parameter-allowTeamDamaging"></a>

> Allow team members to damage each other.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
### autoSpawnPlayer<a name="parameter-autoSpawnPlayer"></a>

> If you want to immediately spawn the player into the scene when joining the lobby. " <br>If not you need to have a UI that sets this to true before going to the next scene.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### cachedRoomList<a name="parameter-cachedRoomList"></a>

> The current photon room list if in the photon lobby. This is updated via the " <br>\"UpdateCachedRoomList\" function which in turn is called via the \"OnRoomListUpdate\" " <br>function.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|None|RoomInfo>|new Dictionary<string, RoomInfo>()

[Back To Top](#)

------------------
### connect_attempts<a name="parameter-connect_attempts"></a>

> How many attempts to reconnect to the room if 'reconnect' is true.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |int|3

[Back To Top](#)

------------------
### database<a name="parameter-database"></a>

> The scene database that holds all of the information about all of the given scenes.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |SceneDatabase|null

[Back To Top](#)

------------------
### debugging<a name="parameter-debugging"></a>

> If you want to log everything to the console that the network manager is doing at runtime.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
### defaultSpawnPoint<a name="parameter-defaultSpawnPoint"></a>

> The point where the player will start when they have successfully connected or if no other available spawn point is specified.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Transform|null

[Back To Top](#)

------------------
### displayDebugWindow<a name="parameter-displayDebugWindow"></a>

> If you want to display a visual window of the current settings found in the network manager at runtime.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
### gameVersion<a name="parameter-gameVersion"></a>

> The version to connect with. Incompatible versions will not connect with each other.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|"1.0"

[Back To Top](#)

------------------
### initalTeamSpawnPointNames<a name="parameter-initalTeamSpawnPointNames"></a>

> The spawn point name that will represent the initial starting point for the team " <br>If more than one of the spawn points are named with this same name then it will randomly " <br>choose between those points and spawn the team member at that location.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |DictionaryOfStringAndString|new DictionaryOfStringAndString()

[Back To Top](#)

------------------
### lobbyEvents<a name="parameter-lobbyEvents"></a>

> Actions to trigger on events that happen in the lobby. Contains the following UnityEvents: " <br>_onJoinedLobby, _onLeftLobby

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |LobbyEvents|None

[Back To Top](#)

------------------
### maxPlayerPerRoom<a name="parameter-maxPlayerPerRoom"></a>

> The max number of player per room. When a room is full, it can't be joined by new players, and so a new room will be created.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |byte|4

[Back To Top](#)

------------------
### otherEvents<a name="parameter-otherEvents"></a>

> Unity events to call based on Misc Network events. This contains the following UnityEvent parameters: " <br>_onMasterClientSwitched, _onDisconnected, _onConnectedToMaster, _onFailedToConnectToPhoton, _onConnectionFail

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |OtherEvents|None

[Back To Top](#)

------------------
### playerEvents<a name="parameter-playerEvents"></a>

> Actions to trigger on events that happen with actions according to each player. This contains " <br>the following UnityEvent parameters: _onPlayerEnteredRoom, _onPlayerLeftRoom

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |PlayerEvents|None

[Back To Top](#)

------------------
### playerPrefab<a name="parameter-playerPrefab"></a>

> The _prefab that will be spawned in when a player successfully connects.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|null

[Back To Top](#)

------------------
### reconnect<a name="parameter-reconnect"></a>

> Automatically attempt to reconnect to the last room you were in if you get disconnected.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
### replayScenes<a name="parameter-replayScenes"></a>

> Save state between scenes. When you re-enter the scene replay all of the actions on the objects with syncScenes enabled. " <br>This allows for persistant dropped items, picked up items, interacted objects, etc. between unity scenes/photon rooms.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### roomEvents<a name="parameter-roomEvents"></a>

> Actions to trigger on events that happen in the room. Contains the following UnityEvents: " <br> _onJoinedRoom, _onLeftRoom, _OnCreatedRoom, _onCreateRoomFailed, _onJoinRoomFailed, _onReconnect

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |RoomEvents|None

[Back To Top](#)

------------------
### spawnAtSaved<a name="parameter-spawnAtSaved"></a>

> On a successfull reconnect, do you want to spawn the character back at the location " <br>you last were at or just at a random spawn in point?

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### spawnPointsTag<a name="parameter-spawnPointsTag"></a>

> Will find all transforms with this tag and treat it as a spawn point. If no tag is specified will only us what is placed in the default spawn point tag.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|"SpawnPoint"

[Back To Top](#)

------------------
### syncScenes<a name="parameter-syncScenes"></a>

> Automatically sync all connected clients scenes. Make sure everyone is always on the same scene together.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
### teamName<a name="parameter-teamName"></a>

> The name of the team you're currently on. If the team name is never set either manually or " <br>via the \"SetTeamName\" function everyone will be able to damage each other. (Free-For-All) " <br>\n\nWARNING: DO NOT SET THIS MANUALLY! " <br>The only reason to set this manually is if you are testing something out related to same " <br>team mechanics.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|""

[Back To Top](#)

------------------
### voiceRecorder<a name="parameter-voiceRecorder"></a>

> The voice recorder that will be set on owning players Primary Recorder slot. This must be set if using voice chat.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Recorder|None

[Back To Top](#)

## Delegate Definitions<a name="delegate-definitions"></a>

Select the delegate name from below to jump directly to it on this page.

[OnClientHostSwitched](#delegate-OnClientHostSwitched)<br>
[OnConnectedToMasterPhotonServer](#delegate-OnConnectedToMasterPhotonServer)<br>
[OnConnectionFailed](#delegate-OnConnectionFailed)<br>
[OnCreateRoomFailure](#delegate-OnCreateRoomFailure)<br>
[OnCreatedPhotonRoom](#delegate-OnCreatedPhotonRoom)<br>
[OnDisconnectedFromPhoton](#delegate-OnDisconnectedFromPhoton)<br>
[OnFailToConnectToPhoton](#delegate-OnFailToConnectToPhoton)<br>
[OnJoinRoomFailure](#delegate-OnJoinRoomFailure)<br>
[OnJoinedChatDataChannel](#delegate-OnJoinedChatDataChannel)<br>
[OnJoinedPhotonLobby](#delegate-OnJoinedPhotonLobby)<br>
[OnJoinedPhotonRoom](#delegate-OnJoinedPhotonRoom)<br>
[OnLeftPhotonLobby](#delegate-OnLeftPhotonLobby)<br>
[OnLeftPhotonRoom](#delegate-OnLeftPhotonRoom)<br>
[OnPlayerJoinedCurrentRoom](#delegate-OnPlayerJoinedCurrentRoom)<br>
[OnPlayerKicked](#delegate-OnPlayerKicked)<br>
[OnPlayerLeftCurrentRoom](#delegate-OnPlayerLeftCurrentRoom)<br>
[OnReconnectingToRoom](#delegate-OnReconnectingToRoom)<br>
[OnUpdatedRoomList](#delegate-OnUpdatedRoomList)<br>

------------------
### public PlayerDelegate OnClientHostSwitched<a name="delegate-OnClientHostSwitched"></a>


>   This delegate is called whenever the master client left and a new master client is selected. 

| Parameter Name | Description
|:---|:---|
|player|player parameter is Photon.Realtime.Player type. This is the player was selected as the master client.|

[Back To Top](#)

------------------
### public BasicDelegate OnConnectedToMasterPhotonServer<a name="delegate-OnConnectedToMasterPhotonServer"></a>


>   This delegate is called when you successfully connect to the photon master server. 

**No parameters**

[Back To Top](#)

------------------
### public DisconnectCauseDelegate OnConnectionFailed<a name="delegate-OnConnectionFailed"></a>


>   This delegate is called when something causes the connection to fail(after it was established), followed by a call to OnDisconnectedFromPhoton(). If the server could not be reached in the first place, OnFailedToConnectToPhoton is called instead.The reason for the error is provided as StatusCode. 

| Parameter Name | Description
|:---|:---|
|cause|cause parameter is Photon.Realtime.DisconnectCause type. This is a basic connection error/cause that is returned.|

[Back To Top](#)

------------------
### public RoomFailure OnCreateRoomFailure<a name="delegate-OnCreateRoomFailure"></a>


>   This delegate is called whenever you failed to create to a photon room. 

| Parameter Name | Description
|:---|:---|
|returnCode|The status code|
|message|A basic error message.|

[Back To Top](#)

------------------
### public BasicDelegate OnCreatedPhotonRoom<a name="delegate-OnCreatedPhotonRoom"></a>


>   This delegate is called when you successfully create a the photon room. 

**No parameters**

[Back To Top](#)

------------------
### public DisconnectCauseDelegate OnDisconnectedFromPhoton<a name="delegate-OnDisconnectedFromPhoton"></a>


>   This delegate is called whenever you disconnect from the photon room. 

| Parameter Name | Description
|:---|:---|
|cause|cause parameter is Photon.Realtime.DisconnectCause type. This is a basic disconnect error that is returned.|

[Back To Top](#)

------------------
### public DisconnectCauseDelegate OnFailToConnectToPhoton<a name="delegate-OnFailToConnectToPhoton"></a>


>   This delegate is called when something causes the connection to the Photon master server to fail. 

| Parameter Name | Description
|:---|:---|
|cause|cause parameter is Photon.Realtime.DisconnectCause type. This is a basic connection error/cause that is returned.|

[Back To Top](#)

------------------
### public RoomFailure OnJoinRoomFailure<a name="delegate-OnJoinRoomFailure"></a>


>   This delegate is called whenever you failed to connect to a photon room. 

| Parameter Name | Description
|:---|:---|
|returnCode|The status code|
|message|A basic error message.|

[Back To Top](#)

------------------
### public StringDelegate OnJoinedChatDataChannel<a name="delegate-OnJoinedChatDataChannel"></a>


>   This delegate is called when you successfully connected to the ChatBox's data channel. 

**No parameters**

[Back To Top](#)

------------------
### public BasicDelegate OnJoinedPhotonLobby<a name="delegate-OnJoinedPhotonLobby"></a>


>   This delegate is called when you successfully connect to the photon lobby. 

**No parameters**

[Back To Top](#)

------------------
### public BasicDelegate OnJoinedPhotonRoom<a name="delegate-OnJoinedPhotonRoom"></a>


>   This delegate is called when you successfully connect to the photon room. 

**No parameters**

[Back To Top](#)

------------------
### public BasicDelegate OnLeftPhotonLobby<a name="delegate-OnLeftPhotonLobby"></a>


>   This delegate is called when you successfully disconnect from the photon lobby. 

**No parameters**

[Back To Top](#)

------------------
### public BasicDelegate OnLeftPhotonRoom<a name="delegate-OnLeftPhotonRoom"></a>


>   This delegate is called when you successfully disconnect from the photon room. 

**No parameters**

[Back To Top](#)

------------------
### public PlayerDelegate OnPlayerJoinedCurrentRoom<a name="delegate-OnPlayerJoinedCurrentRoom"></a>


>   This delegate is called whenever another player joins the photon room. This isn't called when you first join on yourself. 

| Parameter Name | Description
|:---|:---|
|player|player parameter is Photon.Realtime.Player type. This is the player that is joining.|

[Back To Top](#)

------------------
### public PlayerDelegate OnPlayerKicked<a name="delegate-OnPlayerKicked"></a>


>   This delegate is called whenever another player is kicked from the photon room. 

| Parameter Name | Description
|:---|:---|
|player|player parameter is Photon.Realtime.Player type. This is the player that was just kicked from the photon room.|

[Back To Top](#)

------------------
### public PlayerDelegate OnPlayerLeftCurrentRoom<a name="delegate-OnPlayerLeftCurrentRoom"></a>


>   This delegate is called whenever another player leaves the photon room. This isn't called when you leave the photon room on yourself. 

| Parameter Name | Description
|:---|:---|
|player|player parameter is Photon.Realtime.Player type. This is the player that is leaving.|

[Back To Top](#)

------------------
### public BasicDelegate OnReconnectingToRoom<a name="delegate-OnReconnectingToRoom"></a>


>   This delegate is called whenever you are trying to reconnect to a room after you disconnected from it. 

**No parameters**

[Back To Top](#)

------------------
### public RoomListUpdate OnUpdatedRoomList<a name="delegate-OnUpdatedRoomList"></a>


>   This delegate is called a update to the photom room list is received. 

| Parameter Name | Description
|:---|:---|
|roomList|roomList is type Dictionary<string, RoomInfo>. A list of currently found photon rooms.|

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Awake](#Awake)<br>
[ConnectToMasterServer](#ConnectToMasterServer)<br>
[CreateItem](#CreateItem)<br>
[CreateRoom](#CreateRoom)<br>
[Disconnect](#Disconnect)<br>
[DoSceneReplay](#DoSceneReplay)<br>
[GetCachedPlayerData](#GetCachedPlayerData)<br>
[GetChabox](#GetChabox)<br>
[GetChatDataChannel](#GetChatDataChannel)<br>
[GetCurrentSceneIndex](#GetCurrentSceneIndex)<br>
[GetCurrentSceneName](#GetCurrentSceneName)<br>
[GetGlobalRoomName](#GetGlobalRoomName)<br>
[GetIndividualRoomName](#GetIndividualRoomName)<br>
[GetPlayerCount](#GetPlayerCount)<br>
[GetRandomSpawnPoint](#GetRandomSpawnPoint)<br>
[GetTeamSpawnPoint](#GetTeamSpawnPoint)<br>
[GetYourPlayer](#GetYourPlayer)<br>
[IsInLobby](#IsInLobby)<br>
[IsInRoom](#IsInRoom)<br>
[ItemListTheSame](#ItemListTheSame)<br>
[JoinChatDataChannel](#JoinChatDataChannel)<br>
[JoinLobby](#JoinLobby)<br>
[JoinOrCreateRoom](#JoinOrCreateRoom)<br>
[JoinRandomRoom](#JoinRandomRoom)<br>
[JoinRoom](#JoinRoom)<br>
[KickPlayer](#KickPlayer)<br>
[KickPlayer](#KickPlayer)<br>
[LeaveLobby](#LeaveLobby)<br>
[LeaveRoom](#LeaveRoom)<br>
[LoadPlayerData](#LoadPlayerData)<br>
[NetworkInstantiatePersistantPrefab](#NetworkInstantiatePersistantPrefab)<br>
[NetworkInstantiatePrefab](#NetworkInstantiatePrefab)<br>
[NetworkLoadLevel](#NetworkLoadLevel)<br>
[NewSceneLoaded](#NewSceneLoaded)<br>
[OnConnectedToMaster](#OnConnectedToMaster)<br>
[OnConnectionFail](#OnConnectionFail)<br>
[OnCreateRoomFailed](#OnCreateRoomFailed)<br>
[OnCreatedRoom](#OnCreatedRoom)<br>
[OnDisconnected](#OnDisconnected)<br>
[OnFailedToConnectToPhoton](#OnFailedToConnectToPhoton)<br>
[OnJoinRandomFailed](#OnJoinRandomFailed)<br>
[OnJoinRoomFailed](#OnJoinRoomFailed)<br>
[OnJoinedLobby](#OnJoinedLobby)<br>
[OnJoinedRoom](#OnJoinedRoom)<br>
[OnLeftLobby](#OnLeftLobby)<br>
[OnLeftRoom](#OnLeftRoom)<br>
[OnMasterClientSwitched](#OnMasterClientSwitched)<br>
[OnPlayerEnteredRoom](#OnPlayerEnteredRoom)<br>
[OnPlayerLeftRoom](#OnPlayerLeftRoom)<br>
[OnRoomListUpdate](#OnRoomListUpdate)<br>
[ReplaySceneDatabase](#ReplaySceneDatabase)<br>
[SavePlayer](#SavePlayer)<br>
[SetInDataChannel](#SetInDataChannel)<br>
[SetPlayerName](#SetPlayerName)<br>
[SetRoomIsOpen](#SetRoomIsOpen)<br>
[SetRoomVisibility](#SetRoomVisibility)<br>
[SetSpawnAtPoint](#SetSpawnAtPoint)<br>
[SetTeamName](#SetTeamName)<br>
[Start](#Start)<br>
[UpdateCachedRoomList](#UpdateCachedRoomList)<br>
[UpdateSceneDatabase](#UpdateSceneDatabase)<br>

------------------
### protected virtual void Awake()<a name="Awake"></a>

>   This is used to make sure this is the only NetworkManager in the scene as well as setup scene loading delegates 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void ConnectToMasterServer()<a name="ConnectToMasterServer"></a>

>   Connect to the PUN master server. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### private void CreateItem(ObjectAction item)<a name="CreateItem"></a>

>   Used by the DoSceneReplay funcion only, do not modify. This is responsible for creating items in the Unity scene. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|item|The ObjectAction item to create.|

[Back To Top](#)

------------------
### public virtual void CreateRoom(string roomName, RoomOptions options = null, ExitGames.Client.Photon.Hashtable customRoomProperties = null, string[] exposePropertiesToLobby = null)<a name="CreateRoom"></a>

>   Create a room with the target name for other players to join in the default lobby. Will connect to master server and default lobby if not already connected. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|roomName|The name of the room to make|
|options|Options for the room, in case it does not exist yet. Else these values are ignored.|
|customRoomProperties|The room properties to potentially create this room with|
|exposePropertiesToLobby|The custom properties you want to allow other users to see|

[Back To Top](#)

------------------
### public virtual void Disconnect()<a name="Disconnect"></a>

>   Disconnect from the PUN master server. Will be dropped from any lobby or room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### private void DoSceneReplay(bool createsOnly = false, bool updatesOnly = false)<a name="DoSceneReplay"></a>

>   Performs all the actions on this scene that have been stored in the scene database. Actions are received via the Chatbox's data channel. When someone opens a door, presses a button, drops an item, picks up an item, etc. In another scene that information is recieved by everyone in the session via the ChatBox's data channel. This function is responsible to replay all of those actions for a particular scene when you enter the unity scene. That way it is in sync with all of the other players that are currently already in the scene. This also deals with keeping Unity scenes persistant between loads. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|createsOnly|Only perform the creates actions? (ex: Dropped items)|
|updatesOnly|Only perform the updates actions? (ex: opened doors/pressed buttons)|

[Back To Top](#)

------------------
### public virtual PlayerData GetCachedPlayerData()<a name="GetCachedPlayerData"></a>

>   Get the PlayerData that was saved previously. Used for loading saved player stats, inventory, etc. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| cached player data|

**No parameters**

[Back To Top](#)

------------------
### public virtual ChatBox GetChabox()<a name="GetChabox"></a>

>   Get the chatbox component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| The chatbox component|

**No parameters**

[Back To Top](#)

------------------
### public virtual string GetChatDataChannel()<a name="GetChatDataChannel"></a>

>   Get the current chatbox's data channel. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| Chatbox's data channel that you're subscribed to.|

**No parameters**

[Back To Top](#)

------------------
### public virtual int GetCurrentSceneIndex()<a name="GetCurrentSceneIndex"></a>

>   Get the scene index that the network manager thinks it's in. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| Scene index, int|

**No parameters**

[Back To Top](#)

------------------
### public virtual string GetCurrentSceneName()<a name="GetCurrentSceneName"></a>

>   Get the scene name that the network manager thinks it's in. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| The network manager scene name string|

**No parameters**

[Back To Top](#)

------------------
### public virtual string GetGlobalRoomName(string inputName)<a name="GetGlobalRoomName"></a>

>   Will format the string to be session name compliant. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| The session name.|

| Parameter Name | Description |
|:---|:---|
|inputName|The name that you want to make sure is session name formatted.|

[Back To Top](#)

------------------
### public virtual string GetIndividualRoomName()<a name="GetIndividualRoomName"></a>

>   Gets the current session name that your in and combines it with the Unity scene that your in to make it (session name)_(unity scene) 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| A string formatted like: (session name)_(unity scene)|

**No parameters**

[Back To Top](#)

------------------
### public virtual int GetPlayerCount()<a name="GetPlayerCount"></a>

>   Returns the numbers of players connected to this room 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| The number of players currently in the photon room|

**No parameters**

[Back To Top](#)

------------------
### public virtual Transform GetRandomSpawnPoint()<a name="GetRandomSpawnPoint"></a>

>   Returns a random transform from the scene that is tagged with the spawn point tag. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| Transform that is tagged with the specified spawn point tag.|

**No parameters**

[Back To Top](#)

------------------
### public virtual Transform GetTeamSpawnPoint(string teamName)<a name="GetTeamSpawnPoint"></a>

>   Get a spawn point that is specific for the specified team. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| Transform that is tagged with spawn point tag but is also named according to your team definition. If nothing like this is found then GetRandomSpawnPoint() is called.|

| Parameter Name | Description |
|:---|:---|
|teamName|The specific team named spawn point to look for.|

[Back To Top](#)

------------------
### public virtual vThirdPersonController GetYourPlayer()<a name="GetYourPlayer"></a>

>   Get the vThirdPersonController that you own, not the networked players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| vThirdPersonController component|

**No parameters**

[Back To Top](#)

------------------
### public virtual bool IsInLobby()<a name="IsInLobby"></a>

>   Are you currently in a photon lobby? 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| True if you're already in a photon lobby|

**No parameters**

[Back To Top](#)

------------------
### public virtual bool IsInRoom()<a name="IsInRoom"></a>

>   Are you currently in a photon room? 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| True if you're already in a photon room.|

**No parameters**

[Back To Top](#)

------------------
### private bool ItemListTheSame(List<ItemReference> original, List<ItemReference> incoming)<a name="ItemListTheSame"></a>

>   Used by the DoSceneReplay function only, do not modify. This is responsible for building the information array.   The is used by the DoSceneReplay function, do not modify. This is used to make sure that the item list on a particular item is the same for the entering player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|  True or False if the item list is currently the same.|

| Parameter Name | Description |
|:---|:---|
|args|***No found decription**|
|original|The current item list|
|incoming|The proposed update list|

[Back To Top](#)

------------------
### protected virtual void JoinChatDataChannel()<a name="JoinChatDataChannel"></a>

>   Subscribe to the ChatBox's data channel based on the GetGlobalRoomName function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void JoinLobby(TypedLobby lobbyType = null)<a name="JoinLobby"></a>

>   Join the default lobby. If not connected will connect to master server first. If already in lobby, will do nothing. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|lobbyType|A typed lobby to join (must have name and type).|

[Back To Top](#)

------------------
### public virtual void JoinOrCreateRoom(string roomName, RoomOptions options = null, ExitGames.Client.Photon.Hashtable customRoomProperties = null, string[] exposePropertiesToLobby = null, string[] expectedUsers = null)<a name="JoinOrCreateRoom"></a>

>   Attempts to join the selected room. If it doesn't exist it will create it. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|roomName|The name of the room to join/create|
|options|Options for the room, in case it does not exist yet. Else these values are ignored.|
|customRoomProperties|The room properties to potentially create this room with|
|exposePropertiesToLobby|The custom properties you want to allow other users to see|
|expectedUsers|Optional list of users (by UserId) who are expected to join this game and who you want to block a slot for.|

[Back To Top](#)

------------------
### public virtual void JoinRandomRoom(ExitGames.Client.Photon.Hashtable expectedRoomProperties = null)<a name="JoinRandomRoom"></a>

>   Attempt to join a random room in your connected lobby. Will join master server and defaul lobby if not already connected prior to joining. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|expectedRoomProperties|The room properties that need to exist for you to join the room|

[Back To Top](#)

------------------
### public virtual void JoinRoom(string roomName)<a name="JoinRoom"></a>

>   Join a room with name in your connected lobby. Will join master server and defaul lobby if not already connected prior to joining. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|roomName|The name of the photon room to join|

[Back To Top](#)

------------------
### public virtual void KickPlayer(Photon.Realtime.Player playerToKick)<a name="KickPlayer"></a>

>   Boots a player from a photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|playerToKick|The Photon.Realtime.Player to kick from the photon room|

[Back To Top](#)

------------------
### public virtual void KickPlayer(string userId)<a name="KickPlayer"></a>

>   Boots a player from a photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|userId|The UserId to kick from the photon room.|

[Back To Top](#)

------------------
### public virtual void LeaveLobby()<a name="LeaveLobby"></a>

>   Leave your currently connected lobby but stay connect to the master server. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void LeaveRoom()<a name="LeaveRoom"></a>

>   Makes the caller leave the room they are connected to but stay connected to default lobby and master server. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void LoadPlayerData(string playerName, vThirdPersonController player = null, bool useSavedNickname = true, bool loadFromCache = false, bool overrideStartMaxHealth = false)<a name="LoadPlayerData"></a>

>   Load the player data into the target vThirdPersonController. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|playerName|The player name the data is cached under|
|player|The vThirdPersonController you want to load the data into|
|useSavedNickname|If you don't want to overwrite the saved player name|
|loadFromCache|If you want to load what the NetworkManager already knows about or load it from the saved binary file|
|overrideStartMaxHealth|If you want to set the health to whatever is loaded|

[Back To Top](#)

------------------
### public virtual GameObject NetworkInstantiatePersistantPrefab(string prefabName, Vector3 position, Quaternion rotation, byte group = 0, object[] data = null)<a name="NetworkInstantiatePersistantPrefab"></a>

>   Spawn a object from the "Resources" folder on every instance of the game over the network that is owned by the scene, no player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| spawned Gameobject from the resource folder|

| Parameter Name | Description |
|:---|:---|
|prefabName|The name of the prefab in the resource folder|
|position|Vector3 position in the scene to spawn the object|
|rotation|Quaternion rotation in the scene to spawn the object|
|group|The network group to do this for|
|data|Additional data to spawn the object with|

[Back To Top](#)

------------------
### public virtual GameObject NetworkInstantiatePrefab(string prefabName, Vector3 position, Quaternion rotation, byte group=0, object[] data=null)<a name="NetworkInstantiatePrefab"></a>

>   Spawn a object from the "Resources" folder on every instance of the game over the network that is owned by a particular player 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| spawned Gameobject from the resource folder|

| Parameter Name | Description |
|:---|:---|
|prefabName|The name of the prefab in the resource folder|
|position|Vector3 position in the scene to spawn the object|
|rotation|Quaternion rotation in the scene to spawn the object|
|group|The network group to do this for|
|data|Additional data to spawn the object with|

[Back To Top](#)

------------------
### public virtual void NetworkLoadLevel(int level, string spawnAtPoint = null, bool sendEveryone = false)<a name="NetworkLoadLevel"></a>

>   Loads a Unity Scene and triggers creating or joining a room based on the GetIndividualRoomName function's return. Can send one person or everyone together. If everyone only the MasterClient can do this. Calling this also saves the current settings of your player and restores them in the new unity scene when it has spawned your player there. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|level|The index of the unity scene to load|
|spawnAtPoint|The string of the spawn point to find and spawn your character at|
|sendEveryone|Send everyone in the current photon room with you to the new scene.|

[Back To Top](#)

------------------
### public virtual void NewSceneLoaded(Scene scene, LoadSceneMode mode)<a name="NewSceneLoaded"></a>

>   Callback method that is called every time a new scene is loaded. Will potentially spawn your character in the new scene. It also replays the items that were dropped/picked up in this scene as well as other network actions. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|scene|The scene that is getting loaded.|
|mode|LoadSceneMode that is loading this scene.|

[Back To Top](#)

------------------
### public override void OnConnectedToMaster()<a name="OnConnectedToMaster"></a>

>   Callback method. Called when you connect to the photon master server. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void OnConnectionFail(DisconnectCause cause)<a name="OnConnectionFail"></a>

>   Callback Method. Called when you fail to connect to a Photon Room/Lobby. Calls the otherEvents._onConnectionFail UnityEvent and OnConnectionFailed delegate. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|cause|DisconnectCause with a basic error message.|

[Back To Top](#)

------------------
### public override void OnCreateRoomFailed(short returnCode, string message)<a name="OnCreateRoomFailed"></a>

>   Callback method. called when you fail to create a photon room. This also triggers the roomEvents._onCreateRoomFailed UnityEvent and the OnCreateRoomFailure delegate. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|returnCode|The error code|
|message|Simple error message|

[Back To Top](#)

------------------
### public override void OnCreatedRoom()<a name="OnCreatedRoom"></a>

>   Callback method. Called when you have successfully create a photon room. Calls JoinChatDataChannel function, roomEvents._OnCreatedRoom UnityEvent, and OnCreatedPhotonRoom delegate. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnDisconnected(DisconnectCause cause)<a name="OnDisconnected"></a>

>   Callback method. Called when you disconnect from a photon room. Calls the otherEvents._onDisconnected UnityEvent and OnDisconnectedFromPhoton delegate. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|cause|DisconnectCause with a basic error message.|

[Back To Top](#)

------------------
### public virtual void OnFailedToConnectToPhoton(DisconnectCause cause)<a name="OnFailedToConnectToPhoton"></a>

>   Callback method. Called when you fail to connect to the photon master server. Calls the otherEvents._onFailedToConnectToPhoton UnityEvent and OnFailToConnectToPhoton delegate. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|cause|DisconnectCause with a basic error message.|

[Back To Top](#)

------------------
### public override void OnJoinRandomFailed(short returnCode, string message)<a name="OnJoinRandomFailed"></a>

>   Callback method. Called when you fail to join a random photon room. Calls the roomEvents._onJoinRoomFailed UnityEvent and OnJoinRoomFailure delegate. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|returnCode|The error code|
|message|Simple error message|

[Back To Top](#)

------------------
### public override void OnJoinRoomFailed(short returnCode, string message)<a name="OnJoinRoomFailed"></a>

>   Callback method. Called when you fail to join a specified room. Calls the OnJoinRoomFailure delegate and roomEvents._onJoinRoomFailed UnityEvent. If the return code is 32758 (timeout) it will attempt to recreate the room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|returnCode|The error code|
|message|Simple error message|

[Back To Top](#)

------------------
### public override void OnJoinedLobby()<a name="OnJoinedLobby"></a>

>   Callback method. Called when successfully joined the photon lobby. Calls lobbyEvents._onJoinedLobby UnityEvent and OnJoinedPhotonLobby delegate. Will also call JoinRandomRoom, JoinRoom, or CreateRoom based on if you're switching UnityScenes and attempting to join a Photon room or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnJoinedRoom()<a name="OnJoinedRoom"></a>

>   Callback method. Calls JoinChatDataChannel and NetworkInstantiatePrefab functions. Calls OnJoinedPhotonRoom delegate and roomEvents._onJoinedRoom UnityEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnLeftLobby()<a name="OnLeftLobby"></a>

>   Callback method. Called when you have succesfully left the Photon Lobby. Calls lobbyEvents._onLeftLobby UnityEvent and OnLeftPhotonLobby delegate. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnLeftRoom()<a name="OnLeftRoom"></a>

>   Callback method. Called when you have left a photon room. Calls the JoinRoom function or CreateRoom function if switching Unity scenes. Calls roomEvents._onLeftRoom UnityEvent and OnLeftPhotonRoom delegate. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnMasterClientSwitched(Photon.Realtime.Player newMasterClient)<a name="OnMasterClientSwitched"></a>

>   Callback method. Callwed when the photon master client is switched. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|newMasterClient|The Photon.Realtime.Player that is now the new master client|

[Back To Top](#)

------------------
### public override void OnPlayerEnteredRoom(Photon.Realtime.Player newPlayer)<a name="OnPlayerEnteredRoom"></a>

>   Callback method. Called when another player enters the photon room. Isn't called for yourself. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|newPlayer|The Photon.Realtime.Player that just entered the room.|

[Back To Top](#)

------------------
### public override void OnPlayerLeftRoom(Photon.Realtime.Player otherPlayer)<a name="OnPlayerLeftRoom"></a>

>   Callback method. Called when a player leaves a room. Isn't called for yourself. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|otherPlayer|The Photon.Realtime.Player that just left|

[Back To Top](#)

------------------
### public override void OnRoomListUpdate(List<RoomInfo> roomList)<a name="OnRoomListUpdate"></a>

>   Callback method. Called when in a photon lobby and the number of photon rooms changes. Calls UpdateCachedRoomList. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|roomList|***No found decription**|

[Back To Top](#)

------------------
### public virtual void ReplaySceneDatabase(bool createsOnly = false, bool updatesOnly = false)<a name="ReplaySceneDatabase"></a>

>   Triggers the WaitForReplay IEnumerator which triggers DoSceneReplay function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|createsOnly|Only perform the creates actions? (ex: Dropped items)|
|updatesOnly|Only perform the updates actions? (ex: opened doors/pressed buttons)|

[Back To Top](#)

------------------
### public virtual void SavePlayer(vThirdPersonController player)<a name="SavePlayer"></a>

>   Save your players stats, inventory, etc. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|player|The vThirdPersonController that you own and want to save.|

[Back To Top](#)

------------------
### public virtual void SetInDataChannel(bool value)<a name="SetInDataChannel"></a>

>   Set if you are currently joined to the chatbox's data channel or not 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|value|True or False, are you in the chatbox's data channel?|

[Back To Top](#)

------------------
### public virtual void SetPlayerName(string name = "")<a name="SetPlayerName"></a>

>   Set the players network name, if nothing is supplied will auto name as 'Un-named Player' 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|name|The name you want to be known as over the network|

[Back To Top](#)

------------------
### public virtual void SetRoomIsOpen(bool isOpen)<a name="SetRoomIsOpen"></a>

>   Set the current photon room as open and joinable 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isOpen|True or false, Make the room open or not|

[Back To Top](#)

------------------
### public virtual void SetRoomVisibility(bool isVisible)<a name="SetRoomVisibility"></a>

>   The current photon room will be listed or not 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isVisible|Room should be listed?|

[Back To Top](#)

------------------
### public virtual void SetSpawnAtPoint(string pointName)<a name="SetSpawnAtPoint"></a>

>   Set the spawn at point then trigger the "NewSceneLoaded" function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|pointName|The spawn point name to set|

[Back To Top](#)

------------------
### public virtual void SetTeamName(string inputName)<a name="SetTeamName"></a>

>   Set the name of the team you are a member of. This is for your local player only and is not designed to work with Network players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|inputName|The team name to set.|

[Back To Top](#)

------------------
### protected virtual void Start()<a name="Start"></a>

>   This is used to find the chatbox in the scene. Used in start to give awake enough time to destroy duplicate Chatbox's if any. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void UpdateCachedRoomList(List<RoomInfo> roomList)<a name="UpdateCachedRoomList"></a>

>   This is called via "OnRoomListUpdate" function. This will update the list of available rooms and store it in the cachedRoomList parameter. Only usable when in the Photon Lobby 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|roomList|List of current photon rooms.|

[Back To Top](#)

------------------
### public virtual void UpdateSceneDatabase(ObjectAction hashData)<a name="UpdateSceneDatabase"></a>

>   This is used to add/remove actions to be performed by the DoSceneReplay function. The scene database is responsible for playing actions for a player that is entering a Unity scene for the first time. This function will add or remove actions to the scene database. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|hashData|The data that defines what action to do and if to remove or add it|

[Back To Top](#)

