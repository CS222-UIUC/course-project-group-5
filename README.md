<a name="readme-top"></a>
# Move Securely

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
![Tests](https://github.com/CS222-UIUC/course-project-group-5/actions/workflows/eslint.yml/badge.svg)
![Tests](https://github.com/CS222-UIUC/course-project-group-5/actions/workflows/pylint.yml/badge.svg)
![Tests](https://github.com/CS222-UIUC/course-project-group-5/actions/workflows/pytest-coverage.yml/badge.svg)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#introduction">Introduction</a></li>
      </ul>
    </li>
    <li>
      <a href="#technical-architecture">Technical Architecture</a>
      <ul>
        <li><a href="#diagram">Diagram</a></li>
      </ul>
    </li>
    <li><a href="#installation-and-usage">Installation and Usage</a></li>
    <li><a href="#group-members-and-their-roles">Group members and their roles</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## About the Project

Students have limited knowledge about living in a new city. They can find mixed information on Facebook groups, Reddit, online group chats, and discussing with others. By centralizing ratings and information about specific dorms and apartments, our application makes decisions easier and the process of moving to a new city smoother.

## Introduction

Our project is an apartment and dorm rating website application. Right now, it provides data for over 200 residences, allowing users to review, comment, and rate them. 

Anyone using the website can access the main page and scroll through the data smoothly and view residences they choose. Logged in users can access exclusive parts of the website like reviewing and commenting. Users can also view their previously liked apartments on their user page.

Our website differs from many residence finders through the interaction it allows, thereby combining the useful tool of finding residences in your area with social interaction.

## Technical Architecture


### Diagram


## Installation and Usage

The project is deployed to production and is available on the web at ––––?

If you would like to access the project yourself, follow these steps:

1. Clone the repo
   ```sh
   git clone https://github.com/CS222-UIUC/course-project-group-5.git
   ```

2. Install NPM packages
   ```sh
   npm install
   ```

## Group members and their roles

[Minh Phan](https://github.com/MinhPhan8803) created the backend for the main page, which sorts residences based on prices and rating, writes reviews to the database, and deletes reviews. Minh did all the frontend work on the user page, website navigation, and did the most CSS out of everyone.

[Samuel Du](https://github.com/sd-20) created the login and register pages' frontend and contributed to the user page backend. In the user page backend, he updated the user's data and compiled the user's liked residences. Also, he contributed to our GitHub CI/CD pipeline for verifying test coverage and linting our code.

[Zongxian Feng](https://github.com/xxxfzxxx) created the residence scraper to populate our database and completed the right section of the main page, where users can view individual residence data, along with review, comment, and rate them. He also contributed to the CI/CD pipeline.

[Aden Krakman](https://github.com/akrakman) created the search bar and the left section of the main page, where anyone can see the residence data in a scrollable list. He contributed to the user page backend, where users update their data. Also, he implemented the user page API, where a session object is used and the API gets and posts data to the frontend user page.

Everyone tested their code and contributed to the overall design and implementation of the project.

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.

## Acknowledgements
Thank you to our team mentor Nikhil.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/CS222-UIUC/course-project-group-5.svg?style=for-the-badge
[contributors-url]: https://github.com/CS222-UIUC/course-project-group-5/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/CS222-UIUC/course-project-group-5.svg?style=for-the-badge
[forks-url]: https://github.com/CS222-UIUC/course-project-group-5/network/members
[stars-shield]: https://img.shields.io/github/stars/CS222-UIUC/course-project-group-5.svg?style=for-the-badge
[stars-url]: https://github.com/CS222-UIUC/course-project-group-5/stargazers