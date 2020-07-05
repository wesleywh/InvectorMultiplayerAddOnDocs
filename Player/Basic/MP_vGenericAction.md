[Back To Index](../../index.md)

# MP_vGenericAction

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[EndAction](#EndAction)<br>
[ResetActionState](#ResetActionState)<br>
[ResetTriggerSettings](#ResetTriggerSettings)<br>
[TriggerAnimation](#TriggerAnimation)<br>

------------------
 ### protected override void EndAction()<a name="EndAction"></a>
>   Calls `GenericAction_EndAction` RPC which will have the network player end its action when the owner player does. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public override void ResetActionState()<a name="ResetActionState"></a>
>   Calls `AnimatorActionState` RPC which will have the network player reset ther action stat when the owner player does. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public override void ResetTriggerSettings()<a name="ResetTriggerSettings"></a>
>   Calls the `AnimatorActionState` RPC which will have the network player follow the action stat of the owner player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public override void TriggerAnimation()<a name="TriggerAnimation"></a>
>   Is used to call `AnimatorActionState` RPC which will have the network player mimic the action stats of the owner player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

