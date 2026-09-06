"""
Student Marks Analysis using NumPy
===================================

A simple project to demonstrate NumPy functionality for analyzing 
student exam marks and generating statistical insights.

Author: Taniya
GitHub: @taniya2008
Date: 2026
"""

import numpy as np


def generate_marks(num_students=30, min_score=0, max_score=100):
    """
    Generate random marks for students.
    
    Args:
        num_students (int): Number of students. Default: 30
        min_score (int): Minimum possible mark. Default: 0
        max_score (int): Maximum possible mark. Default: 100
    
    Returns:
        numpy.ndarray: Array of random marks
    """
    marks = np.random.randint(min_score, max_score, num_students)
    return marks


def calculate_statistics(marks):
    """
    Calculate key statistics from marks array.
    
    Args:
        marks (numpy.ndarray): Array of student marks
    
    Returns:
        dict: Dictionary containing mean, max, and min values
    """
    statistics = {
        'mean': np.mean(marks),
        'max': np.max(marks),
        'min': np.min(marks)
    }
    return statistics


def analyze_pass_fail(marks, passing_threshold=40):
    """
    Separate students into pass and fail categories.
    
    Args:
        marks (numpy.ndarray): Array of student marks
        passing_threshold (int): Minimum score to pass. Default: 40
    
    Returns:
        tuple: (passed_marks, failed_marks, passed_count, failed_count)
    """
    passed_marks = marks[marks >= passing_threshold]
    failed_marks = marks[marks < passing_threshold]
    
    return passed_marks, failed_marks, len(passed_marks), len(failed_marks)


def main():
    """Main execution function."""
    
    print("--STUDENT MARKS ANALYSIS--\n")
    
    # Generate random marks for 30 students between 0 to 100
    marks = generate_marks(num_students=30, min_score=0, max_score=100)
    print("Generated Student Marks:")
    print(marks)
    print()
    
    # Calculate and display statistics
    stats = calculate_statistics(marks)
    
    print("--AVERAGE MARKS OF CLASS--")
    print(f"{stats['mean']:.2f}")
    print()
    
    print("--MAXIMUM MARKS OF CLASS--")
    print(stats['max'])
    print()
    
    print("--MINIMUM MARKS OF CLASS--")
    print(stats['min'])
    print()
    
    # Analyze pass/fail distribution
    passed_marks, failed_marks, passed_count, failed_count = analyze_pass_fail(marks)
    
    print("--PASS/FAIL ANALYSIS (Passing Score: 40)--")
    print(f"Total passed students: {passed_count}")
    print(f"Total failed students: {failed_count}")
    print()
    
    # Additional statistics
    if passed_count > 0:
        print(f"Average marks of passed students: {np.mean(passed_marks):.2f}")
    if failed_count > 0:
        print(f"Average marks of failed students: {np.mean(failed_marks):.2f}")


if __name__ == "__main__":
    main()
