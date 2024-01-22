<!-- Improved compatibility of back to top link: See: https://github.com/epicbotgamer/RickBot/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the RickBot. If you have a suggestion
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
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/epicbotgamer/RickBot">
    <img style = "border-radius: 15px;"src="static/assets/rick_headshot.png" alt="Logo" width=200>
  </a>

  <h3 align="center">RickBot</h3>

  <p align="center">
    by Aditya Anandan
    <br />
    <a href="https://web-production-d232.up.railway.app/"><strong>See Project»</strong></a>
    <br />
    <br />
    <a href="https://huggingface.co/aanandan/RickGPT-medium-Aditya">View Model</a>
    ·
    <a href="https://github.com/epicbotgamer/RickBot/issues">Report Bug</a>
    ·
    <a href="https://github.com/epicbotgamer/RickBot/issues">Request Feature</a>
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
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


RickBot is a chatbot created to speak and respond like Rick Sanchez from the popular animated show, "Rick and Morty". As a programmer, I've always wanted to combine my interests in Machine Learning and Web Development, and the creating and deploying this chatbot allowed me to do that. 

Here's the pipeline I followed:
* Loaded in a DialoGPT model from hugging face 
* Found "Rick and Morty" dialogue dataset on Kaggle
* Trained model using Causal Language Training and uploaded to Hugging Face 🤗
* Built out Frontend and Backend using Bootstrap/Django and connected to trained model 


The process of creating RickBot was fairly simple, but I would like to improve functionality by further training the model, improving user functionality, and perhaps adding more characters and bots for users to engage with! Please do engage with this repo to suggest improvements, build your own models, and engage with me through LinkedIn! 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![Django][Django.com]][Django-url]
* [![Python][Python.com]][Python-url]
* [![HuggingFace][HuggingFace.com]][Python-url]
* [![Javascript][Javascript.com]][Javascript-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To build your own chatbot, use the `RickandMorty.ipynb` file to get started. Then follow the pipeline described above!

### Prerequisites

These are a couple of the primary packages necessary to follow the pipleine. 
* transformers
  ```sh
  pip install transformers
  ```
* pandas 
  ```sh
  pip install pandas 
  ```
* django 
  ```sh
  pip install django
  ```


View all dependencies in the `requirements.txt` file. 



<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- ROADMAP -->
## Roadmap

Here are some future steps I have for this project! 

- [x] Create Model
- [x] Create Website
- [ ] Improve RickBot functionality by building off GPT-4, etc 
- [ ] Add new features such as new characters, etc. 
- [ ] Improve frontend
    - [ ] Better formatting/responsiveness
    - [ ] Embed within personal portfolio 

See the [open issues](https://github.com/epicbotgamer/RickBot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>







<!-- CONTACT -->
## Contact

Aditya Anandan - [@aditya_anandan](https://twitter.com/aditya_anandan) - anandan2@wisc.edu

Project Link: [https://github.com/epicbotgamer/RickBot](https://github.com/epicbotgamer/RickBot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [DialoGPT on HuggingFace](https://huggingface.co/docs/transformers/model_doc/dialogpt)
* [Article by Lynn Zheng](https://www.freecodecamp.org/news/discord-ai-chatbot/)
* [Django Chatbot Tutorial](https://www.youtube.com/watch?v=qrZGfBBlXpk)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/epicbotgamer/RickBot.svg?style=for-the-badge
[contributors-url]: https://github.com/epicbotgamer/RickBot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/epicbotgamer/RickBot.svg?style=for-the-badge
[forks-url]: https://github.com/epicbotgamer/RickBot/network/members
[stars-shield]: https://img.shields.io/github/stars/epicbotgamer/RickBot.svg?style=for-the-badge
[stars-url]: https://github.com/epicbotgamer/RickBot/stargazers
[issues-shield]: https://img.shields.io/github/issues/epicbotgamer/RickBot.svg?style=for-the-badge
[issues-url]: https://github.com/epicbotgamer/RickBot/issues
[license-shield]: https://img.shields.io/github/license/epicbotgamer/RickBot.svg?style=for-the-badge
[license-url]: https://github.com/epicbotgamer/RickBot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/adityaanandan
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[Django.com]: https://img.shields.io/badge/django-0769AD?style=for-the-badge&logo=django&logoColor=white
[Python.com]:https://img.shields.io/badge/python-90EE90?style=for-the-badge&logo=python&logoColor=black 
[Python-url]: https://www.python.org/
[JQuery-url]: https://jquery.com 
[Django-url]: https://www.djangoproject.com/
[HuggingFace.com]: https://img.shields.io/badge/%F0%9F%A4%97_Hugging_Face-FFFEE0?style=for-the-badge&
[HuggingFace-url]: https://huggingface.co/docs/transformers/model_doc/dialogpt
[Javascript.com]: https://img.shields.io/badge/javascript-C9252C?style=for-the-badge&logo=javascript&logoColor=black
[Javascript-url]: https://www.javascript.com/

