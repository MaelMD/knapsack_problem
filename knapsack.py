import random
import math

class knapsack:
    
    def __init__(self, *args):
                
        if len(args) == 1:
            with open(args[0], "r") as fp:
                ligne = fp.readline().strip().split(' ')
                self.nb_objects = int(ligne[0])
                self.capacity = int(ligne[1])
                lignes = fp.readlines()
                weights = []
                values = []
                for i in range(self.nb_objects):
                    ligne = lignes[i].strip().split(' ')
                    weights.append(int(ligne[1]))
                    values.append(int(ligne[0]))
                self.weights = weights
                self.values = values
        if len(args) == 4:
            self.capacity = int(args[0])
            self.nb_objects = int(args[1])
            self.weights = args[2]
            self.values = args[3]
    
    def _repr_(self):
        txt = "Number of objects    : "
        txt += str(self.nb_objects)
        txt += "\nCapacity of knapsack : "
        txt += str(self.capacity)
        txt += "\n   Weights \t Values :"
        for i in range(self.nb_objects): 
            txt += "\n\t" + str(self.weights[i]) + "\t\t  " + str(self.values[i])
        return txt        
        
    def is_feasible(self, solution):
        
        b = bin(solution)[2:]
        weight = 0
        N = len(b)
        i = N - 1
        while i >= 0:
            if b[i] == '1':
                weight += self.weights[N - 1 - i]
            i -= 1
        return weight <= self.capacity
    
    def print_solution(self, solution):
        
        b = bin(solution)[2:]
        print(b)
        objects = []
        N = len(b)
        i = N - 1
        while i >= 0:
            if b[i] == '1':
                objects.append(N - i)
            i -= 1
        print("Objects to include in the knapsack:", objects)
        print("Knapsack value:", self.eval_solution(solution))
        
    def eval_solution(self, solution):
                
        b = bin(solution)[2:]
        value = 0
        N = len(b)
        i = N - 1
        while i >= 0:
            if b[i] == '1':
                value += self.values[N - 1 - i]
            i -= 1
        return value

    def brute_force(self):
        
        optimal_value = 0
        optimal_solution = None
        for solution in range(0, 2 ** self.nb_objects):
            if self.is_feasible(solution):
                solution_value = self.eval_solution(solution)
                if solution_value > optimal_value:
                    optimal_value = solution_value
                    optimal_solution = solution
        return optimal_solution, optimal_value
                    
            
    def random_solution(self):
        
        while True:
            solution = random.randint(0, 2 ** self.nb_objects - 1)
            if self.is_feasible(solution):
                return solution        
    
    def move(self, solution, i):
        b = bin(solution)[2:]
        b_list = list(b.zfill(self.nb_objects))  # Ensure binary representation length matches the number of objects
        b_list[i] = '1' if b_list[i] == '0' else '0'
        new_b = ''.join(b_list)
        return int(new_b, 2)
    
    def best_improvement_ls(self):
        current_solution = self.random_solution()
        current_value = self.eval_solution(current_solution)

        while True:
            best_solution = current_solution
            best_value = current_value
            improved = False

            for i in range(self.nb_objects):
                new_solution = self.move(current_solution, i)
                new_value = self.eval_solution(new_solution)

                if new_value > best_value and self.is_feasible(new_solution):  # Check feasibility
                    best_solution = new_solution
                    best_value = new_value
                    improved = True

            if not improved:
                return current_solution, current_value

            current_solution = best_solution
            current_value = best_value


    def first_improvement_ls(self):
        current_solution = self.random_solution()
        current_value = self.eval_solution(current_solution)

        while True:
            improved = False

            for i in range(self.nb_objects):
                new_solution = self.move(current_solution, i)
                new_value = self.eval_solution(new_solution)

                if new_value > current_value and self.is_feasible(new_solution):  # Check feasibility
                    current_solution = new_solution
                    current_value = new_value
                    improved = True
                    break

            if not improved:
                return current_solution, current_value
            
    def full_random(self):
        best_solution = None
        best_value = 0
        
        for _ in range(1000):  # Generate a large number of solutions
            solution = self.random_solution()
            value = self.eval_solution(solution)

            if value > best_value:
                best_solution = solution
                best_value = value
        
        return best_solution, best_value
    
    def homogene_sa(self):
        temperature = 1000  # Initial temperature
        cooling_rate = 0.95  # Cooling rate
        
        current_solution = self.random_solution()
        current_value = self.eval_solution(current_solution)
        best_solution = current_solution
        best_value = current_value
        
        while temperature > 1:
            for _ in range(100):  # Number of iterations at each temperature level
                new_solution = self.random_solution()
                new_value = self.eval_solution(new_solution)
                
                delta = new_value - current_value
                
                if delta > 0 or math.exp(delta / temperature) > random.random():
                    current_solution = new_solution
                    current_value = new_value
                
                if new_value > best_value:
                    best_solution = new_solution
                    best_value = new_value
            
            temperature *= cooling_rate
        
        return best_solution, best_value
    

    def no_homogene_sa(self):
        """
        Résout le problème du sac à dos par la méthode du recuit simulé
        en utilisant la variante "non homogène" de l'algorithme.
        """
        temperature = 1000  # Initial temperature
        
        current_solution = self.random_solution()
        current_value = self.eval_solution(current_solution)
        
        best_solution = current_solution
        best_value = current_value
        
        while temperature > 1:
            for _ in range(100):  # Number of iterations at each temperature level
                new_solution = self.random_solution()
                new_value = self.eval_solution(new_solution)
                
                delta = new_value - current_value
                
                if delta > 0 or math.exp(delta / temperature) > random.random():
                    current_solution = new_solution
                    current_value = new_value
                
                if new_value > best_value:
                    best_solution = new_solution
                    best_value = new_value
            
            temperature -= 1
        
        return best_solution, best_value

import tkinter as tk

j = knapsack(80, 5, [10, 20, 30, 40, 50], [100, 200, 300, 400, 500])

def button_click(choice):
    global output_label
    if choice == "1":
        # Brute Force
        opt_sol, val_opt = j.brute_force()
        output_label.config(text="Brute Force:\n" + str(j.print_solution(opt_sol)))
    elif choice == "2":
        # Local Search - First Improvement
        opt_sol, val_opt = j.first_improvement_ls()
        output_label.config(text="Local Search - First Improvement:\n" + str(j.print_solution(opt_sol)))
    elif choice == "3":
        # Local Search - Best Improvement
        opt_sol, val_opt = j.best_improvement_ls()
        output_label.config(text="Local Search - Best Improvement:\n" + str(j.print_solution(opt_sol)))
    elif choice == "4":
        # Simulated Annealing - Homogeneous
        opt_sol, val_opt = j.homogene_sa()
        output_label.config(text="Simulated Annealing - Homogeneous:\n" + str(j.print_solution(opt_sol)))
    elif choice == "5":
        # Simulated Annealing - Non-Homogeneous
        opt_sol, val_opt = j.no_homogene_sa()
        output_label.config(text="Simulated Annealing - Non-Homogeneous:\n" + str(j.print_solution(opt_sol)))
    elif choice == "6":
        # Exit the program
        root.destroy()

root = tk.Tk()
root.title("Knapsack Problem")

button_frame = tk.Frame(root)
button_frame.pack()

button_margin_top = 10
button_max_width = 100

button_1 = tk.Button(button_frame, text="1. Brute Force", command=lambda: button_click("1"))
button_2 = tk.Button(button_frame, text="2. Local Search - First Improvement", command=lambda: button_click("2"))
button_3 = tk.Button(button_frame, text="3. Local Search - Best Improvement", command=lambda: button_click("3"))
button_4 = tk.Button(button_frame, text="4. Simulated Annealing - Homogeneous", command=lambda: button_click("4"))
button_5 = tk.Button(button_frame, text="5. Simulated Annealing - Non-Homogeneous", command=lambda: button_click("5"))
button_6 = tk.Button(button_frame, text="6. Exit", command=lambda: button_click("6"))

button_1.configure(width=button_max_width)
button_2.configure(width=button_max_width)
button_3.configure(width=button_max_width)
button_4.configure(width=button_max_width)
button_5.configure(width=button_max_width)
button_6.configure(width=button_max_width)


button_1.pack(pady=button_margin_top)
button_2.pack(pady=button_margin_top)
button_3.pack(pady=button_margin_top)
button_4.pack(pady=button_margin_top)
button_5.pack(pady=button_margin_top)
button_6.pack(pady=button_margin_top)

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
