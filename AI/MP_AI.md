[Back To Index](../index.md)

# MP_AI

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[components](#parameter-components)<br>

------------------
### components<a name="parameter-components"></a>

> The components to disable if this is not owned by you.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |List<Behaviour>|new List<Behaviour> { }

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[SetComponentStatus](#SetComponentStatus)<br>
[Start](#Start)<br>

------------------
### void SetComponentStatus()<a name="SetComponentStatus"></a>

>   Enables/Disables AI Components based on if this is the owner or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void Start()<a name="Start"></a>

>   Waits to be connected a photon room before doing anything 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

