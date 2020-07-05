[Back To Index](../index.md)

# AutoConnect

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[roomToAutoConnectTo](#parameter-roomToAutoConnectTo)<br>

------------------
 ### roomToAutoConnectTo<a name="parameter-roomToAutoConnectTo"></a>
> The photon room to auto connect to

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|"Testing_room"

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[AutoStart](#AutoStart)<br>
[Start](#Start)<br>

------------------
 ### IEnumerator AutoStart()<a name="AutoStart"></a>
>   Will automatically join the photon server, lobby, and finally the photon room name that you specify in the `roomToAutoConnectTo` parameter. This is used exclusively for testing builds quickly without having to go through a UI interface. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### void Start()<a name="Start"></a>
>   Calls the `AutoStart` IEnumerator 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

