# Jumbo URL Shortener with Click Analytics

This project is a web-based URL shortener that not only provides a convenient way to shorten long URLs but also offers detailed click analytics to track the performance of your links.

## Project Overview

Our goal was to create a user-friendly platform that addresses the challenges associated with long, unwieldy URLs. We aimed to provide a solution that simplifies link sharing while offering valuable insights into link usage.

**Key Features:**

* **URL Shortening:** Converts long URLs into shorter, more manageable links.
* **User Authentication:** Secure login and registration system to manage your links.
* **Dashboard:** A centralized hub to view and manage your shortened URLs.
* **Click Analytics:** Detailed insights into click counts, click timestamps, and historical click data.
* **Graphical Representation:** Bar charts to visualize click trends over time (day, week, month, year).
* **Demo Data:** Option to view demo data, in case of no real data or errors.

## Tackling the Long URL Problem

Long URLs present several challenges:

* **Readability:** They are difficult to read and remember.
* **Sharing:** They are cumbersome to share on social media, messaging apps, and other platforms.
* **Aesthetics:** They can disrupt the visual appeal of content.
* **Character Limits:** Some platforms have character limits that long URLs can exceed.

We tackled these problems by:

* Implementing a robust URL shortening algorithm that generates short, unique links.
* Providing a user-friendly interface to easily create and manage short URLs.
* Offering click analytics to track link performance and understand audience engagement.

## Click Analytics: Understanding Your Audience

Our click analytics feature provides valuable insights into how your shortened URLs are performing. We display:

* **Total Click Count:** The total number of times a link has been clicked.
* **Click Timestamps:** Detailed records of when each click occurred.
* **Historical Click Data:** Visual representation of click trends over time (day, week, month, year) using bar charts.
* **Email of Clicker(Optional):** if the user is logged in, and clicks the short url, we store his email in the click history.

This data helps you understand:

* Which links are most popular.
* When your links are being clicked.
* The overall effectiveness of your link sharing strategies.

## Technology Stack

* **Python:** Backend development using Flask.
* **MongoDB:** Database for storing user and URL data.
* **Werkzeug:** For password hashing and security.
* **Chart.js:** For creating interactive bar charts.
* **HTML/CSS/JavaScript:** Frontend development.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```
2.  **Install dependencies:**
    ```bash
    pip install Flask pymongo werkzeug
    ```
3.  **Start MongoDB:**
    Ensure MongoDB is running on your local machine.
4.  **Run the application:**
    ```bash
    python app.py
    ```
5.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Future Enhancements

* **Custom Short URLs:** Allow users to create custom short URLs.
* **Geographic Click Data:** Track the location of clicks.
* **Device Click Data:** Track the devices used to click links.
* **API Integration:** Provide an API for programmatic URL shortening and analytics.
* **User Roles/Permissions**: Add admin roles, and other user roles.
* **More advanced graph options**: Line graphs, Pie charts etc.
* **Error Handling**: Add more robust error handling.
* **Security improvements**: Add more security features.

## Contributing

Contributions are welcome! If you have any ideas or suggestions, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
