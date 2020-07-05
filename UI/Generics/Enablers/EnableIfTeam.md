[Back To Index](../../../index.md)

# EnableIfTeam

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[checkType](#parameter-checkType)<br>
[items](#parameter-items)<br>
[teamName](#parameter-teamName)<br>

------------------
### checkType<a name="parameter-checkType"></a>

> ForEveryone=Does the NetworkManager teamName variable match this teamName variable?\n" <br>IfOwner=Are you the master client and does the NetworkManager teamName variable match this teamName variable?\n" <br>IfNotOwner=Are you NOT the master client and does the NetworkManager teamName variable match this teamName variable?

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |ChangeType|ChangeType.ForEveryone

[Back To Top](#)

------------------
### items<a name="parameter-items"></a>

> List of items to enable or disable.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject[]|new GameObject[] { }

[Back To Top](#)

------------------
### teamName<a name="parameter-teamName"></a>

> Enable the selected items if you are on the team name.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|""

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[EnableItems](#EnableItems)<br>
[Update](#Update)<br>

------------------
### protected virtual void EnableItems(bool isEnabled)<a name="EnableItems"></a>

>   Enable all the items or disable all the items based on the input value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, enable all the items?|

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   Enable or disable the objects dynamically if the specified settings match. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

