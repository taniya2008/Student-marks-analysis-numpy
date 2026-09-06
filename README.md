# Student Marks Analysis 📊

A beginner-friendly NumPy project for analyzing student exam marks with statistical insights.

## Overview

This project demonstrates fundamental NumPy operations including:
- Generating random datasets
- Computing statistical measures (mean, max, min)
- Array filtering and indexing
- Data analysis workflows

Perfect for learning NumPy basics while working with a real-world-like dataset!

## Features

✨ **What it does:**
- Generates random marks for 30 students (0-100 range)
- Calculates class average, maximum, and minimum scores
- Filters students into pass/fail categories based on a threshold
- Displays comprehensive statistics

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/taniya2008/student-marks-analysis.git
   cd student-marks-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:
```bash
python project.py
```

### Example Output
```
--STUDENT MARKS ANALYSIS--
[45 78 92 55 88 ...]

--AVERAGE MARKS OF CLASS--
72.5

--MAXIMUM MARKS OF CLASS--
98

--MINIMUM MARKS OF CLASS--
12

--PASS/FAIL ANALYSIS (Passing Score: 40)--
Total passed students: 22
Total failed students: 8
```

## Project Structure

```
student-marks-analysis/
├── project.py           # Main analysis script
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules
└── LICENSE             # MIT License
```

## How It Works

The script performs the following steps:

1. **Data Generation**: Creates 30 random marks between 0-100
2. **Statistical Analysis**: 
   - Computes mean using `np.mean()`
   - Finds maximum with `np.max()`
   - Finds minimum with `np.min()`
3. **Pass/Fail Filtering**: Uses array filtering to separate passed (≥40) and failed (<40) students

## Learning Outcomes

This project is great for understanding:
- NumPy array creation and manipulation
- Statistical functions (mean, max, min)
- Boolean indexing and array filtering
- Working with numerical data

## Customization

You can easily modify:
- **Number of students**: Change the `30` in `np.random.randint()`
- **Mark range**: Adjust the `(0, 100)` parameters
- **Pass threshold**: Modify the passing score threshold in the filtering section
- **Display format**: Add more statistics or visualizations

## Future Enhancements

- 📈 Add matplotlib visualizations (histograms, bar charts)
- 📊 Calculate standard deviation and variance
- 🎯 Create grade distribution analysis
- 💾 Save results to CSV file
- 🎨 Add matplotlib visualizations

## Technologies Used

- **Python 3** - Core language
- **NumPy** - Numerical computing and array operations

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Fork and create pull requests

## Author

Taniya
- GitHub: [@taniya2008](https://github.com/taniya2008)
- Email: taniya@example.com

## Acknowledgments

- NumPy documentation: https://numpy.org/
- Great resource for learning NumPy: https://numpy.org/doc/stable/user/index.html

---

**Made with ❤️ for learning NumPy!**
