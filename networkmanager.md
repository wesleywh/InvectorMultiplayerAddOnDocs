[Back To Index](index.md)

# Core Object: NetworkManager  
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

## Lobby Events
<p align="center">
	<img src="https://i.imgur.com/mhNIt7l.jpg">
</p>
<br/>

| Event Name | Description |
|:--- |:---|
| On Joined Lobby | Called when you have successfully joined the photon lobby |
| On Left Lobby | Called when you have successfully left the photon lobby |

## Room Events
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

## Player Events
<p align="center">
	<img src="https://i.imgur.com/Ljtb0in.jpg">
</p>
<br/>

| Event Name | Description |
|:--- |:---|
| On Player Entered Room | When another player has joined the photon room |
| On Player Left Room | When another player has left the photon room |

## Misc Events
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
