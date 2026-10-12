# Student Performance Analytics System

**Course/Internship:** Python with AI — EWB Courses  
**Technology:** Python, Pandas, NumPy, Matplotlib  
**Dataset:** 20 fictional student records

## Objective
Analyze student marks and attendance, calculate averages and grades, determine pass/fail results, and create summary charts.

## Problem Statement
Manually reviewing student marks can be time-consuming. This project automates basic performance and attendance analysis from a CSV dataset.

## Dataset
`students.csv` contains Student_ID, Name, Department, Maths, Python, DBMS, and Attendance. All records are fictional and for demonstration only.

## Rules Used
- Grade A: average >= 90
- Grade B: average >= 75 and < 90
- Grade C: average >= 60 and < 75
- Grade D: average >= 40 and < 60
- Grade F: average < 40
- Pass: marks in every subject are >= 40; otherwise Fail
- Attendance Satisfactory: >= 75%; otherwise Low

## How to Run
1. Install Python 3.10 or later.
2. In a terminal, navigate to this folder.
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`
5. The program creates `student_analysis_output.csv` and `output_summary.png`.

## Project Files
- `main.py` — analysis program
- `students.csv` — input dataset
- `student_analysis_output.csv` — analyzed output
- `output_summary.png` — charts summary
- `requirements.txt` — required libraries
- `sample_run_output.txt` — sample console output
- `PROJECT_DOCUMENTATION.md` — project documentation

## Final Outcome
The system provides a repeatable way to calculate student averages, grades, pass/fail status, attendance status, and visual summaries.

## GitHub Repository
Add your GitHub repository URL here before submission: `PASTE_YOUR_REPOSITORY_URL_HERE`
