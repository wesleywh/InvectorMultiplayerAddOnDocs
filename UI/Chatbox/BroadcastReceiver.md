[Back To Index](../../index.md)

# BroadcastReceiver

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[content](#parameter-content)<br>
[deathMessage](#parameter-deathMessage)<br>
[messageDestroyTime](#parameter-messageDestroyTime)<br>
[scrollView](#parameter-scrollView)<br>

------------------
 ### content<a name="parameter-content"></a>
> The content object of the scrollView.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |GameObject|null

[Back To Top](#)

------------------
 ### deathMessage<a name="parameter-deathMessage"></a>
> The prefab that will be instantiated as a child of the content when " <br>this receive a \"DEATH\" broadcast message.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |GameObject|null

[Back To Top](#)

------------------
 ### messageDestroyTime<a name="parameter-messageDestroyTime"></a>
> How long to have the message be visible before it is removed.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|15.0f

[Back To Top](#)

------------------
 ### scrollView<a name="parameter-scrollView"></a>
> The ScrollView object in this UI.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |GameObject|null

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Awake](#Awake)<br>
[InstantiateDeathMessage](#InstantiateDeathMessage)<br>
[ReceiveBroadCastMessage](#ReceiveBroadCastMessage)<br>
[Update](#Update)<br>

------------------
 ### protected virtual void Awake()<a name="Awake"></a>
>   Disables the scrollview 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void InstantiateDeathMessage(string message)<a name="InstantiateDeathMessage"></a>
>   Adds a death message object to the message view. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|message|string type, the message to display|

[Back To Top](#)

------------------
 ### public virtual void ReceiveBroadCastMessage(BroadCastMessage message)<a name="ReceiveBroadCastMessage"></a>
>   Perform certain actions based on the type of `BroadCastMessage` that is received from the data channel on the ChatBox. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|message|BroadCastMessage type, the message and the type of message|

[Back To Top](#)

------------------
 ### protected virtual void Update()<a name="Update"></a>
>   Enables/Disables the scroll view based on how many messages there are in the view. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

