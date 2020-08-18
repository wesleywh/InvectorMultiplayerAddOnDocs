[Back To Index](../index.md)

# AI_MP_ShooterWeapon

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[SendNetworkShot](#SendNetworkShot)<br>
[Start](#Start)<br>

------------------
### public virtual void SendNetworkShot()<a name="SendNetworkShot"></a>

>   Send the 'Shoot' trigger over the network and tells the other network versions of this object to play their weapon fire function. 

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

