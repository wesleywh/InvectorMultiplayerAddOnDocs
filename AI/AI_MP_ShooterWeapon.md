[Back To Index](../index.md)

# AI_MP_ShooterWeapon

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[ChildTreeCheck](#ChildTreeCheck)<br>
[SendNetworkEmptyClip](#SendNetworkEmptyClip)<br>
[SendNetworkOnFinishAmmo](#SendNetworkOnFinishAmmo)<br>
[SendNetworkOnFinishReload](#SendNetworkOnFinishReload)<br>
[SendNetworkOnFullPower](#SendNetworkOnFullPower)<br>
[SendNetworkReload](#SendNetworkReload)<br>
[SendNetworkShot](#SendNetworkShot)<br>
[SendOnChangerPowerCharger](#SendOnChangerPowerCharger)<br>
[SendOnDisableAim](#SendOnDisableAim)<br>
[SendOnEnableAim](#SendOnEnableAim)<br>
[Start](#Start)<br>

------------------
### protected override void ChildTreeCheck()<a name="ChildTreeCheck"></a>

>   Make sure this has a index tree built for this current object. If not then it builds one. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void SendNetworkEmptyClip()<a name="SendNetworkEmptyClip"></a>

>   Sends a command to the other networked versions of this weapon to trigger their empty clip function 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void SendNetworkOnFinishAmmo()<a name="SendNetworkOnFinishAmmo"></a>

>   Sends a command to the other networked versions of this weapon to trigger their on finish ammo function 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void SendNetworkOnFinishReload()<a name="SendNetworkOnFinishReload"></a>

>   Sends a command to the other networked versions of this weapon to trigger their on finish reload function 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void SendNetworkOnFullPower()<a name="SendNetworkOnFullPower"></a>

>   Sends a command to the other networked versions of this weapon to trigger their on full power function 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void SendNetworkReload()<a name="SendNetworkReload"></a>

>   Sends a command to the other networked versions of this weapon to trigger their reload function 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void SendNetworkShot()<a name="SendNetworkShot"></a>

>   Send the 'Shoot' trigger over the network and tells the other network versions of this object to play their weapon fire function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void SendOnChangerPowerCharger(float amount)<a name="SendOnChangerPowerCharger"></a>

>   Sends a command to the other networked versions of this weapon to trigger their on chane power charger function 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void SendOnDisableAim()<a name="SendOnDisableAim"></a>

>   Sends a command to the other networked versions of this weapon to trigger their on disable aim function 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void SendOnEnableAim()<a name="SendOnEnableAim"></a>

>   Sends a command to the other networked versions of this weapon to trigger their on enable aim function 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected override void Start()<a name="Start"></a>

>   Find the parent MP_vAIShooterManager component. Also makes sure this weapon has a valid vShooterWeapon component. Finally, makes sure the root transform has a photon view. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

