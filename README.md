
# Network Intrusion Detection System (NIDS)

![NIDS Dashboard](/images/home.png)

A Network Intrusion Detection System (NIDS) built using machine learning and deep learning techniques to detect anomalous network activities in real-time. This project leverages TensorFlow for model training, Scapy for packet manipulation, and Flask for the web-based dashboard.

## Features

- **Real-Time Detection**: Monitors network traffic and detects anomalies in real-time.
- **Geeky Dashboard**: A sleek, dark-themed dashboard for visualizing alerts and network activities.
- **Machine Learning**: Utilizes deep learning models for accurate intrusion detection.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Clone the Repository

\`\`\`bash
git clone https://github.com/yourusername/nids.git
cd nids
\`\`\`

### Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Download the Model

Ensure you have the trained TensorFlow model (\`nids_model.h5\`) in the project directory. You can train your own model or use the provided one.

## Running the Application

1. **Start the Flask Application**

   \`\`\`bash
   python app.py
   \`\`\`

2. **Open the Dashboard**

   Open your web browser and navigate to \`http://127.0.0.1:5000\` to view the dashboard.

## Project Structure

\`\`\`plaintext
nids/
│
├── templates/
│   └── dashboard.html          # HTML template for the dashboard
│
├── static/
│   └── styles.css              # CSS styles for the dashboard
│
├── images/
│   ├── dashboard.png           # Screenshot of the dashboard
│   └── another_screenshot.png  # Another screenshot
│
├── app.py                      # Main Flask application and anomaly detection logic
├── requirements.txt            # Python dependencies
├── nids_model.h5               # Pre-trained TensorFlow model
├── IDS.ipynb                   # Jupyter Notebook with project code
└── README.md                   # Project README
\`\`\`


### Dashboard

![Dashboard](path/to/your/dashboard_screenshot.png)

## Technologies Used

- **Flask**: Web framework for Python.
- **TensorFlow**: Open-source library for machine learning.
- **Scapy**: Python library for network packet manipulation.
- **Bootstrap**: CSS framework for responsive web design.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
