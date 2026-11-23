# 📊 NumPy Analyzer 

An interactive Command Line Interface (CLI) application built using **Python** and **NumPy**. This program demonstrates Object-Oriented Programming (OOP) principles while performing complex N-dimensional array manipulations, mathematical operations, array searching/sorting, and statistical analysis.

---

## 🚀 Features

- 🏗️ **Array Creation**: Create custom 1D, 2D, and 3D NumPy arrays dynamically with input validation.
- 🎯 **Indexing & Slicing**: Flat indexing and multi-dimensional slicing (1D, 2D, 3D).
- 🧮 **Mathematical Operations**:
  - Element-wise operations: Addition, Subtraction, Multiplication, Division.
  - Linear Algebra: 1D Vector Dot Product and 2D Matrix Multiplication (`matmul`).
- 🔗 **Combine & Split**: Concatenate arrays vertically/horizontally and split arrays along axes.
- 🔍 **Search, Sort & Filter**:
  - Value searching using `np.where`.
  - Ascending & Descending sorting (with multi-dimensional row-wise handling).
  - Greater-than condition filtering.
- 📈 **Statistical Aggregates**:
  - Sum, Mean, Median, Min, Max, Standard Deviation, Variance.
  - Custom Percentile calculation.
  - Pearson Correlation Coefficient between datasets.
- 🛡️ **Robust Error Handling**: Handles input errors, type mismatched operations, and invalid dimensions gracefully.

---

## 🏗️ Object-Oriented Programming (OOP) Highlights

This project highlights several key Python OOP concepts:

- **Encapsulation**: Private attributes (e.g., `__array`) and private helper methods (e.g., `__show_info`) to prevent unauthorized modifications.
- **Class Methods (`@classmethod`)**: Accessing class-level metadata (e.g., `project_title()`).
- **Static Methods (`@staticmethod`)**: Utility functions independent of instance state (e.g., `check_choice()`).
- **Modular Design**: Dedicated methods for each operational domain.

---

## 🖼️ Output Preview

See the actual program output:

[![View Output](https://img.shields.io/badge/👀_View_Output-red?style=for-the-badge)](https://github.com/dh-2006/Analyzer/blob/main/output.png)

---

## 🎥 Project Demo

Watch the complete working demonstration:

[![Watch Demo](https://img.shields.io/badge/▶️_Watch_Project_Demo-blue?style=for-the-badge)](https://drive.google.com/file/d/1kyuVveu5aXrBBDf-25BZMLDYD42xmJRd/view?usp=sharing)

---

## 💻 Source Code

View the complete Python source code:

[![Open Source Code](https://img.shields.io/badge/💻_View_Source_Code-green?style=for-the-badge)](https://github.com/dh-2006/Analyzer/blob/main/Numpy_Analyzer.py)

---

## 🛠️ Prerequisites & Installation

### Requirements
- **Python 3.x**
- **NumPy library**

## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/dh-2006/Analyzer.git
cd Analyzer
```
2. **Install required dependencies:**
   ```bash
   pip install numpy
   ```

3. **Run the application:**
   ```bash
   python Numpy_Analyzer.py
   ```

---

## 📖 How to Use

1. Run the program and select **Option 1** to initialize and create an array (1D, 2D, or 3D).
2. Once the array is created, navigate through options **2 to 5** to perform arithmetic, statistical calculations, slicing, or sorting.
3. Select **Option 6** to exit the program.

---

## 📜 License

This project is created for educational purposes. Feel free to use and modify it!
