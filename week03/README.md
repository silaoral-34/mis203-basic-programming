# Lab Quiz: Order Approval System (`lab03_order_approval.py`)

## 📋 Task Overview
This Python program processes customer orders by evaluating order amounts, available stock, requested quantities, and membership status. It implements conditional logic to approve or reject orders and applies a 10% discount for eligible members.

---

##  Program Rules & Features
* **Stock & Quantity Validation:** Rejects the order if the requested quantity is less than or equal to 0, or exceeds the available stock.
* **Approval & Reasons:** Displays the specific reason for approval or rejection.
* **Discount Policy:** Applies a 10% discount to approved orders totaling **500 TRY or more** if the customer is a registered member.
* **Output Restrictions:** Does not display a final price if an order is rejected.

---

## Boundary Test Cases Table

| Test Case | Inputs (Order Amount, Stock, Requested Qty, Member) | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Case 1 (Below 500 TRY)** | 450 TRY, Stock: 10, Qty: 2, Member: Yes | Approved, No discount (Final: 450 TRY) | Approved, No discount (Final: 450 TRY) | Pass |
| **Case 2 (Exact 500 TRY)** | 500 TRY, Stock: 10, Qty: 2, Member: Yes | Approved, 10% discount applied (Final: 450 TRY) | Approved, 10% discount applied (Final: 450 TRY) | Pass |
| **Case 3 (Invalid Stock)** | 600 TRY, Stock: 5, Qty: 10, Member: No | Rejected, No final price displayed | Rejected, No final price displayed | Pass |

---

## Testing & Changes Log
* **Test Performed:** Tested the boundary condition with exactly 500 TRY (`500 TRY`, Member: `Yes`) to ensure the 10% discount calculation triggered properly.
* **Change Made After Testing:** Updated the membership input check to handle lowercase and uppercase strings smoothly (`.strip().lower()`), preventing potential user input errors.




