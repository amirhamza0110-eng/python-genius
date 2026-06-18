deferentiate a function called  estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
Then calculate the total monthly cost by the following multiplicatiopn formula  (instances * hourly_rate * 720)
After that if else condition apply to check against budget_cap
Returned the function with f string 

Test the Cases to verify  execution:
print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))

