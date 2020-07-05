[Back To Index](../index.md)

# SceneTransition

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[BeforeTravel](#parameter-BeforeTravel)<br>
[LoadSceneName](#parameter-LoadSceneName)<br>
[OnAnyPlayerEnterTrigger](#parameter-OnAnyPlayerEnterTrigger)<br>
[OnAnyPlayerExitTrigger](#parameter-OnAnyPlayerExitTrigger)<br>
[OnOwnerEnterTrigger](#parameter-OnOwnerEnterTrigger)<br>
[OnOwnerExitTrigger](#parameter-OnOwnerExitTrigger)<br>
[SpawnAtPoint](#parameter-SpawnAtPoint)<br>
[activeOnEnter](#parameter-activeOnEnter)<br>
[autoTravel](#parameter-autoTravel)<br>
[buttonToTravel](#parameter-buttonToTravel)<br>
[database](#parameter-database)<br>
[sendAllTogether](#parameter-sendAllTogether)<br>

------------------
### BeforeTravel<a name="parameter-BeforeTravel"></a>

> UnityEvent, travel has been called, but this event fires right before.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |UnityEvent|null

[Back To Top](#)

------------------
### LoadSceneName<a name="parameter-LoadSceneName"></a>

> The name of the scene to load. This must be an exact spelling according to what is in the build settings.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|""

[Back To Top](#)

------------------
### OnAnyPlayerEnterTrigger<a name="parameter-OnAnyPlayerEnterTrigger"></a>

> UnityEvent, called when ANY player enter the trigger, owner or networked player

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |UnityEvent|null

[Back To Top](#)

------------------
### OnAnyPlayerExitTrigger<a name="parameter-OnAnyPlayerExitTrigger"></a>

> UnityEvent, called when ANY player exits the trigger, owner or networked player

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |UnityEvent|null

[Back To Top](#)

------------------
### OnOwnerEnterTrigger<a name="parameter-OnOwnerEnterTrigger"></a>

> UnityEvent that is called when the owner enters this trigger, not a networked player.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |UnityEvent|null

[Back To Top](#)

------------------
### OnOwnerExitTrigger<a name="parameter-OnOwnerExitTrigger"></a>

> UnityEvent that is called when the owner exits this trigger, not the networked player.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |UnityEvent|null

[Back To Top](#)

------------------
### SpawnAtPoint<a name="parameter-SpawnAtPoint"></a>

> The name of the LoadPoint object to spawn at in the desired scene. This naming must be exact.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|""

[Back To Top](#)

------------------
### activeOnEnter<a name="parameter-activeOnEnter"></a>

> The gameobjects to active/deactive when entering/exiting this trigger.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject[]|null

[Back To Top](#)

------------------
### autoTravel<a name="parameter-autoTravel"></a>

> When entring this trigger whether or not to automatically move to the new scene or not.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### buttonToTravel<a name="parameter-buttonToTravel"></a>

> The button that must be pressed when inside this trigger to travel the new scene.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|"E"

[Back To Top](#)

------------------
### database<a name="parameter-database"></a>

> The scene database that holds a list of all scenes and LoadPoint objects in those scenes.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |SceneDatabase|None

[Back To Top](#)

------------------
### sendAllTogether<a name="parameter-sendAllTogether"></a>

> Whether to send everyone when traveling or to just send the person entering.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[OnTriggerEnter](#OnTriggerEnter)<br>
[OnTriggerExit](#OnTriggerExit)<br>
[SetDatabase](#SetDatabase)<br>
[Travel](#Travel)<br>
[Update](#Update)<br>

------------------
### protected virtual void OnTriggerEnter(Collider other)<a name="OnTriggerEnter"></a>

>   Will do actions only when a vThirdPersonController enters the trigger and nothing else. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|other|Collider type, only vThirdPersonController players fire this|

[Back To Top](#)

------------------
### protected virtual void OnTriggerExit(Collider other)<a name="OnTriggerExit"></a>

>   Will do actions only when a vThirdPersonController leaves the trigger and nothing else. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|other|Collider type, only vThirdPersonController players fire this|

[Back To Top](#)

------------------
### public virtual void SetDatabase(SceneDatabase input)<a name="SetDatabase"></a>

>   Used for automation. Sets the `database` variable with the input sceneDatabase. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|input|SceneDatabase type, the sceneDatabase to have this component reference|

[Back To Top](#)

------------------
### public virtual void Travel()<a name="Travel"></a>

>   Calls `SendToScene` RPC for everyone or yourself based on the `sendAllTogether` variable. Finds the scene to load from the `database` and calls `NetworkLoadLevel` from the NetworkManager component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   If a owning vThirdPersonController is in the trigger and presses the `buttonToTravel` it will call the `Travel` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

