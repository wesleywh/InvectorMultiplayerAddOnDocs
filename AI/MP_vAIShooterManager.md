[Back To Index](../index.md)

# MP_vAIShooterManager

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[LoadIKAdjust](#LoadIKAdjust)<br>
[ReloadWeapon](#ReloadWeapon)<br>
[SetLeftWeapon](#SetLeftWeapon)<br>
[SetRightWeapon](#SetRightWeapon)<br>
[Shoot](#Shoot)<br>

------------------
### public override void LoadIKAdjust(string category)<a name="LoadIKAdjust"></a>

>   Load the IK adjust catagory into vAIShooterManager but also tells the other networked versions to do the same if you're the owner. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|category|string type, the ik catagory to set|

[Back To Top](#)

------------------
### public override void ReloadWeapon()<a name="ReloadWeapon"></a>

>   Reloads the weapon, if owner will tell the other networked versions to play the reload animations. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public new void SetLeftWeapon(GameObject weapon)<a name="SetLeftWeapon"></a>

>   Sets the left weapon in the vAIShooterManager component but also tells the other networked versions to do the same and with what weapon. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|weapon|GameObject type, the weapon to set|

[Back To Top](#)

------------------
### public new void SetRightWeapon(GameObject weapon)<a name="SetRightWeapon"></a>

>   Sets the right weapon in the vAIShooterManager component but also tells the other networked versions to do the same and with what weapon. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|weapon|GameObject type, the weapon to set|

[Back To Top](#)

------------------
### public override void Shoot(Vector3 aimPosition, bool useSecundaryWeapon = false)<a name="Shoot"></a>

>   Shoot your equipped weapon at the target point. If owner will set the aim position that is referenced by the MP_ShooterWeapon component. Which triggers firing the networked versions weapon at that point. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|aimPosition|Vector3 type, the point to fire a shot at|
|useSecundaryWeapon|bool type, fire the secondary weapon?|

[Back To Top](#)

