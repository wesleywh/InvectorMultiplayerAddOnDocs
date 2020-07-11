[Back To Index](../index.md)

# NetworkControl

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[WindowId](#parameter-WindowId)<br>
[WindowRect](#parameter-WindowRect)<br>
[jitterAmount](#parameter-jitterAmount)<br>
[lagAmount](#parameter-lagAmount)<br>
[lossPercent](#parameter-lossPercent)<br>
[simulate](#parameter-simulate)<br>

------------------
### WindowId<a name="parameter-WindowId"></a>

> The id of the unity window, must be unique or it causes issues.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |int|909

[Back To Top](#)

------------------
### WindowRect<a name="parameter-WindowRect"></a>

> Position of the window

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Rect|new Rect(Screen.width-270, 0, 200, 200)

[Back To Top](#)

------------------
### jitterAmount<a name="parameter-jitterAmount"></a>

> The amount of network jitter to simulate over the network. " <br>Adds a random delay of \"up to X milliseconds\" per message

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.0f

[Back To Top](#)

------------------
### lagAmount<a name="parameter-lagAmount"></a>

> The amount of lag to simulate over the network. " <br>Adds a fixed delay to all outgoing and incoming messages. In milliseconds

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.0f

[Back To Top](#)

------------------
### lossPercent<a name="parameter-lossPercent"></a>

> How many lost network packets you want to simulate. Drops the set " <br>percentage of messages. You can expect less than 2% drop in the internet today.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.0f

[Back To Top](#)

------------------
### simulate<a name="parameter-simulate"></a>

> Being the network simulation based on the settings? " <br>Enables and disables the simulation. A sudden, big change of network " <br>conditions might result in disconnects.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[DisconnectFromPhoton](#DisconnectFromPhoton)<br>
[LeaveRoom](#LeaveRoom)<br>
[OnGUI](#OnGUI)<br>
[SetReconnect](#SetReconnect)<br>
[Update](#Update)<br>

------------------
### public void DisconnectFromPhoton()<a name="DisconnectFromPhoton"></a>

>   Will disconnect from photon. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public void LeaveRoom()<a name="LeaveRoom"></a>

>   Leaves your current room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void OnGUI()<a name="OnGUI"></a>

>   Produces a visual interface at runtime which makes this useable with builds as well. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public void SetReconnect(bool isEnabled)<a name="SetReconnect"></a>

>   Sets the Network Managers reconnect value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|reconnect is true or false|

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   Use to automatically update the network settings according to the settings you apply in realtime. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

