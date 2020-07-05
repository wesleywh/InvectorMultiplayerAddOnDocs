[Back To Index](../../../index.md)

# TrackPlayerCount

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[OnCountChanged](#parameter-OnCountChanged)<br>
[ReachedFallPlayerCount](#parameter-ReachedFallPlayerCount)<br>
[ReachedPlayerCount](#parameter-ReachedPlayerCount)<br>
[executeEventAtPlayerCount](#parameter-executeEventAtPlayerCount)<br>
[fallBelowCount](#parameter-fallBelowCount)<br>
[isOwner](#parameter-isOwner)<br>
[reachPlayerCount](#parameter-reachPlayerCount)<br>
[teamName](#parameter-teamName)<br>
[texts](#parameter-texts)<br>
[useRoomOwnerShip](#parameter-useRoomOwnerShip)<br>

------------------
 ### OnCountChanged<a name="parameter-OnCountChanged"></a>
> UnityEvent. Called when the player count changes

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |IntUnityEvent|new IntUnityEvent()

[Back To Top](#)

------------------
 ### ReachedFallPlayerCount<a name="parameter-ReachedFallPlayerCount"></a>
> UnityEvent. Called when you hit the `fallBelowCount` when you were originally at a higher value.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|new UnityEvent()

[Back To Top](#)

------------------
 ### ReachedPlayerCount<a name="parameter-ReachedPlayerCount"></a>
> UnityEvent. Called when you reach the specified `reachPlayerCount`.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|new UnityEvent()

[Back To Top](#)

------------------
 ### executeEventAtPlayerCount<a name="parameter-executeEventAtPlayerCount"></a>
> Trigger the ReachPlayerCount unityevent when the player count = reachPlayerCount.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
 ### fallBelowCount<a name="parameter-fallBelowCount"></a>
> The number of players to fall to to excute the ReachedFallPlayerCount UnityEvent.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |int|2

[Back To Top](#)

------------------
 ### isOwner<a name="parameter-isOwner"></a>
> Excute if are you/are not the owner.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
 ### reachPlayerCount<a name="parameter-reachPlayerCount"></a>
> The number of players to reach before executing this ReachPlayerCount UnityEvent.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |int|4

[Back To Top](#)

------------------
 ### teamName<a name="parameter-teamName"></a>
> If you ony want to count the number of players that are on a certain team.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|""

[Back To Top](#)

------------------
 ### texts<a name="parameter-texts"></a>
> The series of text objects to modify with the number of players in the room.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text[]|new Text[] { }

[Back To Top](#)

------------------
 ### useRoomOwnerShip<a name="parameter-useRoomOwnerShip"></a>
> Only execute these unity events based on whether or not you're the room owner.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[DisplayCount](#DisplayCount)<br>
[EnableReachPlayerCountEvent](#EnableReachPlayerCountEvent)<br>
[SetText](#SetText)<br>
[Update](#Update)<br>

------------------
 ### protected virtual void DisplayCount(int count)<a name="DisplayCount"></a>
>   Calls the `SetText` function to set the values of the `texts` to be what the current input count is. If the input count was different from the last time you called this function it will execute the `OnCountChanged` UnityEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|count|int type, the count to display on all the texts.|

[Back To Top](#)

------------------
 ### public virtual void EnableReachPlayerCountEvent(bool isEnabled)<a name="EnableReachPlayerCountEvent"></a>
>   Used to make sure that the fall and reached unity events are fired only once. This is calls as part of the `Update` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void SetText(string inputText)<a name="SetText"></a>
>   Sets the value of the `texts` to be whatever the input value is. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|inputText|string type, the string to display on all the `texts`|

[Back To Top](#)

------------------
 ### protected virtual void Update()<a name="Update"></a>
>   Dynamically sets the `texts` values to be what the currented connected player count is. Will only update these values if you're currently connected to a photon room. Will call the `ReachedFallPlayerCount` and `ReachedPlayerCount` UnityEvents. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

