# 🚗 Driving Behavior Analysis Challenge

Welcome to the **ARL Workshop** solo coding mission!  
Your task is to implement a function that analyzes a car’s driving behavior based on lane positions over time.

---

## 📝 Problem Statement

A car is driving on a three-lane road. At each second, we record which lane the car is in:

- `0` → Left lane  
- `1` → Middle lane  
- `2` → Right lane  

---

## ⚙️ Requirements

### 1. Lane Change  
Whenever the car switches from one lane to another, it counts as a **lane change**.  

**Example:**  
- `1 → 2`  
- `0 → 1`  

### 2. Dangerous Maneuver  
If the car switches **directly between the left lane (0) and the right lane (2)**, skipping the middle lane, this counts as a **dangerous maneuver**.  

**Example:**  
- `0 → 2`  
- `2 → 0`  

### 3. Edge Cases  
- If the list is empty (`[]`) or has only one element (e.g., `[1]`), there are **no lane changes** and **no dangerous maneuvers**.  

---

## ✅ Expected Output

The function should return a tuple:
-(number_of_lane_changes, number_of_dangerous_maneuvers)


**Example:**

```python
analyze_drive([1, 1, 2, 1, 0, 2, 2])
# Expected Output: (4, 1)


## 🧪 Test Cases

Here are some sample inputs and their expected outputs:

| Input (lanes)            | Output (lane changes, dangerous maneuvers) |
|---------------------------|--------------------------------------------|
| `[1, 1, 2, 1, 0, 2, 2]`   | `(4, 1)` |
| `[0, 1, 2, 1, 0]`         | `(4, 0)` |
| `[0, 2, 1, 2, 0]`         | `(4, 2)` |
| `[1, 1, 1, 1]`            | `(0, 0)` |
| `[0, 2]`                  | `(1, 1)` |
| `[2, 1, 0, 1, 2]`         | `(4, 0)` |
| `[0]`                     | `(0, 0)` |
| `[]`                      | `(0, 0)` |

```

## ▶️ How to Run

1. Write your solution inside **`Lane_maneuvers.py`** in the `analyze_drive` function.  

2. Run the test file:

```bash
python -m unittest .\test_maneuvers_unittest.py
```

## 🎯 Goal

1.Write clean, efficient code

2.Pass all the provided tests

3.Demonstrate your logical reasoning and problem-solving ability
