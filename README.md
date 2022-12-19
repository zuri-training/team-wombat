<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/zuri-training/team-wombat.git">
    <img src="images/crona_icon.png" alt="Logo" width="80" height="80">
  </a>

  <h1 align="center">Auth-Wiki</h1>

  <p align="center">
<a><strong>A web Application for a library of authentication code that allows users register, download material or codes and interact.</strong></a>
   </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Auth_Wiki is a library of authentication code that allows users register, download material and interact.

## Hosting link:
* https://authwiki-teamwombat.netlify.app
* http://35.193.24.21
* https://web-production-26b8.up.railway.app/
* https://web-production-1075.up.railway.app

## Features

- **User: Unauthenticated**

  - Visit the platform to view basic information about it.
  - View and Interact with the documentation.
  - Register to contribute.
  - Browse through library with limited information, download should not be available.

- **User: Authenticated**
  - Full access to the platform.
  - Contribute, however contribution should be limited to comments and reactions.
  - Able to view example usage.
  - Download code samples.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

- Python
- Django
- Figma
- Git
- Bootstrap
- JavaScript

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Run Locally

> Preferred tool for creating and managing virtual environments: `pipenv` (see installation guide: <https://pypi.org/project/pipenv/>).

Clone the project

```bash
git clone https://github.com/zuri-training/team-wombat.git
```

Go to the project directory

```bash
cd team-wombat
```

Create a virtual environment and install needed dependencies in it

```bash
pipenv install
```

Activate the virtual environment

```bash
pipenv shell
```

pip install -r requirements.text

Create a `.env` file in the same directory as the `settings.py` (`config` folder) with the following contents:

> **Don't enclose the secret key in any quotation mark.**

```python
SECRET_KEY=<your-secret-key>
```

_Generate a secret key from <https://djecrety.ir/>._

Run the migrations

```python
python manage.py migrate
```

Run the server

```python
python manage.py runserver
```

> Architecture Used: Monolith (Django Templating)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

- When website is up and running, insert it function here
  _For more examples, please refer to the [Documentation](https://docs.google.com/document/d/1JMyK4SDO66Tbe5y-eS7xEj1emh6zOdzANvlfLntgP5Y/edit?usp=sharing)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Design And Documentation
- [x] Frontend Build
- [x] Backend Build
- [x] Testing
- [x] Server Hosting
  - [ ] Product Feedback
  - [ ] Changelog

<!--See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/team-wombat`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/team-wombat`)
5. Open a Pull Request

See [CONTRIBUTING.md](https://github.com/zuri-training/team-wombat/blob/master/CONTRIBUTING.md) for more details

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Active Contributors Contact

<details><summary>Product Designers</summary>

- [@Hopeee619](https://www.github.com/hopeee619)
- [@Salakoe](https://www.github.com/Salakoe)
- [@Chibliz415](https://www.github.com/Chibliz415)
- [@AyotundeMartins](https://www.github.com/AyotundeMartins)

</details>

<details><summary>Developers</summary>

- [@Prideland-okoi](https://github.com/Prideland-okoi)
- [@Bagais](https://www.github.com/Bagais)
- [@Simplybennie](https://www.github.com/Simplybennie)
- [@ConfyC](https://www.github.com/ConfyC)
- [@Victorebegbuna](https://www.github.com/Victorebegbuna)
- [@Alexditah](https://www.github.com/Alexditah)

</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
- [Malven's Grid Cheatsheet](https://grid.malven.co/)
- [Img Shields](https://shields.io)
- [GitHub Pages](https://pages.github.com)
- [Font Awesome](https://fontawesome.com)
- [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/zuri-training/team-wombat.svg?style=for-the-badge
[contributors-url]: https://github.com/zuri-training/team-wombat/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/zuri-training/team-wombat.svg?style=for-the-badge
[forks-url]: https://github.com/zuri-training/team-wombat/network/members
[stars-shield]: https://img.shields.io/github/stars/zuri-training/team-wombat.svg?style=for-the-badge
[stars-url]: https://github.com/zuri-training/team-wombat/stargazers
[issues-shield]: https://img.shields.io/github/issues/zuri-training/team-wombat.svg?style=for-the-badge
[issues-url]: https://github.com/zuri-training/team-wombat/issues
[license-shield]: https://img.shields.io/github/license/zuri-training/team-wombat.svg?style=for-the-badge
[license-url]: https://github.com/zuri-training/team-wombat/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/SharedScreenshot.jpg
[bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[bootstrap-url]: https://getbootstrap.com
