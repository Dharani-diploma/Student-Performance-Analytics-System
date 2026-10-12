"""Student Performance Analytics System - Python with AI, EWB Courses."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "students.csv"
OUTPUT_FILE = BASE_DIR / "student_analysis_output.csv"
CHART_FILE = BASE_DIR / "output_summary.png"
SUBJECTS = ["Maths", "Python", "DBMS"]

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    return "F"

def analyze_students(data):
    data = data.copy()
    data["Average"] = data[SUBJECTS].mean(axis=1).round(2)
    data["Grade"] = data["Average"].apply(calculate_grade)
    data["Result"] = data[SUBJECTS].ge(40).all(axis=1).map({True: "Pass", False: "Fail"})
    data["Attendance_Status"] = data["Attendance"].apply(
        lambda value: "Satisfactory" if value >= 75 else "Low"
    )
    return data

def create_charts(data, output_path):
    fig, axes = plt.subplots(3, 1, figsize=(12, 15))
    axes[0].bar(data["Name"], data["Average"])
    axes[0].set_title("Student Performance Analysis")
    axes[0].set_xlabel("Student Name")
    axes[0].set_ylabel("Average Marks")
    axes[0].tick_params(axis="x", rotation=75)

    grade_counts = data["Grade"].value_counts().reindex(["A", "B", "C", "D", "F"], fill_value=0)
    axes[1].bar(grade_counts.index, grade_counts.values)
    axes[1].set_title("Grade Distribution")
    axes[1].set_xlabel("Grade")
    axes[1].set_ylabel("Number of Students")

    result_counts = data["Result"].value_counts().reindex(["Pass", "Fail"], fill_value=0)
    axes[2].bar(result_counts.index, result_counts.values)
    axes[2].set_title("Pass and Fail Analysis")
    axes[2].set_xlabel("Result")
    axes[2].set_ylabel("Number of Students")
    plt.tight_layout()
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {INPUT_FILE}")
    students = pd.read_csv(INPUT_FILE)
    required = {"Student_ID", "Name", "Department", *SUBJECTS, "Attendance"}
    missing = required.difference(students.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    result = analyze_students(students)
    result.to_csv(OUTPUT_FILE, index=False)
    create_charts(result, CHART_FILE)
    print("Student Performance Analytics System")
    print("Course: Python with AI - EWB Courses")
    print(f"Total Students: {len(result)}")
    print(f"Pass: {(result['Result'] == 'Pass').sum()}")
    print(f"Fail: {(result['Result'] == 'Fail').sum()}")
    print(f"Class Average: {result['Average'].mean():.2f}")
    print("\nGrade Distribution:")
    print(result["Grade"].value_counts().reindex(["A", "B", "C", "D", "F"], fill_value=0).to_string())
    print("\nAttendance Status:")
    print(result["Attendance_Status"].value_counts().to_string())
    print(f"\nOutput saved: {OUTPUT_FILE.name}")
    print(f"Chart saved: {CHART_FILE.name}")

if __name__ == "__main__":
    main()
