[Back To Index](../../../index.md)

# VisualizeRooms

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[autoUpate](#parameter-autoUpate)<br>
[canDisplaySessionRooms](#parameter-canDisplaySessionRooms)<br>
[debugging](#parameter-debugging)<br>
[filterRooms](#parameter-filterRooms)<br>
[onlyDisplaySessionRooms](#parameter-onlyDisplaySessionRooms)<br>
[parentObj](#parameter-parentObj)<br>
[roomButton](#parameter-roomButton)<br>

------------------
### autoUpate<a name="parameter-autoUpate"></a>

> Watch for any room changes and auto update this list.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### canDisplaySessionRooms<a name="parameter-canDisplaySessionRooms"></a>

> If this is true it will display each sub photon room as part of the session. Basically each Unity" <br>scene that a connected player is in.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
### debugging<a name="parameter-debugging"></a>

> Enable this if you want to have verbose logging to the console. Meant for debugging purposes.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### filterRooms<a name="parameter-filterRooms"></a>

> If this has any value in it that means if the photom room doesn't have this value int it will not be" <br>displayed.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|""

[Back To Top](#)

------------------
### onlyDisplaySessionRooms<a name="parameter-onlyDisplaySessionRooms"></a>

> If this is true it will only display the master session room. As in any photom room with an '_' in" <br>the name will not be displayed.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|""

[Back To Top](#)

------------------
### parentObj<a name="parameter-parentObj"></a>

> The gameobject that will act as the parent. Will replace all child objects according to results.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Transform|null

[Back To Top](#)

------------------
### roomButton<a name="parameter-roomButton"></a>

> Each room found will spawn this as a child of the parentObj.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[GenerateRoomButton](#GenerateRoomButton)<br>
[GetRoomListFromUI](#GetRoomListFromUI)<br>
[ManullayUpdateList](#ManullayUpdateList)<br>
[RefreshList](#RefreshList)<br>
[SetFilter](#SetFilter)<br>
[Update](#Update)<br>
[WaitForChange](#WaitForChange)<br>
[WaitForListChange](#WaitForListChange)<br>

------------------
### protected virtual void GenerateRoomButton(string roomName, RoomInfo roomInfo)<a name="GenerateRoomButton"></a>

>   Sets the room button values based on the room info. Also makes sure its set properly as a child object and its scale is correct. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|roomName|string type, the name of the room to display|
|roomInfo|RoomInfo type, the information used to join the room if this is clicked|

[Back To Top](#)

------------------
### public virtual void GetRoomListFromUI()<a name="GetRoomListFromUI"></a>

>   Dynamically gets the room list that is saved in the `UICoreLogic` component and calls `RefreshList` with this new list. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void ManullayUpdateList(Dictionary<string, RoomInfo> roomList)<a name="ManullayUpdateList"></a>

>   Calls the to set the list of rooms to be displayed manually. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|roomList|Dictionary<string, RoomInfo> type, a list of rooms to be displayed|

[Back To Top](#)

------------------
### protected virtual void RefreshList()<a name="RefreshList"></a>

>   Destroys all child objects first then loops through all found rooms and spawns a new child object for each found room that matches the set criteria. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SetFilter(string filter)<a name="SetFilter"></a>

>   Sets the `filterRooms` parameter value to be whatever you pass in. Then calls the `WaitForListChange` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|filter|string type, the value that the room names must have|

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   If the previous count of the number of rooms is different it will call the `GetRoomListFromUI` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual IEnumerator WaitForChange()<a name="WaitForChange"></a>

>   Waits until the `UICoreLogic`'s room list is greater than zero. As soon as it is it calls the `GetRoomListFromUI` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True| |

**No parameters**

[Back To Top](#)

------------------
### public virtual void WaitForListChange()<a name="WaitForListChange"></a>

>   Calls the `WaitForChange` IEnumerator 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

