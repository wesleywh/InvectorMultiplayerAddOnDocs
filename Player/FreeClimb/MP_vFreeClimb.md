[Back To Index](../../index.md)

# MP_vFreeClimb

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[ClimbJump](#ClimbJump)<br>
[ClimbUp](#ClimbUp)<br>
[EnterClimb](#EnterClimb)<br>
[ExitClimb](#ExitClimb)<br>
[Start](#Start)<br>

------------------
### protected override void ClimbJump()<a name="ClimbJump"></a>

>   Calls `CrossFadeInFixedTime` RPC with the `ClimbJump` Animation. This makes all the networked players play the `ClimbJump` animation. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected override void ClimbUp()<a name="ClimbUp"></a>

>   Calls the `CrossFadeInFixedTime` RPC with `ClimbUpWall`. This is to have the network players mimic the climbing animatiosn of the owner. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected override void EnterClimb()<a name="EnterClimb"></a>

>   Calls the `CrossFadeInFixedTime` RPC with `EnterClimbGrounded` or `EnterClimbAir`. This is to have the network players mimic climbing animations of the owner. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected override void ExitClimb()<a name="ExitClimb"></a>

>   Calls the `CrossFadeInFixedTime` RPC with `ExitGrounded` or `ExitAir`. This is to have the network players mimic the climbing animations of the owner. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected override void Start()<a name="Start"></a>

>   Disables this component if you're a networked player and not the owner player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

