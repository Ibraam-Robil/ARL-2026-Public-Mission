# 🔗 Sensor Fusion Challenge

Welcome to the **ARL Workshop** solo coding mission!  
In this task, you will implement a sensor fusion algorithm that combines readings from three sensors using **majority voting logic**.

---

## 📝 Problem Statement

We have three sensors measuring the same data point at each time step. Due to noise or errors, their readings may not always match.  

You need to write a function:

```python
def fuse_readings(sensor1: list[int], sensor2: list[int], sensor3: list[int]) -> list:
    """
    Combines sensor readings using majority vote logic.
    Falls back to averaging when there is no consensus.
    
    Args:
        sensor1, sensor2, sensor3 (list[int]): Readings from 3 sensors.
    
    Returns:
        list: Final fused readings for each timestep.
              - Majority value if at least 2 sensors agree.
              - Average value if no consensus.
    """

```

## ⚙️ Requirements

### 1. Majority Vote  
If two or more sensors agree on a value, that value is chosen.  

**Example:**  
- Inputs → s1 = 80, s2 = 80, s3 = 82  
- Output → `80` (majority wins)  

---

### 2. Fallback to Average  
If all three sensors disagree, return the **average** of their values for that reading.  

**Example:**  
- Inputs → s1 = 10, s2 = 20, s3 = 30  
- Output → `20.0` (average of 10, 20, 30)  

---

### 3. Edge Cases  
- If the input lists are empty → return an **empty list**.  
- If they contain only one reading each → apply the same fusion logic.  


## ✅ Expected Output

The function should return a list of fused readings, one for each time step.

### Example

```python

sensor1 = [80, 70, 60, 90]
sensor2 = [80, 72, 60, 91]
sensor3 = [82, 70, 59, 90]

fuse_readings(sensor1, sensor2, sensor3)
# Expected Output: [80, 70, 60, 90]

s1 = [10, 20, 30]
s2 = [40, 50, 60]
s3 = [70, 80, 90]

fuse_readings(s1, s2, s3)
# Expected Output: [40.0, 50.0, 60.0]


# ▶️ How to Run

1. Implement your function inside **`solution.py`**.  
2. Run the test file with:

```bash
python -m unittest test_fusion_unittest.py
```

# 🎯 Goal

- Correctly implement **majority vote sensor fusion**  
- Handle **all edge cases** properly  
- Pass all provided **unit tests**  

Good luck — let’s see if you can build a **reliable sensor fusion system! 🚀**


