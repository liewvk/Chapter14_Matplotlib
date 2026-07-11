import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def create_score_bar_chart(df, output_folder):
    plt.figure(figsize=(8, 5))

    plt.bar(df["Name"], df["Score"])

    plt.title("Student Scores")
    plt.xlabel("Student")
    plt.ylabel("Score")
    plt.xticks(rotation=30)
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(output_folder / "student_scores.png")
    plt.show()


def create_attendance_bar_chart(df, output_folder):
    plt.figure(figsize=(8, 5))

    plt.bar(df["Name"], df["Attendance"])

    plt.title("Student Attendance")
    plt.xlabel("Student")
    plt.ylabel("Attendance")
    plt.xticks(rotation=30)
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(output_folder / "student_attendance.png")
    plt.show()


def create_attendance_score_scatter(df, output_folder):
    plt.figure(figsize=(8, 5))

    plt.scatter(df["Attendance"], df["Score"])

    plt.title("Attendance vs Score")
    plt.xlabel("Attendance")
    plt.ylabel("Score")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(output_folder / "attendance_vs_score.png")
    plt.show()


def create_score_histogram(df, output_folder):
    plt.figure(figsize=(8, 5))

    plt.hist(df["Score"])

    plt.title("Distribution of Student Scores")
    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(output_folder / "score_distribution.png")
    plt.show()


def main():
    data_file = Path("data") / "students.csv"
    output_folder = Path("outputs")

    output_folder.mkdir(exist_ok=True)

    df = pd.read_csv(data_file)

    print("Student Data")
    print("------------")
    print(df)

    print()
    print("Creating charts...")

    create_score_bar_chart(df, output_folder)
    create_attendance_bar_chart(df, output_folder)
    create_attendance_score_scatter(df, output_folder)
    create_score_histogram(df, output_folder)

    print()
    print("Charts saved in the outputs folder.")


main()












