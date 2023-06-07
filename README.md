## Knapsack Problem

The Knapsack Problem is a classic optimization problem in computer science and mathematics. It belongs to the class of combinatorial optimization problems and is often used to demonstrate various algorithms and techniques.

### Problem Description

Given a set of items, each with a weight and a value, and a knapsack with a maximum capacity, the problem is to determine the most valuable combination of items to include in the knapsack, without exceeding its capacity.

The goal is to maximize the total value of the selected items while ensuring that the total weight does not exceed the capacity of the knapsack.

### Problem Formulation

The Knapsack Problem can be formulated as follows:

- Input:
  - `n`: The number of items available.
  - `weights`: An array/list of size `n` representing the weights of the items.
  - `values`: An array/list of size `n` representing the values of the items.
  - `capacity`: The maximum weight capacity of the knapsack.

- Output:
  - A binary array/list of size `n` representing the selection of items, where `1` indicates an item is selected and `0` indicates it is not.

- Objective:
  - Maximize the total value of the selected items.

- Constraints:
  - The sum of the weights of the selected items should not exceed the capacity of the knapsack.

### Solution Approaches

Several algorithms and techniques can be employed to solve the Knapsack Problem, including:

- Brute Force: Enumerate all possible combinations of items and select the one with the maximum value while satisfying the capacity constraint. This approach can be computationally expensive for large problem sizes.

- Dynamic Programming: Utilize a dynamic programming table to store intermediate results and compute the optimal solution iteratively. This approach provides an efficient solution for problems with small-to-medium problem sizes.

- Greedy Algorithms: Employ heuristics to make locally optimal choices at each step. Examples include the Fractional Knapsack Algorithm, which selects items based on their value-to-weight ratios, and the Greedy Knapsack Algorithm, which selects items based on their values.

- Metaheuristic Techniques: Utilize stochastic optimization algorithms such as Simulated Annealing, Genetic Algorithms, or Particle Swarm Optimization to search for good solutions in large solution spaces. These techniques are suitable for tackling complex instances of the Knapsack Problem.

### Usage

This repository contains an implementation of the Knapsack Problem in Python. It includes a `knapsack` class that provides various methods for solving the problem, including brute force, local search, and simulated annealing algorithms. The class can be instantiated with either direct input or by reading the problem data from a file.

You can use this implementation to experiment with different solution approaches and compare their performance on different problem instances.

Please refer to the provided documentation and examples for more details on how to use the `knapsack` class and the available solution methods.

### References

- Wikipedia: [Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem)
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). MIT Press.
