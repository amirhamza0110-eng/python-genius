
def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):

    total_billing_hours = 30*24 

    total_monthly_cost = int(instance_count) * float(hourly_rate) * float(total_billing_hours)

    if total_monthly_cost > budget_cap:
        print("REJECTED: Budget Exceeded by $", total_monthly_cost - budget_cap)
    else:
        print("APPROVED: Total Estimated Cost is $", total_monthly_cost)

    return f"{total_monthly_cost}$"

print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))
