[Back To Index](../../index.md)

# NetworkCulling

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[circleColor](#parameter-circleColor)<br>
[distance](#parameter-distance)<br>
[drawGizmos](#parameter-drawGizmos)<br>
[interest_group](#parameter-interest_group)<br>
[last_group](#parameter-last_group)<br>
[last_moveSpeed](#parameter-last_moveSpeed)<br>
[last_rotateSpeed](#parameter-last_rotateSpeed)<br>
[moveSpeed](#parameter-moveSpeed)<br>
[rotateSpeed](#parameter-rotateSpeed)<br>

------------------
### circleColor<a name="parameter-circleColor"></a>

> This only applies to the color you want this circle to be in the gizmo in the editor.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Color|Color.green

[Back To Top](#)

------------------
### distance<a name="parameter-distance"></a>

> The distance the other player must be at or less than to subscribe to be a part " <br>of this photon interest group.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|10

[Back To Top](#)

------------------
### drawGizmos<a name="parameter-drawGizmos"></a>

> Disable or enable the distance gizmos.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |bool|true

[Back To Top](#)

------------------
### interest_group<a name="parameter-interest_group"></a>

> The interest group to subscribe to when another player is within that distance.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |byte|0

[Back To Top](#)

------------------
### last_group<a name="parameter-last_group"></a>

> The distances that will be used to send to certain interest groups. This is to help " <br>return the network load. Objects/Players that are greater distance than the last item in the " <br>list will always receive the least amount of network packets. \n\n" <br>EX: If the other " <br>player is less than or equal to 10 units away from this object and you have an " <br>item in this list with a distance of 10 that means they will be in that specified group " <br>for sending network data. The lower on the list/greater the distance means the less network " <br>packets that player will receive from this object.The interest group to use when the player is further than the greatest cullDistance.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |byte|255

[Back To Top](#)

------------------
### last_moveSpeed<a name="parameter-last_moveSpeed"></a>

> How fast to move the networked players position when they're in this interest group.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|3.0f

[Back To Top](#)

------------------
### last_rotateSpeed<a name="parameter-last_rotateSpeed"></a>

> How fast to move the networked players rotation when they're in this interest group.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|3.0f

[Back To Top](#)

------------------
### moveSpeed<a name="parameter-moveSpeed"></a>

> How fast to move the networked players position when they're in this interest group.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|5.0f

[Back To Top](#)

------------------
### rotateSpeed<a name="parameter-rotateSpeed"></a>

> How fast to move the networked players rotation when they're in this interest group.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|5.0f

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[OnDrawGizmos](#OnDrawGizmos)<br>
[OnPhotonSerializeView](#OnPhotonSerializeView)<br>
[SetInterestGroups](#SetInterestGroups)<br>

------------------
### protected void OnDrawGizmos()<a name="OnDrawGizmos"></a>

>   This is used to draw the wire spheres that is helpful to visualize the distances you're setting for player network culling. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public void OnPhotonSerializeView(PhotonStream stream, PhotonMessageInfo info)<a name="OnPhotonSerializeView"></a>

>   Used to network cull based on registered player distances. Will only send certain messages to certain interest groups. The furthest interest group will receive the least amount of messages while the first interest group will receive all the messages. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|stream|Used by photon|
|info|Used by Photon|

[Back To Top](#)

------------------
### protected void SetInterestGroups()<a name="SetInterestGroups"></a>

>   Used to register the groups you would like to send/receive messages to/from (doesn't send the messages this is just to tell what groups you can actually send to/receive from).It is also responsible for setting the other players (that you see locally) speed and rotation as well as what group they should receive network messages from. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|False|Does not return anything|

**No parameters**

[Back To Top](#)

