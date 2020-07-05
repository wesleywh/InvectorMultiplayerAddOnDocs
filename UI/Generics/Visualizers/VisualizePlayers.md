[Back To Index](../../../index.md)

# VisualizePlayers

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[allocateViewIds](#parameter-allocateViewIds)<br>
[autoSetTeamIfNotSet](#parameter-autoSetTeamIfNotSet)<br>
[debugging](#parameter-debugging)<br>
[joinedSound](#parameter-joinedSound)<br>
[leftSound](#parameter-leftSound)<br>
[otherPlayer](#parameter-otherPlayer)<br>
[ownerPlayer](#parameter-ownerPlayer)<br>
[parentObj](#parameter-parentObj)<br>
[soundSource](#parameter-soundSource)<br>
[teamName](#parameter-teamName)<br>

------------------
 ### allocateViewIds<a name="parameter-allocateViewIds"></a>
> If the child objects have a PhotonView component that you would like to allocate " <br>a unique view id to that belongs to the owning player, only the master client does the " <br>allocation. EX: Each child has a chat icon that only displays when the owner is speaking. " <br>This would require a PhotonView id to be allocated.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
 ### autoSetTeamIfNotSet<a name="parameter-autoSetTeamIfNotSet"></a>
> By default a player enters a game without having his team set. This will automatically " <br>try to evenly choose a team for the entering player.\n\n" <br>IMPORTANT NOTE: You should only ever have this boolean enabled on one of these components at a time. " <br>Otherwise the enabled components will fight with each other.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
 ### debugging<a name="parameter-debugging"></a>
> Enable this if you want to have verbose logging into the console to help you debug things.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
 ### joinedSound<a name="parameter-joinedSound"></a>
> (Optional) Random sound to play when a player joins.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioClip[]|new AudioClip[] { }

[Back To Top](#)

------------------
 ### leftSound<a name="parameter-leftSound"></a>
> (Optional) Random sound to play when a player leaves.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioClip[]|new AudioClip[] { }

[Back To Top](#)

------------------
 ### otherPlayer<a name="parameter-otherPlayer"></a>
> Spawn this object when the found player is NOT the owner of the room.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
 ### ownerPlayer<a name="parameter-ownerPlayer"></a>
> Spawn this object when the found player is the owner of the room.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
 ### parentObj<a name="parameter-parentObj"></a>
> The parent object of these newly spawned UI elements

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Transform|null

[Back To Top](#)

------------------
 ### soundSource<a name="parameter-soundSource"></a>
> (Optional) What AudioSource to play the leave/join sounds.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioSource|null

[Back To Top](#)

------------------
 ### teamName<a name="parameter-teamName"></a>
> If you want to only see the players that are on a certain team. " <br>If blank this will just display everyone.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|""

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[AutoSelectTeam](#AutoSelectTeam)<br>
[DestroyChildObjects](#DestroyChildObjects)<br>
[OnDisable](#OnDisable)<br>
[OnEnable](#OnEnable)<br>
[PlayJoinedSound](#PlayJoinedSound)<br>
[PlayLeftSound](#PlayLeftSound)<br>
[SetOtherPlayerGO](#SetOtherPlayerGO)<br>
[SetOwnerPlayerGO](#SetOwnerPlayerGO)<br>
[SpawnChild](#SpawnChild)<br>
[SpawnChildObjects](#SpawnChildObjects)<br>
[Update](#Update)<br>
[WaitRefresh](#WaitRefresh)<br>
[WaitToRefresh](#WaitToRefresh)<br>

------------------
 ### protected virtual void AutoSelectTeam()<a name="AutoSelectTeam"></a>
>   Will automatically try to evenly add playersto a select team. Loops over all players, skipping ones that already have a team set and captures all the players that don't. Then it will set each captured player into a team one by one, evenly distributing them. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void DestroyChildObjects()<a name="DestroyChildObjects"></a>
>   Destroys all child gameobjects of this gameobject that this component is attached to. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void OnDisable()<a name="OnDisable"></a>
>   Will remove the `WaitRefresh` from being called with the `teamsUpdated` and `voiceViewUpdated` delegates. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void OnEnable()<a name="OnEnable"></a>
>   Will add the `WaitRefresh` to be called with the `teamsUpdated` and `voiceViewUpdated` delegates. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void PlayJoinedSound()<a name="PlayJoinedSound"></a>
>   Plays a random `joinedSound` at the `soundSource`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void PlayLeftSound()<a name="PlayLeftSound"></a>
>   Plays a random `leftSound` at the `soundSource`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SetOtherPlayerGO(GameObject newOtherPlayer)<a name="SetOtherPlayerGO"></a>
>   Can be used by other classes to set the `otherPlayer` gameobject to be spawned. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|newOtherPlayer|GameObject type, the gameobject to spawn when the player connecting is not the master client|

[Back To Top](#)

------------------
 ### public virtual void SetOwnerPlayerGO(GameObject newOwnerPlayer)<a name="SetOwnerPlayerGO"></a>
>   Can be used by other classes to set the `newOwnerPlayer` gameobject to be spawned. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|newOtherPlayer|GameObject type, the gameobject to spawn when the player connecting is the master client|

[Back To Top](#)

------------------
 ### protected virtual void SpawnChild(KeyValuePair<int, Photon.Realtime.Player> target_player)<a name="SpawnChild"></a>
>   Spawns a new child gameobject for the passed in player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target_player|KeyValuePair<int, Photon.Realtime.Player> type, the connected player dictionary|

[Back To Top](#)

------------------
 ### protected virtual void SpawnChildObjects()<a name="SpawnChildObjects"></a>
>   Loops over all the players in the current room and calls `SpawnChild` on each one. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void Update()<a name="Update"></a>
>   Will dynamically instantiate the `ownerPlayer` if you or the `otherPlayer` gameobjects when a player joins the photon room, based on if they're the master client or not. Also plays a sound (if one is set) when a player joins and leave the room. If the `autoSetTeamIfNotSet` is true and the player joining doesn't already have a team set (from joining previously) then this will be called to automatically select a team for them. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void WaitRefresh()<a name="WaitRefresh"></a>
>   Calls the `WaitToRefresh` IEnumerator 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual System.Collections.IEnumerator WaitToRefresh()<a name="WaitToRefresh"></a>
>   Calls `DestroyChildObjects` and `SpawnChildObjects` functions. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False| |

**No parameters**

[Back To Top](#)

