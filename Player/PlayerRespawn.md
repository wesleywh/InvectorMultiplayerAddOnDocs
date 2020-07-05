[Back To Index](../index.md)

# PlayerRespawn

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[broadcastDeathMessage](#parameter-broadcastDeathMessage)<br>
[deathMessage](#parameter-deathMessage)<br>
[debugging](#parameter-debugging)<br>
[respawnDelay](#parameter-respawnDelay)<br>
[respawnPoint](#parameter-respawnPoint)<br>
[respawnType](#parameter-respawnType)<br>
[tag](#parameter-tag)<br>
[teamName](#parameter-teamName)<br>
[teams](#parameter-teams)<br>
[visualCountdown](#parameter-visualCountdown)<br>

------------------
### broadcastDeathMessage<a name="parameter-broadcastDeathMessage"></a>

> Whether or not you want to send a message via the ChatBox (as a BroadCast Message event) " <br>when this player dies. Remember that you need to do something with it by opening the UnityEvent " <br>found on the chatbox under the events tab.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### deathMessage<a name="parameter-deathMessage"></a>

> The message that will be broadcast via the chatbox as a BroadCast Message event. " <br>Remember that you need to do something with it by opening the UnityEvent found on the chatbox " <br>under the events tab.\n\n" <br>\"{Nickname}\" will be replaced with the photon player's name.\n\n" <br>\"{Damager}\" will be replaced with the source player name (if a player, otherwise the transform name) that dealt the killing blow.\n\n" <br>\"{DamageType}\" will be replaced with the damage type that was last recorded.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|"{Nickname} has been killed by {Damager} by using {DamageType}."

[Back To Top](#)

------------------
### debugging<a name="parameter-debugging"></a>

> If you want a verbose log of what is happening in this script to help you debug things.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### respawnDelay<a name="parameter-respawnDelay"></a>

> How long to wait before your player will respawn

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|5.0f

[Back To Top](#)

------------------
### respawnPoint<a name="parameter-respawnPoint"></a>

> Mostly here for debugging purposes. The point where the player will respawn. Is auto selected based on the RespawnType.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Transform|null

[Back To Top](#)

------------------
### respawnType<a name="parameter-respawnType"></a>

> What type of respawning system are you using?\n\n" <br>ClosestPoint = Will find the closest respawn point to where you died and use that.\n\n" <br>//"TeamBased = Find the highest concentration of people on your team and spawn at the respawn point closest to them.\n\n" <br>LastSavePoint = Respawn at whatever is currently set in the respawnPoint transform field.\n\n" <br>Random = Randomly choose a respawn point and respawn there.\n" <br>TeamStatic = Find a random spawn point according to your teams tag and spawn there.\n" <br>TeamDynamic = Find the spawn point that most of your team is next to and spawn there.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |RespawnType|RespawnType.ClosestPoint

[Back To Top](#)

------------------
### tag<a name="parameter-tag"></a>

> Only matters if you have selected \"TeamStatic\" as your respawn type. " <br>The tag that will be found in your scene to determine where you should spawn.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|"SpawnPoint"

[Back To Top](#)

------------------
### teamName<a name="parameter-teamName"></a>

> The name of your team.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|"New Team"

[Back To Top](#)

------------------
### teams<a name="parameter-teams"></a>

> The team names and the tags that will be used as respawn points for that team.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |SpawnTeam[]|new SpawnTeam[] { }

[Back To Top](#)

------------------
### visualCountdown<a name="parameter-visualCountdown"></a>

> The prefab to display when doing a countdown. Does not have to come from the \"Resources\" folder.\n\n" <br>This object needs to implement a function called \"StartCounting\". The component \"Counter\" has " <br>this built in if you would like to make use of it.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|null

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Respawn](#Respawn)<br>
[Respawn](#Respawn)<br>
[RespawnAction](#RespawnAction)<br>
[SelectDynamicTeamSpawn](#SelectDynamicTeamSpawn)<br>
[SelectRespawnPoint](#SelectRespawnPoint)<br>
[SelectStaticTeamSpawn](#SelectStaticTeamSpawn)<br>
[SetRespawnState](#SetRespawnState)<br>

------------------
### public virtual void Respawn(bool keepItems, GameObject lastDamager=null, string lastDamageType=null)<a name="Respawn"></a>

>   Calls the base `Respawn` function. This is used to get the photon view component from the owning player before calling `Respawn`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|keepItems|bool type, keep the items of the player that is respawning|
|lastDamager|Gameobject type, the gameobject of the thing that dealt the last bit of damage|
|lastDamageType|string type, the type of damage that was received.|

[Back To Top](#)

------------------
### public virtual void Respawn(PhotonView playerView, bool keepItems, GameObject lastDamager = null, string lastDamageType = "")<a name="Respawn"></a>

>   Calls the `RespawnAction` IEnumerator to start the respawning process. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|playerView|PhotonView type, the photonview of the player respawning|
|keepItems|bool type, keep the items of the player that is respawning|
|lastDamager|Gameobject type, the gameobject of the thing that dealt the last bit of damage|
|lastDamageType|string type, the type of damage that was received.|

[Back To Top](#)

------------------
### protected virtual IEnumerator RespawnAction(PhotonView playerView, bool keepItems, GameObject lastDamager = null, string lastDamageType = "")<a name="RespawnAction"></a>

>   Will set the death message based on the inputs and broadcasts that message via the Chatbox's data channel to everyone in the session, but only if you allow this. Enables the respawn visual component and starts the countdown. After waiting for the `respawnDelay` time it calls `NetworkInstantiatePrefab` from the NetworkManager to instantiate your new player and sets all of its needed values at a target respawn point. It will then destroy the old player based on the photonView. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|playerView|PhotonView type, the photonview of the player respawning|
|keepItems|bool type, keep the items of the player that is respawning|
|lastDamager|Gameobject type, the gameobject of the thing that dealt the last bit of damage|
|lastDamageType|string type, the type of damage that was received.|

[Back To Top](#)

------------------
### public virtual Transform SelectDynamicTeamSpawn(string teamName)<a name="SelectDynamicTeamSpawn"></a>

>   Returns a random point that one of your team mates is at. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| Transform point of a found team member|

| Parameter Name | Description |
|:---|:---|
|teamName|string type, the name of the team to try and find a point for|

[Back To Top](#)

------------------
### protected virtual Transform SelectRespawnPoint(PhotonView targetView)<a name="SelectRespawnPoint"></a>

>   Will return a target respawn point based on the settings in this component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True| Transform of the target respawn point.|

| Parameter Name | Description |
|:---|:---|
|targetView|The player's PhotonView that needs to select a respwn point|

[Back To Top](#)

------------------
### public virtual Transform SelectStaticTeamSpawn(string teamName)<a name="SelectStaticTeamSpawn"></a>

>   Selects and random "Team" spawn point. These spawn point names are defined in the `NetworkManager` component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| Transform of the target respawn point|

| Parameter Name | Description |
|:---|:---|
|teamName|string type, the team spawn point name to randomly pick|

[Back To Top](#)

------------------
### public void SetRespawnState(bool isEnabled)<a name="SetRespawnState"></a>

>   Enable or disable this `isRespawning` variable. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, is respawning?|

[Back To Top](#)

