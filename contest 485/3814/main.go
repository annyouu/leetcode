package main

func maxCapacity(costs []int, capacity []int, budget int) int {
    n := len(costs)

	ans := 0

	for i := 0; i < n; i++ {
		if costs[i] < budget {
			ans = max(ans, capacity[i])
		}
	}

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			total_cost := costs[i] + costs[j]

			if total_cost >= budget {
				continue;
			}

			total_capacity := capacity[i] + capacity[j]

			ans = max(ans, total_capacity)
		}
	}

	return ans
}