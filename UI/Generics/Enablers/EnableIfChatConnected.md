[Back To Index](../../../index.md)

# EnableIfChatConnected

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[buttons](#parameter-buttons)<br>
[gameObjects](#parameter-gameObjects)<br>
[invertActions](#parameter-invertActions)<br>

------------------
### buttons<a name="parameter-buttons"></a>

> List of buttons to enable or disable.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Button[]|new Button[] { }

[Back To Top](#)

------------------
### gameObjects<a name="parameter-gameObjects"></a>

> List of GameObjects to enable or disable.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject[]|new GameObject[] { }

[Back To Top](#)

------------------
### invertActions<a name="parameter-invertActions"></a>

> False = perform normal, True = Will enable `buttons` and `gameObjects` if the chat is NOT enabled.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[EnableTargets](#EnableTargets)<br>
[Update](#Update)<br>

------------------
### protected virtual void EnableTargets(bool isEnabled)<a name="EnableTargets"></a>

>   Will enable or disable all of the `buttons` and `gameObjects` based on the input value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, enable the targets?|

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   Will enable the buttons or gameobjects if you're connected/not connected to the ChatBox data channel. Actions are opposite if `invertActions` is true. Objects are enabled/disabled by calling `EnableTargets` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

