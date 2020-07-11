[Back To Index](../../../index.md)

# GenericEventCaller

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[EventsToCall](#parameter-EventsToCall)<br>
[onAwake](#parameter-onAwake)<br>
[onDisable](#parameter-onDisable)<br>
[onEnable](#parameter-onEnable)<br>
[onStart](#parameter-onStart)<br>

------------------
### EventsToCall<a name="parameter-EventsToCall"></a>

> UnityEvent. List of user-defined events to call based on the specified settings.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |UnityEvent|new UnityEvent()

[Back To Top](#)

------------------
### onAwake<a name="parameter-onAwake"></a>

> Call these events when this objects calls onAwake (before on start)

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### onDisable<a name="parameter-onDisable"></a>

> Call these events when this gameobject is disabled

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### onEnable<a name="parameter-onEnable"></a>

> Call these events when this gameobject is enabled.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### onStart<a name="parameter-onStart"></a>

> Call these events when starting this object

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Awake](#Awake)<br>
[OnDisable](#OnDisable)<br>
[OnEnable](#OnEnable)<br>
[Start](#Start)<br>

------------------
### protected virtual void Awake()<a name="Awake"></a>

>   If the `onAwake` is true it will call the `EventsToCall` UnityEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void OnDisable()<a name="OnDisable"></a>

>   If the `onDisable` is true it will call the `EventsToCall` UnityEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void OnEnable()<a name="OnEnable"></a>

>   If the `onEnable` is true it will call the `EventsToCall` UnityEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void Start()<a name="Start"></a>

>   If the `onStart` is true it will call the `EventsToCall` UnityEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

