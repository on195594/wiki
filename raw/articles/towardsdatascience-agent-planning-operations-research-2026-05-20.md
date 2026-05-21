---
title: Optimizing AI Agent Planning with Operations Research and Data Science
author: Destin Gong
source: Towards Data Science
source_url: https://towardsdatascience.com/optimizing-ai-agent-planning-with-operations-research-and-data-science/
published: 2026-05-20
captured: 2026-05-21
type: raw-source
status: raw
tags: [agent, multi-agent, orchestration, optimization, research]
extraction: Jina Reader extraction for a Towards Data Science / Medium-family page; Gemini summary output preserved at /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260521-174636-Optimizing-AI-Agent-Planning-with-Operations-Research-and-Data-Science-981597-544223120-summary.md.
---

# Optimizing AI Agent Planning with Operations Research and Data Science

Source URL: https://towardsdatascience.com/optimizing-ai-agent-planning-with-operations-research-and-data-science/
Extraction note: Article prose was extracted via Jina Reader from a Towards Data Science / Medium-family page. The source article uses synthetic data for the optimization examples; preserve the numeric results as illustrative evidence, not Hermes defaults.

to large enterprises, more and more organizations are embracing AI agents and adopting multi-agent architectures to deliver reliable, scalable, and manageable solutions. AI agent and LLM costs can quickly spiral without careful management. In this post, we will uncover several agent planning and cost optimization business problems and frame them as operations research solutions through the lens of data science. If you are interested in learning more about Agent Planning and Agentic AI, check out my article on “[How to Build Your Own Agentic AI System Using CrewAI](https://towardsdatascience.com/how-to-build-your-own-agentic-ai-system-using-crewai/)“.

## What is Optimization in Operations Research?

Operations research leverages mathematical models and optimization to find the best decision under practical constraints. It is the backbone of prescriptive analytics, which transforms predictive insights to actions that are critical to decision making. Framing a real-world situation into an abstract mathematical model is the key to solving any operations research problem.

A simple yet widely mentioned example of operations research is the linear programming problem, where we try to find values of x and y that maximize a linear equation (e.g. 2x + 4y), subject to the constraints x ≥ 0 and y ≥ 0. Operations research problems typically include the following key components:

1.   **Decision Variables:**The variables to be determined.
2.   **Constraints:**The real-world limitations on resources or requirements.
3.   **Objectives:**The goal to be maximized or minimized.

## How to Optimize Agent Cost and Resource Allocation

AI agent planning involves making resource allocation decisions within a company’s budget while still achieving the best possible outcomes, which makes it a strong fit for operations research scenarios. We can map the core components above to agent cost optimization and resource planning use cases.

*   Decision Variables: Agents assign to tasks or projects
*   Constraints: budget, response time, token
*   Objectives: minimize costs, maximize return on investment

We will use 4 most standard optimization patterns to address common agent planning scenarios:

*   **Set-Covering Problem:** Choose the smallest set of agents to cover all required tasks, skills, or business functions, with the objective of minimizing cost without leaving gaps in capability.
*   **Assignment Problem:** Decide which agent should handle each project, with the goal of maximizing overall output value.
*   **Knapsack Problem:** Select the best bundle of agents under a fixed budget, to maximize total output tokens.
*   **Network Problem:** Design workflows across a network of agents to meet department and user demands at the lowest cost under capacity constraints.

To make this more practical, we will walk through four examples in Python using the Gurobi library. Gurobi is an enterprise-grade mathematical optimization solver that supports many problem types, including linear programming and mixed-integer programming. It is often used as the “solver engine” behind operations research applications because it can handle large-scale models efficiently and provides robust APIs, including Python, for defining decision variables, constraints, and objective functions. Gurobi lets data scientists focus on modeling rather than implementing custom optimization algorithms. Please note that this article is not affiliated with Gurobi, and all functionalities mentioned here can be achieved using the free license. All datasets shown in this project are synthetic and are used to demonstrate a proof of concept.

* * *

## 1. Set-Covering Problem – Agent Skill Coverage

![Image 1: Set-Covering Problem - Agent Skill Coverage](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/Screenshot-2026-05-17-at-1.11.56-PM-1024x565.png)
**Set-covering** is a classic optimization problem refers to the problem of choosing the **smallest number of options** so that **every required item is covered at least once**. A common AI agent cost-optimization scenario that fits the set-covering problem is skill coverage, where we aim to identify the minimum number of agents needed to cover the fundamental skills required to support the company’s daily operations.

> Problem Statement: The company wants to embed agents into daily operations and cover the nine skill areas listed in the “Skill Area” table below. Each agent costs $20k to build and specializes in a distinct set of skills as shown in the “Agent Skill” table. How can the company minimize the total cost of building agents while still covering every area?

Skill Area

![Image 2](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/image-211.png)
Agent Skill

![Image 3](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/Screenshot-2026-05-17-at-12.39.58-PM-985x1024.png)
### Implementation

We can frame it as an optimization problem that follows the set-covering pattern and solve it using Gurobi library, defined by following key components — data, model, variables, constraints and objectives.

*   Data: load the data for skills, agents and agent costs (which is 20k each agent)

```
## data
skills = data["skills"]
agents = data["agents"]
agent_skills = data["agent_skills"]
agent_costs = {i: 20 for i in agents}
```

*   Model: Create the Gurobi model with a name “Set Covering”. If you haven’t installed gurobipy yet, run the command

```
## model
import gurobipy as gp
model = gp.Model("Set Covering")
```

*   Variables: The decision variables are binary variables associated with every agent, with a lower bound of 0 and an upper bound of 1 to indicate whether an agent is selected. Gurobi offers a range of preset variable types, including `GRB.BINARY`, `GRB.INTEGER`, and `GRB.CONTINUOUS`, etc.

```
## variables
X = model.addVars(agents, lb=0, ub=1, vtype=GRB.BINARY, name="x")
```

*   Constraints: For each skill area, sum of all selected agents with that skill should be more than 1, ensuring that we have at least one agent to cover the skill area. We use the summation function `gp.quicksum` to add constraints using weighted sum and then use nested loop expressions to iterate through nine skill areas.

```
## constraints: for each skill in skills, sum of agents with that skill ≥ 1
for j in skills:
    model.addConstr(
        gp.quicksum(X[i] for i in agents if j in agent_skills[i]) >= 1,
        name=f'{j}_area_constr'
    )
```

*   Objective: Minimize the total cost of selected agents, calculated as the weighted sum of each agent’s cost multiplied by the decision variable indicating whether that agent is selected.

```
## objectives: minimize sum of agents selected
model.setObjective(
    gp.quicksum(agent_costs[i] * X[i] for i in agents),
    GRB.MINIMIZE
)
```

Lastly, we run the model optimization using `model.optimize()`.

### Business Impact

In this section, we first interpret the model’s optimal output and then estimate the impact of making decisions based on that optimal output versus making random choices. In a business setting, this helps leaders allocate budget effectively by determining which agents to build, deploy, or retire.

#### Optimal Result

`model.ObjVal` prints out the optimal objective value. For each binary decision variable, we use `X[i].X > 0.5` to print out the selected agents.

```
print(f"Total agents selected: {round(model.ObjVal, 4)}")
for i in agents:
    if X[i].X > 0.5:
        print(f"Agent {i} selected.")
```

Alternatively, Claude Code suggests me the following snippet to display the model output in a structured manner.

```
print("================ Set-Covering: Skill Coverage ================")
if model.Status == GRB.OPTIMAL:
    selected = [i for i in agents if X[i].X > 0.5]
    print(f"Minimum agents needed : {len(selected)}")
    print(f"Total cost            : ${model.ObjVal:.0f}k")
    print("\nSelected agents:")
    for agent in selected:
        covered = ", ".join(
            f"{s}({skill_labels[s]})" for s in agent_skills[agent]
        )
        print(f"  - {agent}  [{covered}]")
else:
    print("No optimal solution found.")
```

Output below shows that the optimal agent planning is to select 4 agents (General Support Agent, Access & Permissions Agent, CRM Agent and Cost & Performance Optimization Agent) to cover all skills with $80k budget spend.

```
================ Set-Covering: Skill Coverage ================
Minimum agents needed : 4
Total cost            : $80k

Selected agents:
  - General Support Agent  [F(Support), C(Knowledge), H(Collaboration)]
  - Access & Permissions Agent  [F(Support), E(Automation), G(Governance)]
  - CRM / Relationship Management Agent  [A(Planning), B(Tool Use), C(Knowledge)]
  - Cost & Performance Optimization Agent  [D(Analytics), I(Monitoring), J(Optimization)]
```

#### Simulations

We then simulated random selections and compared them with the optimal outcome. As shown below, we generated 500 feasible agent selections (blue histogram) with costs ranging from $80k to $200k and an average cost of $134.6k (blue dotted line). This means the optimization helps the business to reduce the cost by ($134.6k − $80k)/$134.6 = 40.6% on average.

![Image 4](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/image-179-1024x505.png)
```
──────────────────────────────────────────────────
  Set Covering — Skill Coverage
──────────────────────────────────────────────────
  Minimum (Optimal) : 80.00 k$
  Sim mean           : 132.88 k$
  Sim min            : 80.00 k$
  Sim max            : 220.00 k$
  Feasible solutions : 500/500
──────────────────────────────────────────────────
```

Explore the complete implementation in our GitHub [repo](https://github.com/destingong/agent-optimization.git).

## 2. Assignment Problem – Agent Resource Allocation

![Image 5: Assignment Problem - Agent Resource Allocation](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/Screenshot-2026-05-17-at-1.12.23-PM-1024x563.png)
Assignment Problem follows a common pattern to **match tasks to people or objects**, usually one-to-one or one-to-many relationship, to **maximize output produced or minimize cost**. Agent resource allocation fits this problem pattern, as it requires allocating a set of agents across projects, typically with the constraint that each project is matched with one primary agent and the objective of achieving the highest total output value.

> Problem Statement: The company has built a set of agents to work on 9 projects and each project requires assigning one primary agent. The table below shows how much value each agent can contribute to each project. How can the company maximize the overall value by assigning the most appropriate primary agent to projects?

![Image 6](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/Screenshot-2026-05-17-at-12.44.26-PM-1024x460.png)
### Implementation

We follow the same six-step process to break down this assignment problem.

*   Data: load the data for agents, projects and values. Create a `value_map` dictionary to represent the relationship between agent and project.

```
## data
agents = data["agents"]
projects = data["projects"]
values = data["values"]

# Build value lookup: (agent, project) -> score
value_map = {
    (agents[i], projects[j]): values[i][j]
    for i in range(len(agents))
    for j in range(len(projects))
}
```

*   Model: Create a Gurobi model with the name “Assignment”.

```
## model
import gurobipy as gp
model = gp.Model("Assignment")
```

*   Variables: The decision variables in this problem should indicate whether an agent is assigned to a project, which is a binary variable associated with each unique combination of agent and project.

```
## variables
from gurobipy import GRB
X = model.addVars(agents, projects, lb=0, ub=1, vtype=GRB.BINARY, name="x")
```

*   Constraints: For each project, sum of all assigned agents should be exactly one. For each agent, sum of projects it is assigned to should be at least one.

```
## constraints: each project is assigned exactly one agent
for j in projects:
    model.addConstr(
        gp.quicksum(X[(i, j)] for i in agents) == 1,
        name=f"{j}_project_constr",
    )

## constraints: each agent is assigned at least one project
for i in agents:
    model.addConstr(
        gp.quicksum(X[(i, j)] for j in projects) >= 1,
        name=f"{i}_agent_constr",
    )
```

*   Objective: Maximize the overall value score using the sum of each agent’s score on each project multiplied by the decision variable indicating whether the agent is assigned to the project.

```
## objective: maximize the overall value score
model.setObjective(
    gp.quicksum(value_map[(i, j)] * X[(i, j)] for i in agents for j in projects),
    GRB.MAXIMIZE,
)
```

### Business Impact

By framing agent allocation as an assignment problem, businesses can allocate agents to projects in a way that best matches their skills and maximizes overall value. This improves return on investment by increasing output quality while achieving business objectives with the same set of pre-built agents.

To understand the business impact of this optimization scenario, we will first interpret the recommended allocation after running `model.optimize()`, then estimate the impact on the overall value score by comparing the optimal result with random allocations.

#### Optimal Result

`model.ObjVal` prints out the optimal objective value. For each binary variable that indicates agent allocation, we use `X[i, j].X > 0.5` to examine if agent _i_ is allocated to project _j_.

```
print(f"Total value: {round(model.ObjVal, 4)}")
for i in agents:
    for j in projects:
        if X[(i, j)].X > 0.5:
	        print(f"Agent {i} should be allocated to Project {j}.")
```

OR use the following snippet to display the model output more verbosely.

```
print("================ Assignment Problem: Resource Allocation ================")
if model.Status == GRB.OPTIMAL:
    print(f"Maximum total suitability score: {model.ObjVal:.0f}\n")
    print(f"{'Agent':<45} {'Project':<6} {'Description':<30} {'Score'}")
    print("-" * 95)
    for i in agents:
        for j in projects:
            if X[(i, j)].X > 0.5:
                print(
                    f"{i:<45} {j:<6} {project_labels[j]:<30} {obj_coeffs[(i, j)]}"
```

The output below shows the optimal resource allocation, which assigns one primary agent to each project and achieves a total suitability score of 77.

```
================ Assignment Problem: Resource Allocation ================
Maximum total suitability score: 77

Agent                                         Project Description                    Score
-----------------------------------------------------------------------------------------------
Analytics & Insights Agent                    P1     Exec Metrics Dashboard         9
Analytics & Insights Agent                    P7     Churn Risk Monitor             8
Knowledge Management Agent                    P8     Onboarding Guide Bot           9
Marketing Campaign Orchestration Agent        P3     Lead-Scoring Model             9
Marketing Campaign Orchestration Agent        P6     Feature Launch Brief           8
Customer Support Automation Agent             P2     CX Knowledge Bot               9
Data Quality & Monitoring Agent               P9     SLA Incident Triage            8
Workflow Orchestration Agent                  P5     Experiment Analysis            8
Governance & Compliance Agent                 P4     Policy QA Assistant            9
```

#### Simulations

We simulated 500 random, feasible agent allocations and compared them with the optimal outcome, where the value score is 77. As shown below, the 500 feasible allocations produced overall value scores ranging from 55 to 72, with a mean value score of 63.16. This indicates that optimization improves value scores by (77 − 63.16) / 63.16 = 21.9% on average.

![Image 7](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/image-181-1024x505.png)
```
──────────────────────────────────────────────────
  Assignment — Agent-to-Project Allocation
──────────────────────────────────────────────────
  Maximum (Optimal) : 77.00 score
  Sim mean           : 63.16 score
  Sim min            : 55.00 score
  Sim max            : 72.00 score
  Feasible solutions : 500/500
──────────────────────────────────────────────────
```

## 3. Knapsack Problem – Agent Budgeting

![Image 8: Knapsack Problem - Agent Budgeting](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/Screenshot-2026-05-17-at-1.13.10-PM-1024x569.png)
The knapsack Problem is an optimization scenario where we pick the **best combination of items** while staying within a limit, like a **budget or capacity constraint**. Portfolio management and logistics arrangement are popular real-world implications. It is suitable for agent budget allocation scenarios where we need to maximize the agent output under a limited company budget.

> Problem Statement: Given a $4,000 monthly budget, select agents from the list below, each with a fixed monthly cost, to maximize total tokens generated.

![Image 9](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/image-204.png)
### Implementation

Again, use the 6-step process to break down this knapsack problem.

*   Data: load the agent list, each agent’s monthly cost, and each agent’s token output, along with a fixed $4,000 monthly budget.

```
## data
agents = data["agents"]
N = range(len(agents))  # number of agents
C = data["costs"]   # cost per agent
P = data["tokens"]  # tokens per agent
K = 4000  # $4000 monthly budget
```

*   Model: Create a Gurobi model with the name “Knapsack”.

```
## model
import gurobipy as gp
model = gp.Model("Knapsack")
```

*   Variables: A binary decision variable is associated with each agent to indicate whether they are selected.

```
## variables
X = model.addVars(N, lb=0, ub=1, vtype=GRB.BINARY, name="x")
```

*   Constraints: Total costs of all selected agents should not exceed the budget K.

```
## constraint: total cost must not exceed budget
model.addConstr(
    gp.quicksum(C[i] * X[i] for i in N) <= K,
    name="budget_constr",
)
```

*   Objective: Maximize the total number of tokens generated by all selected agents.

```
## objective: maximize total tokens generated
model.setObjective(
    gp.quicksum(C[i] * X[i] for i in N),
    GRD.MAXIMIZE,
)
```

### Business Impact

This type of optimization problem is widely used in business because it helps maximize output under a fixed budget. We will compare the optimized results with 500 random agent selections under the same budget constraints.

#### Optimal Result

After running `model.optimize()`, we use `model.ObjVal` to get the optimal objective value of total tokens generated. For each binary decision variable, we use `X[i].X > 0.5` to check whether agent _i_ is selected.

```
print(f"Total tokens generated: {round(model.ObjVal, 4)}")
for agent in N:
    if X[agent].X > 0.5:
        print(f"Agent {agent} selected.")
```

The model output suggests selecting 4 agents (Intent Classifier, Inventory Checker, Review Analyzer and Analytics Reporter) that allow us to generate the maximum number of tokens (e.g. 215 million tokens) within the $4000 monthly budget.

```
================ Knapsack Problem: Budgeting ================
Budget              : $4,000
Total cost used     : $4,000
Total tokens (M)    : 215

Agent                            Cost ($)   Tokens (M)
-------------------------------------------------------
Intent Classifier                     800           50
Inventory Checker                   1,200           70
Review Analyzer                       900           45
Analytics Reporter                  1,100           50
-------------------------------------------------------
TOTAL                               4,000          215
```

#### Simulations

We simulated 500 random, feasible agent allocations under the same $4,000 budget and compared them with the optimal result of 215 million tokens. In these simulations, total tokens ranged from 50M to 215M, with an average of 151.61M, showing the optimized plan performs about (215 − 151.61) / 151.61 = 41.8% better than the average random allocation.

![Image 10](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/image-212-1024x505.png)
```
──────────────────────────────────────────────────
  Knapsack — Agent Budget Selection
──────────────────────────────────────────────────
  Maximum (Optimal) : 215.00 tokens (M)
  Sim mean           : 151.61 tokens (M)
  Sim min            : 50.00 tokens (M)
  Sim max            : 215.00 tokens (M)
  Feasible solutions : 500/500
──────────────────────────────────────────────────
```

## 4. Network Problem – Agent Routing

![Image 11: Network Problem - Agent Routing](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/Screenshot-2026-05-17-at-1.14.59-PM-1024x570.png)
Lastly, we will discuss the network problem, which addresses scenarios that **require balancing supply and demand, or inputs and outputs** across a collection of entities. For example, it involves moving inventories through a warehouse network at the lowest cost while respecting shipping capacity. A directed acyclic graph (DAG) is a common graphical model for network problems, where nodes represent distinct entities and arcs represent flows from an input entity to an output entity. A critical constraint in a network problem is that each node meets the requirement of “supply + inflow = demand + outflow”, so net flow equals demand minus supply.

Agent routing and multi-agent orchestration fit this pattern because they coordinate multiple agents across a sequence of inputs and outputs and require designing a workflow that balances user demand with each agent’s available capacity. As demand for multi-agent workflows grows, this domain offers more opportunities to optimize collaboration efficiency and resource consumption.

> Problem Statement: A company has a multi-agent architecture that includes a Coding Agent and a Writing Agent, along with two agent hubs that serve as coordinators. The IT, Marketing, and Operations departments each require a certain number of requests to be fulfilled each month, as shown in the table below. While departments can communicate directly with the two agents, this typically incurs a higher cost per request. Routing requests through the agent hubs reduces costs by standardizing the communication protocol. Each link also has a maximum monthly request capacity, as detailed in the table below. What is the most cost-effective way to route 12,000 task requests from the Coding Agent and Writing Agent to the Marketing, IT, and Operations departments?

Supply & Demand

![Image 12](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/image-207-1024x417.png)
Routing Cost / Capacity

![Image 13](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/image-208-1024x264.png)
### Implementation

*   Data: Load the data for agent supply capacities and department request demands, along with the cost and capacity for each arc flowing from an agent to a hub or directly to a department.

```
## data
nodes = data["nodes"]
supplies = data["supplies"]
demands = data["demands"]
arcs = [(a, b) for a, b, _, __ in data["arcs"]]
costs = {(a, b): c   for a, b, c, __ in data["arcs"]}
capacities = {(a, b): cap for a, b, _, cap in data["arcs"]}
```

*   Model: Create a Gurobi model with the name “Network”.

```
## model
import gurobipy as gp
model = gp.Model("Network")
```

*   Variables: Define a continuous variable for each arc to represent the number of requests flowing from one node to another, with an upper bound equal to the arc’s capacity.

```
## variables
X = model.addVars(arcs, lb=0, ub=capacities, vtype=GRB.CONTINUOUS, name="x")
```

*   Constraints: For each node (including agents, agent hubs and departments), the sum of supply and inflow requests should equal the sum of demand and outflow requests.

```
## constraints: flow balance at each node
for i in nodes:
    model.addConstr(
        supplies[i] + gp.quicksum(X[(j, i)] for j in nodes if (j, i) in arcs)
        == demands[i] + gp.quicksum(X[(i, j)] for j in nodes if (i, j) in arcs),
        name=f"{i}_balance_constr",
    )
```

*   Objective: Minimize the total cost of all requests from an agent to an agent hub or to a department directly.

```
## objective: minimize total routing cost
model.setObjective(
    gp.quicksum(costs[(i, j)] * X[(i, j)] for i, j in arcs),
    GRB.MINIMIZE,
)
```

### Business Impact

Agent routing optimization helps decide how many requests to send along each link so all department demand is met at the lowest cost, while considering the workflow capacity and system limitations.

#### Optimal Result

We use `model.ObjVal` to get the optimal objective value for total cost. Then we use `X[(i,j)].X` to print the number of requests flowing from each input node to each output node.

```
print(f"Total Cost: {round(model.ObjVal, 2)}")
for (i,j) in arcs:
    if X[(i,j)].X > 0:
        print(f"Send {X[(i,j)].X} units of flow on the arc from {i} to {j}")
```

As shown in the output below, we see that the optimal solution costs $5,630 per month to fulfill 12k requests demanded by Marketing, IT and Operations teams.

```
================ Network Routing Problem: Agent Routing ================
Minimum total routing cost: $5,630.00

Arc                                               Flow    Cap   Cost/req   Total Cost
-------------------------------------------------------------------------------------
Coding Agent -> Marketing Dept                     1500   2000       0.80     1,200.00
Coding Agent -> IT Dept                            2000   2000       0.60     1,200.00
Coding Agent -> Operations Dept                    1200   1200       0.30       360.00
Coding Agent -> Relay Hub A                        1200   1500       0.30       360.00
Coding Agent -> Relay Hub B                         600   1200       0.20       120.00
Writing Agent -> Marketing Dept                     2000   2000       0.50     1,000.00
Writing Agent -> IT Dept                            1000   1000       0.20       200.00
Writing Agent -> Operations Dept                    1000   1000       0.20       200.00
Writing Agent -> Relay Hub A                         300   2000       0.40       120.00
Writing Agent -> Relay Hub B                        1200   1200       0.20       240.00
Relay Hub A -> Marketing Dept                     1500   1500       0.30       450.00
Relay Hub B -> IT Dept                            1000   1000       0.10       100.00
Relay Hub B -> Operations Dept                     800   1000       0.10        80.00

Demand fulfillment:
  Marketing Dept: received 5000 / needed 5000
  IT Dept: received 4000 / needed 4000
  Operations Dept: received 3000 / needed 3000
```

#### Simulations

After running 500 feasible solutions with random request routing from agents to departments, we can estimate that the optimal result reduces costs by 33% ($8,425.98 − $5,630.00 = $2,795.98) on average.

![Image 14](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/image-209-1024x505.png)
```
──────────────────────────────────────────────────
  Network — Agent Routing
──────────────────────────────────────────────────
  Minimum (Optimal) : $5,630.00
  Sim mean           : $8,425.98
  Sim min            : $5,750.00
  Sim max            : $11,150.00
  Feasible solutions : 500/500
──────────────────────────────────────────────────
```

* * *

## Take Home Message

In this article, we cover four common optimization patterns in operations research and their practical business impact, using AI agent planning scenarios:

*   **Set Covering:** Choose the smallest set of agents that still covers all required tasks, skills, or business functions, with the objective of minimizing cost without leaving gaps in capability.
*   **Assignment:** Decide which agent should handle each project, with the goal of maximizing overall output value.
*   **Knapsack:** Select the best bundle of agents or features under a fixed budget, to maximize total output tokens.
*   **Network:** Design workflows across a network of agents to meet department and user demand at the lowest cost under capacity constraints.

Complex agent planning becomes tractable when it is framed as a **standard optimization model with variables, constraints, and an objective.** Modern solvers like Gurobi can quickly find optimal solutions that significantly reduce spend or increase return on investment.

### More Resources Like This

Please accept cookies to access this content

Please accept cookies to access this content
