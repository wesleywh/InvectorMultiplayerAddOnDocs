[Back To Index](../index.md)

# MP_vControlAIShooter

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Attack](#Attack)<br>
[ResetAttackTriggers](#ResetAttackTriggers)<br>
[RollTo](#RollTo)<br>
[RotateAimArm](#RotateAimArm)<br>
[RotateAimHand](#RotateAimHand)<br>
[SetCurrentTarget](#SetCurrentTarget)<br>
[TriggerDamageRection](#TriggerDamageRection)<br>
[UpdateAI](#UpdateAI)<br>
[UpdateAimBehaviour](#UpdateAimBehaviour)<br>

------------------
 ### public override void Attack(bool strongAttack = false, int attackID = -1, bool forceCanAttack = false)<a name="Attack"></a>
>   Attacks with hands/melee weapon. If owner will tell the networked version to do the exact same attack via RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|strongAttack|bool type, Is this going to place the strong attack animation?|
|attackID|int type, The attack ID to play the correct animation type|
|forceCanAttack|bool type, *Read the invector documentation on this|

[Back To Top](#)

------------------
 ### public override void ResetAttackTriggers()<a name="ResetAttackTriggers"></a>
>   Resets the attack trigger in the animator, if owner tell the others to do the same via RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public override void RollTo(Vector3 direction)<a name="RollTo"></a>
>   Rolls to a particular direction. If owner will tell the networked versions to roll to that same direction. Call is done via RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|direction|***No found decription**|

[Back To Top](#)

------------------
 ### protected override void RotateAimArm(bool isUsingLeftHand = false)<a name="RotateAimArm"></a>
>   Rotates the aim arm normally if owner, if networked version will only rotate to the values it receives in the OnPhotonSerializeView function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isUsingLeftHand|***No found decription**|

[Back To Top](#)

------------------
 ### protected override void RotateAimHand(bool isUsingLeftHand = false)<a name="RotateAimHand"></a>
>   Rotates the aim hand normally if owner, if networked version will only rotate to the values it receives in the OnPhotonSerializeView function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isUsingLeftHand|***No found decription**|

[Back To Top](#)

------------------
 ### public override void SetCurrentTarget(Transform target, bool overrideCanseTarget)<a name="SetCurrentTarget"></a>
>   Set the current target of the AI. If owner will tell the other networked versions to what target they should update themselves to. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|Transform type, the target to target|
|overrideCanseTarget|bool type, force a sense on the target or not|

[Back To Top](#)

------------------
 ### protected override void TriggerDamageRection(vDamage damage)<a name="TriggerDamageRection"></a>
>   If owner will trigger the damage reaction animation and tell others to play that animation. If networked player this will do nothing. Call to update others is done via RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|damage|vDamage type, tells the type of hit reaction to do.|

[Back To Top](#)

------------------
 ### protected override void UpdateAI()<a name="UpdateAI"></a>
>   Heartbeat actions of the AI, this is only performed if the owner. If network player it only reacts to things the owner sends. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected override void UpdateAimBehaviour()<a name="UpdateAimBehaviour"></a>
>   Sets the IK positions, if not the owner will simply rotate IK placements according to received positions in the OnPhotonSerializeView function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

