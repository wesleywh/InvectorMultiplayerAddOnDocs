[Back To Index](../index.md)

# Counter

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[counter](#parameter-counter)<br>
[counterType](#parameter-counterType)<br>

------------------
 ### counter<a name="parameter-counter"></a>
> The text object that will display the number as it counts up/down.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |Text|null

[Back To Top](#)

------------------
 ### counterType<a name="parameter-counterType"></a>
> Do you want this to count up or down to the target amount?

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |CounterType|CounterType.CountDown

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[StartCounting](#StartCounting)<br>
[Update](#Update)<br>

------------------
 ### public void StartCounting(float amount)<a name="StartCounting"></a>
>   Start counting down from the specified input amount. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|amount|float type, the amount of time to start counting down from.|

[Back To Top](#)

------------------
 ### private void Update()<a name="Update"></a>
>   Is responsible for counting down and setting the `counter` value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

