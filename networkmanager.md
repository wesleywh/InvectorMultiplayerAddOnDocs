[Back To Index](index.md)

# Core Object: NetworkManager  

[Jump To Public Functions/Delegates](#function-anchor)

## Variables

<p align="center">
	<img src="https://i.imgur.com/TlV0f7B.jpg">
</p>
<br/>

### Universal Settings

| Variable Name | Type | Description |
|:--- |:---:|:---|
| Game Version | float | Only matching game versions can play together |
| Players Per Room | int | How many players are allowed to be in a photon room before it doesn't allow anymore |
| Sync Scenes | bool | If you want everyone to be traveling between scenes together |
| Replay Scenes | bool | If you want the actions in a scene to persist between scenes |
| Database | SceneDatabase | Custom database that holds all the info about scenes and their entry points |


### Player Settings

| Variable Name | Type | Description |
|:--- |:---:|:---|
| Player Prefab | GameObject | The prefab that will be spawned when you NetworkInstantiate a player |
| Allow Team Damaging | bool | If you want to allow team member to damage each other |
| Team Name | string | The name of the team you want the instantiated player to be on (If mutliple teams, leave blank)|
| Initial Team Spawn Point Names | Dictionary<string, string> | The spawn point name that you want this particular team to look for an spawn at. If multiple will randomly choose one |

### Spawn Settings

| Variable Name | Type | Description |
|:--- |:---:|:---|
| Auto Spawn Player | bool | If you want to automatically NetworkInstantiate the player when a scene is done loading |
| Default Spawn Point | Transform | The point that will be chosen to spawn the player if no transform is found with teh `Available Spawn Tag` |
| Available Spawn Tag | string | All transforms with this tag will be used as a possible spawn point | 

### Debug Settings

#### (These should all be disabled for a production game)

| Variable Name | Type | Description |
|:--- |:---:|:---|
| Verbose Console Logging | bool | Every action taken by the network manager will be logged to the Unity console |
| Connection Status | string | You can view the connection status on this component. This is normally referenced by other components |
| Display Debug Window | bool | Will display a helpful window at runtime to help you debug things regarding photon settings |

### Lobby Events
<p align="center">
	<img src="https://i.imgur.com/mhNIt7l.jpg">
</p>
<br/>

| Event Name | Description |
|:--- |:---|
| On Joined Lobby | Called when you have successfully joined the photon lobby |
| On Left Lobby | Called when you have successfully left the photon lobby |

### Room Events
<p align="center">
	<img src="https://i.imgur.com/jAVOhvo.jpg">
</p>
<br/>

| Event Name | Description |
|:--- |:---|
| On Joined Room | Called when you have successfully joined a photon room |
| On Left Room | Called when you have successfully left a photon room |
| On Create Room | Called when you have successfully created a photon room |
| On Create Room Failed | Called when you have failed to created a photon room |
| On Join Room Failed | Called when you have failed to join a photon room |

### Player Events
<p align="center">
	<img src="https://i.imgur.com/Ljtb0in.jpg">
</p>
<br/>

| Event Name | Description |
|:--- |:---|
| On Player Entered Room | When another player has joined the photon room |
| On Player Left Room | When another player has left the photon room |

### Misc Events
<p align="center">
	<img src="https://i.imgur.com/dUYINVq.jpg">
</p>
<br/>

| Event Name | Description |
|:--- |:---|
| On Master Client Switched | Called when the owner of the photon room changes. Happens when the owner lefts or a forceable switch is made. |
| On Disconnected | Called when you disconnect from the photon master server. |
| On Connected To Master | Called when you connect to the photon master server. |
| On Failed To Connect To Photon | Called when you fail to connect to the photon master server |
| On Connection Fail | Called when any sort of connection failure occurs. EX: Failing to connect to the lobby/photon room. |

## Public Functions/Delegates
(#function-anchor)

| Function | What It Does |
|:---|:---|
| OnPlayerJoinedCurrentRoom | `(Delegate)` Can subscribe functions to this to get called when a Photon Player joins a photon room. |
| OnPlayerLeftCurrentRoom | `(Delegate)` Can subscribe functions to this to get called when a Photon Player leaves a photon room. |
| void SetTeamName(string inputName) | Will set the NetworkManager team name according to the input |
| Transform GetRandomSpawnPoint() | Gets a random spawn point based on the specified `Available Spawn Point` tag |
| Transform GetTeamSpawnPoint(string teamName) | Gets a team spawn point, if none are found calls `GetRandomSpawnPoint()` |
| string GetGlobalRoomName(string inputName) | Returns the Photon Session name (not the room name) |
| string GetIndividualRoomName() | Returns the Photon Room name |
| void SetSpawnAtPoint(string pointName) | Set the name of the spawn point to spawn at based on the objects found with the `Available Spawn Point` tag |
| string GetCurrentSceneName() | Returns the name of the Unity scene according to the NetworkManager |
| int GetCurrentSceneIndex() | Returns the scene index of the current scene that corresponds to the current Unity Scene of the `SceneDatabase` |
| virtual void NetworkLoadLevel(int level, string spawnAtPoint = null, bool sendEveryone = false) | Load the Unity Scene, cleanup your network player. Can also send everyone in the Photon Room together. |
| virtual void NewSceneLoaded(Scene scene, LoadSceneMode mode) | Called when the Unity scene is loaded. |
| string GetChatDataChannel() | Returns the `ChatBox` data channel for this session. |
| ChatBox GetChabox() | Returns a reference to the current `ChatBox` saved by the NetworkManager |
| void SetInDataChannel(bool value) | Tell the NetworkManager if you're currently in a `ChatBox` data channel or not. |
| vThirdPersonController GetYourPlayer() | Returns a reference to your own local version of the player (not network controlled players) |
| PlayerData GetCachedPlayerData() | Returns the cached player data that was saved perviously |
| void SavePlayer(vThirdPersonController player) | Save the settings of the player to a file (EX: Health, items, etc.) |
| void LoadPlayerData(string playerName, vThirdPersonController player = null, bool useSavedNickname = true, bool loadFromCache = false, bool overrideStartMaxHealth = false) | Load the player data back into the selected player. |
| bool IsInRoom() | Returns if you're in a Photon Room or not |
| bool IsInLobby() | Returns if you're in a Photon Lobby or not |
| virtual void SetPlayerName(string name = "") | Set the name of your own controlled player that will display across the network. Must be set before applying the player name |
| virtual void Disconnect() | Disconnect from the Photon master server. |
| virtual void CreateRoom(string roomName, RoomOptions options = null, ExitGames.Client.Photon.Hashtable customRoomProperties = null, string[] exposePropertiesToLobby = null) | Create a photon room. |
| virtual void LeaveRoom() | Leave a photon room |
| virtual void JoinRandomRoom(ExitGames.Client.Photon.Hashtable expectedRoomProperties = null) | Join a random Photon room |
| virtual void JoinRoom(string roomName) | Join a Photon Room with the specified name |
| virtual void LeaveLobby() | Leave the Photon Lobby |
| virtual void JoinLobby(TypedLobby lobbyType = null) | Join the Photon Lobby |
| virtual void ConnectToMasterServer() | Connect to the Photon Master Server |
| int GetPlayerCount() | Get the number of players currently in this photon room |
| GameObject NetworkInstantiatePrefab(string prefabName, Vector3 position, Quaternion rotation, byte group=0) | Instantiate a prefab across the network that is owned by a particular player |
| GameObject NetworkInstantiatePersistantPrefab(string prefabName, Vector3 position, Quaternion rotation, byte group = 0, object[] data = null) | Instantiate a prefab that isn't owned by anyone but the unity scene |
| void KickPlayer(Photon.Realtime.Player playerToKick) | Boots a player from a phton room |
| void KickPlayer(string userId) | Boots a player from a photon room |
| void SetRoomIsOpen(bool isOpen) | Set the open state of this photon room (Can be joined or not) |
| void SetRoomVisibility(bool isVisible) | Set the visibility state of this photon room when others list rooms in their own photon lobbies |
| void ReplaySceneDatabase(bool createsOnly = false, bool updatesOnly = false) | Will replay all the saved actions that took place in this scene |
| void UpdateSceneDatabase(ObjectAction hashData) | Add or remove actions to the scene database |
