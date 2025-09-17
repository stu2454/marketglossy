# AT Market Intelligence Dashboard

A comprehensive Streamlit web application for monitoring and analyzing Australia's Assistive Technology (AT) market across 13 key segments. Built to support NDIS market stewardship and evidence-based policy decisions.

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

## 📊 Features

### Market Intelligence at a Glance
- **13 AT Market Segments**: Mobility Aids, Communication Devices, Vision Equipment, and more
- **Real-time Health Indicators**: Traffic light system for immediate market status assessment
- **Comprehensive Metrics**: Market value, participant demographics, service delivery, pricing trends
- **Quality Monitoring**: Satisfaction scores, return rates, safety incidents
- **Innovation Tracking**: New product launches, technology trends, R&D investment

### Interactive Visualizations
- **Dynamic Dashboards**: Switch between market segments with live data updates
- **Trend Analysis**: Mini charts showing market growth and performance over time
- **Geographic Insights**: Metro vs regional vs remote access patterns
- **International Benchmarking**: Price comparisons with UK NHS and US Medicare
- **Cross-Segment Analysis**: Scatter plots comparing all 13 segments simultaneously

### Export & Analysis
- **PDF Export**: Generate printable market reports
- **Data Downloads**: CSV exports for further analysis
- **Detailed Tables**: Drill down into raw market data
- **Performance Rankings**: See how segments compare across key metrics

## 🛠 Installation & Setup

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/at-market-dashboard.git
cd at-market-dashboard
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser**
Navigate to `http://localhost:8501`

### Deploy to Streamlit Cloud

1. **Fork this repository** to your GitHub account
2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**
3. **Click "New app"** and select your forked repository
4. **Set the main file path** to `app.py`
5. **Click "Deploy"** - your app will be live in minutes!

## 📁 Project Structure

```
at-market-dashboard/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore           # Git ignore patterns
└── assets/              # Static assets (logos, images)
    └── ndis_logo.png
```

## 🔧 Configuration

### Data Sources
The current version uses simulated data for demonstration. To connect to real NDIS data:

1. **Replace the `generate_sample_data()` function** in `app.py`
2. **Add database connection parameters** to a `.env` file:
```env
DATABASE_URL=your_database_connection_string
NDIS_API_KEY=your_api_key
```
3. **Install additional dependencies** if needed:
```bash
pip install python-dotenv psycopg2-binary requests
```

### Customization
- **Add new segments**: Extend the `segments` list in `generate_sample_data()`
- **Modify metrics**: Update the metric calculations and thresholds
- **Change styling**: Customize CSS in the `st.markdown()` blocks
- **Add features**: Leverage Streamlit's extensive widget library

## 📊 Market Segments Covered

1. **Mobility Aids** - Wheelchairs, scooters, walking aids
2. **Communication Devices** - Speech generating devices, tablets
3. **Vision Equipment** - Magnifiers, screen readers, navigation aids
4. **Hearing Equipment** - Hearing aids, assistive listening devices
5. **Personal Care** - Bathroom aids, dressing aids, eating utensils
6. **Home Modifications** - Ramps, rails, accessible fixtures
7. **Vehicle Modifications** - Hand controls, wheelchair lifts
8. **Prosthetics** - Artificial limbs and devices
9. **Orthotics** - Braces, supports, therapeutic footwear
10. **Workplace Equipment** - Ergonomic aids, computer access
11. **Recreation Equipment** - Sports wheelchairs, adaptive equipment
12. **Smart Home Tech** - IoT devices, home automation
13. **Therapy Equipment** - Exercise equipment, positioning aids

## 📈 Key Metrics Tracked

### Market Health Indicators
- **Market Value & Growth** - Total expenditure and year-over-year trends
- **Participant Demographics** - Age, disability type, geographic distribution
- **Service Delivery** - Wait times from approval to delivery
- **Price Trends** - Inflation rates compared to CPI benchmarks

### Quality & Outcomes
- **Participant Satisfaction** - Survey scores and feedback analysis  
- **Return Rates** - Equipment returns and exchanges
- **Safety Incidents** - Recalls and safety-related issues
- **Provider Performance** - Service delivery quality metrics

### Market Competition
- **Provider Count** - Number of active suppliers
- **Market Concentration** - Market share distribution
- **Geographic Coverage** - Provider availability by region
- **Innovation Activity** - New product launches and R&D investment

## 🎯 Use Cases

### For NDIS Policy Teams
- **Monitor market health** across all AT segments
- **Identify intervention opportunities** before problems escalate
- **Support evidence-based funding decisions** with real-time data
- **Track progress** against strategic objectives

### For Market Stewardship
- **Early warning system** for market failures
- **Competition monitoring** to prevent monopolistic behavior
- **Quality assurance** through outcome tracking
- **Innovation incentive** design based on market gaps

### For Participants & Advocates
- **Transparent market information** for informed decision-making
- **Service quality benchmarks** to set expectations
- **Geographic equity monitoring** to identify access gaps
- **Innovation updates** on new AT technologies

### For Providers & Industry
- **Market intelligence** for business planning
- **Competitive benchmarking** against industry standards
- **Demand forecasting** for capacity planning
- **Performance feedback** for service improvement

## 🤝 Contributing

We welcome contributions to improve the AT Market Intelligence Dashboard!

### How to Contribute
1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines for Python code
- Add docstrings to new functions
- Update README.md if adding new features
- Test locally before submitting PRs
- Keep commits atomic and well-described

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **NDIS** for providing the market stewardship framework
- **Streamlit team** for the excellent dashboard framework
- **Plotly** for powerful visualization capabilities
- **Australian AT community** for insights into market needs

## 📞 Support

For questions, issues, or feature requests:

- **Create an issue** on GitHub for bugs or feature requests
- **Email**: your.email@example.com for general inquiries
- **Documentation**: Check the [Wiki](https://github.com/yourusername/at-market-dashboard/wiki) for detailed guides

## 🔄 Version History

- **v1.0.0** - Initial release with 13 market segments
- **v1.1.0** - Added international benchmarking features
- **v1.2.0** - Enhanced geographic analysis and ATSI tracking
- **v2.0.0** - Real-time data integration (planned)

---

**Built with ❤️ for the Australian assistive technology community**