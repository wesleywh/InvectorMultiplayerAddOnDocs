[Back To Index](../index.md)

# PreviewCamera

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[cameraCloseEnough](#parameter-cameraCloseEnough)<br>
[cameraMoveSpeed](#parameter-cameraMoveSpeed)<br>
[cameraPoints](#parameter-cameraPoints)<br>
[moveImmediatly](#parameter-moveImmediatly)<br>
[networkManager](#parameter-networkManager)<br>
[stopOnJoinRoom](#parameter-stopOnJoinRoom)<br>
[targetCam](#parameter-targetCam)<br>

------------------
### cameraCloseEnough<a name="parameter-cameraCloseEnough"></a>

> How close to the point before considering it close enough?

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|0.1f

[Back To Top](#)

------------------
### cameraMoveSpeed<a name="parameter-cameraMoveSpeed"></a>

> How fast the camera will move between points.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|0.01f

[Back To Top](#)

------------------
### cameraPoints<a name="parameter-cameraPoints"></a>

> List of points the camera will travel do while waiting for the player to join the game.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |List<Transform>|new List<Transform>()

[Back To Top](#)

------------------
### moveImmediatly<a name="parameter-moveImmediatly"></a>

> Whether or not you want to move the camera using the camera points before the player joins a game.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### networkManager<a name="parameter-networkManager"></a>

> The Network Manager component to see if you have joined a room or not

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |NetworkManager|null

[Back To Top](#)

------------------
### stopOnJoinRoom<a name="parameter-stopOnJoinRoom"></a>

> Stop the preview camera when you successfully join a room.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### targetCam<a name="parameter-targetCam"></a>

> The camera that you want to manipulate.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Transform|null

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[GetCameraPoint](#GetCameraPoint)<br>
[ResetPreviewCameraValues](#ResetPreviewCameraValues)<br>
[Start](#Start)<br>
[StartPreviewCamera](#StartPreviewCamera)<br>
[StopPreviewCamera](#StopPreviewCamera)<br>
[Update](#Update)<br>

------------------
### public virtual Transform GetCameraPoint()<a name="GetCameraPoint"></a>

>   Get the target transform point to move towards, set the target index, the start time, and the length from this to that point for smooth transitioning. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| The target transform point|

**No parameters**

[Back To Top](#)

------------------
### public virtual void ResetPreviewCameraValues()<a name="ResetPreviewCameraValues"></a>

>   Will remove the current target point and make the target index to be zero. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void Start()<a name="Start"></a>

>   Sets the needed variables for later use inside of this class 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void StartPreviewCamera()<a name="StartPreviewCamera"></a>

>   Make the camera start moving. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void StopPreviewCamera()<a name="StopPreviewCamera"></a>

>   Make the camera stop moving and call `ResetPreviewCameraValues` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void Update()<a name="Update"></a>

>   Used to smoothly transition the cameras rotations and position based on the current target point it's headed towards. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

